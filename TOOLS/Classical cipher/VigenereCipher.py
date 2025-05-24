import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def vigenere_encrypt(plain_text, key):
    encrypted_text = ''
    key_length = len(key)
    for i, char in enumerate(plain_text):
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char.upper()) - ord('A')
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ''
    key_length = len(key)
    for i, char in enumerate(encrypted_text):
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char.upper()) - ord('A')
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a'))
            else:
                decrypted_text += chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

def on_encrypt():
    text = text_input.get()
    key = key_input.get()
    if not text or not key:
        messagebox.showerror("输入为空！", "请输入待加/解密的内容和密钥！")
        return
    encrypted_text = vigenere_encrypt(text, key)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "加密结果: " + encrypted_text)

def on_decrypt():
    text = text_input.get()
    key = key_input.get()
    if not text or not key:
        messagebox.showerror("输入为空！", "请输入待加/解密的内容和密钥！")
        return
    decrypted_text = vigenere_decrypt(text, key)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "解密结果: " + decrypted_text)

root = tk.Tk()
root.title("维吉尼亚密码")

# 设置图标
root.iconbitmap("../image/icon.ico")

# 获取屏幕的宽度和高度
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 设置窗口的宽度和高度
window_width = 490
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

# 添加关于维吉尼亚密码的介绍文字
vigenere_info_label = ttk.Label(frame, text="维吉尼亚密码是一种多表替换密码，通过使用不同的密钥字符对每个明文字符进行加密。\n密钥循环使用直至整个明文被加密。")
vigenere_info_label.grid(row=4, column=0, columnspan=2, pady=(10,0))

root.mainloop()
