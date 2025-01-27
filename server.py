from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
import math


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ("/rpc2",)


with SimpleXMLRPCServer(("0.0.0.0", 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    def factorial(n):
        print(f"Received request for factorial({n})")
        if n < 0:
            return "Factorial is not defined for negative numbers!"
        return math.factorial(n)

    server.register_function(factorial, "factorial")

    print("Server is running on port 8000...")
    server.serve_forever()