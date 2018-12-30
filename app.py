import os
import re
import sys
import json
import discord
import asyncio
import datetime
import webbrowser

print('Starting up...')

if sys.version_info[0] < 3:
	raise Exception("This program requires Python 3 or greater. Please update your installation.")

def log(type, message):
	class c:
		HEADER = '\033[95m'
		OKBLUE = '\033[94m'
		OKGREEN = '\033[92m'
		WARNING = '\033[93m'
		FAIL = '\033[91m'
		ENDC = '\033[0m'
		BOLD = '\033[1m'
		UNDERLINE = '\033[4m'

	now = datetime.datetime.now()
	timestamp = f"["+now.strftime("%Y-%m-%d %H:%M")+"]"
	log = ""

	if type == "info":
		log = f"{c.OKBLUE}[INFO] {c.ENDC}{message}"
	elif type == "warn":
		log = f"{c.WARNING}[WARN] {c.ENDC}{message}"
	elif type == "err":
		log = f"{c.FAIL}[ERR] {c.ENDC}{message}"
	elif type == "success":
		log = f"{c.OKGREEN}[SUCCESS] {c.ENDC}{message}"
	else:
		log = f"[LOG] {message}"

	return print(f"{timestamp} {log}")

with open("config.json") as file:
	config = json.load(file)

client = discord.Client()
urls = []

@client.event
async def on_ready():
	log("info", "Client ready!")

@client.event
async def on_message(msg):
	try:
		url_regex = r"((?:https?:\/\/)discord\.gift\/[a-zA-Z0-9]{16,}|(?:https?:\/\/)discordapp\.com\/gifts?\/[a-zA-Z0-9]{16,})"
		message = msg.content
		url = re.search(url_regex, message).group(0)
		if url not in urls:
			log("success", f"Detected a gift url! Opening in browser... [ {url} ]")
			webbrowser.open(url, new=2, autoraise=True)
			urls.append(url)
			if config["delete_detected_message"]:
				try:
					await client.delete_message(msg)
				except:
					log("warn", f"Unable to delete message. Am I missing permissions?")
		else:
			log("warn", f"Detected a duplicate gift url, ignoring. [ {url} ]")
	except AttributeError:
		print(urls)

client.run(config["token"])
