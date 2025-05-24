# CTFTool

## 主要特点

*   **GUI 界面:**
    *   使用 Tkinter 库创建主窗口和各个工具窗口，提供用户交互界面。
    *   利用 `ttk` 模块增强了按钮和标签的外观。

*   **多窗口管理:**
    *   通过 `subprocess` 模块，可以在点击按钮时打开不同的工具窗口 (如凯撒密码、栅栏密码等)，并且可以同时打开多个窗口。
    *   使用全局变量 `sub_processes` 来管理所有打开的子进程，以便在主窗口关闭时统一关闭所有子窗口。

*   **功能分类:**
    *   工具按照功能类型分组，例如古典密码工具、Base 系列、WEB 工具和对称密码系列等，每个类别有对应的标签和按钮。
    *   每个按钮通过 `lambda` 表达式调用 `open_window` 函数打开相应的工具窗口。

*   **界面布局:**
    *   使用 `grid` 布局管理按钮和标签的位置，使界面看起来整洁有序。
    *   自动计算并设置主窗口的初始位置，使其始终位于屏幕中央。

*   **关闭处理:**
    *   当用户关闭主窗口时，会触发 `on_closing` 函数，该函数会先关闭所有子进程，然后销毁主窗口，以确保所有相关进程都被正确终止。

## 使用技术

*   **Python:**  主要编程语言。
*   **Tkinter:** 用于创建 GUI 界面的标准库。
*   **ttk (Themed Tkinter):** 改进 Tkinter 控件外观的模块。
*   **subprocess:** 用于创建和管理子进程，实现多窗口功能。
*   **pyinstaller:** 用于将 Python 代码打包成可执行文件 (exe)。

## 功能列表 (当前版本)

*   **古典密码:**
    *   凯撒密码
    *   ... (其他古典密码)

*   **Base 编码:**
    *   Base16
    *   ... (其他 Base 编码)

*   **对称密码:**
    *   AES
    *   ... (其他对称密码, RC4 调试中)

*   **Web 工具:**
    *   端口扫描器

## 使用方法

1.  **安装依赖:**  (推荐使用虚拟环境)

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Linux/macOS
    .venv\Scripts\activate  # Windows
    pip install -r requirements.txt  # 如果有 requirements.txt 文件
    # 或者手动安装 tkinter (通常 Python 自带)
    # pip install tkinter
    ```

2.  **运行主程序:**

    ```bash
    python TOOLS/main/main.py
    ```

3.  **打包成 exe (可选):**

    ```bash
    pip install pyinstaller
    pyinstaller --onefile TOOLS/main/main.py
    # 打包后的 exe 文件位于 dist 目录下
    ```

## 已知问题和未来计划

*   **黑框问题:** 在打包为 exe 后，打开子窗口会出现 Windows 命令黑框。 尝试添加参数后黑框消失，但是关闭主窗口时，子窗口不会被关闭。  此问题尚未解决。

*   **功能完善:**  目前可以实现的功能较少也较简单，后续会继续添加更多加解密算法和 Web 工具。

*   **代码优化:**  深入学习和理解各个加解密模块的函数，优化代码结构和性能。

*   **用户体验改进:** 完善用户界面，提供更好的交互体验。

## 如何贡献

欢迎贡献代码、提供建议和报告 bug!

