# import quickfix as fix

# class TradingApplication(fix.Application):
#     """
#     Aplicación FIX que se conecta como cliente (initiator) y envía órdenes.
#     Hereda de fix.Application — el método base de QuickFIX.
#     """
    
#     def onCreate(self, sessionID):
#         """Llamado cuando se crea la sesión por primera vez."""
#         print(f"Session created: {sessionID}")
    
#     def onLogon(self, sessionID):
#         """Llamado cuando el logon es exitoso."""
#         print(f"Logged in: {sessionID}")
#         self.sessionID = sessionID
    
#     def onLogout(self, sessionID):
#         """Llamado cuando se cierra la sesión."""
#         print(f"Logged out: {sessionID}")
    
#     def toAdmin(self, message, sessionID):
#         """Mensajes administrativos que enviamos (logon, heartbeat, etc.)."""
#         pass
    
#     def fromAdmin(self, message, sessionID):
#         """Mensajes administrativos que recibimos."""
#         pass
    
#     def toApp(self, message, sessionID):
#         """Mensajes de aplicación que enviamos (órdenes)."""
#         print(f"Sending: {message}")
    
#     def fromApp(self, message, sessionID):
#         """Mensajes de aplicación que recibimos (execution reports)."""
#         msg_type = fix.MsgType()
#         message.getHeader().getField(msg_type)
        
#         # Si es Execution Report
#         if msg_type.getValue() == fix.MsgType_ExecutionReport:
#             self.handle_execution_report(message)
    
#     def handle_execution_report(self, message):
#         """Procesa el reporte de ejecución."""
#         order_id = fix.OrderID()
#         cl_ord_id = fix.ClOrdID()
#         exec_type = fix.ExecType()
#         ord_status = fix.OrdStatus()
        
#         message.getField(order_id)
#         message.getField(cl_ord_id)
#         message.getField(exec_type)
#         message.getField(ord_status)
        
#         print(f"Execution Report:")
#         print(f"  OrderID: {order_id.getValue()}")
#         print(f"  ClOrdID: {cl_ord_id.getValue()}")
#         print(f"  ExecType: {exec_type.getValue()}")
#         print(f"  OrdStatus: {ord_status.getValue()}")
    
#     def send_new_order(self, symbol, side, quantity, price):
#         """Construye y envía una New Order Single."""
#         message = fix.Message()
#         header = message.getHeader()
        
#         # Header obligatorio
#         header.setField(fix.BeginString(fix.BeginString_FIX44))
#         header.setField(fix.MsgType(fix.MsgType_NewOrderSingle))
        
#         # Campos de negocio
#         message.setField(fix.ClOrdID(f"ORD-{int(datetime.now().timestamp())}"))
#         message.setField(fix.HandlInst(fix.HandlInst_AUTOMATED_EXECUTION_ORDER_PRIVATE))
#         message.setField(fix.Symbol(symbol))
#         message.setField(fix.Side(side))  # fix.Side_BUY o fix.Side_SELL
#         message.setField(fix.OrderQty(quantity))
#         message.setField(fix.Price(price))
#         message.setField(fix.OrdType(fix.OrdType_LIMIT))
#         message.setField(fix.TimeInForce(fix.TimeInForce_DAY))
#         message.setField(fix.TransactTime())
        
#         # Enviar — QuickFIX calcula BodyLength, CheckSum, MsgSeqNum automáticamente
#         fix.Session.sendToTarget(message, self.sessionID)


# # Configuración del cliente
# def main():
#     settings = fix.SessionSettings("client.cfg")
#     application = TradingApplication()
#     store_factory = fix.FileStoreFactory(settings)
#     log_factory = fix.FileLogFactory(settings)
    
#     initiator = fix.SocketInitiator(application, store_factory, settings, log_factory)
#     initiator.start()
    
#     # Esperar al logon...
#     import time
#     time.sleep(2)
    
#     # Enviar una orden
#     application.send_new_order(
#         symbol="BTC/USD",
#         side=fix.Side_BUY,
#         quantity=0.5,
#         price=45000
#     )
    
