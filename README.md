# grinch.py

Proof of concept Python script for "obtaining" Discord Nitro gift URLs from all servers you are in as they are sent.

This works by reading new messages and searching for the gift URLs within them. If one is detected, it opens it in your computer's default browser for redeeming.

**THIS IS JUST A PROOF OF CONCEPT!** Discord forbids the use of selfbots and doing so can get your account terminated. If you do choose to use this, I claim no responsibility for whatever happens to your account.

## Installation

* Required Python 3.4 or higher, according to Discord.py's documentation. This was developed and tested on 3.7.1 and works fine. Your results may vary.
* Extract the files (`app.py`, `config.json`, and `requirements.txt`) to a folder of your choice.
* Open a command line tool and `cd` into the folder and then run `pip install -r requirements.txt`
* After the required packages are installed, add your client token to `config.json`
* Run the selfbot by running `python app.py` in your command line tool (while still `cd`'d into the same folder)
* ???
* PROFIT!!
