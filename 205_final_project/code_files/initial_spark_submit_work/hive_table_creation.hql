create external table if not exists default.all_events (
    raw_event string,
    timestamp string,
    Accept string,
    Host string,
    User_Agent string,
    event_id string,
    event_type string
  )
  stored as parquet 
  location '/tmp/all_events'
  tblproperties ("parquet.compress"="SNAPPY");
  

create external table if not exists default.event_parameters (
    raw_event string,
    timestamp string,
    Accept string,
    Host string,
    User_Agent string,
    event_id string,
    parameter_name string,
    parameter_value string
    
  )
  stored as parquet 
  location '/tmp/event_parameters'
  tblproperties ("parquet.compress"="SNAPPY");