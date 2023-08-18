def script(s, p, id, sn, pppoe, senha):

    if p < 10:
        pf = f"{p:02d}"
        vlan = str(s) + str(pf)
    else:
        vlan = str(s) + str(p)

    print(f'''
config
interface gpon 0/{s}
ont add {p} sn-auth {sn} omci ont-lineprofile-name \"LP-{s}/{p}_vlan{s}{p}\" ont-srvprofile-name SP-ONT desc {pppoe}
ont port native-vlan {p} {id} eth 1 vlan {vlan} priority 0
quit
service-port vlan {vlan} gpon 0/{s}/{p} ont {id} gemport 1 multi-service user-vlan {vlan} tag-transform translate
interface gpon 0/{s}
ont ipconfig {p} {id} ip-index 0 pppoe vlan {vlan} user-account username {pppoe} password {senha}
ont wan-config {p} {id} ip-index 0 profile-id 49\nont internet-config {p} {id} ip-index 0''')

# Declaração de variáveis

slot = int(input('Slot: '))
porta = int(input('Porta: '))
id = int(input('ID: '))
serial = input('Serial: ')
pppoe = input('PPPoE: ')
senha = int(input('Senha PPPoE: '))

script(slot, porta, id, serial, pppoe, senha)