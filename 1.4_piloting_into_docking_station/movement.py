from rovlib.control import RovMavlink, JoyStickControl
import time



rov = RovMavlink(connection_type = 'udpin', connection_ip = '0.0.0.0', connection_port = '14550', silent_mode = True)
def start_conn():
    rov.establish_connection()


def start_movement():
    rov.arm_vehicle() # you only need to arm the vehicle once, there is no need to arm it every time you want to stablize it
   

    rov.set_vehicle_mode(rov.Mode.STABILIZE)
    # to disarm vehicle
    my_lovely_fake_joy_stick = JoyStickControl(z_throttle=-0.6)
    
    # get down a bit
    start_time = time.time()
    seconds = 2
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
    
        rov.send_control(my_lovely_fake_joy_stick)

        if elapsed_time > seconds:
            break


    my_lovely_fake_joy_stick = JoyStickControl(x_throttle=0.5)


    start_time = time.time()
    seconds = 6
    # move forward
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
    
        rov.send_control(my_lovely_fake_joy_stick)

        if elapsed_time > seconds:
            break
    
    rov.disarm_vehicle()