import threading
import time
import keyboard
import pyautogui

# Global flag to control the loop
stop_flag = False

def loop_task():
    global stop_flag
    counter = 0
    print("Loop started. Press 'Q' to stop.")
    while not stop_flag:
        print("Running...")
        pyautogui.moveTo(1478, 612) # Move over recent tab button
        pyautogui.click()
        time.sleep(0.5)

        pyautogui.moveTo(2394, 1313) # Move over refresh button
        pyautogui.click()
        time.sleep(0.5)

        pyautogui.moveTo(1857, 457) # Move over view button
        pyautogui.click()
        time.sleep(0.5)

        pyautogui.moveTo(1884, 365) # Move over other view button incase the page is scrolled
        pyautogui.click()
        time.sleep(0.5)

        pyautogui.moveTo(2385, 1045) # Move over like button
        pyautogui.click()
        time.sleep(0.5)

        pyautogui.moveTo(1088, 786) # Move over thumbs up button
        pyautogui.click()
        time.sleep(0.5)

        pyautogui.moveTo(2404, 1252) # Move over rating button
        pyautogui.click()
        time.sleep(0.5)
        
        pyautogui.moveTo(1620, 813) # Move over demon button
        pyautogui.click()
        time.sleep(0.5)

        pyautogui.moveTo(1550, 1013) # Move over submit button
        pyautogui.click()
        time.sleep(0.5)

        pyautogui.moveTo(169, 128) # Move over back button
        pyautogui.click()
        time.sleep(0.5)

        pyautogui.moveTo(2394, 1313) # Move over refresh button
        pyautogui.click()
        time.sleep(0.5)

        time.sleep(1)
        counter += 1
        print(f"Estimated levels liked and rated: {counter}")

def monitor_keypress():
    global stop_flag
    # Wait for 'Q' keypress
    keyboard.wait("q")
    stop_flag = True
    print("Stopping...")

# Create and start threads
task_thread = threading.Thread(target=loop_task)
key_thread = threading.Thread(target=monitor_keypress, daemon=True)

task_thread.start()
key_thread.start()

# Wait for the loop to finish
task_thread.join()
print("Program exited.")
