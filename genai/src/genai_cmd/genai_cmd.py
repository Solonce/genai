#!/usr/bin/env python3

import colorama
colorama.init(autoreset=True)

import json
import os
import sys
import argparse
import requests

import pyfiglet
from termcolor import colored

import textwrap

def shell_interface():
	ascii_art = pyfiglet.figlet_format(" genai", font="univers")
	colored_ascii = colored(ascii_art, 'green')

	print(colored_ascii)

	version = '1.0.9'
	github = 'https://github.com/Solonce/genai'
	author = 'Solomon Ince'
	model = "https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2"

	print('  ┌───────────────────────────────────────────────────────')
	print(f"  │ Version: {colored(version, 'yellow')}")
	print(f"  │ Github: {colored(github, 'blue')}")
	print(f"  │ Author: {colored(author, 'blue')}")
	print(f"  │ ")
	print(f"  │ Model: {colored(model, 'dark_grey', attrs=['underline'])}")
	print("  └───────────────────────────────────────────────────────")

def generate(payload, context, length, max_time, raw=False):
	key = get_data('key')
	if key == "":
		print("You need to set up a HuggingFace API key first. Please use the command: \n'genai -S HUGGINGFACE_API_KEY'\n\nVisit: https://huggingface.co/docs/api-inference/en/quicktour#get-your-api-token")
		return "exit"

	API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
	headers = {"Authorization": f"Bearer {key}"}
	_input = {
		"inputs": context + payload,
		"parameters": {"max_new_tokens": int(length), "max_time": int(max_time), "return_full_text": False, "do_sample": False},

	}

	response = requests.post(API_URL, headers=headers, json=_input)

	try:
		rsp = response.json()[0]["generated_text"].split("TERMINATE")[0]
	except Exception as e:
		print(f"Ran into API Error. Likely an issue with _input 'parameters':\n\n{e}\n{response}")
		exit()

	if rsp[0] in '\n\t' or rsp[1] in '\n\t':
		if rsp[0] not in '\n\t' and rsp[1] in '\n\t':
			rsp = rsp[1:]
		rsp = rsp.lstrip('\n\t')
		rsp = rsp.rstrip('\n\t')

	if raw:
		print(f"\n{rsp}\n")
	else:
		print('\n  ┌─────────────────────────────')

		for line in rsp.split('\n'):
			if len(line) > 90:
				wrapper = textwrap.TextWrapper(initial_indent='  │ ', subsequent_indent='  │ ', width=90)
				print(wrapper.fill(line))
			else:
				print(f"  │ {line}")
		
		print('  └─────────────────────────────\n')


	return

def get_data(entry):
	home_dir = os.path.expanduser('~')

	if os.name == 'nt':
		config_dir = os.path.join(home_dir, 'AppData', 'Local', 'genai')
	else:
		config_dir = os.path.join(home_dir, '.genai')

	hidden_file = os.path.join(config_dir, 'data.json')

	try:
		with open(hidden_file, 'r') as file:
			data = json.load(file)
			data = data[entry]
		return data
	except:
		return ""

def set_data(entry, data):

	home_dir = os.path.expanduser('~')

	if os.name == 'nt':
		config_dir = os.path.join(home_dir, 'AppData', 'Local', 'genai')
	else:
		config_dir = os.path.join(home_dir, '.genai')

	hidden_file = os.path.join(config_dir, 'data.json')

	if not os.path.exists(config_dir):
		os.makedirs(config_dir)
	else:
		key = get_data('key')
	context = """
	You are a simple lightweight text-based AI assistant that excells in programming and problem resolution.
	All your responses are to be as short as they can reasonably be.
	If the solution is any amount of code, respond only with the code.
	Do not pad your responses with text or '\n'.

	After you have finished answering the question, please type TERMINATE.
	"""

	if entry == 'key':
		data = {"key": data, "context": context}
		print("API Key Set!")
	elif entry == "context":
		if data == 'default':
			data = context
		data = {"key": key, "context": data}
		print("Context Set!")

	with open(hidden_file, 'w+') as file:
		json.dump(data, file)

	return

def start():
	parser = argparse.ArgumentParser(description="AI text generation tool")
	parser.add_argument('-S', '--set-key', dest='key', help="Set the key for the AI service")
	parser.add_argument('-C', '--reset-context', dest='resetcontext', help="Set the default context for genai.")
	parser.add_argument('-t', '--text-data', dest='textdata', help="No shell, just string. Make sure to wrap input in double quotes!")
	parser.add_argument('-r', '--raw-data', dest='rawdata', help="Direct raw response from the Mixtral-7B-Instruct-v0.2 model. (As of 3/26/24)")
	parser.add_argument('-c', '--context', dest='context', help="The context in which the Mixtral-7B-Instruct-v0.2 model to operate under. (As of 3/26/24)")
	parser.add_argument('-l', '--length', dest="length", help="The length of the return response. Keep in mind, longer length means longer load time!", default=100)
	parser.add_argument('-s', '--seconds', dest="seconds", help="The maximum time in seconds it takes for a response to load. This is non-clusive of overhead network communication time", default=3)
	args = parser.parse_args()

	if args.key:
		set_data('key', args.key)
	if args.resetcontext:
		set_data('context', args.resetcontext)
	
	try:
		if args.context:
			context = args.context
		else:
			context = get_data('context')

		if args.textdata:
			print(f"\n   genai:")
			data = generate(args.textdata, context, args.length, args.seconds)
		elif args.rawdata:
			data = generate(args.rawdata, context, args.length, args.seconds, raw=True)
		else:
			shell_interface()
			while True:
				text = input("genai> ")
				if text == "exit":
					break;
				data = generate(text, context, args.length, args.seconds)
				if data == "exit":
					break;
					print("\nExiting interactive mode.")

	except KeyboardInterrupt:
		pass

if __name__ == "__main__":
	start()