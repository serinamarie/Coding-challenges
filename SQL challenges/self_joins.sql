  
-- 1. How many stops are in the database.
SELECT COUNT(*) AS num_stops 
FROM stops;

-- 2. Find the id value for the stop 'Craiglockhart'
-- filter for stops.name 'Craiglockhart'
-- return id 

SELECT id
FROM stops
WHERE name = 'Craiglockhart';

-- 3. Give the id and the name for the stops on the '4' 'LRT' service.
-- join the stops and route table on route.stop = stops.id
-- filter for company = 'LRT'
-- return stops.id, stops.name


SELECT id, name
FROM stops
JOIN route on route.stop=stops.id
WHERE num = '4'
AND company = 'LRT';