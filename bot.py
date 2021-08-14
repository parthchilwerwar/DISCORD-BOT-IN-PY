import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import requests
from datetime import datetime
import json
import random
import asyncio
from pyrandmeme import *
import time
import DiscordUtils
from io import BytesIO
from discord import FFmpegPCMAudio



client = commands.Bot(command_prefix='k~',intents=discord.Intents.all())
client.remove_command('help')
client.launch_time = datetime.utcnow()
api_key = "6beb4cf35bb9797f16db57512aaa1307"
base_url = "http://api.openweathermap.org/data/2.5/weather?"


@client.event
async def on_ready():

	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"THAT YOU WILL USE | k~  FOR HELP "))

	print("Kan4me is online")
	



snipe_message_author = {}
snipe_message_content = {}
 
@client.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     await asyncio.sleep(60)
     
      
@client.command()
async def snipe(ctx):
    channel = ctx.channel 
    try:
        snipeEmbed = discord.Embed(title=f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id],color=0x43ed35)
        snipeEmbed.set_footer(text=f"Deleted by {snipe_message_author[channel.id]}")
        await ctx.send(embed = snipeEmbed)
    except:
    	embed = discord.Embed(description =f"There are no deleted messages in {ctx.channel.mention}",color = discord.Color.random())
    	await ctx.send(embed = embed)
        


#help commands
@client.group(invoke_without_command=True)
async def help(ctx):
	async with ctx.typing():
		embed = discord.Embed(title="kan4me",description="USE `k~` (command) so it will Extended functionality" ,color=0xF8E3EC)
		embed.add_field(name = "🛡️ | MODERATION", value = "`clean`,`lock`,`unlock`,`nickname`,`poll`,`lockvc`,`unlockvc`,`giverole`",inline = False)
		embed.add_field(name = "✍| GENERAL COMMAND", value = "`snipe`, `ping`,`say`,`weather`")
		embed.add_field(name = "🎮 | GAMES", value = "`truth&dare(td)`",inline = False)
		embed.add_field(name = "😀 | FUN", value = "`meme`")
		embed.add_field(name = "ℹ️ | INFORMATION", value = "`serverinfo`,`userinfo`",inline = False)
		embed.add_field(name = "Link", value = "[invite](https://discord.com/api/oauth2/authorize?client_id=834029114536493066&permissions=8&scope=bot) ",inline = False)
		embed.set_footer(text = f"Requested by  '{ctx.author.name}'",icon_url = ctx.author.avatar_url)
		embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/834029114536493066/a9f7b1a90f23509c21f46b7312c64e07.webp?size=1024")
		await asyncio.sleep(2)

	await ctx.send(embed=embed)


@help.command()
async def clean(ctx):
	embed = discord.Embed(title="clean",description="Use this Command to clear messages",colour = 0x6cfd00 )

	embed.add_field(name ="**command**", value = "k~clean (ammount of number) or else will delete 2 messages")

	await ctx.send(embed = embed)


@help.command()
async def lock(ctx):
	embed = discord.Embed(title="lock",description="Use this Command to lock a channel.",colour = 0x6cfd00 )

	embed.add_field(name ="**command**", value = "k~lock [aliases = l]")

	await ctx.send(embed = embed)

@help.command()
async def unlock(ctx):
	embed = discord.Embed(title="unlock",description="Use this Command to unlock a channel..",colour = 0x6cfd00 )
	embed.add_field(name ="**command**", value = "k~unlock [aliases = ul]")

	await ctx.send(embed = embed)

@help.command()
async def lockvc(ctx):
	embed = discord.Embed(title="lockvc",description="Use this Command to lock all vc of a guild",colour = 0x6cfd00 )
	embed.add_field(name ="**command**", value = "k~lockvc [aliases = lvc]")

	await ctx.send(embed = embed)

@help.command()
async def unlockvc(ctx):
	embed = discord.Embed(title="unlockvc",description="Use this Command to unlock all vc of a guild",colour = 0x6cfd00 )
	embed.add_field(name ="**command**", value = "k~unlockvc [aliases = ulv]")

	await ctx.send(embed = embed)

@help.command()
async def giverole(ctx):
	embed = discord.Embed(title="Giverole",description="Use this Command to give someone specific role",colour = 0x6cfd00 )
	embed.add_field(name ="**command**", value = "k~giverole <mention_user/user_id> <role_id/mention_role> [aliases = gr]")

	await ctx.send(embed = embed)

@help.command()
async def nickname(ctx):
	embed = discord.Embed(title="nicknamee",description="Use this Command to change someone's nickname",colour = 0x6cfd00 )

	embed.add_field(name ="**command**", value = "k~nickname `mention the user or paste the id`")

	await ctx.send(embed = embed)

@help.command()
async def poll(ctx):
	embed = discord.Embed(title="poll",description="Use this Command to Conduct a poll and ```poll is in yes and no```",colour = 0x6cfd00 )

	embed.add_field(name ="**command**", value = "k~poll ```event title```")

	await ctx.send(embed = embed)