#     time.sleep(5)
#     initiator.stop()


# Ejemplo 1 — Crear y enviar una New Order Single
# if __name__ == "__main__":
#     main()

#archivo config 
# [DEFAULT]
# ConnectionType=initiator
# HeartBtInt=30
# ReconnectInterval=60
# FileStorePath=store
# FileLogPath=log
# StartTime=00:00:00
# EndTime=00:00:00
# UseDataDictionary=Y
# DataDictionary=FIX44.xml

# [SESSION]
# BeginString=FIX.4.4
# SenderCompID=BORJA_CLIENT
# TargetCompID=CRYPTO_FIN
# SocketConnectHost=fix.crypto-finance.com
# SocketConnectPort=4444

# #cancelar orden
# def cancel_order(self, original_cl_ord_id, symbol, side):
#     """Cancela una orden previamente enviada."""
#     message = fix.Message()
#     header = message.getHeader()
    
#     header.setField(fix.BeginString(fix.BeginString_FIX44))
#     header.setField(fix.MsgType(fix.MsgType_OrderCancelRequest))  # 35=F
    
#     # Nuevo ClOrdID para esta cancelación
#     message.setField(fix.ClOrdID(f"CXL-{int(datetime.now().timestamp())}"))
    
#     # ID original que queremos cancelar
#     message.setField(fix.OrigClOrdID(original_cl_ord_id))
    
#     # Mismo símbolo y lado de la orden original
#     message.setField(fix.Symbol(symbol))
#     message.setField(fix.Side(side))
    
#     message.setField(fix.TransactTime())
    
#     fix.Session.sendToTarget(message, self.sessionID)


#     #modificar una orden cancel o replace
#     def modify_order(self, original_cl_ord_id, symbol, side, new_quantity, new_price):
#     """Modifica una orden — equivale a cancelar y crear nueva."""
#     message = fix.Message()
#     header = message.getHeader()
    
#     header.setField(fix.BeginString(fix.BeginString_FIX44))
#     header.setField(fix.MsgType(fix.MsgType_OrderCancelReplaceRequest))  # 35=G
    
#     # Nuevo ClOrdID para la modificación
#     message.setField(fix.ClOrdID(f"MOD-{int(datetime.now().timestamp())}"))
    
#     # ID de la orden original
#     message.setField(fix.OrigClOrdID(original_cl_ord_id))
    
#     # Datos comunes
#     message.setField(fix.Symbol(symbol))
#     message.setField(fix.Side(side))
#     message.setField(fix.HandlInst(fix.HandlInst_AUTOMATED_EXECUTION_ORDER_PRIVATE))
    
#     # Nuevos valores
#     message.setField(fix.OrderQty(new_quantity))
#     message.setField(fix.Price(new_price))
#     message.setField(fix.OrdType(fix.OrdType_LIMIT))
    
#     message.setField(fix.TransactTime())
    
#     fix.Session.sendToTarget(message, self.sessionID)




#     test unit en quickfix
#     import pytest
# import quickfix as fix


# class TestNewOrderSingle:
#     """Tests del formato y validación de mensajes FIX."""
    
#     def test_new_order_single_format(self):
#         """Verifica que un mensaje FIX se construye con los tags correctos."""
#         message = fix.Message()
#         header = message.getHeader()
        
#         header.setField(fix.BeginString(fix.BeginString_FIX44))
#         header.setField(fix.MsgType(fix.MsgType_NewOrderSingle))
        
#         message.setField(fix.ClOrdID("TEST-001"))
#         message.setField(fix.Symbol("BTC/USD"))
#         message.setField(fix.Side(fix.Side_BUY))
#         message.setField(fix.OrderQty(0.5))
#         message.setField(fix.Price(45000))
#         message.setField(fix.OrdType(fix.OrdType_LIMIT))
        
#         # Verificar tags individuales
#         msg_type = fix.MsgType()
#         message.getHeader().getField(msg_type)
#         assert msg_type.getValue() == "D"
        
#         symbol = fix.Symbol()
#         message.getField(symbol)
#         assert symbol.getValue() == "BTC/USD"
        
