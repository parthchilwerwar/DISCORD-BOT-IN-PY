import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import datetime
import random
import asyncio
from pyrandmeme import *
import time
import DiscordUtils
from io import BytesIO



client = commands.Bot(command_prefix='k~')
client.remove_command('help')


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
		embed.add_field(name = "✍| GENERAL COMMAND", value = "`snipe`, `ping`,`say`",inline = False)
		embed.add_field(name = "🎮 | GAMES", value = "`truth&dare`(td)",inline = False)
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
async def jack(ctx):
    async with ctx.typing():
        # do expensive stuff here
        await asyncio.sleep(10)
    await ctx.send('done!')
	
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



@client.command()
@commands.has_permissions(manage_channels = True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    embed = discord.Embed(description = ctx.channel.mention + "```went under lockdown mode 🔒 ```",color = 0x3bbf45)
    msg = await ctx.send(embed = embed)
    await msg.add_reaction("✅")
    

@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)

    embed = discord.Embed(description = ctx.channel.mention + "```Has removed the lockdown mode 🔓```" , color = 0x3bbf45)
    msg = await ctx.send(embed = embed) 
    await msg.add_reaction("✅")
    


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
    await on_message_delete()
    


@client.command()
@commands.has_permissions(kick_members=True)
async def poll(ctx,*,question):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(description =f"```The poll: \n{question}```\n✅ = Yes\n❎ = No")
    message = await ctx.send(embed = embed)
    await message.add_reaction('✅')
    await message.add_reaction('❎')



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


@client.command(aliases=['d'])
async def dare(ctx):
	dare_list = []
	embed = discord.Embed(description=f"{random.choice(dare_list)}")
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
