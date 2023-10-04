
SELECT year(sales_date) as year, month(sales_date) as month, count(distinct user_id) as puchased_users,
# 구매 비율
round(count(distinct user_id)/(select count(*) from user_info where year(joined)=2021),1) as puchased_ratio
from online_sale
where user_id in (
    select user_id
    from user_info
    where year(joined) = 2021)
group by year(sales_date), month(sales_date)
order by year, month