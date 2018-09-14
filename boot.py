import esp
import network

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.ifconfig(('192.168.1.210', '255.255.255.0', '192.168.1.1', '192.168.1.1'))
sta.connect('1-FBIsurveillance', 'tInKtHEGoAt06')
