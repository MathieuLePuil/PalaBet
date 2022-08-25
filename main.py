import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_components import *
from discord_components import *


bot = commands.Bot(command_prefix=">", description="Bot de pari sportif pour le ScaryShop", intents=discord.Intents.all())
bot.remove_command("help")
slash = SlashCommand(bot, sync_commands=True)


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing,
                                                                                      name="Jouer comporte des risques : endettement, isolement, dépendance. Pour être aidé, appelez le 09-74-75-13-13 (appel non surtaxé) "))
    print("PalaBet est PRET!")
    DiscordComponents(bot)


@bot.command()
@commands.has_permissions(administrator=True)
async def set_match(ctx):
    embed = discord.Embed(title="**Lancer un match**",
                          description="Pour lancer le pari d'un match, veuillez cliquer sur le bouton sous ce message.",
                          color=0xFF0000)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/1012429275649015819/1012436579366740028/LOGO.png")
    embed.set_footer(text="PalaBet",
                     icon_url="https://cdn.discordapp.com/attachments/1012429275649015819/1012436579366740028/LOGO.png")

    await ctx.send(embed=embed,
                   components=[Button(style=ButtonStyle.green, label="⚽ Lancer un match", custom_id="start_match")])

    await ctx.message.delete()


bot.run("MTAxMTIzNTYzOTU2MTMwMjEwMA.GeVrrj.b27o1rBftj_DdOyfFEUoor6qCDnQACLwMp1Rog")