#         side = fix.Side()
#         message.getField(side)
#         assert side.getValue() == fix.Side_BUY
        
#         order_qty = fix.OrderQty()
#         message.getField(order_qty)
#         assert order_qty.getValue() == 0.5
    
#     def test_message_to_string(self):
#         """Verifica el mensaje completo en formato wire."""
#         message = fix.Message()
#         message.getHeader().setField(fix.BeginString("FIX.4.4"))
#         message.getHeader().setField(fix.MsgType("D"))
#         message.setField(fix.ClOrdID("ORD-001"))
#         message.setField(fix.Symbol("BTC/USD"))
#         message.setField(fix.Side(fix.Side_BUY))
#         message.setField(fix.OrderQty(1))
#         message.setField(fix.Price(45000))
        
#         # toString devuelve el mensaje formateado FIX
#         wire = message.toString()
        
#         assert "8=FIX.4.4" in wire
#         assert "35=D" in wire
#         assert "11=ORD-001" in wire
#         assert "55=BTC/USD" in wire
#         assert "54=1" in wire
#         assert "38=1" in wire
#         assert "44=45000" in wire



#         tests integrador simulator
#         def test_full_order_lifecycle():
#     """
#     Test integration: envía orden, espera execution report, valida resultado.
#     Necesita un simulador FIX corriendo en localhost:4444.
#     """
#     settings = fix.SessionSettings("test_client.cfg")
#     app = TradingApplication()
#     store_factory = fix.FileStoreFactory(settings)
#     log_factory = fix.FileLogFactory(settings)
    
#     initiator = fix.SocketInitiator(app, store_factory, settings, log_factory)
#     initiator.start()
    
#     # Esperar logon
#     time.sleep(2)
#     assert app.is_logged_in
    
#     # Enviar orden
#     app.send_new_order("BTC/USD", fix.Side_BUY, 1, 45000)
    
#     # Esperar execution report
#     time.sleep(3)
    
#     # Verificar que se recibió el reporte
#     assert len(app.execution_reports) == 1
#     report = app.execution_reports[0]
#     assert report["status"] == "executed"
#     assert report["symbol"] == "BTC/USD"
    
#     initiator.stop()





#     most common test_message_to_string# Configuración
# fix.BeginString_FIX44         # "FIX.4.4"
# fix.BeginString_FIX42         # "FIX.4.2"

# # Tipos de mensaje (Tag 35)
# fix.MsgType_Logon                       # "A"
# fix.MsgType_Logout                      # "5"
# fix.MsgType_Heartbeat                   # "0"
# fix.MsgType_NewOrderSingle              # "D"
# fix.MsgType_OrderCancelRequest          # "F"
# fix.MsgType_OrderCancelReplaceRequest   # "G"
# fix.MsgType_ExecutionReport             # "8"
# fix.MsgType_OrderCancelReject           # "9"

# # Side (Tag 54)
# fix.Side_BUY                  # "1"
# fix.Side_SELL                 # "2"

# # OrdType (Tag 40)
# fix.OrdType_MARKET            # "1"
# fix.OrdType_LIMIT             # "2"
# fix.OrdType_STOP              # "3"

# # TimeInForce (Tag 59)
# fix.TimeInForce_DAY                          # "0"
# fix.TimeInForce_GOOD_TILL_CANCEL             # "1"
# fix.TimeInForce_IMMEDIATE_OR_CANCEL          # "3"
# fix.TimeInForce_FILL_OR_KILL                 # "4"

# # OrdStatus (Tag 39)
# fix.OrdStatus_NEW                  # "0"
# fix.OrdStatus_PARTIALLY_FILLED     # "1"
# fix.OrdStatus_FILLED               # "2"
# fix.OrdStatus_CANCELED             # "4"
# fix.OrdStatus_REJECTED             # "8"

# # ExecType (Tag 150)
# fix.ExecType_NEW              # "0"
# fix.ExecType_TRADE            # "F" — fill
# fix.ExecType_CANCELED         # "4"
# fix.ExecType_REJECTED         # "8"