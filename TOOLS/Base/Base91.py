import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import base91

def base91_encrypt(plain_text):
    encoded_bytes = base91.encode(plain_text.encode("utf-8"))
    return encoded_bytes

def base91_decrypt(encoded_text):
    try:
        decoded_bytes = base91.decode(encoded_text)  # 解码函数返回的就是字节型
        decoded_text = decoded_bytes.decode("utf-8")  # 将字节型解码为字符串型
        return decoded_text
    except ValueError:
        return "无效的 Base91 编码！"

def on_encrypt():
    text = text_input.get()
    if not text:
        messagebox.showerror("输入为空！", "请输入待加/解密的内容！")
        return
    encrypted_text = base91_encrypt(text)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "加密结果: " + encrypted_text)

def on_decrypt():
    text = text_input.get()
    if not text:
        messagebox.showerror("输入为空！", "请输入待加/解密的内容！")
        return
    decrypted_text = base91_decrypt(text)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "解密结果: " + decrypted_text)

root = tk.Tk()
root.title("Base91 加解密")

# 设置图标
root.iconbitmap("../image/icon.ico")

# 获取屏幕的宽度和高度
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 设置窗口的宽度和高度
window_width = 460
window_height = 300

# 计算窗口左上角的x和y坐标
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# 设置窗口的初始位置和大小
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0)

text_label = ttk.Label(frame, text="待加/解密内容:")
text_label.grid(row=0, column=0, sticky=tk.W)
text_input = ttk.Entry(frame, width=50)
text_input.grid(row=0, column=1)

encrypt_button = ttk.Button(frame, text="加密", command=on_encrypt)
encrypt_button.grid(row=1, column=0, pady="10")
decrypt_button = ttk.Button(frame, text="解密", command=on_decrypt)
decrypt_button.grid(row=1, column=1, pady="10")

result_text = tk.Text(frame, wrap=tk.WORD, width=50, height=6)
result_text.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E))

# 添加关于Base91加解密的介绍文字
base91_info_label = ttk.Label(frame, text="Base91是一种用91个字符来表示任意二进制数据的方法。\nBase91编码通常比Base64编码更有效率。\nBase91编码后的数据长度通常会比原始数据增加约23%。")
base91_info_label.grid(row=3, column=0, columnspan=2, pady=(10,0))

root.mainloop()
