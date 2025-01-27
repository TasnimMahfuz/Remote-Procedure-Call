import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/rpc2")

try:
    number = int(input("Enter a number: "))
    print(f"Requesting factorial({number})...")
    result = proxy.factorial(number)
    print(f"Result: {result}")
except Exception as e:
    print(f"An error occurred: {e}")