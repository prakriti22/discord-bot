import asyncio
import time

import discord

messages = joined = 0

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

# Define the intents
intents = discord.Intents.default()
intents.message_content = True 
intents.members = True  

client = discord.Client(intents=intents)

async def update_stats():
    await client.wait_until_ready()
    global messages, joined
    while not client.is_closed():
        try:
            with open("stats.txt", "a") as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n")
            messages = 0
            joined = 0
            await asyncio.sleep(5)
        except Exception as e:
            print(e)
        await asyncio.sleep(5)

@client.event
async def on_member_update(before,after):
    n=after.nick
    if n:
        if n.lower().count("Prakriti")>0:
            last=before.nick
            if last:
                await after.edit(nick=last)
            else:
                await after.edit(nick="No Stop that")



@client.event
async def on_member_join(member):
    global joined
    joined += 1
    for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send(f"Welcome to Prakriti's Server {member.mention}")

@client.event
async def on_message(message):
    global messages
    messages += 1
    guild = client.get_guild(1249469767597949002)
    channels = ["commands"]
    valid_users = ["prakriti21bce2349"]
    bad_words=["bad","stop","45"]
    
    if message.content =="!help":
        embed=discord.Embed(title="Help on BOT",description="Some useful commands")
        embed.add_field(name="!hello",value="Greets the user")
        embed.add_field(name="!users",value="Prints the numbers of users")
        await message.channel.send(content=None,embed=embed)
        
    for word in bad_words:
        if message.content.count(word)>0:
            print("A bad word was said")
            await message.channel.purge(limit=1)
    if str(message.channel) in channels and str(message.author) in valid_users:
        if message.content.find("!hello") != -1:
            await message.channel.send("Hi")
        elif message.content == "!users":
            await message.channel.send(f"# of Members: {guild.member_count}")
        else:
            print(f"User: {message.author} tried to do command {message.content}, in channel {message.channel}")

async def main():
    async with client:
        client.loop.create_task(update_stats())
        await client.start(token)

# Run the main function
asyncio.run(main())
