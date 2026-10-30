select * from users 
order by id desc
limit 3

select username, caption from users u 
join posts p on p.user_id =u.id 
where u.id =200


select username,count(*) from users u 
join likes l on l.user_id =u.id 
group by username

show data_directory;

select oid,datname from pg_database;

select * from pg_class

create index on users(username)
--
--drop index users_username_idx

explain analyze select * from users u 
where username='Elise20' --0.5 ms without index and it takes 0.067 with index over 10x
 
select pg_size_pretty(pg_relation_size('users_username_idx')) --880 kb for users and 184kb for index so the downside is the storage
--insert update and delete get slower since a index needs to be created again
--sometimes index might not get used

--b tree index the most commpny used one, there are more types
--

create extension pageinspect;

select * from bt_metap('users_username_idx')

select * from bt_page_items('users_username_idx',3)

--explain gives the plane , explain analyze also runs it and gives the performance analysis 

explain select username	,contents from users u 
join comments on u.id=comments.user_id 
where username='Alyson14'

explain analyze select username	,contents from users u 
join comments on u.id=comments.user_id 
where username='Alyson14'


select * from pg_stats where tablename ='users'
