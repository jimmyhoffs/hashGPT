#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@title  Setting hackGPT Environment with OpenAI API key (Generate one here: https://platform.openai.com/account/api-keys )
#OpenAI API Setup
from dotenv import load_dotenv
import sys
import fade
from pathlib import Path
import openai

api_key = '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'
openai.api_key = api_key
from time import sleep
import os
import fade
from pathlib import Path
import openai

api_key = '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'
openai.api_key = api_key
import requests
import urllib.parse
import urllib.request
import openai

api_key = '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'
openai.api_key = api_key
from dotenv import load_dotenv
import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
import json
import csv
import datetime
import argparse
import inquirer
import webbrowser
from prettytable.colortable import ColorTable, Themes
from prettytable import from_csv



# Load API key from an environment variable or secret management service

load_dotenv(".env")
apiToken = os.environ.get('OPENAI_TOKEN')

if 'OPENAI_TOKEN' in os.environ:
   pass
else:
  error='''           
                     *   )           )            (   
                     `(     ( /((        (  (      )\   
                      )\(   )\())\  (    )\))(  ((((_) 
                     ((_)\ (_))((_) )\ ) ((   ))\  )\) 
                     8"""" 8"""8  8"""8  8"""88 8"""8  
                     8     8   8  8   8  8    8 8   8  
                     8eeee 8eee8e 8eee8e 8    8 8eee8e 
                     88    88   8 88   8 8    8 88   8 
                     88    88   8 88   8 8    8 88   8 
                     88eee 88   8 88   8 8eeee8 88   8 
                                  
   \033[1;33mAttempting to Set OpenAI system variable with API key.'''
  fadederror = fade.fire(error)
  print(fadederror)
  Path(".env").touch()
  setting_token = open(".env", "a")
  userkey = input('Enter OpenAI API Key: ').replace(" ","")
  setting_token.write("OPENAI_TOKEN="+'"'+userkey+'"\n')
   

#@title ChatBot and Web UI for HackGPT
#temp menu
parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", type=str, required=False)
args  = parser.parse_args()  


date_string = datetime.datetime.now()

load_dotenv()  
apiToken = os.environ.get("OPENAI_TOKEN")
headers = {
                    "Accept": "application/json; charset=utf-8",
                    "Authorization": "Token" + str(apiToken)
                }

def progress(percent=0, width=15):
    hashes = width * percent // 100
    blanks = width - hashes

    print('\r', hashes*'▒', blanks*' ', '', f' {percent:.0f}%', sep='',
        end='', flush=True)
print('𝙰𝚙𝚙𝚕𝚢𝚒𝚗𝚐 𝙰𝙿𝙸 𝚃𝚘𝚔𝚎𝚗')
for i in range(101):
    progress(i)
    sleep(.01)
print('\n')
print("𝙰𝙿𝙸 𝙲𝚘𝚗𝚏𝚒𝚐𝚞𝚛𝚊𝚝𝚒𝚘𝚗 𝚂𝚊𝚟𝚎𝚍 𝚝𝚘 .𝚎𝚗𝚟") 
if 'OPENAI_TOKEN' in os.environ:
    pass
else:
    os.environ['OPENAI_TOKEN'] = input('Enter API Key: ').replace(" ","")
token = os.environ.get("OPENAI_TOKEN")
hack=  "\n"*7 + r""" 



|¯¯¯¯| |¯¯¯¯| '/¯¯¯/.\¯¯¯\‚ '/¯¯¯¯/\¯¯¯¯\  |¯¯¯¯| |¯¯¯¯|
|:·.·|_|:·.·| |:·.·|_|:·.·| |:·.·|  |____| |:·.·|./____/ 
|:·.·|¯|:·.·| |:·.·|¯|:·.·| |:·.·|__|¯¯¯¯| |:·.·|.\¯¯¯¯\ 
|____| |____| |____|:|____|  \__ _\/____/  |____| |_____|


                                                                            """ + "\n"*12

