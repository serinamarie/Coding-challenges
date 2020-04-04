-- write a SQL query to count the number of unique users per day who logged in from both iPhone and web,
-- where iPhone logs and web logs are in distinct relations 

iphone: ts | user_id | iphone_sessionid
web: ts | user_id | web_sessionid

-- 1) inner join iphone and web tables
-- 2) match by day and user_id
-- 3) get a count

day | num_unique_users

SELECT DATE_TRUNC('day', i.ts) AS day,
    COUNT(DISTINCT(i.user_id)) AS num_users
FROM iphone i
JOIN web w
    ON i.user_id = w.user_id
    AND DATE_TRUNC('day', i.ts) = DATE_TRUNC('day', w.ts)
GROUP BY 1

web: ts | user_id |iphone_sessionid | web_sessionid

---------

-- new question

-- Mary is a teacher in a middle school and she has a table 'seat' storing
-- students' names and their corresponding seat ids.
-- The column id is continuous increment.
-- Mary wants to change seats for the adjacent students.
-- Can you write a SQL query to output the result for Mary?


SELECT
    (CASE 
        WHEN MOD(id,2) != 0 AND id = tc THEN id
        WHEN MOD(id,2) != 0 THEN id + 1
        ELDE id - 1 END) AS id
FROM seat, (SELECT COUNT(*) AS tc FROM seat) AS total_counts
ORDER BY id