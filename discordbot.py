import time
import discord

#creating a client object of discord
client = discord.Client()

@client.event
async def on_ready():
    #checking if the bot has logged in and in standby
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    #will call this function everytime a new message arrives
    if message.channel.id == 747078225372643399:
        mssg = {'timestamp':int(time.time()),'type': 'chats','discord_id':message.author.id, 'user_name':message.author.name, 'content':message.content}
        print(mssg)
    if message.channel.id == 721334259557597304:
        #check for 'KeyWords ID'
        #return them as a dictinary message

@client.event
async def on_member_join(member):
    #will call this function everytime a member joins
    mssg = {'timestamp':int(time.time()), 'type': 'member_join','discord_id':member.id, 'user_name':member.display_name, 'joined at':member.joined_at,
            'status':member.status, 'roles': member.roles, 'nickname': member.nick, 'activities':member.activities}
    print(mssg)

@client.event
async def on_member_remove(member):
    #will call this function everytime a member leaves or is being removed/kicked
    mssg = {'timestamp':int(time.time()), 'type': 'member_remove','discord_id':member.id, 'user_name':member.display_name, 'joined at':member.joined_at}
    print(mssg)

@client.event
async def on_member_update(before, after):
    #will call this function everytime a member updates its details
    #this might produce a high volume of data.
    if before.id == after.id:
        mssg = {'timestamp':int(time.time()), 'type': 'member_update','discord_id':after.id, 'user_name':after.display_name,
                'status':after.status, 'roles': after.roles, 'nickname': after.nick, 'activities':after.activities}
        print(mssg)

client.run('NzQ3MDcyMzMxMTc5ODg0NjQ0.X0JjUw.WLvxbSp104za--vit1GLarTsDqA')
