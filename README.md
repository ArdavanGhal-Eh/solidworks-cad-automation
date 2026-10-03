# ⚙️ SolidWorks Batch CAD Drafting, DFM Validation & BOM Costing Suite

An industrial automation and mechanical engineering software suite interfacing directly with the **SolidWorks COM API** via Python and C# .NET. Automates batch drawing conversions, enforces **Design for Manufacturing (DFM)** rules, and generates executive Bill of Materials (BOM) costing reports.

---

## 📌 The Engineering Problem
In mechanical fabrication workshops, sheet metal cutting facilities, and design offices:
1. Drafting technicians spend dozens of hours manually opening hundreds of `.slddrw` files just to export `.dxf` files for CNC laser cutters and `.pdf` files for quality control inspection.
2. Fabrication errors frequently occur when sheet metal parts violate minimum bend radii ($R < t$) or place holes too close to bend lines, causing torn edges and expensive shop-floor scrap.
3. Compiling Bills of Materials (BOM) with part counts, material specs, and mass estimates is traditionally done via manual copy-pasting, leading to procurement mismatches.

This suite eliminates these repetitive workflows through programmatic CAD automation.

---

## 🌟 Architecture & Core Modules

```text
┌──────────────────────────────────────┐
│ SolidWorks Assemblies & 2D Drawings  │
│  (*.sldasm, *.sldprt, *.slddrw)      │
└──────────────────┬───────────────────┘
                   │
                   ├──────────────────────────────────┐
                   │ COM Automation                   │ Native Add-In
                   ▼                                  ▼
┌──────────────────────────────────────┐  ┌──────────────────────────────────────┐
│  Python Batch Tool (cad_batch_tool)  │  │  C# .NET Engine (SolidWorksDfmAddin) │
│  - OpenDoc6 / SaveAs3 Automation     │  │  - Direct In-Viewport DFM Rules      │
│  - DXF (1:1 Laser Cutting) Export    │  │  - ISldWorks & IPartDoc Interfaces   │
│  - PDF Engineering Drawing Export    │  │  - Real-Time Geometry Inspection     │
└──────────────────┬───────────────────┘  └──────────────────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  DFM & Material Costing Engine       │ ───> Live Alloy Market Prices (Toman/kg)
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  Assembly_BOM_Costing_Report.xlsx    │ ───> Part Numbers, Quantities, DFM Flags,
│                                      │      Mass (kg) & Material Costs (Toman)
└──────────────────────────────────────┘
```

---

## 🔑 Key Engineering Features

### 1. Automated Design for Manufacturing (DFM) Rule Engine
- **Minimum Bend Radius Rule:** Verifies that internal bend radius $R_{bend} \ge t_{sheet}$. Flags bends where $R < t$ as high risk for micro-cracking and material fracture.
- **Minimum Hole-to-Bend Distance:** Enforces $d_{hole} \ge 2 \cdot t_{sheet}$ to prevent hole ovality and deformation during press-brake forming.
- **Machining Feasibility:** Validates internal corner radii against standard CNC end-mill cutter diameters.

### 2. Automated Bill of Materials & Cost Estimation
- Iterates through assembly component hierarchies to extract part names, quantities, and density-derived mass properties.
- Multiplies mass by real market raw material costs (St37, CK45, Al 6061-T6, 8620 alloy steel) to deliver early-stage manufacturing cost projections.

### 3. Batch 2D Drawing Conversion
- Bulk-converts drawing files (`.slddrw`) to standard `.pdf` documentation and 1:1 scale `.dxf` vector files formatted specifically for laser and plasma cutting controllers.

### 4. Cross-Platform Simulation Engine
- Includes an internal mock engine that seamlessly simulates SolidWorks API calls on Linux, macOS, or CI/CD servers without requiring an active Windows SolidWorks license.

---

## 📊 Sample BOM with DFM & Costing Output

