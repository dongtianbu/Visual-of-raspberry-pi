import car_control
import lifting
import time

# source ~/.venvs/opencv_env/bin/activate


if __name__ == '__main__':
    #car_control.move_forward(800, 200)

    #car_control.move_forward(0, 250)

    #car_control.move_backwards(400, 200)

    #car_control.turn_left_speed(300, 200)

    #car_control.turn_right_speed(500, 200)

    #car_control.move_left(100, 200)

    #car_control.move_right(600, 200)

    #car_control.move_forward(0, 200)

    #car_control.turn_left_position(800, 240)

    #car_control.turn_right_position(800, 240)

    lifting.lifting_up(300, 200, 10)
    time.sleep(2)
    lifting.lifting_down(300, 200, 10)
    time.sleep(2)
    lifting.claw_forward(300, 200, 10)
    time.sleep(2)
    lifting.claw_backward(300, 200, 10)
    time.sleep(6)

    lifting.claw_backward(300, 200, 32)
    lifting.lifting_down(300, 200, 20)
    



