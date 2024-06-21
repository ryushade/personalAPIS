import pymysql

def obtener_conexion():
    return pymysql.connect(host='AngelMontenegro.mysql.pythonanywhere-services.com',
                                user='AngelMontenegro',
                                password='USAT2024',
                                db='AngelMontenegro$discos')