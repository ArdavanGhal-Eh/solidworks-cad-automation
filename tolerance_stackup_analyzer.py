"""
Tolerance Stack-Up & Statistical 6-Sigma Assembly Clearance Analyzer
Part of SolidWorks CAD Automation & DFM Suite
Author: Ardavan Ghal-Eh | Sharif University of Technology
"""

import numpy as np
from typing import List, Dict, Any


class ToleranceStackupAnalyzer:
    """
    Evaluates mechanical assembly dimensional chains using both
    Worst-Case Analysis (WCA) and Root-Sum-Squares (RSS) statistical models.
    """

    def __init__(self, target_cpk: float = 1.33):
        self.target_cpk = target_cpk

    def analyze_stackup(
        self,
        dimensions: List[Dict[str, Any]],
        clearance_limits: Dict[str, float]
    ) -> Dict[str, Any]:
        """
        dimensions: list of dicts [{'name': 'Chassis Slot', 'nominal': 50.0, 'tol': 0.15, 'dir': +1}, ...]
        clearance_limits: {'min': 0.10, 'max': 0.80}
        """
        nominal_gap = 0.0
        worst_case_tol = 0.0
        rss_variance = 0.0

        for dim in dimensions:
            direction = dim.get('dir', 1)  # +1 or -1 in vector loop
            nominal = dim['nominal']
            tol = dim['tol']

            nominal_gap += direction * nominal
            worst_case_tol += abs(direction) * tol
            rss_variance += (direction * tol) ** 2

        rss_tol = np.sqrt(rss_variance)

        # Gap bounds
        gap_wc_min = nominal_gap - worst_case_tol
        gap_wc_max = nominal_gap + worst_case_tol

        gap_rss_min = nominal_gap - rss_tol
        gap_rss_max = nominal_gap + rss_tol

        # Check against specification
        spec_min = clearance_limits.get('min', 0.0)
        spec_max = clearance_limits.get('max', nominal_gap + worst_case_tol)

        wc_pass = (gap_wc_min >= spec_min) and (gap_wc_max <= spec_max)
        rss_pass = (gap_rss_min >= spec_min) and (gap_rss_max <= spec_max)

        # Statistical Cpk estimation (assuming 3-sigma equals RSS tolerance)
        sigma = rss_tol / 3.0 if rss_tol > 0 else 1e-6
        cpu = (spec_max - nominal_gap) / (3.0 * sigma)
        cpl = (nominal_gap - spec_min) / (3.0 * sigma)
        cpk = min(cpu, cpl)

        # Estimated defect rate in Parts Per Million (PPM)
        # Using standard normal cumulative distribution
        from math import erf
        def normal_cdf(z):
            return 0.5 * (1.0 + erf(z / np.sqrt(2.0)))

        z_upper = (spec_max - nominal_gap) / sigma
        z_lower = (nominal_gap - spec_min) / sigma
        prob_defect = (1.0 - normal_cdf(z_upper)) + (1.0 - normal_cdf(z_lower))
        ppm = round(prob_defect * 1e6, 1)

        return {
            "nominal_gap_mm": round(nominal_gap, 3),
            "worst_case_tolerance_mm": round(worst_case_tol, 3),
            "worst_case_gap_range": (round(gap_wc_min, 3), round(gap_wc_max, 3)),
            "worst_case_status": "✅ پاس شد (Pass)" if wc_pass else "⚠️ نقض تلرانس بدترین حالت (Violated)",
            "rss_tolerance_mm": round(rss_tol, 3),
            "rss_gap_range": (round(gap_rss_min, 3), round(gap_rss_max, 3)),
            "rss_status": "✅ پاس شد (Pass)" if rss_pass else "⚠️ نقض آماری (Violated)",
            "cpk_index": round(cpk, 2),
            "estimated_defect_ppm": ppm,
            "recommendation": "طراحی کاملاً ایمن و مناسب تولید انبوه" if cpk >= 1.33 else "نیاز به بازنگری تلرانس‌ها یا اصلاح زنجیره ابعادی"
        }


def run_demo_stackup():
    analyzer = ToleranceStackupAnalyzer()
    
    # 5-component drive shaft assembly stack-up
    dims = [
        {"name": "محفظه شاسی (Chassis Housing)", "nominal": 120.0, "tol": 0.12, "dir": +1},
        {"name": "فلنج یاتاقان اول (Bearing Flange 1)", "nominal": 25.0, "tol": 0.05, "dir": -1},
        {"name": "بلبرینگ اول (Bearing 1 Width)", "nominal": 15.0, "tol": 0.03, "dir": -1},
        {"name": "اسپیسر شفت (Shaft Spacer)", "nominal": 64.5, "tol": 0.08, "dir": -1},
        {"name": "بلبرینگ دوم (Bearing 2 Width)", "nominal": 15.0, "tol": 0.03, "dir": -1},
    ]
    
    limits = {"min": 0.15, "max": 0.85}
    res = analyzer.analyze_stackup(dims, limits)

    print("=" * 65)
    print("📏 تحلیل تلرانس تجمعی مونتاژ مکانیکی (Worst-Case & RSS):")
    print("=" * 65)
    print(f"لقی اسمی مونتاژ (Nominal Gap): {res['nominal_gap_mm']} mm")
    print(f"محدوده لقی در بدترین حالت (WCA): {res['worst_case_gap_range'][0]} تا {res['worst_case_gap_range'][1]} mm -> {res['worst_case_status']}")
    print(f"محدوده لقی آماری (RSS): {res['rss_gap_range'][0]} تا {res['rss_gap_range'][1]} mm -> {res['rss_status']}")
    print(f"شاخص توانمندی فرآیند (Cpk): {res['cpk_index']}")
    print(f"نرخ تخمینی خرابی تولید: {res['estimated_defect_ppm']} PPM (قطعه در میلیون)")
    print(f"توصیه مهندسی: {res['recommendation']}")
    print("=" * 65)


if __name__ == "__main__":
    run_demo_stackup()
