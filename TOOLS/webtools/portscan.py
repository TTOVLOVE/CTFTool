import tkinter as tk
from tkinter import ttk, messagebox
import socket
import threading

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            scan_results[port] = '开放'
        else:
            scan_results[port] = '关闭'
        sock.close()
    except Exception as e:
        print(f"错误的扫描端口 {port}: {e}")

def multi_threaded_scan(ip, start_port, end_port):
    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    update_result_text()
    update_summary_text()

    messagebox.showinfo("扫描结束", "扫描已完成！")

def start_scan():
    target_ip = ip_entry.get()
    start_port_str = start_port_entry.get()
    end_port_str = end_port_entry.get()

    if not target_ip:
        messagebox.showerror("输入为空！","请输入目标IP！")
        return

    try:
        start_port = int(start_port_str)
        end_port = int(end_port_str)
    except ValueError:
        messagebox.showerror("输入有误！","端口号必须为整数")
        return

    if start_port < 1 or end_port > 65535:
        messagebox.showerror("输入有误！","端口号范围应该在1到65535之间")
        return

    result_text.delete('1.0', tk.END)
    summary_text.delete('1.0', tk.END)
    multi_threaded_scan(target_ip, start_port, end_port)


def update_result_text():
    result_text.delete('1.0', tk.END)
    for port, status in scan_results.items():
        result_text.insert(tk.END, f"端口 {port}: {status}\n")

def update_summary_text():
    summary_text.delete('1.0', tk.END)
    open_ports = [port for port, status in scan_results.items() if status == '开放']
    summary_text.insert(tk.END, f"开放的端口: {open_ports}")

root = tk.Tk()
root.title("端口扫描器")

# 设置图标
root.iconbitmap("../image/icon.ico")

window_width = 360
window_height = 360

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0)#frame放在主窗口第一行第一列

ip_label = tk.Label(frame, text="目标IP:")
ip_label.grid(row=0, column=0, sticky=tk.W)
ip_entry = tk.Entry(frame)  # 将Entry放在Frame内
ip_entry.grid(row=0, column=1, padx=5)

start_port_label = tk.Label(frame, text="起始端口:")
start_port_label.grid(row=1, column=0, sticky=tk.W)
start_port_entry = tk.Entry(frame)  # 将Entry放在Frame内
start_port_entry.grid(row=1, column=1, padx=5)
start_port_entry.insert(0,"1")

end_port_label = tk.Label(frame, text="结束端口:")
end_port_label.grid(row=2, column=0, sticky=tk.W)
end_port_entry = tk.Entry(frame)  # 将Entry放在Frame内
end_port_entry.grid(row=2, column=1, padx=5)
end_port_entry.insert(0,"1024")

scan_button = tk.Button(root, text="开始扫描", command=start_scan)
scan_button.grid(row=3, column=0, pady=10)

result_text = tk.Text(root, height=10, width=40)  # 调整高度和宽度
result_text.grid(row=4, column=0, padx=10, pady=10)

summary_text = tk.Text(root, height=2, width=40)  # 调整高度和宽度
summary_text.grid(row=5, column=0, padx=10, pady=10)

scan_results = {}

root.mainloop()
