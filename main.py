import discord
import os
import random
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!foo'):
        await message.channel.send('bar!')

    if message.content.startswith('!help'):
        await message.channel.send('There is no helping you.')

    if message.content.startswith('!woof'):
        copy_pasta = ("What the fuck did you ...")
        await message.channel.send(copy_pasta)
        await message.channel.send("I mean..")
        await message.channel.send("Woof woof.")
        

    if message.content.startswith('!event'):
        box = message.content[7:].split(' ')

        if box[0] == 'encounter':
            foes =random.randint(1,10)
            send_str = "You are attacked by " + str(foes) + ' ' + box[1]
            await message.channel.send(send_str)

        if box[0] == 'NPC':
            age = random.choice(['young ' , ' middle aged ' , 'old '])
            gender = random.choice(['female ', 'male '])
            race = random.choice(['elf ' , ' dwarf ' , 'gnome '])
            carry = random.choice(['A pair of rabbits ' , 'A hammer ', 'A large sack ', 'A push cart ', 'A pack ladden animal '])
            sports = random.choice(['Crazy hair ' , ' extreme build ' , 'scars ' , ' disablity ' ,' extreme build'])
            accent = random.choice(['suprisingly plain ' , ' softspoken like an asmr vid ' , 'boisterous ' , 'quickly stumbling over there words ' 
            ,'slowly like an ent ', 'a deep accent from a far of land ', 'they numble and stutter ', 'they like to cuss'])
            send_str = "a "  + age + gender + race + " approaches you they carry with them " +carry+ "you instantly notice there "+sports+"but when they open there mouth there accent shocks you, they are " + accent
            await message.channel.send(send_str)

client.run(os.getenv("TOKEN"))
