import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import base64

def KSA(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]  # 交换 S[i] 和 S[j]
    return S

def PRGA(S, n):
    i = 0
    j = 0
    key_stream = []
    for _ in range(n):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # 交换 S[i] 和 S[j]
        K = S[(S[i] + S[j]) % 256]
        key_stream.append(K)
    return key_stream

def rc4_encrypt(text, key):
    key = [ord(c) for c in key]
    S = KSA(key)
    key_stream = PRGA(S, len(text))
    encrypted_text = bytes([ord(text[i]) ^ key_stream[i] for i in range(len(text))])
    return base64.b64encode(encrypted_text).decode('utf-8')

def rc4_decrypt(encrypted_text, key):
    encrypted_text = base64.b64decode(encrypted_text)
    key = [ord(c) for c in key]
    S = KSA(key)
    key_stream = PRGA(S, len(encrypted_text))
    decrypted_text = ''.join([chr(encrypted_text[i] ^ key_stream[i]) for i in range(len(encrypted_text))])
    return decrypted_text

def on_encrypt():
    text = text_input.get()
    key = key_input.get()
    if not text or not key:
        messagebox.showerror("输入为空！", "请输入待加/解密的内容和密钥！")
        return
    encrypted_text = rc4_encrypt(text, key)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "加密结果: " + encrypted_text)

def on_decrypt():
    text = text_input.get()
    key = key_input.get()
    if not text or not key:
        messagebox.showerror("输入为空！", "请输入待加/解密的内容和密钥！")
        return
    decrypted_text = rc4_decrypt(text, key)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "解密结果: " + decrypted_text)

root = tk.Tk()
root.title("RC4 加密工具")

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

key_label = ttk.Label(frame, text="密钥:")
key_label.grid(row=1, column=0, sticky=tk.W)
key_input = ttk.Entry(frame, width=50)
key_input.grid(row=1, column=1)

encrypt_button = ttk.Button(frame, text="加密", command=on_encrypt)
encrypt_button.grid(row=2, column=0, pady="10")
decrypt_button = ttk.Button(frame, text="解密", command=on_decrypt)
decrypt_button.grid(row=2, column=1, pady="10")

result_text = tk.Text(frame, wrap=tk.WORD, width=50, height=6)
result_text.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E))

# 添加关于RC4加密的介绍文字
rc4_info_label = ttk.Label(frame, text="RC4是一种流加密算法，它使用变长密钥，可用于加密和解密数据。\n请注意，RC4 的加密和解密方法是一样的。")
rc4_info_label.grid(row=4, column=0, columnspan=2, pady=(10,0))

root.mainloop()
