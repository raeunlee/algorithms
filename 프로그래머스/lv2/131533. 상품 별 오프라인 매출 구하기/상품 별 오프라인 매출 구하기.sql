-- 코드를 입력하세요
-- 프로덕트 아이디로 join 하자! --> 판매가 * 판매량 
-- 프로덕트 테이블의 프로덕트 코드, 오프라인 세일의 판매량? = sales

SELECT P.PRODUCT_CODE, sum(P.PRICE * S.SALES_AMOUNT) AS SALES
FROM PRODUCT P
    JOIN OFFLINE_SALE S
    ON P.PRODUCT_ID = S.PRODUCT_ID
GROUP BY P.PRODUCT_CODE
ORDER BY SALES DESC, PRODUCT_CODE
