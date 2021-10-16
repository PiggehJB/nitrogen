import discord
from discord.ext import commands
from colorama import Fore
import time
import sys
import string
import random
autoreset=True
token = input(f"{Fore.CYAN}Enter your token: ")
prefix = input(f"{Fore.YELLOW}Enter your prefix: ")


bot = commands.Bot(command_prefix=prefix, self_bot=True)

@bot.event
async def on_ready():
    print(f"{Fore.GREEN}Starting")

@bot.command(help="<prefix>nitrogen [amount of times]\nPlease note this is completely random, not 100% guranteed results")
async def nitrogen(ctx, amount):
    try:
        for i in range(int(amount)):
            rand_code = "".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k = 16))
            await ctx.send(f"https://discord.gift/{rand_code}")
    except Exception as e:
        await ctx.send("Error! Make sure `amount` is entered correctly (number)")
        print(e)
try:
    bot.run(token, bot=False)
except:
    print(f"{Fore.RED}Uh oh! There's an error.. Make sure your token was entered correctly")
    time.sleep(4)
    sys.exit(f"Terminating program, please rerun with proper token {Fore.MAGENTA}NO QUOTATIONS IN TOKEN!")
