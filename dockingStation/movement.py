from rovlib.control import RovMavlink, JoyStickControl
from time import sleep

rov = RovMavlink(connection_type = 'udpin', connection_ip = '0.0.0.0', connection_port = '14555', silent_mode = True)
rov.establish_connection()
my_lovely_fake_joy_stick = JoyStickControl(x_throttle=1)
# move forward
for i in range(800):
    print(i)
    rov.send_control(my_lovely_fake_joy_stick)
    sleep(0.01)