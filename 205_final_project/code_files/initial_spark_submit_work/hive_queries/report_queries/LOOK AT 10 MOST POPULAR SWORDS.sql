
select 
    un.parameter_value as sword_name,
    et.event_type as event,
    count(un.parameter_value) as popular_sword_count
from 
    all_events et
join 
    event_parameters un
on 
    et.event_id = un.event_id
and 
    un.parameter_name = 'sword_type'
group by 
    un.parameter_value
    ,et.event_type
order by 
    count(un.parameter_value) desc limit 10