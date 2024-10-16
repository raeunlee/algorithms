-- 코드를 작성해주세요

with tmp as(
    select E.EMP_NO, E.EMP_NAME,
        case 
            when avg(G.SCORE) >= 96 then 'S'
            when avg(G.SCORE) >= 90 then 'A'
            when avg(G.SCORE) >= 80 then 'B'
            else 'C'
        end as GRADE,
        
        case
            when avg(G.SCORE) >= 96 then E.SAL * 0.2
            when avg(G.SCORE) >= 90 then E.SAL * 0.15
            when avg(G.SCORE) >= 80 then E.SAL * 0.10
            else SAL * 0 
        end BONUS
    
    from HR_GRADE G JOIN HR_EMPLOYEES E ON E.EMP_NO = G.EMP_NO
    group by E.EMP_NO 
)


select *
from TMP