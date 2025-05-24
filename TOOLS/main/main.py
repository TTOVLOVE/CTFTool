import tkinter as tk
from tkinter import ttk
import subprocess

# 定义全局变量来存储子进程
sub_processes = []

def open_window(window_name):
    # 使用subprocess模块打开相应的加解密窗口，并将进程对象存储在全局列表中
    process = subprocess.Popen(["python", f"{window_name}.py"],shell=True)
    sub_processes.append(process)

def main():
    # 创建主窗口
    root = tk.Tk()
    root.title("CTF工具集")

    # 设置图标
    root.iconbitmap("../image/icon.ico")

    def on_closing():
        # 关闭主窗口时，关闭所有子进程
        for process in sub_processes:
            process.terminate()
        root.destroy()

    # 设置关闭主窗口时的回调函数
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # 获取屏幕的宽度和高度
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 设置窗口的宽度和高度
    window_width = 550
    window_height = 300

    # 计算窗口左上角的x和y坐标
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # 设置窗口的初始位置和大小
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    #介绍
    info_label=ttk.Label(root,text="\t\t这是一个CTF工具集成程序。\n\t提供多种加解密及web工具。你可以通过点击按钮打开不同的工具窗口。")
    info_label.grid(column=0,row=0,columnspan=5,rowspan=3)


    # 创建密码工具标签
    label = ttk.Label(root, text="古典密码工具")
    label.grid(column=0, row=3)

    # 创建凯撒按钮
    button1 = ttk.Button(root, text="凯撒密码", command=lambda: open_window("../Classical cipher/CaesarCipher"))
    button1.grid(column=0, row=4)

    # 创建栅栏按钮
    button2 = ttk.Button(root, text="栅栏密码", command=lambda: open_window("../Classical cipher/RailFenceCipher"))
    button2.grid(column=1, row=4)

    # 创建培根按钮
    button3 = ttk.Button(root, text="培根密码", command=lambda: open_window("../Classical cipher/BaconCipher"))
    button3.grid(column=2, row=4)

    # 创建维吉尼亚按钮
    button4 = ttk.Button(root, text="维吉尼亚密码", command=lambda: open_window("../Classical cipher/VigenereCipher"))
    button4.grid(column=3, row=4)

    # 创建埃特巴什按钮
    button5 = ttk.Button(root, text="埃特巴什码", command=lambda: open_window("../Classical cipher/AtbashCipher"))
    button5.grid(column=4, row=4)

    #创建Base标签
    label2=ttk.Label(root,text="Base系列")
    label2.grid(column=0,row=5)

    #创建base16按钮
    button6 = ttk.Button(root, text="Base16", command=lambda: open_window("../Base/Base16"))
    button6.grid(column=0, row=6)

    #创建base32按钮
    button7 = ttk.Button(root, text="Base32", command=lambda: open_window("../Base/Base32"))
    button7.grid(column=1, row=6)

    #创建base64按钮
    button8 = ttk.Button(root, text="Base64", command=lambda: open_window("../Base/Base64"))
    button8.grid(column=2, row=6)

    #创建base91按钮
    button9 = ttk.Button(root, text="Base91", command=lambda: open_window("../Base/Base91"))
    button9.grid(column=3, row=6)

    #创建web工具标签
    label2=ttk.Label(root,text="WEB工具")
    label2.grid(column=0,row=7)

    #创建端口扫描按钮
    button10 = ttk.Button(root, text="端口扫描", command=lambda: open_window("../webtools/portscan"))
    button10.grid(column=0, row=8)

    #创建对称密码标签
    label2=ttk.Label(root,text="对称密码系列")
    label2.grid(column=0,row=9)

    #创建DES按钮
    button10 = ttk.Button(root, text="DES", command=lambda: open_window("../Dc cipher/des"))
    button10.grid(column=0, row=10)

    #创建3DES按钮
    button10 = ttk.Button(root, text="3DES", command=lambda: open_window("../Dc cipher/3des"))
    button10.grid(column=1, row=10)

    #创建AES按钮
    button10 = ttk.Button(root, text="AES", command=lambda: open_window("../Dc cipher/aes"))
    button10.grid(column=2, row=10)

    #创建RC4按钮
    button10 = ttk.Button(root, text="RC4", command=lambda: open_window("../Dc cipher/rc4"))
    button10.grid(column=3, row=10)

    #添加功能..
    

    # 运行主循环
    root.mainloop()

if __name__ == "__main__":
    main()
