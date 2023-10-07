Select b.author_id, a.author_name, b.category,
    sum(bs.sales * b.price) as total_sales
    
from book as b join author as a on b.author_id = a.author_id
    join book_sales as bs on b.book_id = bs.book_id 
    
where bs.sales_date like '2022-01%'

group by 1, 3

order by 1 asc, 3 desc