# Universal PDF Converter

Was tired of paid PDF converters or having to upload personal or sensitive data to be converted on the internet, so I decided to make this. It supports converting multiple file types to PDF, runs completely **locally**, and is **free**. Your personal data stays safe on your own machine.

---

## Supported File Types

- Microsoft Office documents: `.docx`, `.xlsx`, `.pptx`
- Text files: `.txt`
- Markdown files: `.md`
- HTML files: `.html`, `.htm`
- Images: `.jpg`, `.jpeg`, `.png`, `.bmp`

---

## Requirements

Make sure you have the following installed:

- [Python 3.x](https://www.python.org/downloads/)
- [LibreOffice](https://www.libreoffice.org/download/download/) (for Office files conversion)
- [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html) (for HTML, Markdown, and text conversions)

Add LibreOffice and wkhtmltopdf binaries to your system PATH.

---

## Python Dependencies

Install required Python packages using pip:

```bash
pip install pillow pdfkit markdown2
```

---

## Usage

Run the Python script `converter.py` (or whatever your filename is):

```bash
python converter.py
```

A simple GUI window will open. Click **Choose File** and select any supported file type. The converted PDF will be saved in the same folder as the original file.

---

## Notes

- LibreOffice must be installed for `.docx`, `.xlsx`, `.pptx` conversion.
- `wkhtmltopdf` must be installed and accessible for `.html`, `.md`, and `.txt` conversion.
- Images are converted directly to PDF using Pillow.
- Conversion errors will show a popup with details.

---

## License

This project is free and open source — use it however you like.

---

Feel free to reach out if you have questions or want to contribute!
