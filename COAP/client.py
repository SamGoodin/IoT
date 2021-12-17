import logging
import asyncio

from aiocoap import *

logging.basicConfig(level=logging.INFO)

async def main():
    protocol = await Context.create_client_context()
    
    #input_ip = str(input("Enter IP of PI: "))
    #input_ip = "169.254.10.78"
    input_ip = "192.168.1.244"
    #input_ip = "149.162.255.255"
    #input_ip = "149.162.242.88"
    input_code = str(input("Enter code: "))
    
    uri_concat = "coap://" + input_ip + "/" + input_code

    request = Message(code=GET, uri=uri_concat)
    #request = Message(code=GET, uri='coap://169.254.10.78/helloworld')

    try:
        response = await protocol.request(request).response
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)
    else:
        print('Result: %s\n%r'%(response.code, response.payload))

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())