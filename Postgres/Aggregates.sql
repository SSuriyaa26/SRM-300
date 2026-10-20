select user_id,count(id) as num_comments_created from comments
group by user_id;

-- u can only select the grouped column or aggregate function

select count(user_id)from photos --null isnt counted

select count(*)from photos

select photo_id,count(*) as num_comments from comments 
group by photo_id 

--having is the 'where' of groups

select photo_id , count(*) from comments
where photo_id <3
group by photo_id 
having count(*)>2


select user_id,count(*) from comments 
where photo_id <50
group by user_id 
having count(*)>20


