import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#加密函数
def caesar_encrypt(plain_text, shift):
    encrypted_text = ''
    for char in plain_text:
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a')) if char.islower() \
                else chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

#解密函数
def caesar_decrypt(encrypted_text, shift):
    decrypted_text = ''
    for char in encrypted_text:
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a')) if char.islower() \
                else chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

def on_encrypt():
    text = text_input.get()
    if not text:
        messagebox.showerror("输入为空！", "请输入待加/解密的内容！")
        return
    shift = int(shift_input.get())
    encrypted_text = caesar_encrypt(text, shift)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "加密结果: " + encrypted_text)

def on_decrypt():
    text = text_input.get()
    if not text:
        messagebox.showerror("输入为空！", "请输入待加/解密的内容！")
        return
    shift = int(shift_input.get())
    decrypted_text = caesar_decrypt(text, shift)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "解密结果: " + decrypted_text)

root = tk.Tk()
root.title("凯撒密码")

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

shift_label = ttk.Label(frame, text="偏移量:")
shift_label.grid(row=1, column=0, sticky=tk.W)
shift_input = ttk.Entry(frame, width=50)
shift_input.grid(row=1, column=1)
shift_input.insert(0, "10")  # 设置偏移的默认值为10

encrypt_button = ttk.Button(frame, text="加密", command=on_encrypt)
encrypt_button.grid(row=2, column=0, pady="10")
decrypt_button = ttk.Button(frame, text="解密", command=on_decrypt)
decrypt_button.grid(row=2, column=1, pady="10")

result_text = tk.Text(frame, wrap=tk.WORD, width=50, height=6)
result_text.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E))

# 添加关于凯撒加密的介绍文字
caesar_info_label = ttk.Label(frame, text="凯撒加密是一种古老的加密技术，将明文中的每个字母替换为字母表中\n位于固定位置的另一个字母。您可以通过指定偏移量来加密或解密信息。")
caesar_info_label.grid(row=4, column=0, columnspan=2, pady=(10,0))

root.mainloop()
