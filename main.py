import discord
from discord.ext import commands
from discord_slash import SlashCommand, ButtonStyle
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

'''
@slash.slash(name="set_match", guild_ids=[733712051280543785], description="Lance les paris pour un match")
async def set_match(ctx):

    foot_channel = bot.get_channel(1011251793067511860)
    tennis_channel = bot.get_channel(1012680502110601217)

    em1 = discord.Embed(description="Quel est le sport du match ? (foot ou tennis)",
                        color=0xFF0000)
    em2_foot = discord.Embed(description="Quelle est l'équipe n°1 ?",
                             color=0xFF0000)
    em2_tennis = discord.Embed(description="Qui est le joueur n°1 ?",
                               color=0xFF0000)
    em3_foot = discord.Embed(description="Quelle est l'équipe n°2 ?",
                             color=0xFF0000)
    em3_tennis = discord.Embed(description="Qui est le joueur n°2 ?",
                               color=0xFF0000)
    em4_foot = discord.Embed(description="Quelle est la côte pour l'équipe n°1 ?",
                             color=0xFF0000)
    em4_tennis = discord.Embed(description="Quelle est la côte pour le joueur n°1 ?",
                               color=0xFF0000)
    em5_foot = discord.Embed(description="Quelle est la côte pour l'équipe n°2 ?",
                             color=0xFF0000)
    em5_tennis = discord.Embed(description="Quelle est la côte pour le joueur n°2 ?",
                               color=0xFF0000)
    em_nul = discord.Embed(description="Quelle est la côte pour match nul ?",
                             color=0xFF0000)

    await ctx.send(embed=em1)

    try:
        sport = await bot.wait_for("message", timeout=10)
    except:
        await ctx.channel.purge(limit=2, check=lambda msg: not msg.pinned)
        await ctx.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
        return

    if sport.content == "foot":
        await ctx.channel.send(embed=em2_foot)

        try:
            equipe_1 = await bot.wait_for("message", timeout=10)
        except:
            await ctx.channel.purge(limit=2, check=lambda msg: not msg.pinned)
            await ctx.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
            return

        await ctx.channel.send(embed=em3_foot)

        try:
            equipe_2 = await bot.wait_for("message", timeout=10)
        except:
            await ctx.channel.purge(limit=2, check=lambda msg: not msg.pinned)
            await ctx.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
            return

        await ctx.channel.send(embed=em4_foot)

        try:
            cote_1 = await bot.wait_for("message", timeout=10)
        except:
            await ctx.channel.purge(limit=2, check=lambda msg: not msg.pinned)
            await ctx.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
            return

        await ctx.channel.send(embed=em5_foot)

        try:
            cote_2 = await bot.wait_for("message", timeout=10)
        except:
            await ctx.channel.purge(limit=2, check=lambda msg: not msg.pinned)
            await ctx.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
            return

        await ctx.channel.send(embed=em_nul)

        try:
            cote_nul = await bot.wait_for("message", timeout=10)
        except:
            await ctx.channel.purge(limit=2, check=lambda msg: not msg.pinned)
            await ctx.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
            return


    elif sport.content == "tennis":
        await ctx.channel.send(embed=em2_tennis)

        try:
            equipe_1 = await bot.wait_for("message", timeout=10)
        except:
            await ctx.channel.purge(limit=2, check=lambda msg: not msg.pinned)
            await ctx.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
            return

        await ctx.channel.send(embed=em3_tennis)

        try:
            equipe_2 = await bot.wait_for("message", timeout=10)
        except:
            await ctx.channel.purge(limit=2, check=lambda msg: not msg.pinned)
            await ctx.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
            return

        await ctx.channel.send(embed=em4_tennis)

        try:
            cote_1 = await bot.wait_for("message", timeout=10)
        except:
            await ctx.channel.purge(limit=2, check=lambda msg: not msg.pinned)
            await ctx.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
            return

        await ctx.channel.send(embed=em5_tennis)

        try:
            cote_2 = await bot.wait_for("message", timeout=10)
        except:
            await ctx.channel.purge(limit=2, check=lambda msg: not msg.pinned)
            await ctx.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
            return

        cote_nul = "null"

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

    print(cote_1_int)

    cote_1_int = float(cote_1_int)

    for i in cote_2.content:
        if i in digits:
            cote_2_int += i

    print(cote_2_int)

    cote_2_int = float(cote_2_int)

    if cote_nul == "null":
        buttons = [
            create_button(
                style=ButtonStyle.green,
                label=f"{equipe_1.content} - {cote_1.content}",
                custom_id="pari_1"
            ),
            create_button(
                style=ButtonStyle.grey,
                label=f"Match Nul",
                custom_id="pari_nul",
                disabled=True
            ),
            create_button(
                style=ButtonStyle.red,
                label=f"{equipe_2.content} - {cote_2.content}",
                custom_id="pari_2"
            )
        ]
        action_row = create_actionrow(*buttons)
        message = await tennis_channel.send(embed=em_final_tennis, components=[action_row])
        await ctx.channel.purge(limit=10, check=lambda msg: not msg.pinned)
        await ctx.send(embed=em_valid)

    else:
        buttons = [
            create_button(
                style=ButtonStyle.green,
                label=f"{equipe_1.content} - {cote_1.content}",
                custom_id="pari_1"
            ),
            create_button(
                style=ButtonStyle.grey,
                label=f"Match Nul - {cote_nul.content}",
                custom_id="pari_nul"
            ),
            create_button(
                style=ButtonStyle.red,
                label=f"{equipe_2.content} - {cote_2.content}",
                custom_id="pari_2"
            )
        ]
        action_row = create_actionrow(*buttons)
        message = await foot_channel.send(embed=em_final_foot, components=[action_row])
        await ctx.channel.purge(limit=12, check=lambda msg: not msg.pinned)
        await ctx.send(embed=em_valid)

    button_ctx = await wait_for_component(bot, components=action_row)
    if button_ctx.custom_id == "pari_1":
        await button_ctx.channel.send(f"{cote_1_int + 1}")
    if button_ctx.custom_id == "pari_2":
        await button_ctx.channel.send(f"{cote_2_int + 1}")
'''

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





bot.run("MTAxMTIzNTYzOTU2MTMwMjEwMA.GeVrrj.b27o1rBftj_DdOyfFEUoor6qCDnQACLwMp1Rog")