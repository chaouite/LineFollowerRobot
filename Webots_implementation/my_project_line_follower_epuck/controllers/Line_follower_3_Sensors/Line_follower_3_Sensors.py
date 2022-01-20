from controller import Robot

def run_robot(robot):

    time_step = 32
    max_speed = 3
    my_value=5.3
    
    kp=0.001
    ki=0
    kd=1.5
    
    P=0
    I=0
    D=0
    
    error= 0
    last_error= 0


    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)

    left_ir = robot.getDevice('leftIR')
    left_ir.enable(time_step)

    right_ir = robot.getDevice('rightIR')
    right_ir.enable(time_step)
    
    center_ir = robot.getDevice('centerIR')
    center_ir.enable(time_step)



    #infinite loop
    while robot.step(time_step) != -1:
        left_ir_value = left_ir.getValue()
        right_ir_value = right_ir.getValue()
        center_ir_value = center_ir.getValue()


        print("----------------------------------")
        print("left: {}".format(left_ir_value))
        print("center: {} ".format(center_ir_value))
        print("right: {} ".format(right_ir_value))
        print("----------------------------------")

        left_speed = max_speed 
        right_speed = max_speed 

        #left: out center: in righet: out
        if(left_ir_value < my_value and center_ir_value > my_value and right_ir_value < my_value):
            print("Go straight")
            error = 0
            P=error
            I= error + I
            D = error - last_error
            print("----------------------------------")
            print("P: {}".format(P))
            print("I: {} ".format(I))
            print("D: {} ".format(D))
            print("----------------------------------")
            PID =(kp*P) +(ki*I) +(kd*D)
            print("----------------PID----------------")
            print("PID: {}".format(PID))
            print("----------------------------------")
            last_error = error
            left_speed= max_speed - PID
            right_speed= max_speed + PID
            print("----------------------------------")
            print("right_speed: {}".format(right_speed))
            print("left_speed: {}".format(left_speed))
            print("----------------------------------")
             
        
        #left: in center: in righet: out    
        elif(left_ir_value > my_value and center_ir_value > my_value and right_ir_value < my_value) :
            print("GO left")
            error = -1.5
            P=error
            I= error + I
            D = error - last_error
            print("----------------------------------")
            print("P: {}".format(P))
            print("I: {} ".format(I))
            print("D: {} ".format(D))
            print("----------------------------------")
            PID =(kp*P) +(ki*I) +(kd*D)
            print("----------------PID----------------")
            print("PID: {}".format(PID))
            print("----------------------------------")
            last_error = error
            right_speed = max_speed - PID
            left_speed = max_speed + PID
            print("----------------------------------")
            print("right_speed: {}".format(right_speed))
            print("left_speed: {}".format(left_speed))
            print("----------------------------------")
        
        #left: out center: in righet: in               
        elif(left_ir_value < my_value and center_ir_value > my_value and right_ir_value > my_value) :
            print("Go right")
            error = 1.5
            P = error
            I= error + I
            D = error - last_error
            print("----------------------------------")
            print("P: {}".format(P))
            print("I: {} ".format(I))
            print("D: {} ".format(D))
            print("----------------------------------")
            PID =(kp*P) +(ki*I) +(kd*D)
            print("----------------PID----------------")
            print("PID: {}".format(PID))
            print("----------------------------------")
            last_error = error
            right_speed = max_speed - PID
            left_speed = max_speed + PID
            print("----------------------------------")
            print("right_speed: {}".format(right_speed))
            print("left_speed: {}".format(left_speed))
            print("----------------------------------")

             

        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)

if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)  
