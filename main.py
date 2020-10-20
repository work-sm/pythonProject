import win32gui

windows = {}


def get_all_hwnd(hwnd, hwnds):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        temp = [hex(hwnd), win32gui.GetClassName(hwnd), win32gui.GetWindowText(hwnd)]
        windows[hwnd] = temp


win32gui.EnumWindows(get_all_hwnd, 0)


for h, t in windows.items():
    if t:
        print(h, t[0], t[1], t[2])

if __name__ == '__main__':
    pass
