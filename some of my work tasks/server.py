from opcua import Server # модуль для работы с opc ua
import time
from random import randint

server = Server() # создание сервера

url = "opc.tcp://ip:port" # адрес образеиня к серверу

server.set_endpoint(url) # добовление сервера в конечную точку

name = "OPC UA SIMULATION SERVER" # название сервера
add_space = server.register_namespace(name) # адресное пространство

node = server.get_objects_node() # узел

param = node.add_object(add_space, "PARAMETERS") # необходимый параметр внутри адресного пространства

# параметр который отвечает за температуру, так же добавляем в адресное пространство
# начальное значение будет '0' 
temp = param.add_variable(add_space, "Tempetature", 0) 

temp.set_writable() # допустимость для записи на сервер
server.start() # запуск сервера
print(f"Server started at {url}") # сообщения о запуске

while True:
    temperature = randint(10,50) # рандомная темпаратура от 10 до 50
    temp.set_value(temperature) # после устанавливаем это значение

    time.sleep(1)


