
-- sales_by_sales_person_summary table 
INSERT INTO sales_by_sales_person_summary (num_toys_sold, sales_dollars, frn_sales_person_id, Year, Month)
SELECT COUNT(pi.purchase_item_id) AS num_toys_sold,
       SUM(t.price) AS sales_dollars,
       p.frn_sales_person_id AS frn_sales_person_id,
       YEAR(p.purchase_date) AS Year,
       MONTH(p.purchase_date) AS Month
FROM purchase p
INNER JOIN purchase_item pi ON p.purchase_id = pi.frn_purchase_id
INNER JOIN toy t ON pi.frn_toy_id = t.toy_id
INNER JOIN sales_person sp ON p.frn_sales_person_id = sp.sales_person_id
GROUP BY p.frn_sales_person_id, Year, Month;

-- sales_by_status_summary
INSERT INTO sales_by_status_summary (total_sales, frn_purchase_status_id, Year, Month)
SELECT 
    COUNT(purchase_id) AS total_sales,
    frn_purchase_status_id,
    YEAR(purchase_date) AS Year,
    MONTH(purchase_date) AS Month
FROM purchase
GROUP BY frn_purchase_status_id, Year, Month;

-- sales_by_user_summary
INSERT INTO sales_by_user_summary (num_toys_sold, sales_total, birth_year, purchase_year, purchase_month)
SELECT 
    COUNT(pi.purchase_item_id) AS num_toys_sold,
    SUM(t.price) AS sales_total,
    YEAR(u.birth_date) AS birth_year,
    YEAR(p.purchase_date) AS purchase_year,
    MONTH(p.purchase_date) AS purchase_month
FROM purchase p
INNER JOIN purchase_item pi ON pi.frn_purchase_id = p.purchase_id
INNER JOIN toy t ON pi.frn_toy_id = t.toy_id
INNER JOIN user u ON p.frn_user_id = u.user_id
GROUP BY YEAR(u.birth_date), YEAR(p.purchase_date), MONTH(p.purchase_date); 

-- query1 on Summary table 
SELECT ssps.frn_sales_person_id, sp.first_name, sp.last_name, ssps.num_toys_sold
FROM sales_by_sales_person_summary ssps
INNER JOIN sales_person sp
    ON ssps.frn_sales_person_id = sp.sales_person_id
WHERE ssps.Year = 2018
    AND ssps.Month = 12
ORDER BY ssps.num_toys_sold DESC
LIMIT 5;

-- count the row
SELECT COUNT(*) AS total_rows
FROM sales_by_sales_person_summary
INNER JOIN sales_person 
    ON sales_by_sales_person_summary.frn_sales_person_id = sales_person.sales_person_id;

-- query2 on Summary table
SELECT ssps.frn_sales_person_id, sp.first_name, sp.last_name, ssps.sales_dollars as salesTotal
FROM sales_by_sales_person_summary ssps
INNER JOIN sales_person sp ON ssps.frn_sales_person_id = sp.sales_person_id
WHERE ssps.Year = 2018 AND ssps.Month = 12
ORDER BY ssps.sales_dollars DESC
LIMIT 5;


-- query3 on Summary table
SELECT 
    SUM(total_sales) AS totalSales,
    SUM(IF(frn_purchase_status_id = 3, total_sales, NUll)) AS Shipped,
    CONCAT(
        (SUM(CASE WHEN frn_purchase_status_id = 3 THEN total_sales ELSE 0 END) /
        SUM(total_sales) * 100),
        '%'
    ) AS CompletedPercent
FROM sales_by_status_summary
WHERE Year = 2018
    AND (Month = 12 OR Month IS NULL);
    
-- count the row
SELECT COUNT(*) AS total_rows
FROM sales_by_status_summary;
    
-- query4 on Summary table
SELECT 
    num_toys_sold AS numToysSold,
    sales_total AS salesTotal,
    birth_year,
    purchase_year - birth_year AS Age,
    purchase_year
FROM sales_by_user_summary
WHERE purchase_year = 2018
    AND purchase_month = 12
ORDER BY salesTotal DESC
LIMIT 5;

