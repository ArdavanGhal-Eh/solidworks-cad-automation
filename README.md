# ⚙️ Polyglot SolidWorks CAD Automation & DFM Suite (Python + C# .NET)

An enterprise engineering framework combining a **native C# .NET SolidWorks Add-in** for DFM rule checking with a **Python batch drawing & BOM costing tool**.

## 🌟 Polyglot Architecture
- **C# .NET Engine (`csharp_solidworks_addin/`):** Directly interfaces with SolidWorks COM API to validate sheet metal bend radii ($R \ge t$).
- **Python Automation Tool (`cad_batch_tool.py`):** Batch drawing export (DXF/PDF) and BOM cost computation.

## 🎯 Real-World Applications & Cross-Industry Impact
### ⚙️ Mechanical & Manufacturing
- Sheet metal cracking prevention and automated laser-cutting DXF generation.
- Real-time BOM material weight and pricing for procurement.
### 🌐 Cross-Industry & Software
- Cloud CAD-as-a-Service automated manufacturing quoting pipelines (Xometry/Fictiv).
- Enterprise ERP direct integration for inventory planning.

## 🚀 Execution
```bash
# C# .NET DFM Engine:
cd csharp_solidworks_addin && dotnet run

# Python BOM Generator:
pip install -r requirements.txt && python cad_batch_tool.py
```

## 👨‍💻 Author
**Ardavan Ghal-Eh** | Sharif University of Technology
