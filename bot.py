import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import requests
import datetime
import json
import random
import asyncio
from pyrandmeme import *
import time
import DiscordUtils
from io import BytesIO



client = commands.Bot(command_prefix='k~')
client.remove_command('help')
api_key = "6beb4cf35bb9797f16db57512aaa1307"
base_url = "http://api.openweathermap.org/data/2.5/weather?"


@client.event
async def on_ready():

	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{len(client.guilds)} Guilds | Use  k~  For help "))

	print("bot is online")
	



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
		embed = discord.Embed(title="kan4me",description="USE `k~` (command) so it will Extended functionality" ,color=0xff0800)
		embed.add_field(name = "🛡️ | MODERATION", value = "`clean`,`lock`,`unlock`,`nickname`,`poll`",inline = False)
		embed.add_field(name = "✍| GENERAL COMMAND", value = "`snipe`, `ping`,`say`,`weather`",inline = False)
		embed.add_field(name = "🎮 | GAMES", value = "`truth&dare(td)`",inline = False)
		embed.add_field(name = "😀 | FUN", value = "`meme`",inline = False)
		embed.add_field(name = "ℹ️ | INFORMATION", value = "`serverinfo`,`userinfo`",inline = False)
		embed.add_field(name = "Link", value = "[invite](https://discord.com/api/oauth2/authorize?client_id=834029114536493066&permissions=8&scope=bot) ",inline = False)
		embed.set_footer(text = f"Requested by  '{ctx.author.name}'",icon_url = ctx.author.avatar_url)
		await asyncio.sleep(2)

	await ctx.send(embed=embed)


@help.command()
async def clean(ctx):
	embed = discord.Embed(title="clean",description="Use this Command to clear messages",colour = 0x6cfd00 )

	embed.add_field(name ="**command**", value = "k~clean (ammount of number)")

	await ctx.send(embed = embed)


@help.command()
async def lock(ctx):
	embed = discord.Embed(title="lock",description="Use this Command to lock a channel.",colour = 0x6cfd00 )

	embed.add_field(name ="**command**", value = "k~lock ")

	await ctx.send(embed = embed)

@help.command()
async def unlock(ctx):
	embed = discord.Embed(title="unlock",description="Use this Command to unlock a channel..",colour = 0x6cfd00 )
	embed.add_field(name ="**command**", value = "k~unlock")

	await ctx.send(embed = embed)


@help.command()
async def nickname(ctx):
	embed = discord.Embed(title="nicknamee",description="Use this Command to change someone's nickname",colour = 0x6cfd00 )

	embed.add_field(name ="**command**", value = "k~nickname `mention the user or paste the id`")

	await ctx.send(embed = embed)

@help.command()
async def poll(ctx):
	embed = discord.Embed(title="poll",description="Use this Command to Conduct a poll and ```poll is in yes and no```",colour = 0x6cfd00 )

	embed.add_field(name ="**command**", value = "k~poll ``event title```")

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
	embed.add_field(name ="**command**", value = "k~truth,Aliases('t') `for truth Qustions` and k~dare,Aliases('d') `for dare Question`") 

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


@client.command()
async def ping(ctx):
	embed = discord.Embed(description = f"ping : {round(client.latency * 100, 2)} ms",color = discord.Color.green())
	embed.set_footer(text=f"Requested by  {ctx.author.name}",icon_url = ctx.author.avatar_url)
	await ctx.send(embed = embed)

@client.command()
async def invite(ctx):
	embed = discord.Embed(description = '[Invite](https://discord.com/api/oauth2/authorize?client_id=834029114536493066&permissions=8&scope=bot)',color = 0xE500FF)
	await ctx.send(embed = embed)
	


@client.command()
async def say(ctx,*,text):
	embed = discord.Embed(description =text,color = discord.Color.random())
	await ctx.message.delete()

	await ctx.send(embed = embed)

@client.command()
async def twitch(ctx):
	embed = discord.Embed(title="TWITCH",url = "https://www.twitch.tv/kan4me",color = discord.Color.purple())
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

	embed = discord.Embed(description = color = 0xE500FF , timestamp = ctx.message.created_at)
	embed.set_author(name = f"Avatar of {member}")
	embed.set_image(url = member.avatar_url)
	embed.set_footer(text=f"Requested by {ctx.author.name}",icon_url = ctx.author.avatar_url)
	await ctx.send(embed = embed)

@client.command()
@commands.has_permissions(manage_channels = True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    embed = discord.Embed(description = ctx.channel.mention + "```went under lockdown mode 🔒 ```",color = 0x3bbf45)
    msg = await ctx.send(embed = embed)
    await msg.add_reaction("✅")
    await ctx.message.delete()
    
    

@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)

    embed = discord.Embed(description = ctx.channel.mention + "```Has removed the lockdown mode 🔓```" , color = 0x3bbf45)
    msg = await ctx.send(embed = embed) 
    await msg.add_reaction("✅")
    await ctx.message.delete()
    


@client.command()
async def serverinfo(ctx):
	role_count = len(ctx.guild.roles)
	list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
	embed = discord.Embed(title = "SERVERINFO",color = 0xffdf00,timestamp =ctx.message.created_at)
	embed.set_thumbnail(url=ctx.guild.icon_url)

	embed.add_field(name ="Server Name", value =ctx.guild.name,inline =False)
	embed.add_field(name ="Total Members", value = ctx.guild.member_count,inline =False)
	embed.add_field(name="Server Region", value=ctx.guild.region,inline =False)
	embed.add_field(name="Server Owner", value=ctx.guild.owner,inline = False)
	embed.add_field(name="Server ID", value=ctx.guild.id,inline =False)
	embed.add_field(name ="Higher role", value = ctx.guild.roles[-2],inline =False)
	embed.add_field(name ="Number of roles", value = str(role_count),inline =False)
	
	embed.set_footer(text=f"Request by {ctx.author.name}",icon_url = ctx.author.avatar_url)

	msg = await ctx.send(embed = embed)
	await msg.add_reaction("✅")


@client.command(aliases=["whois"])
async def userinfo(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author

    roles = [str(role.mention) for role in member.roles][1:]
    
    embed = discord.Embed(colour=0x3bbf45, timestamp=ctx.message.created_at,title=f"User Info - {member}")
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
    embed = discord.Embed(description=f"✅ | Nickname of {member.mention} has been changed")
    await ctx.send(embed = embed)
    await ctx.message.delete()
    


@client.command()
@commands.has_permissions(kick_members=True)
async def poll(ctx,*,question):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(description =f"```The poll: \n{question}```\n✅ = Yes\n❎ = No")
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
	embed = discord.Embed(description=f"{random.choice(dares)}")
	await ctx.send(embed = embed)


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
		"Have you ever blamed your fart on someone else ?"]
    embed = discord.Embed(description =f"{random.choice(truth_list)}")
    await ctx.send(embed = embed)


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
