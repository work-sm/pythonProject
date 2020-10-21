import win32api
import win32con
import win32gui

windows = []
child_windows = []


def get_all_hwnd(hwnd, parent):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        win_bean = {'hwnd': hwnd, 'hex': hex(hwnd), 'class': win32gui.GetClassName(hwnd),
                    'title': win32gui.GetWindowText(hwnd)}
        windows.append(win_bean)


def get_child_hwnd(hwnd, parent):
    child_bean = {'hwnd': hwnd, 'hex': hex(hwnd), 'class': win32gui.GetClassName(hwnd),
                  'title': win32gui.GetWindowText(hwnd)}
    child_windows.append(child_bean)


def find_win(title):
    win32gui.EnumWindows(get_all_hwnd, 0)
    for win_bean in iter(windows):
        if title in win_bean['title']:
            return win_bean


def find_child_win(parent, class_name):
    win32gui.EnumChildWindows(parent, get_child_hwnd, 0)
    for win_bean in iter(child_windows):
        if class_name in win_bean['class']:
            return win_bean


def find_child_win1(parent, class_name):
    hwnd = win32gui.FindWindowEx(parent, 0, 'Edit', None)
    return {'hwnd': hwnd, 'hex': hex(hwnd), 'class': win32gui.GetClassName(hwnd),
            'title': win32gui.GetWindowText(hwnd)}


if __name__ == '__main__':
    win32api.MessageBox(None, '你好hello word!', 'Note', win32con.MB_OK)
    win = find_win('记事本')
    print(win['class'], win['title'])
    # hwndChildList = []
    # win32gui.EnumChildWindows(win['hwnd'], lambda hwnd, param: param.append(hwnd), hwndChildList)
    # print(hwndChildList)

    # child_win = find_child_win(win['hwnd'], 'Edit')
    child_win = find_child_win1(win['hwnd'], 'Edit')
    print(child_win['class'], child_win['title'])
    win32gui.SendMessage(child_win['hwnd'], win32con.WM_SETTEXT, None, '你好hello word!')
    win32gui.PostMessage(child_win['hwnd'], win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
