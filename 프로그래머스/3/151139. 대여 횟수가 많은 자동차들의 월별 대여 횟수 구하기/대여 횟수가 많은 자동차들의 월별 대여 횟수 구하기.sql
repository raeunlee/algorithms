Select month(start_date) as month, car_id, count(car_id) as records
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where car_id in (
    select car_id
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
    group by car_id
    having count(car_id) >= 5
) and START_DATE BETWEEN '2022-08-01' AND '2022-10-31'

group by car_id, month
order by month asc, car_id desc
