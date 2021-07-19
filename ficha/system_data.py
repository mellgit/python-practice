"""
Получаем данные о системе 

Кроссплатформенная библиотека psutil позволяет получать информацию о процессоре, 
памяти, диске, сети, датчиках и запущенных процессах в системе. 
Примеры базового использования показаны на картинке. 

Если говорить про практические применение, psutil полезен в основном для мониторинга 
системы, ограничения ресурсов процессов и управления запущенными процессами. 

Помимо привычных Windows, MacOS и Linux, библиотека также поддерживает 
системы FreeBSD, OpenBSD, NetBSD, Sun Solaris и AIX. 

https://www.geeksforgeeks.org/psutil-module-in-python/#:~:text=Psutil%20is%20a%20Python%20cross,network%2C%20sensors%20can%20be%20monitored.
"""

import psutil as p



print(p.cpu_percent(1)) # загруженность процессора
print(p.cpu_count()) # показывает количество логических процессоров в системе
print(p.sensors_battery()) # состояние батареи
print(p.disk_usage('/')) # дает статистику использования диска в виде кортежа для заданного пути
print(p.virtual_memory()) # показывает использование системной памяти в байтах