@help.command()
async def snipe(ctx):
	embed = discord.Embed(title="snipe",description="Shows the last deleted message from a specified channel",color = 0x43ed35)

	embed.add_field(name ="**command**", value = "k~snipe")

	await ctx.send(embed = embed)


@help.command()
async def meme(ctx):
	embed = discord.Embed(title="MEME",description="use this command to create random meme", color = discord.Color.random())

	embed.add_field(name ="**command**", value = "k~meme")

	await ctx.send(embed = embed)

@help.command()
async def  weather(ctx):
	embed = discord.Embed(title="Weather",description="use this command to know the weather of any `city in the world`", color = discord.Color.random())

	embed.add_field(name ="**command**", value = "k~weather , example: k~weather (`city name`)")

	await ctx.send(embed = embed)



@help.command()
async def ping(ctx):
	embed = discord.Embed(title="PING",description="Use this command to check your ping", color = discord.Color.purple())

	embed.add_field(name ="**command**", value = "k~ping")

	await ctx.send(embed = embed)



@help.command()
async def say(ctx):
	embed = discord.Embed(title="SAY",description="Use this command to say in embed", color = discord.Color.random())
	embed.add_field(name ="**command**", value = "k~say (your text)")


	await ctx.send(embed = embed)

@help.command()
async def serverinfo(ctx):
	embed = discord.Embed(title="SERVER INFO",description="Use this command to see info of server", color = discord.Color.random())
	embed.add_field(name ="**command**", value = "k~serverinfo")


	await ctx.send(embed = embed)

@help.command()
async def userinfo(ctx):
	embed = discord.Embed(title="USER INFO",description="Use this command to see someones or else your info", color = discord.Color.random())
	embed.add_field(name ="**command**", value = "k~userinfo ``mention the person or else add his id``  or Aliases ``k~whois``") 

	await ctx.send(embed = embed)


@help.command()
async def td(ctx):
	embed = discord.Embed(title="TRUTH & DARE ",description="Use this command to play game of truth and dare", color = discord.Color.random())
	embed.add_field(name ="**command**", value = "k~truth,Aliases('t') `for truth Qustions` and k~dare,Aliases('d') `for dare Questions`") 

	await ctx.send(embed = embed)





@help.command()
async def music(ctx):
    embed1 = discord.Embed(color=0x3bbf45).add_field(name="Prefix", value="k~")
    embed2 = discord.Embed(color=0x3bbf45).add_field(name="ABOUT ME", value="I was made by a person who just completed the codes of mine in one year , He was a noob coder but later on he made many bot's and Now i'm proud to be his bot")
    embed3 = discord.Embed(color=0x3bbf45).add_field(name="Vote", value="#")
    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx)
    paginator.add_reaction('⏮️', "first")
    paginator.add_reaction('⏪', "back")
    paginator.add_reaction('🔐', "lock")
    paginator.add_reaction('⏩', "next")
    paginator.add_reaction('⏭️', "last")
    embeds = [embed1, embed2, embed3]
    await paginator.run(embeds)



#all commands

@client.command()
async def uptime(self ,ctx):
	delta_uptime = datetime.datetime.utcnow() - self.bot.launch_time
	hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
	minutes, seconds = divmod(remainder, 60)
	days, hours = divmod(hours, 24)
	embed = discord.Embed(title=f"I've been up  for {days}d, {hours}h, {minutes}m, {seconds}s,", color=discord.Color.green())
	await ctx.send(embed = embed)

@client.command(aliases=["anou"])
async def announce(ctx,channel: discord.TextChannel,* ,msg):
    embed = discord.Embed(description=f"{msg}",color= discord.Color.random())
    await channel.send(embed = embed)
    await ctx.send(f"Announcement Done Successful")
    await ctx.message.delete()

@client.command()
async def ping(ctx):
	embed = discord.Embed(description = f"ping : {round(client.latency * 100, 2)} ms",color = discord.Color.green())
	embed.set_footer(text=f"Requested by  {ctx.author.name}",icon_url = ctx.author.avatar_url)
	await ctx.send(embed = embed)

@client.command()
async def invite(ctx):
	embed = discord.Embed(description = '[```Invite```](https://discord.com/api/oauth2/authorize?client_id=834029114536493066&permissions=8&scope=bot)',color = 0xF8E3EC)
	await ctx.send(embed = embed)
	
@client.command(pass_context=True,aliases=["gr"])
async def giverole(ctx, user: discord.Member, role: discord.Role):
    embed = discord.Embed(description=f"{user.mention},{ctx.author.name} Just gave you{role.mention} Role")
    await user.add_roles(role)
    await ctx.send(embed=embed)

@client.command()
async def say(ctx,*,text):
	embed = discord.Embed(description =text,color = discord.Color.random())
	await ctx.message.delete()

	await ctx.send(embed = embed)

