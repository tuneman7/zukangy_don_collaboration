import sys, getopt,os,smtplib,time
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import subprocess
import random

def main():
    
    with open('guild_names.csv', encoding='ISO-8859-1') as g:
        guild_names = [row.split(',')[0].strip('\n') for row in g]
        g.close()
    with open('sword_types.csv',encoding='ISO-8859-1') as s:
        sword_types = [row.split(',')[0].strip('\n') for row in s]
        s.close()
    rand_int  = random.randint(5,110)
    thisdir   = os.getcwd()
    users     = ['ben', 'aastha', 'lise', 'theresa', 'don']
    events    = ['purchase_a_sword', 'join_a_guild', 'leave_guild', 'get_credit']
    
    
    flask_shutdown_command = "docker-compose exec mids curl http://localhost:5000/shutdown"

    print("pitching events")
    # Just create 10000 events.
    i = 1
    
    while i < 140:
        i+=1
        e_randint = random.randint(0,len(events)-1)
        u_randint = random.randint(0,len(users)-1)
        g_randint = random.randint(0,len(guild_names)-1)
        s_randint = random.randint(0,len(sword_types)-1)
        b_randint = random.randint(0,40)
        base      = 'docker-compose exec mids ab -n {} -H "Host: user2.att.com" http://localhost:5000/'.format(b_randint)

        
        if events[e_randint] =='join_a_guild':
            line = base + 'join_a_guild"?user={}&guild_name={}"'
            line = line.format(users[u_randint],guild_names[g_randint])
        elif events[e_randint] =='leave_guild':
            line = base + 'leave_guild"?user={}&guild_name={}"'
            line = line.format(users[u_randint],guild_names[g_randint])
        elif events[e_randint] == 'purchase_a_sword':
            line = base + 'purchase_a_sword"?user={}&sword_type={}"'
            line = line.format(users[u_randint],sword_types[s_randint])
        else:
            line = base + 'get_credit"?user={}&guild_name={}"'
            line = line.format(users[u_randint],guild_names[g_randint])
        print(line)
        subprocess.call(line, shell=True)
        print("Press and HOLD CTRL+C to terminate, else 10000 events will be created")
        
        

main()
