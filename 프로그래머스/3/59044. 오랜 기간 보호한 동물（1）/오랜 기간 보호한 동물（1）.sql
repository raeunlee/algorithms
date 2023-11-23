select name, datetime
from animal_ins
#animal in에 있는데 animal out에는 없는 동물 중 
where animal_id not in( 
    select animal_id
    from animal_outs)
order by datetime
limit 3
