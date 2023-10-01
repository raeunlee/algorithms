-- 코드를 입력하세요
select concat('/home/grep/src/',B.BOARD_ID, '/', F.FILE_ID, F.FILE_NAME, F.FILE_EXT) as FILE_PATH
from USED_GOODS_BOARD B join USED_GOODS_FILE F on B.BOARD_ID = F.BOARD_ID

WHERE B.BOARD_ID = (
    SELECT BOARD_ID FROM USED_GOODS_BOARD 
    order by views desc
    limit 1)

order by F.file_id desc

