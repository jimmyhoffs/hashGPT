#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Setting hackGPT Environment with OpenAI API key (Generate one here: https://platform.openai.com/account/api-keys)
from dotenv import load_dotenv
import os
from pathlib import Path
from time import sleep
import gradio as gr
import csv
import webbrowser
import inquirer
from termcolor import colored
import fade

# Load API key from an environment variable or set it if not available
load_dotenv(".env")
api_key = os.environ.get('OPENAI_TOKEN')
if api_key is None:
    error = '''
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

    # If API key is not available in the environment variable, prompt the user
    user_key = input('Enter OpenAI API Key: ').replace(" ", "")
    api_key = user_key
else:
    print("API Key already set.")

# Import other required libraries
import openai
import pandas as pd
import matplotlib.pyplot as plt
import json
import datetime
import argparse
from prettytable.colortable import ColorTable, Themes
from prettytable import from_csv

# Initialize OpenAI API key
openai.api_key = api_key


# Initialize OpenAI API key
  # Replace with your actual OpenAI API key

# Set the date_string and hackgpt_persona
date_string = "2024-02-01"  # Replace with your actual date
hackgpt_persona = ""

# Define the add_text function
def add_text(state, inputs):
    text, file_data = inputs

    # Handle text input
    response_text = client.completions.create(
        model="text-davinci-003",
        prompt=str(hackGPT_mode) + str(text),
        temperature=0,
        max_tokens=3000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\285643", "\""]
    )
    response_text = response_text.choices[0].text

    # Handle file input
    if file_data is not None:
        file_response = client.completions.create(
            model="text-davinci-003",
            prompt=str(file_data.decode("utf-8")) + "\n",
            temperature=0,
            max_tokens=3000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\"\"\""]
        )
        response_file = file_response.choices[0].text
    else:
        response_file = None

    state = state + [(str(response_text), str(text), str(response_file))]

    # Save to CSV
    try:
        with open('output/chat_hackGPT_log.csv', 'a+', encoding='UTF8', newline='') as f:
            w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            w.writerow([date_string, hackgpt_persona, str(text).strip('\n'), str(response_text).lstrip('\n')])
    except Exception as e:
        print(f"An error occurred while writing to CSV: {e}")

    return state, state


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

# Set OpenAI API key
openai.api_key = api_key


# Gradio setup
iface = gr.Interface(
    fn=add_text,
    live=True,
    inputs=[gr.Textbox(show_label=False, placeholder="Enter query and press enter"),
            gr.Upload(label="Upload a file", type="file")],
    outputs="text",
)


# Open the browser
webbrowser.open("http://127.0.0.1:1337")

# Results sample
with open('output/chat_hackGPT_log.csv', 'r', encoding='UTF8') as f:
    t = from_csv(f)
    t._max_width = {"Date": 10, "Persona": 8, "Query": 8, "Response": 48}
    print(fade.purplepink(str(t)))

# Launch Gradio
iface.launch(
    height=1000,
    quiet=True,
    favicon="res/hackgpt_fav.png",
    share=True,
    debug=True,
)
