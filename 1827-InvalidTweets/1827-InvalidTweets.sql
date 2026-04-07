-- Last updated: 07/04/2026, 11:35:44
# Write your MySQL query statement belowSELECT tweet_id
SELECT tweet_id
FROM Tweets
WHERE CHAR_LENGTH(content) > 15;