@client.command()
async def twitch(ctx):
	embed = discord.Embed(title="TWITCH",url = "https://www.twitch.tv/kan4me",color = 0xF8E3EC)
	await ctx.send(embed = embed)

@client.command()
async def meme(ctx):
	embed = await pyrandmeme()
	embed.title = "kan4me"
	embed.description = "Memes"
	embed.color = discord.Color.random()
	await ctx.send(embed = embed)

@client.command()
@commands.has_permissions(kick_members= True)
async def clean(ctx , amount=2):
	await ctx.message.delete()
	await ctx.channel.purge(limit=amount)

@client.command(aliases=["av"])
async def avatar(ctx,*, member: discord.Member=None):
	if not member:
		member = ctx.message.author
	userAvatar = member.avatar_url

	embed = discord.Embed(color = 0xE500FF , timestamp = ctx.message.created_at)
	embed.set_author(name = f"Avatar of {member}")
	embed.set_image(url = member.avatar_url)
	embed.set_footer(text=f"Requested by {ctx.author.name}",icon_url = ctx.author.avatar_url)
	await ctx.send(embed = embed)

@client.command(aliases=["l"])
@commands.has_permissions(manage_channels = True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    embed = discord.Embed(description = ctx.channel.mention + "```went under lockdown mode 🔒 ```",color = 0x3bbf45)
    msg = await ctx.send(embed = embed)
    await msg.add_reaction("✅")
    await ctx.message.delete()
    
    

@client.command(aliases=["ul"])
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)

    embed = discord.Embed(description = ctx.channel.mention + "```Has removed the lockdown mode 🔓```" , color = 0x3bbf45)
    msg = await ctx.send(embed = embed) 
    await msg.add_reaction("✅")
    await ctx.message.delete()
    
@client.command(aliases=["lvc"])  
async def lockvc(ctx):
     msg = await ctx.channel.send(f"```{ctx.guild.name}    Voice channels are now lockded 🔒```")
     for channel in ctx.guild.voice_channels:
          await channel.set_permissions(ctx.guild.default_role, connect=False)
          await msg.add_reaction("✅")

@client.command(aliases=["ulv"])
async def unlockvc(ctx):
    msg = await ctx.channel.send(f"```{ctx.guild.name}    Voice channels are now unlock  🔓```")
    for channel in ctx.guild.voice_channels:
        await channel.set_permissions(ctx.guild.default_role, connect=True) 
        await msg.add_reaction("✅")  

@client.command()
async def serverinfo(ctx):
	role_count = len(ctx.guild.roles)
	list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
	embed = discord.Embed(title = "SERVERINFO",color = 0xffdf00,timestamp =ctx.message.created_at)
	embed.set_thumbnail(url=ctx.guild.icon_url)

	embed.add_field(name ="Server Name", value =ctx.guild.name)
	embed.add_field(name ="Total Members", value = ctx.guild.member_count,inline =False)
	embed.add_field(name="Server Region", value=ctx.guild.region)
	embed.add_field(name="Server Owner", value=str(ctx.guild.owner),inline = False)
	embed.add_field(name="Server ID", value=ctx.guild.id)
	embed.add_field(name ="Higher role", value = ctx.guild.roles[-2],inline =False)
	embed.add_field(name ="Number of roles", value = str(role_count))
	
	embed.set_footer(text=f"Request by {ctx.author.name}",icon_url = ctx.author.avatar_url)

	msg = await ctx.send(embed = embed)
	await msg.add_reaction("✅")


