with tmp as (
    select car_id
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where start_date <= '2022-10-16' and
    end_date >= '2022-10-16')
   -- WHERE START_DATE <= '2022-10-16' AND END_DATE >= '2022-10-16'
select distinct CAR_ID,
    case 
        when car_id in (select * from tmp) then '대여중'
        else '대여 가능'
        end as AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
order by car_id desc