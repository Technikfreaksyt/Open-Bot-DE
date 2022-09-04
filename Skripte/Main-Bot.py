import time
import discord
from requests import delete
from asyncio import TimeoutError
from discord.utils import get






intents = discord.Intents.all()
intents.members = True
intents.voice_states = True 
client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    
    activity = discord.Game(name="Akivität deines Bots", type=1)

    await client.change_presence(status=discord.Status.online, activity=activity)




autoroles = {
    "ID of your Server": {'memberoles': ["Memberoles"],  }
}

@client.event
async def on_member_join(member):
    await client.get_channel("ID from your Welcome Channel").send (f"Hi {member.mention} willkommen auf meinem Server!")
    guild: guild = member.guild 
    autoguild  = autoroles.get(guild.id)
    if autoguild: autoguild  ['memberoles']
    for roleId in  autoguild['memberoles']:
               role = guild.get_role(roleId)
               if role: 
                   await member.add_roles(role, reason='autoroles, atomic=True')



                             

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')


        

    if message.content.startswith('//support'):
         guild = message.guild
         await message.channel.send('Das Ticket wird erstellt, bitte warten!')
         await message.channel.purge(limit=2)
        
         channel = await guild.create_text_channel(str(message.author))
         await channel.set_permissions(message.author,send_messages=True,read_message_history=True,read_messages=True)
         await channel.set_permissions(discord.utils.get(message.author.guild.roles, id = ("Member") ),send_messages=False,read_messages = False,read_message_history=False)
         await channel.set_permissions(discord.utils.get(message.author.guild.roles, id = ("Staff") ),send_messages=True,read_messages = True,read_message_history=True)

    if message.content.startswith('//voice'):
        guild = message.guild   
        voicechannel = await guild.create_voice_channel(f"vc {str(message.author)}")   

        await message.channel.send('Der Sprachkanal wird erstellt, bitte warten!') 
    
        def checkjoin(member, before, after):

            return member == message.author and after.channel == voicechannel
            
        def checkleave(member, before, after):

            return member == message.author and before.channel == voicechannel and after.channel is None
        await message.channel.purge(limit=2)    
        try:    
            await client.wait_for("voice_state_update", check=checkjoin, timeout=5)   
            
        except TimeoutError:
            print(TimeoutError)
            await voicechannel.delete()
        await client.wait_for("voice_state_update", check=checkleave) 
        await voicechannel.delete()     
    

 

        


    


client.run("Your Token")