-- count the row
SELECT COUNT(*) AS total_rows
FROM sales_by_user_summary;
    

-- Create the scheduled event for Monthly Sales Person Summary Data
CREATE EVENT Monthly_Sales_Person_Summary_Data
ON SCHEDULE
    EVERY 1 MONTH
    STARTS CONCAT(LAST_DAY(CURRENT_DATE() - INTERVAL 1 MONTH) + INTERVAL 1 DAY, ' 23:00:00')
COMMENT 'Run monthly on the 15th at 11:00 PM'
DO
    INSERT INTO sales_by_sales_person_summary (num_toys_sold, sales_dollars, frn_sales_person_id, Year, Month)
    SELECT COUNT(pi.purchase_item_id) AS num_toys_sold,
           SUM(t.price) AS sales_dollars,
           p.frn_sales_person_id AS frn_sales_person_id,
           YEAR(p.purchase_date) AS Year,
           MONTH(p.purchase_date) AS Month
    FROM purchase p
    INNER JOIN purchase_item pi ON p.purchase_id = pi.frn_purchase_id
    INNER JOIN toy t ON pi.frn_toy_id = t.toy_id
    INNER JOIN sales_person sp ON p.frn_sales_person_id = sp.sales_person_id
    WHERE YEAR(p.purchase_date) = YEAR(CURRENT_DATE() - INTERVAL 1 MONTH)
        AND MONTH(p.purchase_date) = MONTH(CURRENT_DATE() - INTERVAL 1 MONTH)
    GROUP BY p.frn_sales_person_id, Year, Month;
  
  
-- Create the scheduled event for Monthly Sales Status Summary Data
CREATE EVENT Monthly_Sales_Status_Summary_Data
ON SCHEDULE
    EVERY 1 MONTH
    STARTS CONCAT(LAST_DAY(CURRENT_DATE() - INTERVAL 1 MONTH) + INTERVAL 1 DAY, ' 23:20:00')
DO
    INSERT INTO sales_by_status_summary (total_sales, frn_purchase_status_id, Year, Month)
    SELECT 
        COUNT(purchase_id) AS total_sales,
        frn_purchase_status_id,
        YEAR(purchase_date) AS Year,
        MONTH(purchase_date) AS Month
    FROM purchase
    WHERE YEAR(purchase_date) = YEAR(CURRENT_DATE() - INTERVAL 1 MONTH)
        AND MONTH(purchase_date) = MONTH(CURRENT_DATE() - INTERVAL 1 MONTH)
    GROUP BY frn_purchase_status_id, Year, Month;

  
  -- Create the scheduled event for Monthly Sales User Summary Data
CREATE EVENT Monthly_Sales_User_Summary_Data
ON SCHEDULE
    EVERY 1 MONTH
    STARTS CONCAT(LAST_DAY(CURRENT_DATE() - INTERVAL 1 MONTH) + INTERVAL 1 DAY, ' 23:40:00')
DO
    INSERT INTO sales_by_user_summary (num_toys_sold, sales_total, birth_year, purchase_year, purchase_month)
    SELECT 
        COUNT(pi.purchase_item_id) AS num_toys_sold,
        SUM(t.price) AS sales_total,
        YEAR(u.birth_date) AS birth_year,
        YEAR(p.purchase_date) AS purchase_year,
        MONTH(p.purchase_date) AS purchase_month
    FROM purchase p
    INNER JOIN purchase_item pi ON pi.frn_purchase_id = p.purchase_id
    INNER JOIN toy t ON pi.frn_toy_id = t.toy_id
    INNER JOIN user u ON p.frn_user_id = u.user_id
    WHERE YEAR(p.purchase_date) = YEAR(CURRENT_DATE() - INTERVAL 1 MONTH)
        AND MONTH(p.purchase_date) = MONTH(CURRENT_DATE() - INTERVAL 1 MONTH)
    GROUP BY YEAR(u.birth_date), YEAR(p.purchase_date), MONTH(p.purchase_date);


SHOW EVENTS;
DROP EVENT Monthly_Sales_Person_Summary_Data;




