
CREATE TABLE cities(
	name VARCHAR(50),
  country VARCHAR(50),
  population INTEGER,
  area INTEGER
)

insert into cities(name,country,population,area)
values('Tokyo','Japan',38505000,8223);
insert into cities(name,country,population,area)
values 
	('Delhi','India',28125000,2240),
	('Shangai','China',22125000,4015),
	('Sao Paulo','Brazil',20935000,3043);

select * from cities 

select name,country from cities

-- So far just basic create ,insert and select commands

--now processing

select name,population/area as population_density --rename calculated column
from cities

/*
 * select name , price * units_sold as revenue
 * from phones
 * 
 */

 /*
  * String operators and functions:
  * 
  * || :Joint 2 strings
  * Concat()
  * Lower()
  * Upper()
  * Length()
  */

select name ||', ' || country as location from cities

select concat(name,', ',country) as location from cities 

select concat(upper(name),', ',upper(country))as location from cities

--filtering (where)

select name ,  area from cities where area >4000

select name , area from cities where area =8223

select name , area from cities where area between 2000 and 5000

select name , area from cities where name not in ('Delhi','Shangai') or name='Delhi'

--select name, price from phones where units_sold>5000

--select name , manufacturer from phones 
--where manufacturer in ('Apple','Samsung')

select name, population/area as density from cities where population/area >6000
--select name, price * units_sold as total_revenue from phones 
--where price * units_sold>1000000


-- Update 
update cities set population =39505000 where name ='Tokyo'

select * from cities 

delete from cities where name = 'Tokyo'

select * from cities

insert into cities(name,country,population,area)
values ('Tokyo','Japan',38505000,8223)

--update phones set units_sold=8543 where name ='N8';
--select * from phones



