-- Last updated: 07/04/2026, 11:38:27
# Write your MySQL query statement below


select name ,population , area 
from World 
where area >= 3000000 or  population >= 25000000 ;