import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='admin',
    passwd='123',
    database='personal',
    charset="utf8mb4",  # Specify character set for wider character support
    collation="utf8mb4_spanish_ci"  # Set collation for Spanish text handling
)