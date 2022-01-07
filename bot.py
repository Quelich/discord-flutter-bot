import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from scrape_data import *

load_dotenv()

# GET TOKEN FROM .ENV FILE
TOKEN = os.getenv('DISCORD_TOKEN')
# GET GUILD FROM .ENV FILE
GUILD = os.getenv('DISCORD_GUILD')


bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    # A bot user can be connected to many guilds.
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print("{} has connected to Discord\nGuild: name:{}(id:{})".format(
        bot.user, guild.name, guild.id))
    members = '\n - '.join([member.name for member in guild.members])
    print("Guild Members:\n - {}".format(members))


@bot.command(name='flutter', help='Display the latest version of Flutter and Dart SDKs')
async def call_version(ctx):
    f_program = FlutterVersion()
    f_result = f_program.get_response()
    d_program = DartVersion()
    d_result = d_program.get_response()
    msg = f_result + "\n" + d_result
    await ctx.send(msg)


bot.run(TOKEN)
