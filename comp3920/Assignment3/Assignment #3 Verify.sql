#Verify Base and Summary Tables in bigtoys.
use bigtoys;
describe sales_by_sales_person_summary;
describe sales_by_status_summary;
describe sales_by_user_summary;
select count(*) AS 'sales_by_sales_person_summary' from sales_by_sales_person_summary;
select count(*) AS 'sales_by_status_summary' from sales_by_status_summary;
select count(*) AS 'sales_by_user_summary' from sales_by_user_summary;
select uuid(), utc_timestamp();
select * from sales_by_sales_person_summary order by year, month, frn_sales_person_id;
select * from sales_by_status_summary order by year, month, frn_purchase_status_id;
select * from sales_by_user_summary order by purchase_year, purchase_month, birth_year;
show create event Monthly_Sales_Person_Summary_Data;
show create event Monthly_Sales_Status_Summary_Data;
show create event Monthly_Sales_User_Summary_Data;
