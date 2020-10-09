from opcua import Client  # модуль для работы с клиентом
import time
import os

# url = "opc.tcp://ip:port
url = input("enter ip: ")
if len(url) != 0:

    

    client = Client(url)  # создание клиента
    client.connect_socket()
    client.send_hello()
    client.open_secure_channel()
    client.create_session()

    parameters = [
        client.get_endpoints()[0].Server.ProductUri,
        client.get_endpoints()[0].Server.ApplicationUri,
        client.get_endpoints()[0].Server.ApplicationName,
        client.get_endpoints()[0].Server.ApplicationType,
        client.get_endpoints()[0].Server.GatewayServerUri,
        client.get_endpoints()[0].Server.DiscoveryProfileUri,
        client.get_endpoints()[0].Server.DiscoveryUrls
    ]

    keys = [
        "ProductUri",
        "ApplicationUri",
        "ApplicationName",
        "ApplicationType",
        "GatewayServerUri",
        "DiscoveryProfileUri",
        "DiscoveryUrls",
    ]

    for i in range(len(parameters)):
        print(f"{keys[i]}: \t{parameters[i]}")

    client.close_secure_channel()
    client.disconnect_socket()

    os._exit(1)
else:
    print("empty address")