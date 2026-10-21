--order by
select * from products 
order by price   --ASC for ascending (default),DESC

select * from products
order by name desc

select * from products 
order by price,weight

--offset 
select * from users offset(40)
--limit

select * from users limit 5

(
select * from products
order by price desc
limit 4)
union
(
select * from products
order by price /weight desc
limit 4)

--results must have same colums data types and names
/*
 * Set operations:
 * Union
 * Union all
 * intersept
 * intersept all
 * except
 * except all
 * 
 */

(
select * from products
order by price desc
limit 4)
except 
(
select * from products
order by price /weight desc
limit 4)

-- distinct 

select distinct department from products

--subqueries

select name,price from products
where price >( select max(price) from products where department ='Toys')

select name , price , (select max (price)from products) from products
where price >867

select name ,price,(select price from products where id=3)from products
where price >867


select name , price_weight_ratio
from (
	select name,price/weight as price_weight_ratio from products
) as p
where price_weight_ratio > 5


select * from 
(select Max(price) from products )as p

--greates and least
select greatest(10,20,30);

select name , weight ,greatest(30,2*weight) from products 

select least(10,20,100)

select name,price , least(400,0.5*price) from products 

--case
select name,price,
case
	when price >600 then 'high'
	when price>300 then 'medium'
	else 'cheap'
end
from products

select AVG(order_count)
from (
		select user_id,count(*) as order_count from orders 
		group by user_id
)	as p

select first_name
from users
join(
select user_id from orders where product_id=3
)as o
on o.user_id =users.id

select id from orders 
where product_id in (
select id from products where price/weight>50
)

select name from products 
where price > (select avg(price) from products)


select name,department from products 
where department not in (select department from products where price <100)


--select name , department ,price from products 
--where price > (select max(price) from products where department='Industrial')

select name,department,price from products
where price > all (select price from products where department = 'Industrial')

select name,department,price from products
where price > some (select price from products where department = 'Industrial')

--corelated subqueries

select name,department,price from products p1
where price = (select max(price)from products p2 where p1.department =p2.department )

select name,(select count(*) from orders where orders.product_id =p.id)from products as p

