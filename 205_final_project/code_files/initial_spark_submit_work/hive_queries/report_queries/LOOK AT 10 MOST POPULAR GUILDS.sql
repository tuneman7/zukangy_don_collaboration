select 
    un.parameter_value as guild_name,
    et.event_type as event,
    count(un.parameter_value) as popular_guild_count
from 
    all_events et
join 
    event_parameters un
on 
    et.event_id = un.event_id
and 
    un.parameter_name = 'guild_name'
and 
    et.event_type = 'join_guild'
group by 
    un.parameter_value
    ,et.event_type
order by 
    count(un.parameter_value)