import http.server
import socketserver

puerto=5000
handler= http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("",puerto),handler) as servidor:
    print("Servidor levantado mediante http.server")
    print (f"Servidor ejecutado en puerto {puerto}")
    servidor.serve_forever() 


#¿Qué facilidades nos proporciona Django?

#Django ofrece desarrollo rapido y codigo reutilizable gracias a sus caracteristicas integradas, haciendolo seguro y escalable para aplicaciones web.



#Con relación al levantamiento de un servidor. ¿Existe una forma de realizarlo con Python y sin Django?
#¿Qué desventajas nos trae este tipo de proyectos sin Django?

#Si se puede realizar con Python. Hacerlo solo con Python carece de las abstractiones de alto nivel y funcionalidad integrada que proporciona Django.