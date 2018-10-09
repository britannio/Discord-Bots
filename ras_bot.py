# Work with Python 3.6
import discord
from conf import confidentials

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!rules'):
        msg = '__**The Ralph Allen Way**__ \n- Be ready to learn\n- Enable others to learn ' \
              '\n- Treat others and the environment with respect \n- Work to the best of your ability ' \
              '\n- Fulfil your responsibilities'.format(message)
        await client.send_message(message.channel, msg)
        

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(confidentials.RAS_BOT_TOKEN)
