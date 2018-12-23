# grinch.py

Proof of concept Python script for obtaining Discord gift URLs from all servers it operates within as they are sent.

## How it works

This works by reading new messages and searching for the gift URLs within them. If one is detected, it opens it in your computer's default browser for redeeming.

## Installation

* Requires Python 3.4 or higher, according to Discord.py's documentation. This was developed and tested on 3.7.1 and works fine. Your results may vary.
  * Also requires pip
* Extract the files (`app.py`, `config.json`, and `requirements.txt`) to a folder of your choice.
* Open a command line tool and `cd` into the folder and then run `pip install -r requirements.txt`
* After the required packages are installed, add your bot's token to `config.json`
* Run the script by running `python app.py` in your command line tool (while still `cd`'d into the same folder)
* ???
* PROFIT!!

## Will I get in trouble for using this?

It depends on how you use it. This does not use any exploits and uses what the Discord API provides us. However using this as a selfbot and not through a bot account will risk getting your account banned. You have been warned.
