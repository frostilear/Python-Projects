import discord
import time
bot=discord.Client()
@bot.command()
async def ping(ctx):
    await ctx.send(f'My ping is {bot.latency}!')
bot.run("NjQ4NDU3NTM2ODkwMjA4Mjg3.XduhJA.OlEcESRQISB9dJLkDSh9uu6K_3k")