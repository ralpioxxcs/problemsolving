# https://school.programmers.co.kr/learn/courses/30/lessons/132204
SELECT ap.APNT_NO, pt.PT_NAME, ap.PT_NO, ap.MCDP_CD, dt.DR_NAME, ap.APNT_YMD FROM APPOINTMENT ap
LEFT JOIN DOCTOR dt ON ap.MDDR_ID = dt.DR_ID
LEFT JOIN PATIENT pt ON ap.PT_NO = pt.PT_NO
WHERE DATE_FORMAT(APNT_YMD, "%Y-%m-%d") = "2022-04-13" AND ap.APNT_CNCL_YN = "N" AND dt.MCDP_CD = "CS"
ORDER BY ap.APNT_YMD