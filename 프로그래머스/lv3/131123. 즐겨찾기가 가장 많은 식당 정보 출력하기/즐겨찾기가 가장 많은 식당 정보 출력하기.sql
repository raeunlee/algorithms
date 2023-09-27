SELECT food_type, rest_id, rest_name, favorites
from rest_info 
WHERE FAVORITES IN(
    SELECT MAX(FAVORITES) FROM REST_INFO
    GROUP BY FOOD_TYPE
)

GROUP BY 1
ORDER BY 1 DESC