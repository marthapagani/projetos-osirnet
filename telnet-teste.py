import telnetlib

HOST = "172.20.2.170"
user = input ('Username: ')
password = input('Password: ')

tn = telnetlib.Telnet(HOST)

tn.read_until(b"User name:")
tn.write(user.encode('ascii') +b"\n")

tn.read_until(b"User password:")
tn.write(password.encode('ascii') +b"\n")

tn.write(b"enable\n")
tn.write(b"display ont autofind all\n")

print(tn.read_all().decode('ascii'))