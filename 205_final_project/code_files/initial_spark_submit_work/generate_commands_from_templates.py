import sys, getopt,os,smtplib,time
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import subprocess
import random
from utility import Utility as util

def main():

    u = util()
    yaml_template       = os.path.join(u.get_this_dir(),"docker-compose.template")
    yaml_outfile        = os.path.join(u.get_this_dir(),"docker-compose.yml")
    this_directory      = u.get_this_dir()
    yaml_template_text  = u.get_data_from_file(yaml_template)
    yaml_text           = yaml_template_text.replace("<project_dir_token>",this_directory)
    u.write_text_to_file(yaml_outfile,yaml_text)

    bash_template       = os.path.join(u.get_this_dir(),"dd.template")
    bash_outfile        = os.path.join(u.get_this_dir(),"dd.sh")
    this_directory      = u.get_this_dir()
    bash_template_text  = u.get_data_from_file(bash_template)
    bash_text           = bash_template_text.replace("<project_dir_token>","/w205/")
    u.write_text_to_file(bash_outfile,bash_text)

    es_template       = os.path.join(u.get_this_dir(),"es.template")
    es_outfile        = os.path.join(u.get_this_dir(),"es.sh")
    this_directory    = u.get_this_dir()
    es_template_text  = u.get_data_from_file(es_template)
    es_text           = es_template_text.replace("<project_dir_token>","/w205/")
    u.write_text_to_file(es_outfile,es_text)


main()
