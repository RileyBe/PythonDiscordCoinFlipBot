import discord
import random

TOKEN = 'BOT TOKEN'


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)

    if (message.author == client.user):
        return

    if (user_message.lower() == '$flip'):
        random.seed(a=None)
        fNum = random.random()
        if(fNum <= 0.425 and fNum > 0.15):
            with open('heads.png', 'rb') as file:
                pic = discord.File(file)
            await message.channel.send(file=pic)
            return
        elif(fNum > 0.425):
            with open('tails.png', 'rb') as file:
                pic = discord.File(file)
            await message.channel.send(file=pic)
            return
        else:
            await message.channel.send('Shut up')
            return
        return

    #if (user_message.lower() == '$picka'):
    #    movies = discord.utils.get(client.get_all_channels(), name='movie-queue')
    #    messages = [message async for message in movies.history(limit=123)]
    #    movie1 = messages[random.randint(0,len(messages)- 1)].content
    #    movie2 = messages[random.randint(0,len(messages)- 1)].content
    #    await message.channel.send('Heads: ' + str(movie1) + ' \nTails: ' + str(movie2))
    #    return


client.run(TOKEN)
