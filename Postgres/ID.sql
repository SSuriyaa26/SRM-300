
create table users
(
	id serial primary key,
	username varchar(50)
);	

insert into users (username)
values 
('monahan93'),
('pferrer'),
('si93onis'),
('99stroman');


create table photos(
	id serial primary key,
	url varchar(200),
	user_id integer references users(id)
);

insert into photos(url,user_id)
values
('http://one.jpg',4);

insert into photos (url,user_id)
values
('http://two.jpg',1),
('http://25.jpg',1),
('http://36.jpg',1),
('http://754.jpg',2),
('http://35.jpg',3),
('http://256.jpg',4);

select * from photos;


select * from photos where user_id=4;

select url,username from photos join users on users.id=photos.user_id;

--foreign key constraint

-- use NULL as foreign key and it works
--dangling referenses can be caused due to deletion (refering smth that doesnt exist)

/*
 * On delete options:
 * restrict - throw an error (this is applied by default)
 * no action-throw an error
 * cascae - delete the image too
 * set null - set user id to null
 * set defailt-set to a default value if provided
 */

create table comments(
 id serial,
 photo_id integer references photos(id),
 user_id integer references useres(id)
 contents varchar(240)
);




