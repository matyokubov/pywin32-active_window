import win32gui
import time

def callback(hwnd):
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    print("Window %s:" % win32gui.GetWindowText(hwnd))
    print("Location: (%d, %d)" % (x, y))
    print("Size: (%d, %d)" % (w, h))

if __name__ == '__main__':
    time.sleep(3)
    callback(win32gui.GetForegroundWindow())
