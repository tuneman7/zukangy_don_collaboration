#!/usr/bin/env python
"""Extract events from kafka and write them to hdfs
"""
import json,time
from pyspark.sql import SparkSession, Row
#from pyspark.sql.functions import udf
from pyspark.sql.functions import udf, from_json
from pyspark.sql.types import *

def general_event_schema():
    """
    root
    |-- Accept: string (nullable = true)
    |-- Host: string (nullable = true)
    |-- User-Agent: string (nullable = true)
    |-- event_type: string (nullable = true)
    """
    return StructType([
        StructField("Accept", StringType(), True),
        StructField("Host", StringType(), True),
        StructField("User-Agent", StringType(), True),
        StructField("event_id", StringType(), True),
        StructField("event_type", StringType(), True),
    ])

def event_parameter_event_schema():
    """
    root
    |-- Accept: string (nullable = true)
    |-- Host: string (nullable = true)
    |-- User-Agent: string (nullable = true)
    |-- event_type: string (nullable = true)
    """
    return StructType([
        StructField("Accept", StringType(), True),
        StructField("Host", StringType(), True),
        StructField("User-Agent", StringType(), True),
        StructField("event_id", StringType(), True),
        StructField("parameter_name", StringType(), True),
        StructField("parameter_value", StringType(), True),
    ])




@udf('string')
def munge_event(event_as_json):
    event = json.loads(event_as_json)
    event['Host'] = "moe"
    event['Cache-Control'] = "no-cache"
    return json.dumps(event)

def main():
    """main
    """
    spark = SparkSession \
        .builder \
        .appName("ExtractEventsJob") \
        .getOrCreate()

    raw_events = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "kafka:29092") \
        .option("subscribe", "events") \
        .load()
    
    raw_event_parameters = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "kafka:29092") \
        .option("subscribe", "event_parameters") \
        .load()

    event_parameters = raw_event_parameters \
        .select(raw_event_parameters.value.cast('string').alias('raw_event'),
                raw_event_parameters.timestamp.cast('string'),
                from_json(raw_event_parameters.value.cast('string'),
                          event_parameter_event_schema()).alias('json')) \
        .select('raw_event', 'timestamp', 'json.*')

    all_events = raw_events \
        .select(raw_events.value.cast('string').alias('raw_event'),
                raw_events.timestamp.cast('string'),
                from_json(raw_events.value.cast('string'),
                          general_event_schema()).alias('json')) \
        .select('raw_event', 'timestamp', 'json.*')    
    
    sink1 = event_parameters \
        .writeStream \
        .format("parquet") \
        .option("checkpointLocation", "/tmp/checkpoints_for_event_parameters") \
        .option("path", "/tmp/event_parameters") \
        .trigger(processingTime="10 seconds") \
        .start()
        
    sink2 = all_events \
        .writeStream \
        .format("parquet") \
        .option("checkpointLocation", "/tmp/checkpoints_for_all_events") \
        .option("path", "/tmp/all_events") \
        .trigger(processingTime="10 seconds") \
        .start()        
    

    sink1.awaitTermination()
    sink2.awaitTermination()

    
if __name__ == "__main__":
    main()
