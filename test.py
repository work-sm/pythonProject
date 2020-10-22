import math

import win32api
import win32con
import win32gui

NUM = 1000  # 取1000个点


def main():
    hInstance = win32api.GetModuleHandle()  # 获取当前的实例句柄

    # 定义窗口类
    wndClass = win32gui.WNDCLASS()
    wndClass.lpszClassName = 'window'  # 窗口的类名
    wndClass.lpfnWndProc = wndProc
    wndClass.hInstance = hInstance
    wndClass.cbWndExtra = 0
    wndClass.style = win32con.CS_HREDRAW | win32con.CS_VREDRAW
    wndClass.hIcon = win32gui.LoadIcon(None, win32con.IDI_APPLICATION)
    wndClass.hCursor = win32gui.LoadCursor(None, win32con.IDC_ARROW)
    wndClass.hbrBackground = win32gui.GetStockObject(win32con.WHITE_BRUSH)


    # 注册窗口类
    wndClassAtom = win32gui.RegisterClass(wndClass)

    # 创建窗口
    hWindow = win32gui.CreateWindow(
        wndClassAtom,
        'Python Win32 Window',
        win32con.WS_OVERLAPPEDWINDOW,
        win32con.CW_USEDEFAULT,
        win32con.CW_USEDEFAULT,
        win32con.CW_USEDEFAULT,
        win32con.CW_USEDEFAULT,
        0,
        0,
        hInstance,
        None)

    # 显示窗口
    win32gui.ShowWindow(hWindow, win32con.SW_SHOWNORMAL)

    # 更新窗口
    win32gui.UpdateWindow(hWindow)

    # 消息循环
    win32gui.PumpMessages()


def wndProc(hWnd, message, wParam, lParam):
    if not hasattr(wndProc, 'cxClient'):
        wndProc.cxClient = 0
        wndProc.cyClient = 0

    if message == win32con.WM_SIZE:
        wndProc.cxClient = win32gui.LOWORD(lParam)  # 附加参数的低位字保存窗口的宽度
        wndProc.cyClient = win32gui.HIWORD(lParam)  # 附加参数的高位字保存窗口的高度

    if message == win32con.WM_PAINT:
        hdc, paintStruct = win32gui.BeginPaint(hWnd)  # 获取窗口的dc和窗口客户区所需要的信息的结构
        win32gui.MoveToEx(hdc, 0, int(wndProc.cyClient / 2))  # 移动到直线的起始点，这里比win32 API少了最后一个参数
        win32gui.LineTo(hdc, wndProc.cxClient, int(wndProc.cyClient / 2))  # 画出直线
        vertices = list()  # 定义一个列表用来存储点，形式为[x,y]的形式
        point = list()  # 定义一个列表用来存储一系列作图的点
        for i in range(NUM):
            vertices = []
            vertices.append(int(i * wndProc.cxClient / NUM))  # 计算出x坐标
            vertices.append(int(wndProc.cyClient / 2 * (1 - math.sin(2 * math.pi * i / NUM))))  # 计算出y坐标
            point.append(tuple(vertices))  # 将点添加到列表当中
        win32gui.Polyline(hdc, point)  # 画出正弦图像
        win32gui.EndPaint(hWnd, paintStruct)  # 关闭dc
        return 0

    if message == win32con.WM_DESTROY:
        win32gui.PostQuitMessage(0)  # 发送消息，退出窗口的进程
        return 0
    else:
        return win32gui.DefWindowProc(hWnd, message, wParam, lParam)  # 其他消息路由给操作系统处理


if __name__ == '__main__':
    main()
