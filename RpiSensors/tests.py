from appServer import SensorHTTPServer



server = SensorHTTPServer.SensorHttpServer(('localhost',8090),SensorHTTPServer.APIHandler)
server.serve_forever()
