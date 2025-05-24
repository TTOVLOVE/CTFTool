import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def rail_fence_encrypt(plain_text, rails):
    encrypted_text = [''] * rails
    direction = 1
    rail = 0

    for char in plain_text:
        encrypted_text[rail] += char
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    return ''.join(encrypted_text)


def rail_fence_decrypt(encrypted_text, rails):
    decrypted_text = [''] * len(encrypted_text)
    direction = 1
    rail = 0

    for i in range(len(encrypted_text)):
        decrypted_text[i] = ' '

    index = 0
    for i in range(rails):
        for j in range(len(encrypted_text)):
            if (j % (2 * (rails - 1)) == i) or (j % (2 * (rails - 1)) == (2 * (rails - 1) - i)):
                decrypted_text[j] = encrypted_text[index]
                index += 1

    return ''.join(decrypted_text)


def on_encrypt():
    text = text_input.get()
    if not text:
        messagebox.showerror("输入为空！", "请输入待加/解密的内容！")
        return
    rails = int(rails_input.get())
    encrypted_text = rail_fence_encrypt(text, rails)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "加密结果: " + encrypted_text)


def on_decrypt():
    text = text_input.get()
    if not text:
        messagebox.showerror("输入为空！", "请输入待加/解密的内容！")
        return
    rails = int(rails_input.get())
    decrypted_text = rail_fence_decrypt(text, rails)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "解密结果: " + decrypted_text)


root = tk.Tk()
root.title("栅栏密码")

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

rails_label = ttk.Label(frame, text="栏目数:")
rails_label.grid(row=1, column=0, sticky=tk.W)
rails_input = ttk.Entry(frame, width=50)
rails_input.grid(row=1, column=1)
rails_input.insert(0, "3")

encrypt_button = ttk.Button(frame, text="加密", command=on_encrypt)
encrypt_button.grid(row=2, column=0, pady="10")
decrypt_button = ttk.Button(frame, text="解密", command=on_decrypt)
decrypt_button.grid(row=2, column=1, pady="10")

result_text = tk.Text(frame, wrap=tk.WORD, width=50, height=6)
result_text.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E))

# 介绍
caesar_info_label = ttk.Label(frame, text="栅栏密码是一种简单的替换密码，它通过重新排列明文中的字符来实现加密.\n在栅栏密码中，加密的关键是栏数（或称为栅栏数），即将明文分成多少列。\n例如，如果栏数为3，则明文中的字符会被分成3列，然后按照顺序读取每一\n列的字符，形成密文。解密过程与加密过程相反.")
caesar_info_label.grid(row=4, column=0, columnspan=2, pady=(10,0))

root.mainloop()
