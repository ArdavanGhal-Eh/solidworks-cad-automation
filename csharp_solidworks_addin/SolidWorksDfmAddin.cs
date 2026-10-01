using System;

namespace SolidWorksDfmAddin
{
    public class DfmValidator
    {
        public static bool CheckSheetMetalBend(double thicknessMm, double bendRadiusMm)
        {
            // DFM Rule: Minimum bend radius >= thickness
            return bendRadiusMm >= thicknessMm;
        }

        public static void Main()
        {
            Console.WriteLine("SolidWorks Native C# .NET DFM Engine Initialized.");
            bool pass = CheckSheetMetalBend(3.0, 3.5);
            Console.WriteLine($"Sheet Metal Bend DFM Status: {(pass ? "PASS" : "FAIL")}");
        }
    }
}
