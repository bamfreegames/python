#import quickfix as fix
import simplefix
import pytest

class TestFIXOrderCreation:

    def test_simplefix(self):
        # Crear un mensaje FIX
        msg = simplefix.FixMessage()
        msg.append_pair(8, "FIX.4.4")
        msg.append_pair(35, "D")
        msg.append_pair(49, "BORJA_CLIENT")
        msg.append_pair(56, "CRYPTO_FIN")
        msg.append_pair(11, "ORD-001")
        msg.append_pair(55, "BTC/USD")
        msg.append_pair(54, 1)
        msg.append_pair(38, 0.5)
        msg.append_pair(44, 45000)
        msg.append_pair(40, 2)
        msg.append_pair(59, 0)

        # Imprime el mensaje — con BodyLength y CheckSum calculados automáticamente
        print(msg)

    def test_new_order_single_format(self):
        # Crear mensaje
        #message = fix.Message()
        #message.getHeader().setField(fix.MsgType("D"))
        #message.setField(fix.ClOrdID("TEST-001"))
        #message.setField(fix.Symbol("BTC/USD"))
        #message.setField(fix.Side(fix.Side_BUY))
        #message.setField(fix.OrderQty(0.5))
        #message.setField(fix.Price(45000))
        
        # Verificar que el mensaje es válido según FIX 4.4
        #assert message.getHeader().getField(fix.MsgType()).getValue() == "D"
        #assert message.getField(fix.Symbol()).getValue() == "BTC/USD"
        #assert message.getField(fix.OrderQty()).getValue() == 0.5
        pass

    def test_invalid_quantity_rejected(self):
        # Un sistema bien implementado rechaza cantidades negativas
        # con un Business Message Reject (35=j)
        pass  # implementación depende del sistema
    

    def test_send_fix_order(self, message, sessionID):
        # Cuando envías — QuickFIX calcula automáticamente:
        # - BeginString (tag 8)
        # - BodyLength (tag 9)
        # - SenderCompID y TargetCompID (tags 49, 56) — del sessionID
        # - MsgSeqNum (tag 34) — secuencia
        # - SendingTime (tag 52) — timestamp
        # - CheckSum (tag 10)
        #fix.Session.sendToTarget(message, sessionID)
        pass

        