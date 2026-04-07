-- Last updated: 07/04/2026, 11:36:56
# Write your MySQL query statement below

select  distinct
Product.product_name ,Sales.year , Sales.price 
from 
Sales
left join Product on Sales.product_id= Product.product_id ;