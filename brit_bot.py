# Work with Python 3.6
import discord
import random
import asyncio
import aiohttp
import json
import confidentials
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = "."
TOKEN = confidentials.BRIT_BOT_TOKEN  # Get at discordapp.com/developers/applications/me

client = Bot(command_prefix=BOT_PREFIX)


@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))


@client.command()
async def fizzbuzz():
    for x in range(100 + 1):
        if x%3 == 0 and x%5 == 0:
            await client.say("FizzBuzz")
        elif x % 3 == 0:
            await client.say("Fizz")
        elif x % 5 == 0:
            await client.say("Buzz")
        else:
            await client.say(str(x))
    

@client.command(name='x3', aliases=["triple"]) # either !x3 or !triple can be sent in discord
async def triple(number):
    tripled_value = int(number) * 3
    await client.say(str(number)+ " tripled is " + str(tripled_value))


@client.command(pass_context = True)
async def alert(context, msg, time):
    await client.say("Alerting you in: " + str(time) + " seconds")
    await asyncio.sleep(int(time))
    await client.say("**ALERT** " + context.message.author.mention + "\n" + str(msg).format(msg))

    

@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])
    

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with humans"))
    print("Logged in as " + client.user.name)


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(TOKEN)
