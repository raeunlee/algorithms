select p.product_code, sum(s.sales_amount * p.price) as sales
from product as p join offline_sale as s on p.product_id = s.product_id
group by product_code
order by sales desc, p.product_code asc