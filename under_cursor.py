from datetime import datetime
import subprocess

import cv2
import numpy as np
import pyautogui


class WithApplescript:
  def get_active_application():
        script = 'tell application "System Events" to get name of first application process whose frontmost is true'
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
        return result.stdout.strip()

  def get_active_window_title():
        script = 'tell application "System Events" to get name of first window of (first application process whose frontmost is true)'
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
        return result.stdout.strip()

class WithCV:
  def print_screen_size():
      # Get the screen size
      screen_size = pyautogui.size()
      print("Screen size", screen_size)

  def take_screenshot():
        # Get the current mouse position
        mouse_pos = pyautogui.position()
        print("Mouse position", mouse_pos)

        # Get the screen size
        screen_size = pyautogui.size()
        print("Screen size", screen_size)
        width = 250
        height = 250

        # Define the size of the screenshot
        screenshot_size = (width, height)
        print("screenshot dimensions", screenshot_size)

        # Calculate the coordinates of the top-left corner of the screenshot
        screenshot_pos = (mouse_pos.x - (screenshot_size[0] // 2), mouse_pos.y - (screenshot_size[1] // 2))
        # screenshot_pos = (mouse_pos.x + 125, mouse_pos.y + 125)
        print("we think top left is", screenshot_pos)

        # Take the screenshot
        # screenshot = pyautogui.screenshot(imageFilename=f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.png', region=(screenshot_pos[0], screenshot_pos[1], screenshot_size[0], screenshot_size[1]))
        screenshot = pyautogui.screenshot(imageFilename=f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.png', region=(424+(250*2.26), 493+(250*2.26), 250, 250))
        return screenshot

        # Save the screenshot as a PNG file with the datetime as the filename
        # cv2.imwrite(f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.png', screenshot)




if __name__ == '__main__':
    application = WithApplescript.get_active_application()
    window_title = WithApplescript.get_active_window_title()

    print(application, '>>>', window_title)
    print("screensize", WithCV.print_screen_size())
    WithCV.take_screenshot()
