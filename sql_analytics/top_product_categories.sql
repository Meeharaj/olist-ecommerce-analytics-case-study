-- Top Product Categories by Revenue (Market Analysis)
-- The Business Problem: Procurement and warehousing managers want to know which macro product lines bring in the highest raw dollar amounts so they can prioritize
--  vendor acquisitions.

-- The SQL Logic: We join three tables: order_items (for pricing metrics), products (to link keys),
--  and translation (to display names in English instead of Portuguese). We group by the translated name and sort dynamically.

                  SELECT TOP 5 
                      p.product_category_name_english AS category,
                      COUNT(DISTINCT oi.order_id) AS total_orders_placed,
                      ROUND(SUM(oi.price), 2) AS total_gross_revenue
                  FROM olist_order_items_dataset oi
                  JOIN clean_products p ON oi.product_id = p.product_id
                  GROUP BY p.product_category_name_english
                  ORDER BY total_gross_revenue DESC;

-- What the Actual Data Tells Us (The Insight):
-- The top 5 product categories driving the entire platform's financial engine are:

-- Health & Beauty: $1,258,681.34 (8,836 orders)

-- Watches & Gifts: $1,205,005.68 (5,624 orders)

-- Bed, Bath & Table: $1,036,988.68 (9,417 orders)

-- Sports & Leisure: $988,048.97 (7,720 orders)

-- Computers Accessories: $911,954.32 (6,689 orders)