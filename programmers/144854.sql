# https://school.programmers.co.kr/learn/courses/30/lessons/144854
SELECT bk.BOOK_ID, atr.AUTHOR_NAME, DATE_FORMAT(bk.PUBLISHED_DATE, "%Y-%m-%d") AS "PUBLISHED_DATE" FROM BOOK bk
LEFT JOIN AUTHOR atr ON atr.AUTHOR_ID = bk.AUTHOR_ID
WHERE bk.CATEGORY = "경제"
ORDER BY PUBLISHED_DATE