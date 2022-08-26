import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_components import *


bot = commands.Bot(command_prefix=">", description="Bot de pari sportif pour le ScaryShop", intents=discord.Intents.all())
bot.remove_command("help")
slash = SlashCommand(bot, sync_commands=True)


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing,
                                                                                      name="Jouer comporte des risques : endettement, isolement, dépendance. Pour être aidé, appelez le 09-74-75-13-13 (appel non surtaxé) "))
    print("PalaBet est PRET!")


@slash.slash(name="set_match", guild_ids=[733712051280543785], description="Lance les paris pour un match")
async def set_match(ctx):
    em1 = discord.Embed(description="Quel est le sport du match ? (foot ou tennis)",
                        color=0xFFA500)
    em2_foot = discord.Embed(description="Quelle est l'équipe n°1 ?",
                             color=0xFFA500)
    em2_tennis = discord.Embed(description="Qui est le joueur n°1 ?",
                               color=0xFFA500)
    em3_foot = discord.Embed(description="Quelle est l'équipe n°2 ?",
                             color=0xFFA500)
    em3_tennis = discord.Embed(description="Qui est le joueur n°2 ?",
                               color=0xFFA500)
    em4_foot = discord.Embed(description="Quelle est la côte pour l'équipe n°1 ?",
                             color=0xFFA500)
    em4_tennis = discord.Embed(description="Quelle est la côte pour le joueur n°1 ?",
                               color=0xFFA500)
    em5_foot = discord.Embed(description="Quelle est la côte pour l'équipe n°2 ?",
                             color=0xFFA500)
    em5_tennis = discord.Embed(description="Quelle est la côte pour le joueur n°2 ?",
                               color=0xFFA500)
    em_nulle = discord.Embed(description="Quelle est la côte pour match nul ?",
                             color=0xFFA500)

    await ctx.channel.send(embed=em1)

    try:
        sport = await bot.wait_for("message", timeout=10)
    except:
        await ctx.channel.purge(limit=2, check=lambda msg: not msg.pinned)
        await ctx.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
        return

    if sport.content == "foot":
        print("foot")
    elif sport.content == "tennis":
        print("tennis")


bot.run("MTAxMTIzNTYzOTU2MTMwMjEwMA.GeVrrj.b27o1rBftj_DdOyfFEUoor6qCDnQACLwMp1Rog")