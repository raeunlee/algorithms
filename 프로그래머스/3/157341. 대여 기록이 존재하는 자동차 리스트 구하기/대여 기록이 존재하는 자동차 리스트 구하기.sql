-- 코드를 입력하세요
SELECT DISTINCT C.CAR_ID
FROM CAR_RENTAL_COMPANY_CAR AS C JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H 
ON C.CAR_ID = H.CAR_ID
WHERE H.START_DATE LIKE '2022-10-%' AND C.CAR_TYPE = '세단'
ORDER BY CAR_ID DESC