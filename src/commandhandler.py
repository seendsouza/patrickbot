"""
Class for handling commands
"""

import discord
import json

class CommandHandler():
    """
    This class makes integrating commands easier by ingesting an easy format and delivering the commands.
    Examples can be found in main.py
    """
    def __init__(self,client):
        self.client = client
        self.commands = []
    
    def add_command(self,command):
        """
        Adds commands to commands list
        """
        self.commands.append(command)
    
    def command_handler(self,message):
        """
        Main function for handling commands
        """
        for command in self.commands:
           if message.content.startswith(command['trigger']):
                args = message.content.split(' ')
                if args[0] == command['trigger']:
                    args.pop(0)
                    if command['args_num'] == 0:
                        return self.client.send_message(message.channel, str(command['function'](message, self.client, args)))
                        break
                    else:
                        if len(args) >= command['args_num']:
                            return self.client.send_message(message.channel, str(command['function'](message, self.client, args)))
                            break
                        else:
                            return self.client.send_message(message.channel, 'command "{}" requires {} argument(s) "{}"'.format(command['trigger'], command['args_num'], ', '.join(command['args_name'])))
                            break
                else:
                    break  
