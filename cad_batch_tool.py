import pandas as pd

class CadBatchTool:
    def generate_bom(self):
        items = [
            {"PN": "PN-001", "Component": "Main Chassis", "Qty": 1, "Mat": "Steel St37", "Mass_kg": 14.5, "DFM": "PASS", "Cost_Toman": 942500},
            {"PN": "PN-002", "Component": "Drive Shaft", "Qty": 2, "Mat": "Steel CK45", "Mass_kg": 2.3, "DFM": "PASS", "Cost_Toman": 437000}
        ]
        df = pd.DataFrame(items)
        df.to_excel("Assembly_BOM_Costing.xlsx", index=False)
        print("BOM exported: Assembly_BOM_Costing.xlsx")

if __name__ == "__main__":
    CadBatchTool().generate_bom()
