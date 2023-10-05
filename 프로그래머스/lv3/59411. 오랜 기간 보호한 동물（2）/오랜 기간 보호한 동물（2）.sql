with tmp1 as( 
    select *
    from animal_ins), 
    tmp2 as(
    select *
    from animal_outs)

SELECT t1.ANIMAL_ID, t1.NAME
FROM tmp1 t1 join tmp2 t2 on t1.animal_id = t2.animal_id
order by t2.datetime - t1.datetime desc
limit 2

