import time
import pyvjoy
import pyautogui

# Initialize vJoy device (Ensure that vJoy Device 1 is configured)
j = pyvjoy.VJoyDevice(1)

def move_virtual_joystick(x, y):
    j.data.wAxisX = x
    j.data.wAxisY = y
    j.update()

def main():
    # Move the virtual joystick in a loop
    positions = [(-1104, 24), (180, 344)]
    while True:
        for pos in positions:
            move_virtual_joystick(pos[0], pos[1])
            print(f"Moving to position: {pos}")
            pyautogui.click()
            time.sleep(1)

if __name__ == "__main__":
    main()
