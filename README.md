# 📊 A/B Testing Conversion Analysis | Python | Data Analytics Project

## 🚀 Executive Summary

This end-to-end analytics project evaluates **conversion performance** of an old vs. new landing page using **Python**, **pandas**, and **matplotlib**.

The objective is to simulate how a data analyst supports product and marketing teams by analyzing user behavior, calculating conversion rates, performing **statistical significance tests (Z-test)**, and providing actionable recommendations for website optimization.

**Workflow:**  
Raw Data → Data Cleaning → Conversion Rate Analysis → Statistical Testing → Visualization → Actionable Insights

---

## 🧠 Business Questions Answered

- What is the **conversion rate** for the old landing page vs. the new landing page?  
- Is the difference in conversion **statistically significant**?  
- Should the new landing page be **launched or kept in testing**?  
- How do conversion rates differ visually between the two pages?

---

## 🛠 Tech Stack

- Python 3.x  
- pandas (Data manipulation)  
- numpy (Statistical calculations)  
- matplotlib (Visualization)  
- CSV dataset handling  
- Statistical Analysis (Z-test)

---

## 📂 Repository Structure

```
ab-testing-conversion-analysis/
│
├── data/
│   └── ab_data.csv
│
├── images/
│   └── conversion_rate_chart.png
│
├── ab_test.py
└── README.md

```

---

## 🔍 Analytical Framework

### 1️⃣ Data Cleaning
- Remove rows where `group` and `landing_page` do not match  
- Remove duplicate users to prevent double-counting  

### 2️⃣ Conversion Rate Calculation
- Calculate **mean conversion rates** for control (old page) and treatment (new page) groups  

### 3️⃣ Statistical Testing (Z-test)
- Calculate pooled probability and standard error  
- Compute Z-score for conversion rate difference  
- Determine statistical significance (95% confidence interval)

### 4️⃣ Final Recommendation
- Launch new page if Z-score > 1.96  
- Keep old page if difference is not significant  

### 5️⃣ Visualization
- Bar chart showing **control vs. treatment conversion rates**  
- Annotated chart with percentages for clarity

---

## 📈 Key Results (Sample Output)

- Control Group (Old Page) Conversion Rate: **12.0%**  
- Treatment Group (New Page) Conversion Rate: **12.3%**  
- Z-Score: **2.56**  
- **Conclusion:** New Page is statistically better. **Launch it.**

---

## 📊 Visualization

![Conversion Rate Chart](images/conversion_rate_chart.png)

> The chart visually compares conversion rates between control and treatment groups.

---

## 💡 Business Impact

✔ Quantified the impact of a new landing page  
✔ Recommended data-driven decision on page launch  
✔ Improved understanding of user behavior and conversion efficiency  
✔ Visualized results for clear stakeholder communication

---

## 📌 Skills Demonstrated

- Python Data Manipulation (`pandas`)  
- Statistical Analysis (Z-test)  
- Data Cleaning & Deduplication  
- Data Visualization (`matplotlib`)  
- Business Decision Support based on Analytics  

---

## 🚀 Next Steps (Optional but Impressive)
- Segment A/B test by **device type or geography**  
- Run **multi-page A/B experiments** simultaneously  
- Incorporate **confidence intervals in charts**  
- Automate report generation for management dashboards

---

## 📦 Data Availability

The `ab_data.csv` dataset is included for running the analysis.  
Can be replaced with any similar dataset for replication or further testing.

---

## 👤 Author

**Y. Rithvesh**  
Python | Data Analytics | A/B Testing  
Date: 15-02-2026  

