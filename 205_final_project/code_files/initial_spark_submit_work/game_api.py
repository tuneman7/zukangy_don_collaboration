#!/usr/bin/env python
from __future__ import print_function
import json
import uuid
from kafka import KafkaProducer
from flask import Flask, request, session
from flask import jsonify
import sys
from multiprocessing import Value


counter = Value('i', 0)
app = Flask(__name__)

event_id = 0

def get_event_id():
    out = str(uuid.uuid4())
    return out

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

app = Flask(__name__)
producer = KafkaProducer(bootstrap_servers='kafka:29092')

def log_event_parameters():
    args = request.args
    print(args, file=sys.stderr)
    print(request.args.to_dict(),file=sys.stderr)
    print(request.args.viewkeys(),file=sys.stderr)
    key_views = request.args.viewkeys()
    output_list = []
    output_dict = {}
    event_id = get_event_id()
    return_string = ""
    key_count = 0
    for key in request.args.viewkeys():
        my_dict = {}
        my_dict["event_id"] = event_id
        my_dict["parameter_name"] = key
        my_dict["parameter_value"] = request.args.get(key)       
        print(key,file=sys.stderr)
        print(request.args.get(key),file=sys.stderr)
        output_dict[key]=request.args.get(key)       
        output_list.append(my_dict)
        key_count = key_count +1
        producer.send("event_parameters", json.dumps(my_dict).encode())
    if key_count==0:
        my_dict = {}
        my_dict["event_id"] = event_id
        my_dict["parameter_name"] = "user"
        my_dict["parameter_value"] = "NONE"
        producer.send("event_parameters", json.dumps(my_dict).encode())
    return event_id

def log_to_kafka(topic, event):
    event_id = log_event_parameters()
    event.update(request.headers)
    event_id_dict={'event_id':event_id}
    event.update(event_id_dict)
    producer.send(topic, json.dumps(event).encode())


@app.route("/")
def default_response():
    default_event = {'event_type': 'default'}
    log_to_kafka('events', default_event)
    return "This is the default response!\n"


@app.route("/purchase_a_sword")
def purchase_a_sword():
    purchase_sword_event = {'event_type': 'purchase_sword'}
    log_to_kafka('events', purchase_sword_event)
    return "Sword Purchased!\n"

@app.route("/join_a_guild")
def join_guild():
    join_guild_event = {'event_type': 'join_guild'}
    log_to_kafka('events', join_guild_event)
    return "Joined Guild!\n"

@app.route("/leave_guild")
def leave_guild():
    leave_guild_event = {'event_type': 'leave_guild'}
    log_to_kafka('events', leave_guild_event)
    return "Left Guild!\n"

@app.route("/get_credit")
def get_credit():
    get_credit_event = {'event_type': 'get_credit'}
    log_to_kafka('events', get_credit_event)
    return "Received Credit!\n"

@app.route("/shutdown")
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return ""

