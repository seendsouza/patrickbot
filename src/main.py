"""
A bot specifically tailored for my friends' server.
"""

import asyncio
import json

import discord

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import available_backends, execute


# configuring the bot using config.json
with open('config.json') as f:
    data = json.load(f)

token = data["token"]
command_prefix = data["prefix"]
observe_0 = "star"
observe_1 = "wang"

client = discord.Client()

def observe_equal_superposition():
    """
    This function observes a qubit in equal quantum superposition.
    Don't question the practicality of this.
    @return: observed state (0 or 1)
    """
    # TODO: This is deprecated, so consider updating it.
    # Create a Quantum Register with 1 qubit.
    q = QuantumRegister(1)
    # Create a Classical Register with 1 bit.
    c = ClassicalRegister(1)
    # Create a Quantum Circuit
    qc = QuantumCircuit(q, c)
    # Add a H gate on qubit 0, putting this qubit in superposition.
    qc.h(q[0])
    # Add a Measure gate to see the state.
    qc.measure(q, c)
    # Compile and run the Quantum circuit on a simulator backend
    job_sim = execute(qc, "local_qasm_simulator",shots = 1)
    sim_result = job_sim.result()
    return next(iter(sim_result.get_counts(qc)))

def observe_success():
    """
    When a user guesses the state of the qubit after observation correctly
    """
    # TODO: Add currency to users stored in an external file.
    # TODO: Let the user only observe once a day
    pass

def observe_failure():
    """
    When a user guesse the state of the qubit after observation incorrectly
    """
    pass

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('{}test'.format(command_prefix)):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('{}observe'.format(command_prefix)):
        if observe_0 in message.content.lower():
            if int(observe_equal_superposition()) == 0:
                await client.send_message(message.channel, '{} has successfully guessedthe state of '\
                                                           'Patrick.'.format(message.author))
                observe_success()
            else:
                await client.send_message(message.channel, '{} has unsuccessfully guessed the state of '\
                                                           'Patrick.'.format(message.author))
                observe_failure()
        elif observe_1 in message.content.lower():
            if int(observe_equal_superposition()) == 1:
                await client.send_message(message.channel, '{} has successfully guessed the state of '\
                                                           'Patrick.'.format(message.author))
                observe_success()
            else:
                await client.send_message(message.channel, '{} has unsuccessfully guessed the state of '\
                                                           'Patrick.'.format(message.author))
                    
                observe_failure()
        else:
            await client.send_message(message.channel, 'Invalid Input')
    elif message.content.startswith('{}swear'.format(command_prefix)):

client.run(token)
