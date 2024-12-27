-- Table: Transactions

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | country       | varchar |
-- | state         | enum    |
-- | amount        | int     |
-- | trans_date    | date    |
-- +---------------+---------+
-- id is the primary key of this table.
-- The table has information about incoming transactions.
-- The state column is an enum of type ["approved", "declined"].
 

-- Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.

-- Return the result table in any order.

select DATE_FORMAT(trans_date, '%Y-%m') as month,
country,
count(*) as trans_count,
COUNT(CASE WHEN state = 'approved' THEN 1 END) as approved_count,
SUM(amount) as trans_total_amount,
SUM(CASE WHEN state = 'approved' then amount ELSE 0 END) as approved_total_amount
from Transactions 
group by DATE_FORMAT(trans_date, '%Y-%m'), country
order by DATE_FORMAT(trans_date, '%Y-%m'), country