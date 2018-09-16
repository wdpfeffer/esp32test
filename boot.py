import esp
import webrepl

esp.osdebug(None)
def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    if not sta_if.isconnected():
        print("Connecting...")
        sta_if.ifconfig(('192.168.1.192', '255.255.255.0', '192.168.1.1', '8.8.8.8'))
        sta_if.connect('1-FBIsurveillance', 'tInKtHEGoAt06')
        while not sta_if.isconnected():
            pass
        print('network config:', sta_if.ifconfig())
        webrepl.start()

do_connect()