gpt = "\n"*4 +r""" 

                                                           ______  _______  ________ 
                                                         /      \|       \|        \
                                                         |  ▓▓▓▓▓▓\ ▓▓▓▓▓▓▓\\▓▓▓▓▓▓▓▓
                                                         | ▓▓ __\▓▓ ▓▓__/ ▓▓  | ▓▓   
                                                         | ▓▓|    \ ▓▓    ▓▓  | ▓▓   
 | ▓▓ \▓▓▓▓ ▓▓▓▓▓▓▓   | ▓▓   
| ▓▓__| ▓▓ ▓▓        | ▓▓   
 \▓▓    ▓▓ ▓▓        | ▓▓ 
  \▓▓▓▓▓▓ \▓▓         \▓▓
                      """                                                                                                 

fadedhack = fade.water(hack)
fadedgpt = fade.random(gpt)


import openai
api_key = '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'
openai.api_key = api_key
import gradio as gr
import csv
import webbrowser
import inquirer
from termcolor import colored, cprint
import subprocess

# Initialize OpenAI API key
  # Replace with your actual OpenAI API key

# Set the date_string and hackgpt_persona
date_string = "2024-02-01"  # Replace with your actual date
hackgpt_persona = ""

# Define the add_text function
def add_text(state, text):
    response = client.completions.create(model="text-davinci-003",
    prompt=str(hackGPT_mode) + str(text),
    temperature=0,
    max_tokens=3000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["\285643", "\""])
    response = response.choices[0].text
    state = state + [(str(response), str(text))]

    try:
        with open('output/chat_hackGPT_log.csv', 'a+', encoding='UTF8', newline='') as f:
            w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            w.writerow([date_string, hackgpt_persona, str(text).strip('\n'), str(response).lstrip('\n')])
    finally:
        return state, state

# Define the add_file function
def add_file(file_state, file):
    try:
        with open(file.name, 'r') as targets:
            search = targets.read()
            response = client.completions.create(model="text-davinci-003",
            prompt=str(search) + "\n",
            temperature=0,
            max_tokens=3000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\"\"\""])

        file_response = response.choices[0].text
        file_state = file_state + [("" + str(file_response), "Processed file: " + str(file.name))]

        with open('output/chat_hackGPT_file_log.csv', 'a+', encoding='UTF8', newline='') as f:
            w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            w.writerow([date_string, hackgpt_persona, str(search).strip('\n'), str(response).lstrip('\n')])

    except Exception as e:
        # Handle the exception if needed
        print(f"An error occurred: {e}")

    finally:
        return file_state, file_state

# Set hackGPT_mode based on user input
questions = [
    inquirer.List("Persona", message="\033[0;34m𝗦𝗘𝗟𝗘𝗖𝗧 𝗣𝗘𝗥𝗦𝗢𝗡𝗔 \033[1;97m",
                  choices=['hackGPT', 'chatGPT-DEV', 'DAN'],
    )
]

answers = inquirer.prompt(questions)
hackgpt_persona = answers['Persona']

if hackgpt_persona == 'hackGPT':
    hackGPT_mode = open('personas/hackGPTv1.md', "r").read()
elif hackgpt_persona == 'chatGPT-DEV':
    hackGPT_mode = open('personas/DEVv1.md', "r").read()
elif hackgpt_persona == 'DAN':
    hackGPT_mode = open('personas/DANv11.md', "r").read()

# Gradio setup
with gr.Blocks(css="#chatbot .output::-webkit-scrollbar {display: none;}") as hackerchat:
    state = gr.State([])
    chatbot = gr.Chatbot()

    with gr.Column():
        txt = gr.Textbox(show_label=False, placeholder="Enter query and press enter")
    with gr.Column(scale=0.15, min_width=0):
        btn = gr.UploadButton("📁", file_types=["file"])

    txt.submit(add_text, [state, txt], [chatbot, state])
    txt.submit(lambda: "", None, txt)
    btn.upload(add_file, [state, btn], [state, chatbot])


# Open the browser
webbrowser.open("http://127.0.0.1:1337 GPT_log.csv | res/tools/csv_hack | lolcat -p 23")

# Results sample
with open('output/chat_hackGPT_log.csv', 'r', encoding='UTF8') as f:
    t = from_csv(f)
    t._max_width = {"Date": 10, "Persona": 8, "Query": 8, "Response": 48}
    print(fade.purplepink(str(t)))

# Launch Gradio
if __name__ == "__main__":
    hackerchat.launch(height=1000, quiet=True, favicon_path="res/hackgpt_fav.png", server_port=1337)


