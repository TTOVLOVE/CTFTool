import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

BACON_ALPHABET = {
    'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB', 'E': 'AABAA',
    'F': 'AABAB', 'G': 'AABBA', 'H': 'AABBB', 'I': 'ABAAA', 'J': 'ABAAA',
    'K': 'ABAAB', 'L': 'ABABA', 'M': 'ABABB', 'N': 'ABBAA', 'O': 'ABBAB',
    'P': 'ABBBA', 'Q': 'ABBBB', 'R': 'BAAAA', 'S': 'BAAAB', 'T': 'BAABA',
    'U': 'BAABB', 'V': 'BAABB', 'W': 'BABAA', 'X': 'BABAB', 'Y': 'BABBA',
    'Z': 'BABBB',
}

REVERSE_BACON_ALPHABET = {v: k for k, v in BACON_ALPHABET.items()}

def bacon_encrypt(plain_text):
    encrypted_text = ''
    for char in plain_text.upper():
        if char.isalpha():
            encrypted_text += BACON_ALPHABET[char] + ' '
        else:
            encrypted_text += char
    return encrypted_text.strip()

def bacon_decrypt(encrypted_text):
    decrypted_text = ''
    for chunk in encrypted_text.split():
        if chunk in REVERSE_BACON_ALPHABET:
            decrypted_text += REVERSE_BACON_ALPHABET[chunk]
        else:
            decrypted_text += ' '
    return decrypted_text

def on_encrypt():
    text = text_input.get()
    if not text:
        messagebox.showerror("输入为空！", "请输入待加/解密的内容！")
        return
    encrypted_text = bacon_encrypt(text)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "加密结果: " + encrypted_text)

def on_decrypt():
    text = text_input.get()
    if not text:
        messagebox.showerror("输入为空！", "请输入待加/解密的内容！")
        return
    decrypted_text = bacon_decrypt(text)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "解密结果: " + decrypted_text)

root = tk.Tk()
root.title("培根密码")

# 设置图标
root.iconbitmap("../image/icon.ico")

# 获取屏幕的宽度和高度
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 设置窗口的宽度和高度
window_width = 460
window_height = 280

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

# 添加关于培根密码的介绍文字
bacon_info_label = ttk.Label(frame, text="培根密码是一种字母替换密码，将每个字母转换为一组由'A'和'B'组成的码字。\n您可以通过将码字分组解密来还原明文。")
bacon_info_label.grid(row=3, column=0, columnspan=2, pady=(10,0))

root.mainloop()
