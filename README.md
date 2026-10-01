# ⚙️ SolidWorks CAD Automation, DFM Verification & Cost Estimation Suite

An industrial automation framework interfacing with the **SolidWorks COM API** via Python. Combines batch drafting conversion with automated **Design for Manufacturing (DFM)** rule validation and **Raw Material Cost Estimation**.

---

## 🌟 Advanced Features
- **Automated DFM Rule Validation:** Automatically validates sheet-metal bend radius limits ($R \ge t$) and minimum hole-to-edge clearances ($d \ge 2t$) before sending files to CNC/laser machines.
- **Dynamic Raw Material Costing:** Computes mass and multiplies by alloy unit pricing (St37, CK45, Al 6061-T6) to give engineering management early-stage cost estimates.
- **Batch 2D Drawing Conversion:** Converts `.slddrw` files in bulk into clean `.dxf` (laser/plasma ready) and `.pdf` documents.
- **Cross-Platform Simulation Mode:** Fully executable on Linux/macOS and headless CI/CD systems without requiring a SolidWorks license.

---

## 🎯 Real-World Applications & Cross-Industry Impact

### ⚙️ Mechanical & Manufacturing Engineering
* **Sheet Metal Fabrication & Laser Cutting:** Preventing costly shop-floor scrap by catching tight bends or misaligned punch holes automatically.
* **Procurement & Supply Chain Automation:** Instant generation of Bill of Materials (BOM) with material weights and estimated unit costs for purchasing departments.

### 🌐 Cross-Industry & Software Applications
* **CAD-as-a-Service (Cloud Manufacturing):** Cloud estimation pipelines (similar to Xometry or Fictiv) providing instant manufacturing quotes from uploaded 3D geometry.
* **Digital Inventory & ERP Integration:** Feeding structured BOM hierarchies directly into enterprise ERP and MRP databases.

---

## 🚀 Installation & Setup

```bash
git clone https://github.com/ArdavanGhal-Eh/solidworks-cad-automation.git
cd solidworks-cad-automation
pip install -r requirements.txt
python cad_batch_tool.py --mode all
```

---

## 📊 Sample BOM with DFM & Costing Output
| شماره فنی (Part Number) | نام قطعه (Component) | وزن کل (kg) | روش ساخت (Process) | وضعیت DFM | برآورد هزینه متریال |
| :--- | :--- | :--- | :--- | :--- | :--- |
| PN-001 | شاسی اصلی (Main Chassis) | 14.50 | برش لیزر و خمکاری | ✅ تأیید DFM (Pass) | 942,500 تومان |
| PN-002 | شفت محرک (Drive Shaft) | 4.60 | تراشکاری CNC | ✅ تأیید ماشین‌کاری | 437,000 تومان |
| PN-003 | فلنج اتصال (Mounting Flange) | 3.40 | فرزکاری CNC | ✅ تأیید ماشین‌کاری | 1,088,000 تومان |

---

## 👨‍💻 Author
**Ardavan Ghal-Eh**  
Mechanical Engineering Student, Sharif University of Technology  
*Focus: Mechanical CAD Design, DFM & Engineering Automation*
