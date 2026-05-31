# olist-ecommerce-analytics-case-study
An end-to-end e-commerce analytics case study using Python for data engineering, advanced SQL for business diagnostics, and Power BI to build an interactive 2-tab executive sales &amp; supply chain logistics optimization dashboard.

______________________________________________________________________________________________________________________________________________________________________
# Olist’s Business Model
Olist is a Brazilian departmental store (marketplace) that operates in e-commerce segment, but is not an e-commerce itself (as she says). It operates as a SaaS (Software as a Service) technology company since 2015. It offers a marketplace solution (of e-commerce segment) to shopkeepers of all sizes (and for most segments) to increase their sales whether they have online presence or not

___________________________________________________________________________________________________________________________________________________________________

# 🇧🇷 Olist E-Commerce Marketplace: End-to-End Sales & Logistics Optimization Case Study

## 🎯 Project Overview & Executive Summary
This repository contains a full-scale enterprise analytics solution transforming **100,000 real-world Brazilian marketplace transactions** into an interactive business intelligence asset. Moving from raw, unindexed transactional logs to an optimized Star-Schema data warehouse, this project tracks macro revenue trajectories, maps logistical bottlenecks, and explicitly measures the impact of fulfillment delays on customer churn and brand retention.

---

## ⚡ Skills Demonstrated
* **Python (Pandas & NumPy):** Automated automated data parsing, handling of structural nulls, and programmatic date-type enforcement.
* **Relational SQL:** Developed advanced metrics utilizing **Common Table Expressions (CTEs)**, **Multi-Table Joins**, and **Window Functions (`LAG()`)**.
* **Power BI & Data Modeling:** Implemented a performant **Star-Schema relational layout**, explicit **DAX measure groups**, data categorization, and multi-axis strategic charts.

---

## 💼 The Business Problem
Olist leadership faced two major operational blindspots:
1. **Revenue Volatility:** Executive teams lacked a granular view of Month-over-Month (MoM) momentum and did not have predictive modeling to forecast upcoming demand peaks.
2. **Fulfillment Friction:** High freight costs and delivery exceptions were heavily penalizing sales margins, but the logistics team could not quantify exactly how shipping delays directly impacted public customer reviews.

---

## 🛠️ Project Architecture & Methodology

### 🔹 Step 1: Automated Pipeline & Schema Enforcement (Python)
Raw database records parsed temporal elements as default string objects, breaking potential database indexes. A pipeline was built to cast fields explicitly and impute empty review logs with system fallback values.

# python 
import pandas as pd

def clean_review_pipeline(file_path):
    df = pd.read_csv(file_path)
    
    # Enforce strict chronological datatypes
    date_fields = ['review_creation_date', 'review_answer_timestamp']
    for field in date_fields:
        df[field] = pd.to_datetime(df[field])
        
    # Standardize string nulls to ensure record preservation
    df['review_comment_title'] = df['review_comment_title'].fillna('No Title Provided').astype(str)
    df['review_comment_message'] = df['review_comment_message'].fillna('No Message Provided').astype(str)
    
    return df

# Relational Financial Analytics (SQL)
 To evaluate corporate growth trajectories, advanced diagnostic queries were executed to measure MoM revenue velocity.

 WITH MonthlyAggregates AS (
    SELECT 
        strftime('%Y-%m', o.order_purchase_timestamp) AS calendar_month,
        SUM(p.payment_value) AS gross_revenue
    FROM orders o
    JOIN payments p ON o.order_id = p.order_id
    WHERE o.order_status = 'delivered'
    GROUP BY 1
)
SELECT 
    calendar_month,
    ROUND(gross_revenue, 2) AS current_month_sales,
    ROUND(LAG(gross_revenue) OVER (ORDER BY calendar_month), 2) AS prior_month_sales,
    ROUND(((gross_revenue - LAG(gross_revenue) OVER (ORDER BY calendar_month)) / 
           LAG(gross_revenue) OVER (ORDER BY calendar_month)) * 100, 2) AS mom_growth_pct
FROM MonthlyAggregates;

# Interactive Visual Application (Power BI)

 The curated dataset was imported into Power BI to create a dynamic, 2-tab diagnostic environment.

📊 Tab 1: Executive Sales & Market Performance

# Financial Ribbon:
       Tracks Total Gross Revenue, Volume Processed, Average Order Value (AOV), and Net Satisfaction via isolated DAX measures.
# Predictive Forecasting: 
        Features an advanced monthly time-series chart with a built-in 3-month predictive trend overlay.
# Geospatial Processing:
       Standardized 2-letter state abbreviations by engineering a custom contextual column to map global order densities correctly over SouthAmerica
           State Full Context= {customer_state} &", Brazil"
          
# 🚛 Tab 2: Logistics & Operations Optimization
Built specifically for supply chain managers to optimize performance and prevent customer churn.

# Fulfillment Drift Chart:
       Overlays regional Days Ahead of Schedule directly against the Customer Satisfaction Index to prove that shipping delays immediately hurt public brand              Rating.
# Shipping Cost Elasticity Plot: 
     Correlates product weight against freight charges, enabling managers to visually isolate regional pricing outliers.

# 📈 Key Insights & Strategic Recommendations
# Logistical Impacts on Brand Loyalty: 
    Data analysis confirmed a strong correlation between shipping delays and drop-offs in customer reviews. States showing a decline in target delivery speeds         experienced a sharp drop in satisfaction indices.

# Targeted Fulfillment Restructuring: 
     Operations should prioritize third-party carrier audits in lagging territories to stabilize core regional hubs.

# Inventory Scaling:
    Marketing expenditures and fulfillment space should expand to favor the Health & Beauty and Watches & Gifts categories, which represent the top marketplace        revenue drivers.

# 📬 Contact & Links
LinkedIn:https://www.linkedin.com/in/meharaj-jamadar-7034a5401/
Email: jamadarmeharaj@gmail.com
