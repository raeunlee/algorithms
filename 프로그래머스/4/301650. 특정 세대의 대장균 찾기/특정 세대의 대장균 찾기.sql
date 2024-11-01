-- 코드를 작성해주세요
# a.parent_id, b.id, b.parent_id, c.id, c.parent_id

select a.id
from ecoli_data a 
    left join ecoli_data b on a.parent_id = b.id
    left join ecoli_data c on b.parent_id = c.id
where a.parent_id is not null && b.id is not null && b.parent_id is not null && c.id is not null && c.parent_id is null
order by a.id
    