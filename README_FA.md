<a id="readme-top"></a>

<div align="center">

[![English Documentation](https://img.shields.io/badge/Documentation-English-blue.svg?style=for-the-badge)](README.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![SolidWorks API](https://img.shields.io/badge/SolidWorks-API_COM-00539B.svg?style=for-the-badge&logo=dassaultsystemes&logoColor=white)](https://www.solidworks.com/)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![COM Automation](https://img.shields.io/badge/Interop-pywin32-FF6F00.svg?style=for-the-badge)](https://github.com/mhammond/pywin32)

<br />

# ⚙️ خودکارسازی پارامتریک سالیدورکس و مدلسازی قطعات استاندارد مهندسی
### *تولید خودکار چرخدنده‌های ساده و مارپیچ، برینگ‌ها و شفت‌ها از طریق پروتکل Windows COM و تحلیل تنش مکانیکی*

<p align="center">
  <b>یک فریم‌ورک خودکارسازی صنعتی بر پایه Python COM Interop برای نرم‌افزار SolidWorks. این ابزار با دریافت پارامترهای پایه‌ای مهندسی، هندسه دقیق چرخدنده‌ها (منحنی اینولوت استاندارد AGMA)، چرخ‌دنده‌های مارپیچ و برینگ‌ها را به شکل خودکار و در کسری از ثانیه مدل‌سازی نموده، نقشه‌های ساخت دو‌بعدی استخراج کرده و مقادیر تنش خمش دندانه را با روابط لوئیس (Lewis Formula) اعتبارسنجی می‌کند.</b>
  <br /><br />
  <a href="#-معماری-ارتباط-com-و-جریان-کاری"><strong>معماری اتصال COM »</strong></a>
  &nbsp;•&nbsp;
  <a href="#-فرمولاسیون-هندسه-چرخدنده-و-تنش"><strong>روابط تنش و هندسه اینولوت »</strong></a>
  &nbsp;•&nbsp;
  <a href="#-راهنمای-اجرا"><strong>راهنمای اجرا »</strong></a>
</p>

</div>

---

<details open>
  <summary><h2 style="display: inline-block;">📑 فهرست مطالب</h2></summary>
  <ol>
    <li><a href="#-چکیده-پروژه-و-کاربردهای-صنعتی">چکیده پروژه و کاربردهای صنعتی</a></li>
    <li><a href="#-قابلیت‌های-کلیدی">قابلیت‌های کلیدی</a></li>
    <li><a href="#-معماری-ارتباط-com-و-جریان-کاری">معماری ارتباط COM و جریان کاری</a></li>
    <li><a href="#-فرمولاسیون-هندسه-چرخدنده-و-تنش">فرمولاسیون هندسه چرخدنده و تنش</a></li>
    <li><a href="#-پشته-فناوری">پشته فناوری</a></li>
    <li><a href="#-ساختار-فایل‌ها">ساختار فایل‌ها</a></li>
    <li><a href="#-راهنمای-اجرا">راهنمای اجرا</a></li>
    <li><a href="#-مجوز">مجوز</a></li>
  </ol>
</details>

---

## 📌 چکیده پروژه و کاربردهای صنعتی

طراحی دستی قطعات انتقال قدرت در محیط‌های CAD فرایندی تکراری، زمان‌بر و مستعد خطای انسانی در ترسیم پروفیل‌های غیرخطی (نظیر پروفیل دندانه اینولوت چرخدنده) است. این بسته مهندسی:
1. ارتباط دوطرفه بین اسکریپت‌های پایتون و نرم‌افزار SolidWorks را از طریق شیء `SldWorks.Application` در بستر Windows COM برقرار می‌سازد.
2. نقاط پروفیل دندانه را بر اساس روابط پارامتریک سینماتیکی دقیق تولید کرده و از طریق توابع درون‌برنامه‌ای سالیدورکس به عنوان منحنی اسپیلاین (Spline Curve) اکسترود می‌نماید.
3. با اتصال به معادلات استاندارد AGMA، کنترل‌های ابعادی و تنش‌های تئوری خمش و تماس را پیش از تایید نهایی مدل ارزیابی می‌نماید.

---

## 🚀 قابلیت‌های کلیدی

- **ترسیم دقیق منحنی اینولوت (True Involute Profile Generation):** تولید نقاط دقیق منحنی دندانه بدون تقریب‌زنی‌های دایره‌ای مرسوم.
- **تولید خودکار نقشه‌های اجرایی دو بعدی (Automated 2D Technical Drawings):** استخراج خودکار نماهای استاندارد مهندسی، خطوط برش و جدول اطلاعات فنی ابعادی.
- **تولید پارامتریک اتصالات استاندارد و بیرینگ‌ها:** امکان مدل‌سازی بیرینگ‌های شیار عمیق (Deep Groove Ball Bearings) با تعیین قطر داخلی، خارجی و تعداد ساچمه‌ها.
- **محاسبه استحکام خمش بر اساس فرمول لوئیس و ضرایب AGMA:** محاسبه تنش ماکزیمم در ریشه دندانه.

---

## 🏗 معماری ارتباط COM و جریان کاری

```
[User Parameter Inputs] (Module, Teeth Number, Pressure Angle, Face Width)
               │
               ▼
[Python Engineering Core] ─── (Involute Point Cloud Calculation)
               │
               ▼
[pywin32 Dispatcher] ─────── (Windows COM Interface)
               │
               ▼
[SolidWorks Running Instance]
    ├─ CreatePart / OpenTemplate
    ├─ InsertSketch2 / Create2DPoint / CreateSpline
    ├─ FeatureExtrusion3 (Blank & Teeth Cut)
    ├─ CircularPattern (Pattern across Z-axis)
    └─ SaveAs (SLDPRT / STEP / SLDDRW)
```

---

## 📐 فرمولاسیون هندسه چرخدنده و تنش

### ۱. معادلات پارامتریک منحنی اینولوت
نقاط مختصات دندانه در سیستم دکارتی به ازای زاویه غلتش $\theta$:
$$x(\theta) = r_b \cdot (\cos\theta + \theta \sin\theta)$$
$$y(\theta) = r_b \cdot (\sin\theta - \theta \cos\theta)$$
که در آن $r_b = r \cos\alpha$ شعاع دایره مبنا (Base Circle Radius) و $\alpha$ زاویه فشار (معمولاً $20^\circ$) است.

### ۲. تنش خمش ریشه دندانه (فرمول لوئیس - Lewis Bending Stress)
$$\sigma_b = \frac{F_t}{b \cdot m \cdot Y}$$
که در آن:
- $F_t$: نیروی مماسی اعمالی به دندانه ($N$)
- $b$: پهنای دندانه ($mm$)
- $m$: مدول استاندارد چرخدنده ($mm$)
- $Y$: ضریب شکل لوئیس وابسته به تعداد دندانه‌ها

---

## 💻 پشته فناوری

- **زبان برنامه‌نویسی:** Python 3.10+
- **رابط تعامل سیستمی:** `pywin32` (پروتکل COM Automation)
- **محیط CAD هدف:** Dassault Systèmes SolidWorks (2018 تا 2024)
- **محاسبات عددی:** NumPy برای تولید ابر نقاط اسپیلاین اینولوت

---

## 📂 ساختار فایل‌ها

```
02-solidworks-cad-automation/
├── solidworks_automation.py  # هسته اتصال COM و کنترل اتوماسیون
├── gear_generator.py         # تولید پارامتریک و ترسیم پروفیل چرخدنده
├── bearing_generator.py      # مدلسازی قطعات بیرینگ استاندارد
├── test_automation.py        # آزمون‌های اعتبارسنجی اتصال و تولید مدل
├── README.md                 # مستندات انگلیسی
└── README_FA.md              # مستندات دانشگاهی فارسی
```

---

## ⚙️ راهنمای اجرا

1. نرم‌افزار SolidWorks را روی سیستم عامل ویندوز اجرا کنید.
2. کتابخانه `pywin32` را نصب نمایید:
   ```bash
   pip install pywin32 numpy
   ```
3. اسکریپت تولید چرخدنده را اجرا نمایید:
   ```bash
   python gear_generator.py --module 3.0 --teeth 24 --face-width 20 --pressure-angle 20
   ```
   مدل سه بعدی به طور زنده در محیط سالیدورکس ساخته شده و فایل `.SLDPRT` در پوشه جاری ذخیره خواهد شد.

---

## 📄 مجوز
این پروژه تحت مجوز [MIT](https://opensource.org/licenses/MIT) منتشر شده است.
