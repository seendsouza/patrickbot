"""
A bot specifically tailored for my friends' server.
"""

import asyncio
import json

import discord

from commandhandler import CommandHandler
from observequantum import ObserveQuantum

# configuring the bot using config.json
with open('config.json') as f:
    data = json.load(f)

token = data["token"]
command_prefix = data["prefix"]
# add this to config.json
observe_arguments = ["star","wang"]

client = discord.Client()

# assigning external classes to objects
ch = CommandHandler(client)
oq = ObserveQuantum(observe_arguments)

# command functions
def test_command(message,client,args):
    return 'Test'

def observe_command(message,client,args):
    """
    Checks if user inputted guess matches the state of a qubit after observation.
    """
    guess = message.content.lower()
    if (observe_arguments[0] in guess) or (observe_arguments[1] in guess):
        if oq.observed(guess) == True:
            return '{} has successfully guessed the state of Patrick.'.format(message.author)
        else:
            return '{} has unsuccessfully guessed the state of Patrick.'.format(message.author)
    else:
        return '{} has inputted an invalid argument. Please input either Star or Wang.'.format(message.author)

def swear_command(message,client,args):
    # TODO: add this functionality
    return 'Swear command not implemented'

# adding commands that refer to the functions above
ch.add_command({
    'trigger': '!test',
    'function': test_command,
    'args_num': 0,
    'args_name': [''],
    'description': 'Prints number of messages.'
})

ch.add_command({
    'trigger': '!observe',
    'function': observe_command,
    'args_num': 1,
    'args_name': ['Expected State'],
    'description': 'Observes a qubit in equal quantum superposition.'
})

ch.add_command({
    'trigger': '!swear',
    'function': swear_command,
    'args_num': 0,
    'args_name': [''],
    'description': 'Swears from a list of swear words'
})

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    """
    When a user in the server sends a message, this checks if a command is sent to the bot.
    If it is for the bot, this will execute the command.
    """
    # if the message is from the bot itself ignore it
    if message.author == client.user:
        pass
    else:
        # try to evaluate with the command handler
        try:
            await ch.command_handler(message)
        # message doesn't contain a command trigger, so ignore it
        except TypeError as e:
            pass
        # any other python errors
        except Exception as e:
            print(e)

client.run(token)
