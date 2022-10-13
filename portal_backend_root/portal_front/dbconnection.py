# from asyncio.windows_events import NULL
import time
from mysql.connector import connect, Error
from django.db import connections

mydb = connect(
  host="172.16.16.43",
  user="admin",
  password="admin",
  database="glpi"
)

def getDevicesFromDb(devType):
    select_query = ''
    if (devType == 'NETWORKING'):
        select_query = f'select id, name, serial from glpi_networkequipments'
    if (devType == 'PHONES'):
        select_query = f'select id, name, serial from glpi_phones'
    if (devType == 'COMPUTERS'):
        select_query = f'select id, name, serial from glpi_computers'
    try:           
        with connections['glpi'].cursor() as cursor:
            cursor.execute(select_query)
            r = cursor.fetchall()
            result = [] 
            # result = [{'2': '34', 'type': 3}, {'1':'45', '67':87}]
            for dev in r:
                result.append({'id':dev[0], 'name':dev[1], 'serial':dev[2]})
                
            return result
            

    except Error as e:
        print(e)
