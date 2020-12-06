# discord-bot
A discord bot that can provide top 5 links from google search and maintains the user search history.

**To search with google**: 
* Command: `!google nodejs`
* Will search "nodejs" keyword in the google and returns top 5 links.

**User search history against a value**:
* Command: `!recent nodejs`
* Will look for "nodejs" in all the before searched keywords. Matching keywords will be returned.

### Setup
* Create a virtual environment using `virtualenv sanbox -p python3` and install the requirements through `requirements.txt`
* Create a `.env` file from `env.tmpl` and fill your discord token.
* Run the bot using command `python -m discord_bot.bot.client`
* Python version used during development: `3.6.9`