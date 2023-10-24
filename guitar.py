import mss
import time
import pyautogui

# Define the points and corresponding keys
points_and_keys = {
    (119, 39): 'a',   # Green
    (269, 39): 's',   # Red
    (415, 39): 'j',   # Yellow
    (567, 39): 'k',   # Blue
    (720, 39): 'l'    # Orange
}

time.sleep(5)

while True:
    with mss.mss() as sct:
        monitor = {'top': 1837 // 2, 'left': 1306 // 2, 'width': 800 // 2, 'height': 100 // 2}
        sct_img = sct.grab(monitor)

        keys = ""
        for point, key in points_and_keys.items():
            color = sct_img.pixel(point[0], point[1])
            # Print debug information
            print(f"Point {point}: Detected color {color}")
            if color == (244, 244, 81):
                keys+= 'j '
            if color == (67, 150, 247):
                keys+= 'k '
                print('\nblue\nblue\nblue\n')
            if color == (234, 51, 35):
                keys+= 's '
            if color == (67, 150, 42):
                keys+= 'a '
        if keys: 

            pyautogui.press(keys.split())
            


