import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import json
from pathlib import Path
from param_parser import parse_parametrize_code, filename_to_key,preprocess_code

class ParamToJsonGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Parametrize → JSON 轉換工具")

        self.code_input = scrolledtext.ScrolledText(root, width=80, height=15)
        self.code_input.grid(row=1, column=0, columnspan=4, padx=10, pady=5)

        tk.Button(root, text="📂 選擇 .py 檔", command=self.load_file).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(root, text="📋 清除貼上內容", command=lambda: self.code_input.delete("1.0", tk.END)).grid(row=0, column=1)

        tk.Label(root, text="JSON key 名稱：").grid(row=2, column=0, sticky='e')
        self.key_entry = tk.Entry(root, width=30)
        self.key_entry.grid(row=2, column=1, sticky='w')

        tk.Label(root, text="輸出檔名：").grid(row=2, column=2, sticky='e')
        self.file_entry = tk.Entry(root, width=30)
        self.file_entry.insert(0, "output.json")
        self.file_entry.grid(row=2, column=3, sticky='w')

        tk.Button(root, text="💾 轉換並儲存 JSON", command=self.convert_and_save).grid(row=3, column=0, columnspan=4, pady=10)

        self.output = scrolledtext.ScrolledText(root, width=80, height=15)
        self.output.grid(row=4, column=0, columnspan=4, padx=10, pady=5)

    def load_file(self):
        path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
        if path:
            with open(path, encoding="utf-8") as f:
                code = f.read()
            self.code_input.delete("1.0", tk.END)
            self.code_input.insert(tk.END, code)
            # 預設 json key 用檔名
            key = filename_to_key(Path(path).name)
            self.key_entry.delete(0, tk.END)
            self.key_entry.insert(0, key)
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, f"{key}.json")

    def convert_and_save(self):
        raw_code = self.code_input.get("1.0", tk.END).strip()
        key = self.key_entry.get().strip()
        out_file = Path("json") / self.file_entry.get().strip()

        if not raw_code or not key:
            messagebox.showerror("錯誤", "請填寫必要欄位")
            return

        try:
            code = preprocess_code(raw_code)
            data = parse_parametrize_code(code, key)
            out_file.parent.mkdir(parents=True, exist_ok=True)
            with open(out_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            self.output.delete("1.0", tk.END)
            self.output.insert(tk.END, json.dumps(data, indent=2, ensure_ascii=False))
            messagebox.showinfo("成功", f"已儲存至 {out_file}")
        except Exception as e:
            messagebox.showerror("轉換失敗", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = ParamToJsonGUI(root)
    root.mainloop()
