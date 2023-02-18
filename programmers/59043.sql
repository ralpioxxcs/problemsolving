# https://school.programmers.co.kr/learn/courses/30/lessons/59043
SELECT ai.ANIMAL_ID, ai.NAME FROM ANIMAL_INS ai
LEFT JOIN ANIMAL_OUTS ao ON ai.ANIMAL_ID = ao.ANIMAL_ID
WHERE ai.DATETIME > ao.DATETIME
ORDER BY ai.DATETIME