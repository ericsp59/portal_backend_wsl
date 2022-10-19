# from asyncio.windows_events import NULL
import time
# from mysql.connector import connect, Error
from django.db import connections, Error

# mydb = connect(
#   host="172.16.16.43",
#   user="admin",
#   password="admin",
#   database="glpi"
# )

def filter_ip_4(ip_arr):
    ipv4_list = []
    for ip in ip_arr:
        if (not "::" in ip and ip != '127.0.0.1'):
            ipv4_list.append(ip)
    return ipv4_list        


def getComputerInfoById(id):
    select_query = f'''
    select
        glpi_computers.id,
        glpi_computers.name,
		glpi_computers.serial,
		glpi_computers.contact
    FROM 
        glpi_computers
    where glpi_computers.id = {id}
    '''

    select_ip_query = f'''select glpi_ipaddresses.name FROM glpi_ipaddresses WHERE glpi_ipaddresses.mainitems_id = {id} and glpi_ipaddresses.mainitemtype="Computer"'''
        
    try:           
        with connections['glpi'].cursor() as cursor:
            result = {} 
            cursor.execute(select_query)
            r = cursor.fetchall()
            # result = [{'2': '34', 'type': 3}, {'1':'45', '67':87}]
            for dev in r:
                result.update({
                    'id':dev[0],
                    'name':dev[1],
                    'serial':dev[2],
                    'contact':dev[3]
                })

            ip_list= []
            cursor.execute(select_ip_query)
            r = cursor.fetchall()
            for ip in r:
                if ip != ():
                    ip_list.append(ip[0])
            result.update({'ip': filter_ip_4(ip_list)})
            return result
            
    except Error as e:
        print(e)

def getPhoneInfoById(id):
    select_query = f'''
    select
        glpi_phones.id,
        glpi_phones.name,
		glpi_phones.serial,
		glpi_phones.contact_num
    FROM 
        glpi_phones
    where glpi_phones.id = {id}
    '''

    select_ip_query = f'''select glpi_ipaddresses.name FROM glpi_ipaddresses WHERE glpi_ipaddresses.mainitems_id = {id} and glpi_ipaddresses.mainitemtype="Phone"'''
        
    try:           
        with connections['glpi'].cursor() as cursor:
            result = {} 
            cursor.execute(select_query)
            r = cursor.fetchall()
            # result = [{'2': '34', 'type': 3}, {'1':'45', '67':87}]
            for dev in r:
                result.update({
                    'id':dev[0],
                    'name':dev[1],
                    'serial':dev[2],
                    'contact_num':dev[3]
                })

            ip_list= []
            cursor.execute(select_ip_query)
            r = cursor.fetchall()
            for ip in r:
                if ip != ():
                    ip_list.append(ip[0])
            result.update({'ip': ip_list})
            return result
            

    except Error as e:
        print(e)  


def getNetDeviceInfoById(id):
    select_query = f'''
    select
        glpi_networkequipments.id,
        glpi_networkequipments.name,
		glpi_networkequipments.serial,
		glpi_networkequipments.uptime
    FROM 
        glpi_networkequipments
    where glpi_networkequipments.id = {id}
    '''

    select_ip_query = f'''select glpi_ipaddresses.name FROM glpi_ipaddresses WHERE glpi_ipaddresses.mainitems_id = {id} and glpi_ipaddresses.mainitemtype="NetworkEquipment"'''
        
    try:           
        with connections['glpi'].cursor() as cursor:
            result = {} 
            cursor.execute(select_query)
            r = cursor.fetchall()
            # result = [{'2': '34', 'type': 3}, {'1':'45', '67':87}]
            for dev in r:
                result.update({
                    'id':dev[0],
                    'name':dev[1],
                    'serial':dev[2],
                    'uptime':dev[3]
                })

            ip_list= []
            cursor.execute(select_ip_query)
            r = cursor.fetchall()
            for ip in r:
                if ip != ():
                    ip_list.append(ip[0])
            result.update({'ip': ip_list})
            return result
            

    except Error as e:
        print(e)    

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
