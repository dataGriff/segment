select email,name,user_id,item,signed_up_date from `tutorialapp_nodejs.identifies` 
where signed_up_date is not null;


select event_text,revenue,shipping_method,user_id from `tutorialapp_nodejs.ag_shoe` 
union all
select event_text,revenue,shipping_method,user_id from `tutorialapp_nodejs.fg_shoe` 
union all
select event_text,revenue,shipping_method,user_id from `tutorialapp_nodejs.mg_shoe`;

select user_id, SUM(revenue) FROM
(
select event_text,revenue,shipping_method,user_id from `tutorialapp_nodejs.ag_shoe` 
union all
select event_text,revenue,shipping_method,user_id from `tutorialapp_nodejs.fg_shoe` 
union all
select event_text,revenue,shipping_method,user_id from `tutorialapp_nodejs.mg_shoe`
) group by user_id


