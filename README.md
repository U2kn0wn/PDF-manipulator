# PDF Manipulator CLI Tool

**PDF Manipulator** is a simple Python command-line tool to **split**, **multi-split**, **merge**, and **password-protect** PDF files using [pikepdf](https://pypi.org/project/pikepdf/).  

---

## Features

- **Split a PDF** between two pages  
- **Multi-split** a PDF into multiple ranges  
- **Merge** multiple PDFs in a specific order  
- **Password-protect** PDFs with custom permissions  

---

## Requirements

- Python 3.10+  
- [pikepdf](https://pypi.org/project/pikepdf/)  

Install dependencies:

```bash
pip install pikepdf
````

---

## Usage

```bash
python split.py [OPTIONS]
```

### Arguments

| Option              | Description                                                              |
| ------------------- | ------------------------------------------------------------------------ |
| `-p, --pdfname`     | Name of the PDF file to manipulate                                       |
| `-s, --split`       | Split a PDF once: provide start and end page numbers. Example: `-s 2 5`  |
| `-sl, --split_list` | Multi-split a PDF: provide multiple ranges. Example: `-sl 2,3 5,7 10,12` |
| `-m, --merge`       | Merge multiple PDFs. Provide the list of files in the desired order      |
| `-o, --output`      | Output filename (required for merge and encryption)                      |
| `--passw`           | Password to encrypt the PDF                                              |
| `--encrypt`         | Flag to enable PDF encryption                                            |

---

## Examples

### 1. Split a PDF

```bash
python split.py -p report.pdf -s 2 8
```

Creates a PDF containing pages 2–8 of `report.pdf` named `split_report.pdf`.

---

### 2. Multi-Split a PDF

```bash
python split.py -p report.pdf -sl 2,3 5,7 10,12
```

Creates multiple split files:

* `split_1_report.pdf` → pages 2–3
* `split_2_report.pdf` → pages 5–7
* `split_3_report.pdf` → pages 10–12

---

### 3. Merge PDFs

```bash
python split.py -m file1.pdf file2.pdf file3.pdf -o merged.pdf
```

Merges the PDFs in the order specified and saves as `merged.pdf`.

---

### 4. Password Protect a PDF

```bash
python split.py -p report.pdf --encrypt --passw mypassword -o report_protected.pdf
```

Encrypts `report.pdf` with password `mypassword` and saves as `report_protected.pdf`.

---

### Notes

* `-p/--pdfname` is **required** for splitting and encryption.
* `-o/--output` is **required** for merge and encryption actions.
* If `--encrypt` is not provided, the PDF will remain unprotected.
* Multi-split supports **multiple ranges**, e.g., `-sl 2,5 7,10`.

---

## License

This project is licensed under the **MIT License**.

See [LICENSE](LICENSE) for details.

---

## Author

**U2kn0wn (Mohit)** — a simple utility to automate common PDF tasks using Python.