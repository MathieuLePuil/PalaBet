import discord
from discord.ext import commands
from discord_slash import SlashCommand, ButtonStyle
from discord_slash.utils.manage_components import *
from discord_components import *
import json


bot = commands.Bot(command_prefix=">", description="Bot de pari sportif pour le ScaryShop", intents=discord.Intents.all())
bot.remove_command("help")
slash = SlashCommand(bot, sync_commands=True)



@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing,
                                                                                      name="Jouer comporte des risques : endettement, isolement, dépendance. Pour être aidé, appelez le 09-74-75-13-13 (appel non surtaxé) "))
    print("PalaBet est PRET!")
    DiscordComponents(bot)


async def get_pari_data():
    with open("pari.json", "r") as f:
        info_pari = json.load(f)

    return info_pari


async def when_pari(message):
    info_pari = await get_pari_data()

    if str(message.id) in info_pari:
        return False
    else:

        info_pari[str(message.id)] = {}
        info_pari[str(message.id)]["player_1"] = ""
        info_pari[str(message.id)]["cote_1"] = 0
        info_pari[str(message.id)]["player_2"] = ""
        info_pari[str(message.id)]["cote_2"] = 0
        info_pari[str(message.id)]["cote_nul"] = 0

    with open("pari.json", "w") as f:
        json.dump(info_pari, f, indent=2)
    return True


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


@bot.event
async def on_button_click(interactions: Interaction):
    if interactions.custom_id == "start_match":

        foot_channel = bot.get_channel(1011251793067511860)
        tennis_channel = bot.get_channel(1012680502110601217)

        await interactions.respond(type=7)

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

        await interactions.channel.send(embed=em1)

        try:
            sport = await bot.wait_for("message", timeout=10)
        except:
            await interactions.channel.purge(limit=2, check=lambda msg: not msg.pinned)
            await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
            return

        if sport.content == "foot":
            await interactions.channel.send(embed=em2_foot)

            try:
                equipe_1 = await bot.wait_for("message", timeout=10)
            except:
                await interactions.channel.purge(limit=2, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            await interactions.channel.send(embed=em3_foot)

            try:
                equipe_2 = await bot.wait_for("message", timeout=10)
            except:
                await interactions.channel.purge(limit=2, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            await interactions.channel.send(embed=em4_foot)

            try:
                cote_1 = await bot.wait_for("message", timeout=10)
            except:
                await interactions.channel.purge(limit=2, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            await interactions.channel.send(embed=em5_foot)

            try:
                cote_2 = await bot.wait_for("message", timeout=10)
            except:
                await interactions.channel.purge(limit=2, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            await interactions.channel.send(embed=em_nul)

            try:
                cote_nul = await bot.wait_for("message", timeout=10)
            except:
                await interactions.channel.purge(limit=2, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

        elif sport.content == "tennis":
            await interactions.channel.send(embed=em2_tennis)

            try:
                equipe_1 = await bot.wait_for("message", timeout=10)
            except:
                await interactions.channel.purge(limit=2, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            await interactions.channel.send(embed=em3_tennis)

            try:
                equipe_2 = await bot.wait_for("message", timeout=10)
            except:
                await interactions.channel.purge(limit=2, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            await interactions.channel.send(embed=em4_tennis)

            try:
                cote_1 = await bot.wait_for("message", timeout=10)
            except:
                await interactions.channel.purge(limit=2, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            await interactions.channel.send(embed=em5_tennis)

            try:
                cote_2 = await bot.wait_for("message", timeout=10)
            except:
                await interactions.channel.purge(limit=2, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            cote_nul = "null"
            cote_nul_int = 0

        em_final_foot = discord.Embed(title=f"**⚽ {equipe_1.content}** VS **{equipe_2.content}**",
                                      description="> Pour parier, cliquez sur le bouton correspond à l'équipe sur laquelle vous souhaitez miser.",
                                      color=0xFF0000)
        em_final_foot.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/1012429275649015819/1012436579366740028/LOGO.png")
        em_final_foot.set_footer(text="PalaBet - Made by MathieuLP (Dr3Xt3r)",
                                 icon_url="https://cdn.discordapp.com/attachments/1012429275649015819/1012436579366740028/LOGO.png")

        em_final_tennis = discord.Embed(title=f"🎾 **{equipe_1.content}** VS **{equipe_2.content}**",
                                        description="> Pour parier, cliquez sur le bouton correspond à l'équipe sur laquelle vous souhaitez miser. \n \n En cas d'abandon, vous serez remboursé.",
                                        color=0xFF0000)
        em_final_tennis.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/1012429275649015819/1012436579366740028/LOGO.png")
        em_final_tennis.set_footer(text="PalaBet - Made by MathieuLP (Dr3Xt3r)",
                                   icon_url="https://cdn.discordapp.com/attachments/1012429275649015819/1012436579366740028/LOGO.png")

        em_valid = discord.Embed(description="Le match a bien été lancé. À vos paris !",
                                 color=0xFF0000)

        digits = "0123456789."
        cote_1_int = ""
        cote_2_int = ""
        cote_nul_int = ""

        for i in cote_1.content:
            if i in digits:
                cote_1_int += i

        cote_1_int = float(cote_1_int)

        for i in cote_2.content:
            if i in digits:
                cote_2_int += i

        cote_2_int = float(cote_2_int)

        if cote_nul == "null":
            message = await tennis_channel.send(embed=em_final_tennis, components=[[
                Button(style=ButtonStyle.green, label=f"{equipe_1.content} - {cote_1.content}", custom_id="pari_1"),
                Button(style=ButtonStyle.grey, label=f"Match Nul", custom_id="pari_nul", disabled=True),
                Button(style=ButtonStyle.red, label=f"{equipe_2.content} - {cote_2.content}", custom_id="pari_2")]])
            await interactions.channel.purge(limit=10, check=lambda msg: not msg.pinned)
            await interactions.channel.send(embed=em_valid, delete_after=5)

        else:

            for i in cote_nul.content:
                if i in digits:
                    cote_nul_int += i

            cote_nul_int = float(cote_nul_int)

            message = await tennis_channel.send(embed=em_final_tennis, components=[[
                Button(style=ButtonStyle.green, label=f"{equipe_1.content} - {cote_1.content}", custom_id="pari_1"),
                Button(style=ButtonStyle.grey, label=f"Match Nul - {cote_nul.content}", custom_id="pari_nul"),
                Button(style=ButtonStyle.red, label=f"{equipe_2.content} - {cote_2.content}", custom_id="pari_2")]])
            await interactions.channel.purge(limit=12, check=lambda msg: not msg.pinned)
            await interactions.channel.send(embed=em_valid, delete_after=5)

        await when_pari(message)
        pari_info = await get_pari_data()


        try:
            pari_info[str(message.id)]["cote_1"] = cote_1_int
            pari_info[str(message.id)]["player_1"] = equipe_1.content
            pari_info[str(message.id)]["cote_2"] = cote_2_int
            pari_info[str(message.id)]["player_2"] = equipe_1.content
            pari_info[str(message.id)]["cote_nul"] = cote_nul_int
        except KeyError:
            print(f"Il y a une erreur!")

        with open("pari.json", "w") as f:
            json.dump(pari_info, f, indent=2)


bot.run("MTAxMTIzNTYzOTU2MTMwMjEwMA.GeVrrj.b27o1rBftj_DdOyfFEUoor6qCDnQACLwMp1Rog")