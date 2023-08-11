select '-----------LOOK AT TOTAL EVENT COUNTS--------------------';
select
    event_type,
    count(event_type) as event_count
from 
    all_events
group by event_type;
select '-----------LOOK USER GUILD JOIN COUNT--------------------';
select 
    un.parameter_value as user_name,
    et.event_type as event,
    count(un.parameter_value) as guid_join_count
from 
    all_events et
join 
    event_parameters un
on 
    et.event_id = un.event_id
and 
    et.event_type = 'join_guild'
and 
    un.parameter_name = 'user'    
group by 
    un.parameter_value
    ,et.event_type
order by 
    count(un.parameter_value) desc limit 10;
select '-----------LOOK USER GUILD LEAVE COUNT--------------------';
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
    count(un.parameter_value) desc limit 10;
select '-----------LOOK USER GET CREDIT COUNT--------------------';
select 
    un.parameter_value as user_name,
    et.event_type as event,
    count(un.parameter_value) as get_credit_count
from 
    all_events et
join 
    event_parameters un
on 
    et.event_id = un.event_id
and 
    et.event_type = 'get_credit'
and 
    un.parameter_name = 'user'    
group by 
    un.parameter_value
    ,et.event_type
order by 
    count(un.parameter_value) desc limit 10;
select '-----------LOOK AT 10 MOST POPULAR SWORDS--------------------';
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
    count(un.parameter_value) desc limit 10;
select '-----------LOOK AT 10 MOST POPULAR GUILDS--------------------';
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
    count(un.parameter_value) desc limit 10;
select '-------------------------------';    