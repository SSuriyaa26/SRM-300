select contents,username from comments
join users on users.id=comments.user_id 

select contents , url from comments 
join photos on photos.id=comments.photo_id 

select comments.id,photos.id from comments 
join photos on photos.id=comments.photo_id 

select url,username from photos 
join users on users.id=photos.user_id 

insert into photos(url,user_id)
values ('banner.jpg',NULL)

/*
 * Types of joins
 * Inner join - intersection between 2 tables , drops a row if its not in both,(default)
 * left outer join - intersection between 2 tables , keeps the row from left even if missing,makes the missing values null
 * right outer join - intersection between 2 tables , keeps the row from the right even if missing ,makes the missing values null
 * full join - complete intersection , adds even missing intersections and makes it null
 */

select url,username from photos 
left join users on users.id=photos.user_id 


select url,contents,username from photos 
join comments on comments.photo_id  = photos.id
join users on comments.user_id =users.id and users.id = photos.user_id 



