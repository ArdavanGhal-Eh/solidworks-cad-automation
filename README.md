# ⚙️ SolidWorks Batch CAD & Drafting Automation Utility

An industrial automation script interfacing with the **SolidWorks COM API** via Python. Designed to eliminate manual repetitive drafting operations in engineering offices and manufacturing plants.

---

## 🎯 What Problem Does This Solve?
In manufacturing workshops (sheet metal cutting, machining, CNC fabrication), draftspersons spend dozens of hours:
1. Manually opening drawings one by one to save them as `.DXF` for laser-cutting machines or `.PDF` for quality inspection.
2. Manually copy-pasting part numbers, materials, quantities, and weights to create procurement Bill of Materials (BOM) spreadsheets.

This tool automates the entire pipeline into a single command-line execution.

---

## 🌟 Key Features
- **Batch 2D Drawing Conversion:** Automatically iterates through folders of `.slddrw` files and generates clean, manufacturing-ready `PDF` and `DXF` files.
- **Automated BOM Extraction:** Interrogates active SolidWorks assembly trees (`ModelDoc2` / `Component2`) to extract:
  - Part Numbers
  - Component Descriptions
  - Quantities & Sub-assembly structures
  - Material designations (e.g. St37, Al 6061-T6, CK45)
  - Estimated component mass (kg)
  - Manufacturing processes (Sheet Metal, CNC Milling, Turning, Standard Hardware)
- **Cross-Platform Simulation Mode:** Runs seamlessly in demo/simulation mode on any OS (including Linux/macOS) for testing and CI/CD without requiring a live SolidWorks license.

---

## 🚀 Installation & Setup

1. **Clone repository:**
   ```bash
   git clone https://github.com/your-username/solidworks-cad-automation.git
   cd solidworks-cad-automation
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Usage

### Run full pipeline (Drawings + BOM):
```bash
python cad_batch_tool.py --mode all --output-dir "output_exports" --bom-output "Assembly_BOM_Report.xlsx"
```

### Export drawings only:
```bash
python cad_batch_tool.py --mode drawings --drawings-dir "sample_drawings" --output-dir "dxf_pdf_exports"
```

### Extract BOM only:
```bash
python cad_batch_tool.py --mode bom --assembly "MyAssembly.sldasm" --bom-output "BOM_Output.xlsx"
```

---

## 📊 Sample BOM Output Table
| شماره قطعه (Part Number) | نام قطعه (Component) | تعداد (Qty) | جنس (Material) | وزن (kg) | روش ساخت (Process) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| PN-001 | شاسی اصلی (Main Chassis) | 1 | Steel St37 | 14.50 | برش لیزر و خمکاری |
| PN-002 | شافت محرک (Drive Shaft) | 2 | Steel CK45 | 2.30 | تراشکاری CNC |
| PN-003 | فلنج اتصال (Mounting Flange) | 4 | Al 6061-T6 | 0.85 | فرزکاری CNC |

---

## 🛠️ Architecture & Tech Stack
- **Language:** Python 3.10+
- **CAD API:** SolidWorks COM API (`win32com.client`)
- **Reporting:** `pandas`, `openpyxl`
- **Standard Compliance:** DIN / ISO drawing output naming standards

---

## 👨‍💻 Author
**Ardavan Ghal-Eh**  
Mechanical Engineering Student, Sharif University of Technology  
*Focus: Mechanical CAD Design, DFM & Engineering Automation*
