select 
    event_type, 
    count(event_type) as event_count 
from 
    all_events 
group 
    by event_type