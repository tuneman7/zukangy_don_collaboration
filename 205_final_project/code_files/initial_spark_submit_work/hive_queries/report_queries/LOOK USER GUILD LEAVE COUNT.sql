select 
    un.parameter_value as user_name,
    et.event_type as event,
    count(un.parameter_value) as guild_leave_count
from 
    all_events et
join 
    event_parameters un
on 
    et.event_id = un.event_id
and 
    et.event_type = 'leave_guild'
and 
    un.parameter_name = 'user'    
group by 
    un.parameter_value
    ,et.event_type
order by 
    count(un.parameter_value) desc