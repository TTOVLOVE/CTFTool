import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import base64

def base64_encrypt(plain_text):
    encoded_bytes = base64.b64encode(plain_text.encode("utf-8"))
    encoded_text = encoded_bytes.decode("utf-8")
    return encoded_text

def base64_decrypt(encoded_text):
    decoded_bytes = base64.b64decode(encoded_text.encode("utf-8"))
    decoded_text = decoded_bytes.decode("utf-8")
    return decoded_text

def on_encrypt():
    text = text_input.get()
    if not text:
        messagebox.showerror("输入为空！", "请输入待加/解密的内容！")
        return
    encrypted_text = base64_encrypt(text)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "加密结果: " + encrypted_text)

def on_decrypt():
    text = text_input.get()
    if not text:
        messagebox.showerror("输入为空！", "请输入待加/解密的内容！")
        return
    try:
        decrypted_text = base64_decrypt(text)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "解密结果: " + decrypted_text)
    except base64.binascii.Error:
        messagebox.showerror("解密失败！", "输入的内容不是有效的 Base64 编码！")

root = tk.Tk()
root.title("Base64 加解密")

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

# 添加关于Base64加解密的介绍文字
base64_info_label = ttk.Label(frame, text="Base64是一种用64个字符来表示任意二进制数据的方法。\n在Base64中，将原始数据每3个字节一组，转换为4个字符。\nBase64编码后的数据长度通常会比原始数据增加约1/3。")
base64_info_label.grid(row=3, column=0, columnspan=2, pady=(10,0))

root.mainloop()