| شماره فنی (Part Number) | نام قطعه (Component) | تعداد | جنس (Material) | وزن کل (kg) | روش ساخت (Process) | وضعیت DFM | برآورد هزینه متریال |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **PN-001** | شاسی اصلی (Main Chassis) | ۱ | Steel St37 | ۱۴.۵۰ | برش لیزر و خمکاری | ✅ تأیید DFM (Pass) | ۹۴۲,۵۰۰ تومان |
| **PN-002** | شفت محرک (Drive Shaft) | ۲ | Steel CK45 | ۴.۶۰ | تراشکاری CNC | ✅ تأیید ماشین‌کاری | ۴۳۷,۰۰۰ تومان |
| **PN-003** | فلنج اتصال (Mounting Flange) | ۴ | Aluminum 6061-T6 | ۳.۴۰ | فرزکاری CNC | ✅ تأیید ماشین‌کاری | ۱,۰۸۸,۰۰۰ تومان |
| **PN-004** | چرخ‌دنده مخروطی (Bevel Gear) | ۲ | Steel 8620 | ۲.۲۰ | سنگ‌زنی و دنده‌زنی | ✅ تأیید ماشین‌کاری | ۲۸۶,۰۰۰ تومان |
| **PN-005** | پین تثبیت (Dowel Pin m6x20) | ۸ | Hardened Steel | ۰.۴۰ | استاندارد DIN 6325 | ℹ️ استاندارد کاتالوگی | ۵۶,۰۰۰ تومان |
| **PN-006** | بلبرینگ شیار عمیق (Bearing 6205) | ۴ | Bearing Steel | ۰.۹۲ | خرید بازرگانی (SKF) | ℹ️ استاندارد کاتالوگی | ۲۵۷,۶۰۰ تومان |

---


---

## ⚙️ Module 4: CNC Machining Time & Cost Estimator ()
- **Material Removal Rate (MRR):** Calculates rough-to-finish volume removal rates ($	ext{cm}^3/	ext{min}$) tailored to specific alloys (Al 6061: 20 	ext{ cm}^3/	ext{min}$, St37: 5 	ext{ cm}^3/	ext{min}$, CK45: 5 	ext{ cm}^3/	ext{min}$).
- **Cycle Time Prediction:** Evaluates cutting hours, standard peck drilling cycles (5	ext{s}$ per hole), and machine setup overhead.
- **Total Manufacturing Costing:** Combines raw material alloy weight costs with workshop machine hourly rates (50,000 	ext{ Toman/hr}$ for 3-axis CNC):
  42777	ext{Total Cost} = 	ext{Raw Material Cost} + 	ext{CNC Machining Cost}42777
- **Quick Run:**
  

## 🚀 Installation & Usage

### 1. Clone Repository
```bash
git clone https://github.com/ArdavanGhal-Eh/solidworks-cad-automation.git
cd solidworks-cad-automation
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Automation Pipeline
```bash
# Run complete pipeline (Batch Drawing Conversion + DFM Costing BOM):
python cad_batch_tool.py --mode all --output-dir "output_exports" --bom-output "Assembly_BOM_Costing_Report.xlsx"

# Run drawing conversion only:
python cad_batch_tool.py --mode drawings --drawings-dir "sample_drawings" --output-dir "dxf_pdf_exports"

# Run BOM & DFM costing only:
python cad_batch_tool.py --mode bom --assembly "Main_Drive_Assembly.sldasm"
```

### 4. (Optional) Compile Native C# .NET Add-In
```bash
cd csharp_solidworks_addin
dotnet build
```

---

## 📋 CLI Arguments Reference
| Argument | Default | Description |
| :--- | :--- | :--- |
| `--mode` | `all` | Operation mode: `all`, `drawings`, or `bom` |
| `--drawings-dir` | `sample_drawings` | Input directory containing `.slddrw` files |
| `--output-dir` | `output_exports` | Destination directory for `.dxf` and `.pdf` files |
| `--assembly` | `Main_Drive_Assembly.sldasm` | Target assembly for BOM and tree extraction |
| `--bom-output` | `Assembly_BOM_Costing_Report.xlsx` | Output Excel workbook filename |
| `--simulate` | `True` | Runs in headless simulation mode on systems without SolidWorks |

---

## 🛠️ Tech Stack
- **Automation Core:** Python 3.10+, `win32com.client`
- **Native Add-In:** C# .NET 8.0, SolidWorks COM API (`ISldWorks`, `IModelDoc2`)
- **Reporting & Data:** `pandas`, `openpyxl`
- **Industry Standards:** ISO 2768 (General Tolerances), DIN 912, DIN 6325

---

## 👨‍💻 Author
**Ardavan Ghal-Eh**  
Mechanical Engineering Student, Sharif University of Technology  
*Focus: Mechanical CAD Design, DFM Validation & Industrial Process Automation*
