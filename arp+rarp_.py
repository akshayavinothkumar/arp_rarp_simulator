import sqlite3

conn = sqlite3.connect("network.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS devices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip_address TEXT UNIQUE,
    mac_address TEXT UNIQUE
)
""")

sample_data = [
    ("192.168.1.1",  "AA:BB:CC:DD:EE:01"),
    ("192.168.1.2",  "AA:BB:CC:DD:EE:02"),
    ("192.168.1.3",  "AA:BB:CC:DD:EE:03"),
    ("192.168.1.4",  "AA:BB:CC:DD:EE:04"),
    ("192.168.1.5",  "AA:BB:CC:DD:EE:05"),
    ("192.168.1.6",  "AA:BB:CC:DD:EE:06"),
    ("192.168.1.7",  "AA:BB:CC:DD:EE:07"),
    ("192.168.1.8",  "AA:BB:CC:DD:EE:08"),
    ("192.168.1.9",  "AA:BB:CC:DD:EE:09"),
    ("192.168.1.10", "AA:BB:CC:DD:EE:0A"),
    ("192.168.1.11", "AA:BB:CC:DD:EE:0B"),
    ("192.168.1.12", "AA:BB:CC:DD:EE:0C"),
    ("192.168.1.13", "AA:BB:CC:DD:EE:0D"),
    ("192.168.1.14", "AA:BB:CC:DD:EE:0E"),
    ("192.168.1.15", "AA:BB:CC:DD:EE:0F"),
    ("192.168.1.16", "AA:BB:CC:DD:EE:10"),
    ("192.168.1.17", "AA:BB:CC:DD:EE:11"),
    ("192.168.1.18", "AA:BB:CC:DD:EE:12"),
    ("192.168.1.19", "AA:BB:CC:DD:EE:13"),
    ("192.168.1.20", "AA:BB:CC:DD:EE:14")
]

for ip, mac in sample_data:
    try:
        cursor.execute("INSERT INTO devices (ip_address, mac_address) VALUES (?, ?)", (ip, mac))
    except:
        pass

conn.commit()

def arp():
    ip = input("\nEnter IP address: ")
    cursor.execute("SELECT mac_address FROM devices WHERE ip_address = ?", (ip,))
    result = cursor.fetchone()
    if result:
        print(f"MAC address: {result[0]}")
    else:
        print("IP address not found")

def rarp():
    mac = input("\nEnter MAC address: ")
    cursor.execute("SELECT ip_address FROM devices WHERE mac_address = ?", (mac,))
    result = cursor.fetchone()
    if result:
        print(f"IP address: {result[0]}")
    else:
        print("MAC address not found")

while True:
    print("\n1. ARP")
    print("2. RARP")
    print("3. Exit")
    c=int(input("Enter your choice: "))
    if c==1:
        arp()
    elif c== 2:
        rarp()
    elif c ==3:
        print("Exit")
        break
    else:
        print("Invalid")