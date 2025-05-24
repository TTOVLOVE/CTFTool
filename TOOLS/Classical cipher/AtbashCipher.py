import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# 埃特巴什码加密字典
atbash_cipher = {
    'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v',
    'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q',
    'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l',
    'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g',
    'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b',
    'z': 'a'
}

def atbash_encrypt(plain_text):
    encrypted_text = ''
    for char in plain_text.lower():
        if char.isalpha():
            encrypted_text += atbash_cipher[char]
        else:
            encrypted_text += char
    return encrypted_text

def atbash_decrypt(encrypted_text):
    decrypted_text = ''
    for char in encrypted_text.lower():
        if char.isalpha():
            decrypted_text += atbash_cipher[char]
        else:
            decrypted_text += char
    return decrypted_text

def on_encrypt():
    text = text_input.get()
    if not text:
        messagebox.showerror("输入为空！", "请输入待加/解密的内容！")
        return
    encrypted_text = atbash_encrypt(text)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "加密结果: " + encrypted_text)

def on_decrypt():
    text = text_input.get()
    if not text:
        messagebox.showerror("输入为空！", "请输入待加/解密的内容！")
        return
    decrypted_text = atbash_decrypt(text)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "解密结果: " + decrypted_text)

root = tk.Tk()
root.title("埃特巴什码")

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

result_text = tk.Text(frame, wrap=tk.WORD, width=62, height=6)
result_text.grid(row=2, column=0, columnspan=2, sticky=tk.W)

# 关于埃特巴什码的介绍
atbash_info_label = ttk.Label(frame, text="埃特巴什码是一种简单的替换密码，字母被替换为倒序的另一个字母。\n例如：a 被替换为 z，b 被替换为 y，以此类推。")
atbash_info_label.grid(row=3, column=0, columnspan=2, pady=(10,0))

root.mainloop()
