# 우유를 산 테이블과 요거트를 산 테이블 각각을 구함 
with tmp as (
select *
from cart_products
where name = 'Milk') ,
tmp2 as (
select *
from cart_products
where name = 'Yogurt'
)

# 그리고 그 테이블 중 카트 아이디가 같은것을 고른다
select t2.cart_id
from tmp t join tmp2 t2 on t.cart_id = t2.cart_id
group by t2.cart_id