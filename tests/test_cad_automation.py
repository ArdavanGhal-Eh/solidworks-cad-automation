import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from tolerance_stackup_analyzer import ToleranceStackupAnalyzer
from cnc_machining_estimator import CncMachiningEstimator
from cad_batch_tool import SolidWorksAutomationTool


def test_tolerance_stackup_worst_case_and_rss():
    analyzer = ToleranceStackupAnalyzer()
    dims = [
        {"name": "Slot", "nominal": 50.0, "tol": 0.10, "dir": +1},
        {"name": "Block", "nominal": 49.5, "tol": 0.05, "dir": -1},
    ]
    limits = {"min": 0.30, "max": 0.70}
    res = analyzer.analyze_stackup(dims, limits)

    assert res["nominal_gap_mm"] == pytest.approx(0.50, rel=1e-3)
    assert res["worst_case_tolerance_mm"] == pytest.approx(0.15, rel=1e-3)
    # RSS tolerance: sqrt(0.10^2 + 0.05^2) = sqrt(0.0125) = ~0.1118
    assert res["rss_tolerance_mm"] == pytest.approx(0.112, abs=1e-2)
    assert "پاس شد" in res["worst_case_status"]
    assert "پاس شد" in res["rss_status"]


def test_tolerance_monte_carlo_simulation():
    analyzer = ToleranceStackupAnalyzer()
    dims = [
        {"name": "Slot", "nominal": 50.0, "tol": 0.10, "dir": +1},
        {"name": "Block", "nominal": 49.5, "tol": 0.05, "dir": -1},
    ]
    limits = {"min": 0.20, "max": 0.80}
    mc = analyzer.simulate_monte_carlo(dims, limits, samples=5000)

    assert mc["samples"] == 5000
    assert mc["mean_gap_mm"] == pytest.approx(0.50, abs=0.02)
    assert mc["yield_rate_percent"] > 99.0


def test_cnc_machining_estimator():
    estimator = CncMachiningEstimator(hourly_cnc_rate=450_000)
    res = estimator.estimate_part_manufacturing(
        part_name="Bracket",
        material="Aluminum 6061-T6",
        rough_volume_cm3=500.0,
        final_volume_cm3=200.0,
        hole_count=4,
        material_cost_toman=500_000,
        machine_type="3_AXIS_CNC_MILL"
    )

    assert res["removed_volume_cm3"] == 300.0
    assert res["cutting_time_min"] == pytest.approx(300.0 / 120.0, rel=1e-2)
    assert res["total_machining_time_min"] > 0
    assert res["total_manufacturing_cost_toman"] > 500_000


def test_dfm_checks():
    tool = SolidWorksAutomationTool(simulation_mode=True)
    sheet_check = tool.run_dfm_checks("Chassis", "Sheet Metal خمکاری", thickness_mm=2.0)
    assert "تأیید DFM" in sheet_check["DFM_Status"]

    cnc_check = tool.run_dfm_checks("Shaft", "تراشکاری CNC")
    assert "ماشین‌کاری" in cnc_check["DFM_Status"]
