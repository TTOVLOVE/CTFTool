import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64


BLOCK_SIZE = 16

def generate_aes_key(key):
    try:
        # Adjust key to be 16, 24, or 32 bytes long (AES key length)
        if len(key) not in [16, 24, 32]:
            raise ValueError("AES key长度必须为 16, 24, 或者 32 字节")
        return key.ljust(32, ' ')  # Pad with spaces if key length is less than 32 bytes
    except Exception as e:
        messagebox.showerror("错误", f"密钥生成失败: {e}")
        return None

def aes_encrypt(plain_text, key):
    try:
        key = generate_aes_key(key)
        cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
        padded_text = pad(plain_text.encode('utf-8'), BLOCK_SIZE)
        encrypted_text = cipher.encrypt(padded_text)
        return base64.b64encode(encrypted_text).decode('utf-8')
    except Exception as e:
        messagebox.showerror("错误", f"加密失败: {e}")
        return None

def aes_decrypt(encrypted_text, key):
    try:
        key = generate_aes_key(key)
        cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
        encrypted_data = base64.b64decode(encrypted_text)
        decrypted_text = unpad(cipher.decrypt(encrypted_data), BLOCK_SIZE)
        return decrypted_text.decode('utf-8')
    except Exception as e:
        messagebox.showerror("错误", f"解密失败: {e}")
        return None

def on_encrypt():
    text = text_input.get()
    key = key_input.get()
    if not text or not key:
        messagebox.showerror("输入为空！", "请输入待加/解密的内容和密钥！")
        return
    encrypted_text = aes_encrypt(text, key)
    if encrypted_text:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "加密结果: " + encrypted_text)

def on_decrypt():
    text = text_input.get()
    key = key_input.get()
    if not text or not key:
        messagebox.showerror("输入为空！", "请输入待加/解密的内容和密钥！")
        return
    decrypted_text = aes_decrypt(text, key)
    if decrypted_text:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "解密结果: " + decrypted_text)

root = tk.Tk()
root.title("AES 加密工具")

# 设置图标
root.iconbitmap("../image/icon.ico")

# 获取屏幕的宽度和高度
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 设置窗口的宽度和高度
window_width = 520
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

key_label = ttk.Label(frame, text="密钥(16, 24, 或 32字符):")
key_label.grid(row=1, column=0, sticky=tk.W)
key_input = ttk.Entry(frame, width=50)
key_input.grid(row=1, column=1)

encrypt_button = ttk.Button(frame, text="加密", command=on_encrypt)
encrypt_button.grid(row=2, column=0, pady="10")
decrypt_button = ttk.Button(frame, text="解密", command=on_decrypt)
decrypt_button.grid(row=2, column=1, pady="10")

result_text = tk.Text(frame, wrap=tk.WORD, width=50, height=6)
result_text.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E))

# 添加关于AES加密的介绍文字
aes_info_label = ttk.Label(frame, text="AES加密是一种对称加密算法，支持不同长度的密钥进行加密和解密。\n请注意，密钥长度必须为16、24或32个字符。")
aes_info_label.grid(row=4, column=0, columnspan=2, pady=(10,0))

root.mainloop()
