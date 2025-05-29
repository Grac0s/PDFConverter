import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess
from PIL import Image
import pdfkit
import markdown2

def convert_file(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    output_dir = os.path.dirname(filepath)
    base_name = os.path.splitext(os.path.basename(filepath))[0]
    output_pdf = os.path.join(output_dir, base_name + '.pdf')

    try:
        if ext in {'.docx', '.xlsx', '.pptx'}:
            subprocess.run(['libreoffice', '--headless', '--convert-to', 'pdf', '--outdir', output_dir, filepath], check=True)

        elif ext in {'.jpg', '.jpeg', '.png', '.bmp'}:
            img = Image.open(filepath)
            img.convert('RGB').save(output_pdf)

        elif ext == '.txt':
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            html = f"<pre>{content}</pre>"
            pdfkit.from_string(html, output_pdf)

        elif ext == '.md':
            with open(filepath, 'r', encoding='utf-8') as f:
                md_content = f.read()
            html = markdown2.markdown(md_content)
            pdfkit.from_string(html, output_pdf)

        elif ext in {'.html', '.htm'}:
            pdfkit.from_file(filepath, output_pdf)

        else:
            raise ValueError(f"Unsupported file type: {ext}")

        return output_pdf

    except Exception as e:
        raise RuntimeError(f"Failed to convert {filepath} to PDF: {e}")

def select_file():
    filepath = filedialog.askopenfilename(
        title="Select a File to Convert",
        filetypes=[("Supported files", "*.docx *.xlsx *.pptx *.txt *.md *.html *.htm *.jpg *.jpeg *.png *.bmp")]
    )
    if filepath:
        try:
            output_pdf = convert_file(filepath)
            messagebox.showinfo("Success", f"PDF saved at:\n{output_pdf}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("Universal PDF Converter")
root.geometry("350x180")

label = tk.Label(root, text="Select a file to convert to PDF")
label.pack(pady=10)

select_button = tk.Button(root, text="Choose File", command=select_file)
select_button.pack(pady=10)

root.mainloop()
