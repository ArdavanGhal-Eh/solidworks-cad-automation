"""
CNC Machining Time & Manufacturing Cost Estimation Module
Part of SolidWorks CAD Automation Suite
Author: Ardavan Ghal-Eh | Sharif University of Technology
"""

from typing import Dict, List, Any


class CncMachiningEstimator:
    """
    Estimates cycle times for milling, turning, and drilling operations,
    and calculates total manufacturing cost (Raw Material + CNC Machining).
    """

    # Material Removal Rate (MRR) in cm3/min for standard carbide tooling
    MRR_BY_MATERIAL = {
        "Steel St37": 35.0,
        "Steel CK45": 25.0,
        "Aluminum 6061-T6": 120.0,
        "Steel 8620": 20.0,
        "Stainless Steel 304": 15.0,
    }

    # Shop labor + machine operational rates (Toman / Hour)
    SHOP_RATES = {
        "3_AXIS_CNC_MILL": 450_000,
        "CNC_LATHE": 400_000,
        "MANUAL_MILL": 250_000,
        "LASER_CUTTING_PER_METER": 25_000,
    }

    def __init__(self, hourly_cnc_rate: int = 450_000):
        self.hourly_cnc_rate = hourly_cnc_rate

    def estimate_part_manufacturing(
        self,
        part_name: str,
        material: str,
        rough_volume_cm3: float,
        final_volume_cm3: float,
        hole_count: int,
        material_cost_toman: int,
        machine_type: str = "3_AXIS_CNC_MILL"
    ) -> Dict[str, Any]:
        """
        Calculates MRR, cutting time, setup time, tool changes, and total manufacturing cost.
        """
        removed_volume = max(0.0, rough_volume_cm3 - final_volume_cm3)
        mrr = self.MRR_BY_MATERIAL.get(material, 30.0)

        # Cutting time in minutes
        cutting_time_min = removed_volume / mrr if mrr > 0 else 0.0

        # Drilling time (standard 15 seconds per hole including positioning & peck drilling)
        drilling_time_min = (hole_count * 0.25)

        # Setup and tool change overhead (approx. 5 minutes per unique setup)
        overhead_time_min = 5.0

        total_time_min = cutting_time_min + drilling_time_min + overhead_time_min
        machining_hours = total_time_min / 60.0

        hourly_rate = self.SHOP_RATES.get(machine_type, self.hourly_cnc_rate)
        machining_cost_toman = int(machining_hours * hourly_rate)
        total_manufacturing_cost = material_cost_toman + machining_cost_toman

        return {
            "part_name": part_name,
            "material": material,
            "removed_volume_cm3": round(removed_volume, 2),
            "mrr_cm3_per_min": mrr,
            "cutting_time_min": round(cutting_time_min, 1),
            "drilling_time_min": round(drilling_time_min, 1),
            "total_machining_time_min": round(total_time_min, 1),
            "material_cost_toman": material_cost_toman,
            "machining_cost_toman": machining_cost_toman,
            "total_manufacturing_cost_toman": total_manufacturing_cost,
            "machining_cost_percentage": round((machining_cost_toman / total_manufacturing_cost) * 100.0, 1) if total_manufacturing_cost > 0 else 0.0
        }


def run_demo_estimation():
    estimator = CncMachiningEstimator()
    sample_part = estimator.estimate_part_manufacturing(
        part_name="فلنج اتصال گیربکس (Mounting Flange)",
        material="Aluminum 6061-T6",
        rough_volume_cm3=650.0,
        final_volume_cm3=380.0,
        hole_count=6,
        material_cost_toman=1_088_000,
        machine_type="3_AXIS_CNC_MILL"
    )

    print("=" * 65)
    print("⚙️ برآورد زمان ماشین‌کاری و هزینه ساخت CNC:")
    print("=" * 65)
    print(f"نام قطعه: {sample_part['part_name']}")
    print(f"متریال: {sample_part['material']}")
    print(f"حجم براده‌برداری شده: {sample_part['removed_volume_cm3']} cm³")
    print(f"زمان کل ماشین‌کاری: {sample_part['total_machining_time_min']} دقیقه")
    print(f"هزینه متریال: {sample_part['material_cost_toman']:,} تومان")
    print(f"هزینه ماشین‌کاری CNC: {sample_part['machining_cost_toman']:,} تومان")
    print(f"هزینه نهایی ساخت: {sample_part['total_manufacturing_cost_toman']:,} تومان")
    print(f"سهم هزینه ماشین‌کاری: {sample_part['machining_cost_percentage']}%")
    print("=" * 65)


if __name__ == "__main__":
    run_demo_estimation()
