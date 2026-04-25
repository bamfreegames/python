import requests
from datetime import datetime
from unittest.mock import patch
import pytest


def send_email(to, subject, body):
    """Envía email vía API externa."""
    response = requests.post(
        "https://api.email-service.com/send",
        json={"to": to, "subject": subject, "body": body},
        timeout=10
    )
    response.raise_for_status()
    return response.json()["message_id"]


def log_to_database(message_id, status):
    """Guarda en BBDD el envío."""
    response = requests.post(
        "https://api.crypto-finance.com/notifications/log",
        json={
            "message_id": message_id,
            "status": status,
            "timestamp": datetime.utcnow().isoformat()
        }
    )
    response.raise_for_status()


def notify_order_executed(client_email, order_id, amount, asset):
    """Notifica al cliente la ejecución de su orden."""
    subject = f"Order {order_id} executed"
    body = f"Your order to buy {amount} {asset} has been executed successfully."
    
    try:
        message_id = send_email(client_email, subject, body)
        log_to_database(message_id, "sent")
        return True
    except requests.exceptions.RequestException:
        log_to_database("N/A", "failed")
        return False
    

#TEST 1 — happy path: notificación enviada con éxito
@patch("tests.unit.test_mocks_new.log_to_database")
@patch("tests.unit.test_mocks_new.send_email")
def test_notification_sent(mock_send, mock_log):
    #Mock send_email devuelve "msg-123"
    mock_send.return_value = "msg-123"
    #Mock log_to_database devuelve None
    mock_log.return_value = None
    #Verifica que la función devuelve True
    result = notify_order_executed("client@email.com","ORD-001",1,"BTC")
    assert result
    #Verifica que send_email se llamó con los args correctos
    mock_send.assert_called_once_with(
        "client@email.com",
        "Order ORD-001 executed",
        "Your order to buy 1 BTC has been executed successfully."
    )
    #Verifica que log_to_database se llamó con "msg-123" y "sent"
    mock_log.assert_called_once_with("msg-123", "sent")

#TEST 2 — fallo en envío de email
@patch("tests.unit.test_mocks_new.log_to_database")
@patch("tests.unit.test_mocks_new.send_email")
def test_notification_failed(mock_send, mock_log):
    #Mock send_email lanza ConnectionError
    mock_send.side_effect = requests.exceptions.ConnectionError("error message")
    mock_log.return_value = None
    #Verifica que la función devuelve False
    result = notify_order_executed("client@email.com", "ORD-001", 1, "BTC")
    assert result == False
    #Verifica que log_to_database se llamó con "N/A" y "failed"
    mock_log.assert_called_with("N/A","failed")

@patch("tests.unit.test_mocks_new.log_to_database")
@patch("tests.unit.test_mocks_new.send_email")
def test_send_email_called_with_correct_args(mock_send, mock_log):
    mock_send.return_value = "msg-123"
    mock_log.return_value = None
    
    notify_order_executed("test@borja.com", "ORD-001", 0.5, "BTC")
    
    mock_send.assert_called_once_with(
        "test@borja.com",
        "Order ORD-001 executed",
        "Your order to buy 0.5 BTC has been executed successfully."
    )

@patch("tests.unit.test_mocks_new.log_to_database")
@patch("tests.unit.test_mocks_new.send_email")
def test_log_called_exactly_once(mock_send, mock_log):
    mock_send.return_value = "msg-456"
    mock_log.return_value = None
    
    notify_order_executed("client@email.com", "ORD-001", 1, "BTC")
    
    mock_log.assert_called_once()

@patch("tests.unit.test_mocks_new.log_to_database")
@patch("tests.unit.test_mocks_new.send_email")
def test_db_log_fails_after_email_sent(mock_send, mock_log):
    mock_send.return_value = "msg-456"
    mock_log.side_effect = requests.exceptions.ConnectionError("DB down")
    
    # La función NO captura este error → se propaga
    with pytest.raises(requests.exceptions.ConnectionError):
        notify_order_executed("client@email.com", "ORD-001", 1, "BTC")
    
    # Verificar que el email SÍ se envió antes del fallo
    mock_send.assert_called_once()