@client.command(aliases=["whois"])
async def userinfo(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author

    roles = [str(role.mention) for role in member.roles][1:]
    
    embed = discord.Embed(colour=0xffdf00, timestamp=ctx.message.created_at,title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")
    embed.add_field(name="ID:", value=member.id,inline =False)
    embed.add_field(name="Display Name:", value=member.display_name,inline =False)
    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Highest Role:", value=member.top_role.mention,inline =False)
    embed.add_field(name="Roles:", value=" ".join(roles),inline =False)

    await ctx.send(embed=embed)

@client.command(pass_context=True)
@commands.has_permissions(kick_members =True)
async def nickname(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    embed = discord.Embed(description=f"✅ | Nickname of {member.mention} has been changed",color = 0xF8E3EC)
    await ctx.send(embed = embed)
    await ctx.message.delete()
    


@client.command()
@commands.has_permissions(kick_members=True)
async def poll(ctx,*,question):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(description =f"{question}\n✅ = Yes\n❎ = No",colour = 0xFFF474)
    message = await ctx.send(embed = embed)
    await message.add_reaction('✅')
    await message.add_reaction('❎')


@client.command(aliases=["d"])
async def dare(ctx):
	dares = ["Serenade the person to your right.",
		"Kiss the person to your left.",
		"Attempt to do a magic trick.",
		"Do four cartwheels in row.",
		"Let someone shave part of your body.",
		"Go up to someone and scare them.",
		"Very affectionately kiss another participant (the rest can choose whom).",
		"Give a massage to a companion for 5 minutes.",
		"Eat a tablespoon of butter.",
		"Do an impression of your favorite celebrity",
		"Close your eyes and send a blind text to a random person",
		"Go grab a broom and do your best tango",
		"Give a 3 minute stand-up comedy routine",
		"Break dance",
		"Make up a story about the item to your right",
		"Sing the alphabet without moving your mouth",
		"Do your best president impression",
		"Yell out the first word that comes to your mind right now",
		"Call the pizza place and order 300 sardine pizzas",
		"Pound on your chest and act like a gorilla for the next minute",
		"Sing everything you say for the next 10 minutes",
		"Give a foot massage to someone beside you",
		"Say the alphabet backwards in 15 seconds",
		"Go to the neighbour’s house and ask for a banana",
		"Go up to someone random and ask for a hug",
		"Set your cell phone language to Chinese for the next 10 minutes",
		"Act like your favourite Disney character for the rest of the game",
		"Sing “Twinkle Twinkle, Little Star” while beat boxing",
		"Give a concert with your air guitar",
		"Make a poem using the words orange and moose",
		"Unbuckle your own belt using your elbows",
		"Brush someone else’s teeth",
		"Twerk for a minute",
		"Belly dance to a country song",
		"Make up a country song of the top of your head",
		"Get on all fours and act like a dog until your next turn",
		"Make up a short rap about another player",
		"Act like Romeo from “Romeo and Juliet” (pick who you want to be Juliet)",
		"Do an impression of someone until another player can guess who you are,"
		"Say “ya heard meh” after everything you say for the next 5 minutes",
		"Act like you do not understand your own language until your next turn (come up with your own language)",
		"Use the letters of the name of another player to describe them (ex. SAM : S – Silly ; A – Attractive ; M – Merry)",
		"Only use sign language for the next round",
		"Do pushups until it’s your turn again",
		"Wear a finger moustache for the next 5 minutes",
		"Only use your elbows and knees to go make a sandwich",
		"Write a Facebook (or other social media) post only using your toes",
		"Take a selfie with the toilet and post it online",
		"Paint your toenails only using your teeth",
		"Asks for money on the street telling a funny story and nothing credible and board 50$.",
		"Sing and dance in the street like crazy.",
		"Become the slave of another player of your choosing for 5 mins.",
		"Embrace the first passing through the street",
		"Dance with a broom or mop.",
		"For guys: Briefly walk like a lady in high heels.",
		"Climb to sing in the bar of a bar.",
		"Declare who is your true love.",
		"Tell something very intimate.",
		"Completely cover yourself in toilet paper to look like a mummy.",
		"Randomly ring a person from your phone and sing them a song.",
		"Ring a family member of someone in the room and explain why you love your friend so much.",
		"Mix all the sauces you have in your fridge and drink up.",
		"Prank call a friend’s partner.",
		"Call up a pizza and order Chinese food",
		"Take a shower without removing any of your clothes.",
		"Cover up your eyes (or wear a blindfold), and walk around the room for two minutes without watching where you’re going.",
		"Impersonate someone in the room and people have to guess who it is.",
		"Improvise and perform a two-minute comedy routine in front of everyone.",
		"Act like a dog for two minutes without laughing.",
		"Pour a freezing cold glass of water over your face without reacting.",
		"Tell a stranger walking past that you love them.",
		"Put as many pieces of cheese puffs in your mouth at one time as you can.",
		"Screenshot a picture of your browser history and send it to a random person in your contacts.",
		"Log into Facebook and like every picture for the past year of the first person you see.",
		"Rip off a piece of paper and eat it.",
		"Take out an eat and eat it raw.",
		"Cover your hair with milk and don’t wash off until the end of the game.",
		"Text your mom the last picture saved on your phone.",
		"Pretend to be a chicken for 30 seconds.",
		"Stand up and run on the spot as fast as you can until it’s your turn.",
		"Sniff the player to your right’s armpit.",
		"Allow another player to throw flour in your face.",
		"Allow a random player to tickle you for 30 seconds.",
		"Kiss someone’s bare foot.",
		"Go into the kitchen and take a bite out of something in the trash.",
		"Spritz perfume into your mouth.",
		"Head outside a lick a car tire.",
		"Take a picture of yourself pulling a funny face and set it as your Facebook profile picture for the rest of the day and night.",
		"Pass your phone to the person to your right and allow them to put any status on one of your social media accounts.",
		"Let someone in the group give you a wedgie.",
		"Grab a random object in the room and try and sell it to the group for two minutes.",
		"Kiss the second person to your left on the lips.",
		"Sing the chorus from a random song with all your heart.",
		"Speak in a baby’s voice for the next five things you have to say.",
		"Give someone in the group all the money you have in your purse.",
		"Take someone’s socks off and wear them like gloves for three minutes.",
		"Slap yourself in the face any time someone says “and” in the next three minutes.",
		"Blindfold yourself and let someone in the group feed you something of their choosing.",
		"Knock on your neighbor’s door and tell them how grateful they should be to live next to someone so awesome.",
		"Try to lick your elbow for the next three minutes.",
		"Laugh out loud at everything the person to your left says until it’s your turn.",
		"Stand up and try to break dance."]
	embed = discord.Embed(description=f"{random.choice(dares)}",color =0xF8E3EC)
	await ctx.reply(embed=embed, mention_author=False)


@client.command(aliases=["t"])
async def truth(ctx):
    truth_list = ["Have you ever skipped school ?",
    	"Have you ever cried during a movie? If so, which one ?",
    	"Have you ever lied about your age ?",
    	"Do you have any secrets ?",
    	"What are some ways you cheat on chores ?",
    	"Have you ever snuck a snack ?",
    	"When was the last time you cleaned your room ?",
    	"What is the least favorite gift you’ve ever received ?",
    	"Have you ever broken something and blamed someone else ?",
    	"If you could be any celebrity, who would you be and why ?",
    	"Have you ever used your lunch money for something other than lunch ?",
    	"What is your biggest fear ?",
    	"Describe a time you thought to yourself, oh no! I am turning into my parents!",
    	"When was the last time you lied ?",
		"When was the last time you cried ?",
		"What's your biggest fear ?",
		"What's your biggest fantasy ?",
		"Do you have any fetishes ?"
		"What's something you're glad your mum doesn't know about you ?"
		"Have you ever cheated on someone ?",
		"What's a secret you've never told anyone ?",
		"Who was your first celebrity crush ?",
		"What are your thoughts on polyamory ?",
		"What's the worst intimate experience you've ever had ?",
		"What's the best intimate experience you've ever had ?",
		"Have you ever cheated in an exam ?",
		"What's the most drunk you've ever been ?",
		"Have you ever broken the law ?",
		"What's the most embarrassing thing you've ever done ?",
		"What's your biggest insecurity ?",
		"Have you ever stayed friends with someone because it benefitted you beyond just the friendship ?",
		"What's the biggest mistake you've ever made ?",
		"What's the most disgusting thing you've ever done ?",
		"Who would you like to kiss in this room ?",
		"What's one thing you hate people knowing about you ?",
		"What's the worst thing anyone's ever done to you ?",
		"What's the best thing anyone's ever done for you ?",
		"Have you ever had a run in with the law ?",
		"What's your worst habit ?",
		"What's the most embarrassing thing you've done in a taxi ?",
		"What's the worst thing you've ever said to anyone ?",
		"Have you ever peed in the shower ?",
		"What's the strangest dream you've had ?",
		"Have you ever been caught doing something you shouldn't have ?",
		"What's the worst date you've been on ?",
		"What's the best date you've been on ?",
		"What happened on the latest night out you've ever had ?",
		"What's your biggest regret ?",
		"What's the biggest misconception about you ?",
		"Have you ever said something you regret about someone in this room ?",
		"What's one thing you wish people knew about you ,"
		"Where's the weirdest place you've had sex?",
		"Why did your last relationship break down ?",
		"Have you ever lied to get out of a bad date ?",
		"What's the most trouble you've been in ?",
		"When did you last have sex outside ?",
		"What's the worst thing you've lied about ?",
		"What's one thing you wish you'd lied about ?",
		"What's the best piece of advice you've been given ?",
		"What's the most you've spent on a night out ?",
		"Name a time you think you were a bad partner",
		"What's your guilty pleasure ?",
		"What's one thing you only do when you're alone ?",
		"If you had to get back with an ex, who would you choose ?",
		"If you had to cut one friend out of your life, who would it be ?",
		"Do you have a favourite friend ?",
		"Do you have a favourite sibling ?",
		"What's the strangest rumour you've heard about yourself ?",
		"What's your biggest turn on ?",
		"What's the silliest reason you've left a club early ?",
		"If you could swap lives with someone in this room, who would it be ?",
		"Have you ever had a crush on a teacher ?",
		"What’s the longest time you’ve stayed in the bathroom, and why did you stay for that long ?",
		"Who do you prefer, your mom or your dad ?",
		"Do you pee in the shower ?",
		"Have you ever told a secret you promised to keep ?",
		"How old were you when you found out how babies are made ?",
		"What’s the dumbest thing you’ve done to impress a crush ?",
		"Have you ever publicly peed yourself ?",
		"If you could get surgery to look like any celebrity, who would it be ?",
		"If you could rob a bank and get away with it, would you ?",
		"If you had to swap lives with someone in this room, who would it be and why ?",
		"Have you ever pretended to like a gift you hated and what did you do with it ?",
		"If you had to date someone in this room, who would it be and why ?",
		"Have you ever started a rumor about someone else ?",
		"What would you do if you found out you were cheated on ?",
		"Have you ever flirted with a friend’s sibling ?",
		"If you had to stop talking to one person in this room, who would it be and why ?",
		"What’s the longest amount of recreational time you’ve spent on your phone or computer ?",
		"If you were to become famous, what would it be for ?",
		"Where do you see yourself in five years ?",
		"What would you do if you were invisible for a day ?",
		"What was the most awkward date you’ve been on ?",
		"What is a word that you’ve made up ?",
		"What is your least favorite meal that your mom makes ?",
		"What was the last thing you search for on your phone ?",
		"Have you ever pretended to be sick to get out of plans ?",
		"If you could add a single option to your car (anything!), what would it be ?",
		"If you were a student at Hogwarts, which professor would you want ?",
		"Have you ever lied during a round of Truth or Dare ?",
		"What’s something you like to eat that other people would find weird ?",
		"Have you ever farted in an elevator ?",
		"Have you ever broken something and not told somebody ?",
		"Is there anything hidden under your bed right now ?",
		"What would you do with $1000 ?",
		"What do you consider your worst habit to be ?",
		"Have you ever peed in a swimming pool ?",
		"When was the last time you flossed your teeth ?",
		"Do you pick at your scabs ?",
		"Have you ever had foot fungus ?",
		"What’s the strangest dream you’ve ever had ?",
		"Would you rather have a sibling or a pet ?",
		"Which Harry Potter character would you be and why ?",
		"If you had a time machine, which time period would you travel back to visit ?",
		"If you could have a pet dinosaur, what kind would you want ?",
		"Have you ever fed your vegetables to the dog ?",
		"Have you ever watched a movie you’re not supposed to ?",
		"What’s your least favorite movie ?",
		"What do you dislike most about family gatherings ?",
		"Do you have a strange collection? If so, what ?",
		"Have you ever shared your chewing gum (chewed) with someone else before ?",
		"What’s the longest you’ve ever had an overdue library book ?",
		"Would you eat a piece of pizza out of the trash ?",
		"Have you ever thrown up on a roller coaster ?",
		"Have you ever blamed your fart on someone else ?",
		












		]
    embed = discord.Embed(description =f"{random.choice(truth_list)}",color =0xF8E3EC)
    await ctx.reply(embed = embed, mention_author=False)


@client.command()
async def weather(ctx, *, city: str):
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    channel = ctx.message.channel
    if x["cod"] != "404":
    	async with channel.typing():
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature_celsiuis: str = str(round(current_temperature - 273.15))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            embed = discord.Embed(title=f"Weather in {city_name}",
                                  color= 0x55e4ff,
                                  timestamp=ctx.message.created_at, )
            embed.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
            embed.add_field(name="Temperature(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
            embed.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
            embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
            embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRR3h_gwYzhHV9_yJj9tnPLomfRqF2iWLlyKSi4V1eZdFBP7N8KnrAjPeUAv0Ir0T-lPqtMo-xNSiw&usqp=CAU")
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await channel.send(embed=embed)
    elif not x["cod"] != "404":
    	embed = discord.Embed(description="The following city was not found `due to wrong spelling of city` ")
    	await ctx.message.delete()
    	await asyncio.sleep(1)
    	await channel.send(embed=embed)
       
#fun commands

@client.command(aliases=["k"])
async def kiss(ctx):


    kiss =[
    "https://media1.giphy.com/media/kU586ictpGb0Q/giphy.gif?cid=ecf05e478364xmyyaif02ureji086b3ls6lzpqhpk666lh0g&rid=giphy.gif&ct=g", 
    "https://media1.giphy.com/media/zkppEMFvRX5FC/giphy.gif?cid=ecf05e47aswq2rkl87iqpswtn7rpthceezksgmhl5mdi9iua&rid=giphy.gif&ct=g",
    "https://media3.giphy.com/media/bm2O3nXTcKJeU/giphy.gif?cid=ecf05e47ou3d5q96rn8h9xkgumigf1v80ozfcdcl30imy3d1&rid=giphy.gif&ct=g", 
    "https://media1.giphy.com/media/jR22gdcPiOLaE/giphy.gif?cid=ecf05e47vty3hv8rp5an2fqnt3851wtncoqm6ebkhmwm2cpy&rid=giphy.gif&ct=g",
    "https://media3.giphy.com/media/Ka2NAhphLdqXC/giphy.gif?cid=ecf05e47tyhvmlb1l8b6u7lclh4opg60evfvzz1a1t1hafn0&rid=giphy.gif&ct=g",
    "https://media1.giphy.com/media/bm2O3nXTcKJeU/giphy.gif?cid=ecf05e47f6ujv7jsrwcn998lrl1y7kfvhh835fasd215x5il&rid=giphy.gif&ct=g",
    "https://media0.giphy.com/media/nyGFcsP0kAobm/giphy.gif?cid=ecf05e47037uw2euh7q6txd13zhgu369516yh8k32t792dyz&rid=giphy.gif&ct=g",
    "https://media0.giphy.com/media/AZSjToDmW19WU/giphy.gif?cid=ecf05e47h3kil4tedh89v5jtmnlyn85xad07v1sypi5dg5hx&rid=giphy.gif&ct=g",
    "https://media1.giphy.com/media/JYpVJEcNrDAWc/giphy.gif?cid=ecf05e471od5itckugvl6dm8f7rgas4zsqxcbv499furk6sy&rid=giphy.gif&ct=g",
    "https://media4.giphy.com/media/w9xag7QUzLgLC/giphy.gif?cid=ecf05e477brcf2ak15okjs7b62z6gs79wp06rrszldhkqgdb&rid=giphy.gif&ct=g",
    "https://media0.giphy.com/media/H8XZI3PJm258c/giphy.gif?cid=ecf05e471ok5vo6cegt8thwq48fq68xo2brskturmws0ivjx&rid=giphy.gif&ct=g",
    "https://media0.giphy.com/media/VXsUx3zjzwMhi/giphy.gif?cid=ecf05e47ebfupjgmiogjsqzfunry2hpa9e3548obivsb1u23&rid=giphy.gif&ct=g",
    "https://media1.giphy.com/media/9oEli3vlVaOys/giphy.gif?cid=ecf05e47391ilxca9zmo232ohl2fjsog3p772voy3a66kei7&rid=giphy.gif&ct=g"]
    embed = discord.Embed(color = discord.Color.random())	
    random_link = random.choice(kiss)
    embed.set_image(url = random_link)
    await ctx.send(embed = embed)

@client.command(aliases=["h"])
async def hug(ctx):

    hug =[
    "https://media2.giphy.com/media/od5H3PmEG5EVq/giphy.gif?cid=ecf05e47hr1v6n1cw9v1xwg5ymepkmisnu6aj10v02338ejh&rid=giphy.gif&ct=g",
    "https://media2.giphy.com/media/ZQN9jsRWp1M76/giphy.gif?cid=ecf05e47r0yddo90i00k9qg00yd9nsvk9nccovzne2221yqk&rid=giphy.gif&ct=g",
    "https://media2.giphy.com/media/DjczAlIcyK1Co/giphy.gif?cid=ecf05e47rv588n2k7n3bkizs7xftx2md8iu1cp79cgdsqmvx&rid=giphy.gif&ct=g",
    "https://media4.giphy.com/media/xJlOdEYy0r7ZS/giphy.gif?cid=ecf05e47f914mf50rmrx9ax1v32edl6tiyrt2swy3mknf5fo&rid=giphy.gif&ct=g",
    "https://media4.giphy.com/media/sUIZWMnfd4Mb6/giphy.gif?cid=ecf05e47hr1v6n1cw9v1xwg5ymepkmisnu6aj10v02338ejh&rid=giphy.gif&ct=g",
    "https://media3.giphy.com/media/wSY4wcrHnB0CA/giphy.gif?cid=ecf05e47ozgkengb3ss9x8k6k3vm44xba1ddnvec926opgew&rid=giphy.gif&ct=g",
    "https://media4.giphy.com/media/svXXBgduBsJ1u/giphy.gif?cid=ecf05e47o2a2hviriw4io4aow6g71gmw50pmlhrhf4xoc5dm&rid=giphy.gif&ct=g",
    "https://media3.giphy.com/media/IRUb7GTCaPU8E/giphy.gif?cid=ecf05e47kcjghjiiqwfnvy0o1ysulsiufmcy1paenver04na&rid=giphy.gif&ct=g",
    "https://media0.giphy.com/media/u9BxQbM5bxvwY/giphy.gif?cid=ecf05e47sv3vb435bafpcy000idda2p2d0yctrkw9aiz3irh&rid=giphy.gif&ct=g",
    "https://media0.giphy.com/media/49mdjsMrH7oze/giphy.gif?cid=ecf05e47xp6v79bnn8pra2k4w8rq413boqx9cfs6jtrlip5c&rid=giphy.gif&ct=g",
    "https://media0.giphy.com/media/3OCOHkV0ZOZ2g/giphy.gif?cid=ecf05e47dh5x9pbtfjhcui3r0450ahb9x8wfw9efw7xf1syl&rid=giphy.gif&ct=g",
    "https://media2.giphy.com/media/2A75Y6NodD38I/giphy.gif?cid=ecf05e47i2mx5fnz8ur4ejjh39qrbgw0o9ar9szadj6ode3f&rid=giphy.gif&ct=g",
    "https://media3.giphy.com/media/2z0vIXgRbRrb2/giphy.gif?cid=ecf05e472rhfo6ntmep3h4pzgkpwtifi9xyxd9hks8s941hi&rid=giphy.gif&ct=g",
    "https://media4.giphy.com/media/C4gbG94zAjyYE/giphy.gif?cid=ecf05e47lts8xc8rhugnexojkmdw0559vaavz76sccoyfddz&rid=giphy.gif&ct=g",
    "https://media0.giphy.com/media/ZQN9jsRWp1M76/giphy.gif?cid=ecf05e47l7twrsoq5bcyhc6520u7k3dge8bfo4bwgnzu1t68&rid=giphy.gif&ct=g",]
    embed = discord.Embedcolor = discord.Color.random())	
    random_link = random.choice(hug)
    embed.set_image(url = random_link)
    await ctx.send(embed = embed)


@client.command(aliases=["s"])
async def slap(ctx):
    slap =[
    "https://media2.giphy.com/media/tX29X2Dx3sAXS/giphy.gif?cid=ecf05e47auaianv8wu2sifvpa3xegqny85ht374wdey97qrg&rid=giphy.gif&ct=g",
    "https://media2.giphy.com/media/Zau0yrl17uzdK/giphy.gif?cid=ecf05e477tzj0undwh0m076uljg6uq09a787fa27kcppnu6a&rid=giphy.gif&ct=g",
    "https://media0.giphy.com/media/xUO4t2gkWBxDi/giphy.gif?cid=ecf05e47ull4fm9cyrti9okbo8a3dxfsj1v95uvm6v8azee2&rid=giphy.gif&ct=g",
    "https://media3.giphy.com/media/Gf3AUz3eBNbTW/giphy.gif?cid=ecf05e47uub0cvr5a9v7xxv2sm3hwwckq0hvn9gqdcdyvp8t&rid=giphy.gif&ct=g",
    "https://media4.giphy.com/media/9U5J7JpaYBr68/giphy.gif?cid=ecf05e47auaianv8wu2sifvpa3xegqny85ht374wdey97qrg&rid=giphy.gif&ct=g",
    "https://media4.giphy.com/media/xUNd9HZq1itMkiK652/giphy.gif?cid=ecf05e47auaianv8wu2sifvpa3xegqny85ht374wdey97qrg&rid=giphy.gif&ct=g",
    "https://media3.giphy.com/media/6Fad0loHc6Cbe/giphy.gif?cid=ecf05e47e4frejj7bb1p7xlx0v1mwfs9tsdd15kbdrrpshaa&rid=giphy.gif&ct=g",
    "https://media0.giphy.com/media/AW8xRg8LNiR2g/giphy.gif?cid=ecf05e47m9wh0wx7q7c76abr2sco8dct7r5idr43iibksnpl&rid=giphy.gif&ct=g",
    "https://media3.giphy.com/media/qNtqBSTTwXyuI/giphy.gif?cid=ecf05e47pamc15zulqv5971a2wsbd75rtal6at21zpy9l924&rid=giphy.gif&ct=g",
    "https://media4.giphy.com/media/Y6c59hTH3TJoA/giphy.gif?cid=ecf05e472wclrvj134n30melshpmriddb7j08w4ehpbmoib4&rid=giphy.gif&ct=g",
    "https://media4.giphy.com/media/EQ85WxyAAwEaQ/giphy.gif?cid=ecf05e47ym8mm1sx7rect5kjib30xlis65t2166ogf5anr64&rid=giphy.gif&ct=g",
    "https://media1.giphy.com/media/LB1kIoSRFTC2Q/giphy.gif?cid=ecf05e47j1qz7o218j04jt7v7i1xlb1zl95uj4ta36igk0f2&rid=giphy.gif&ct=g",
    "https://media3.giphy.com/media/k1uYB5LvlBZqU/giphy.gif?cid=ecf05e471q920321wrkkliatsupntd98lxeg1ciax1q4gxwf&rid=giphy.gif&ct=g",
    "https://media4.giphy.com/media/7u6Lr6c6ZIOqY/giphy.gif?cid=ecf05e479p119xq1iyxfzmg2qrt59h36426a9xkd3xf6758f&rid=giphy.gif&ct=g",
   	]
    embed = discord.Embed(color = discord.Color.random())	
    random_link = random.choice(slap)
    embed.set_image(url = random_link)
    await ctx.send(embed = embed)


#music commands



@client.event
async def on_command_error(ctx,error):
	if isinstance(error ,CommandNotFound):
		embed = discord.Embed(tittle=f"Command",description="❌  | You have used wrong command so, use `k~help` to get help! Thank You",color = 0xff0800)
		await ctx.message.delete()
		await ctx.send(embed = embed)
	if isinstance(error,commands.MissingPermissions):
		embed = discord.Embed(description="❌  | You are not able to use that command",color = 0xff0800)
		await ctx.message.delete()
		await ctx.send(embed = embed)
	elif isinstance(error,commands.MissingRequiredArgument):
		embed = discord.Embed(description="✅   |  Hey, provide a proper Arguments",color = 0x3bbf45)
		await ctx.message.delete()
		await ctx.send(embed = embed)




client.run("ODM0MDI5MTE0NTM2NDkzMDY2.YH68JA.oIgLjbDK3ZGUqCj-Sh8AfvsSyUU")
