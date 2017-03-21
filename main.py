import server
import client

ckFlag = int(raw_input('Enter 0 to become the server and 1 for client'))
if ckFlag == 0:
    servObj= server.Server()
    servObj.start()
else:
    cliObj = client.Client()
    cliObj.start()
