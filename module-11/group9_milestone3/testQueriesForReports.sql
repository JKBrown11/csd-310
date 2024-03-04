-- We cannot run this entire file, as some of the code doesn't work. I've
-- added notes throughout but I'm stuck in several places. The only 
-- one complete is the 6 months of customers. 

use wilson_financial; 

# Last 6 months of new customers
-- This one works as screenshotted in discord.
select concat(f_name, ' ', l_name) as 'Client_Name', monthname(date_added) as 'Month_Added'
from clients 
where date_added >= '2023-09-01' AND date_added < '2024-03-01';

-- --------------------------------------------
-- this math is correct, but I don't know if we would lose points for using 8. 
-- We can manually divide by the number of clients. 
SELECT sum(transactions.amount)/8 AS average_assets
FROM transactions
JOIN accounts ON transactions.account_id = accounts.account_id;

-- shows all account balances
-- Created View, maybe we can get total average from this in Python?
-- it will import as [100, 3000, 101, 3000, ....] so I'm thinking we could try
-- to iterate through the second sets by starting at i=1, and +2 every time to get the sum
-- and use length/2 for the number of accounts or balances to average over. 
create view all_account_balances as 
select accounts.account_id as account_number, 
sum(transactions.amount) as balance
from accounts
left join transactions using (account_id)
group by account_id;
select * from all_account_balances;

-- Attempted balances with names
-- Error code 1055 bc clients isn't dependent on anything?
select concat(c.f_name, ' ', c.l_name) as 'Client Name',
	a.account_id as 'Account Number', sum(t.amount) as balance
from transactions t
left join clients c using (client_id)
left join accounts a using (account_id)
group by 'Client Name';
    
    
-- notes from trying to average all balances.
-- math is wrong here
select (sum(transactions.amount))/count(accounts.account_id) as 'Average Balance of all assets'
from transactions
join accounts using (account_id);

-- can't use a function on a view.
select sum(all_account_balances.balance) as total_asset_average;

-- these are mathematially correct, but they don't divide correctly.
select count(accounts.account_id) as NumAccts from accounts;
select sum(transactions.amount) as total_balance from transactions;

-- Hlee's idea for average of all assets, incorrect math as well. 
SELECT AVG(transactions.amount) AS average_assets
FROM transactions
JOIN accounts ON transactions.account_id = accounts.account_id;



-- more than 10 transactions per month
-- This currently does all the transactions ever. 
-- how to acheive per month?
select concat(c.f_name, ' ', c.l_name) as Client_Name, count(t.trans_id)
from clients c
left join transactions t on t.client_id = c.client_id
group by Client_Name
having count(t.trans_id) > 10;
-- where count(t.trans_id) > 10;
-- and t.transaction_date between '2023-01-01' and '2023-01-31'