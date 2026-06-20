# Write your MySQL query statement below
SELECT product_name, year, price  FROM 
SALES INNER JOIN PRODUCT ON 
SALES.product_id = PRODUCT.product_id ;