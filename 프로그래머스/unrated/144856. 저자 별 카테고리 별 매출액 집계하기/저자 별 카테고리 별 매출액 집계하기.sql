select b.author_id, a.author_name, b.category, sum(b.price*s.sales) as total_sales
from book b join author a on b.author_id = a.author_id
    join book_sales s on b.book_id = s.book_id
where s.sales_date like '2022-01-%'
group by a.author_id, b.category
order by a.author_id, b.category desc