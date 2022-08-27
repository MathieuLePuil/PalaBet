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

async def get_user_data():
    with open("user_data.json", "r") as f:
        user_data = json.load(f)

    return user_data

async def get_mise_data():
    with open("mise.json", "r") as f:
        user_data = json.load(f)

    return user_data

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
        info_pari[str(message.id)]["msg_pari"] = 0

    with open("pari.json", "w") as f:
        json.dump(info_pari, f, indent=2)
    return True

async def first_pari(user):
    user_data = await get_user_data()

    if str(user.id) in user_data:
        return False
    else:

        user_data[str(user.id)] = {}
        user_data[str(user.id)]["nbr_pari"] = 0

    with open("user_data.json", "w") as f:
        json.dump(user_data, f, indent=2)
    return True

async def when_mise(user):
    user_data = await get_user_data()

    if str(user.id) in user_data:
        return False
    else:

        user_data[str(user.id)] = {}
        user_data[str(user.id)]["mise"] = 0
        user_data[str(user.id)]["gain_pot"] = 0
        user_data[str(user.id)]["vainqueur"] = ""
        user_data[str(user.id)]["looser"] = ""
        user_data[str(user.id)]["cote"] = 0

    with open("mise.json", "w") as f:
        json.dump(user_data, f, indent=2)
    return True

async def convert_int(string):
    string = string.replace('k', '000').replace('m', '000000').replace(' ', '').replace('$', '').replace('.', '').replace('a', '').replace('b', '').replace('c', '').replace('d', '').replace('e', '').replace('f', '').replace('g', '').replace('h', '').replace('i', '').replace('j', '').replace('l', '').replace('n', '').replace('o', '').replace('p', '').replace('q', '').replace('r', '').replace('s', '').replace('t', '').replace('u', '').replace('v', '').replace('w', '').replace('x', '').replace('y', '').replace('z', '').replace('A', '').replace('B', '').replace('C', '').replace('D', '').replace('E', '').replace('F', '').replace('G', '').replace('H', '').replace('I', '').replace('J', '').replace('K', '000').replace('L', '').replace('M', '000000').replace('N', '').replace('O', '').replace('P', '').replace('Q', '').replace('R', '').replace('S', '').replace('T', '').replace('U', '').replace('V', '').replace('W', '').replace('X', '').replace('Y', '').replace('Z', '')
    string = int(string)
    return string


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
        em_nul = discord.Embed(description="Quelle est la côte pour match nul ?",
                            color=0xFFA500)

        await interactions.channel.send(embed=em1)

        try:
            sport = await bot.wait_for("message", timeout=30)
        except:
            await interactions.channel.purge(limit=1, check=lambda msg: not msg.pinned)
            await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
            return

        if sport.content == "foot":
            await interactions.channel.send(embed=em2_foot)

            try:
                equipe_1 = await bot.wait_for("message", timeout=30)
            except:
                await interactions.channel.purge(limit=3, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            await interactions.channel.send(embed=em3_foot)

            try:
                equipe_2 = await bot.wait_for("message", timeout=30)
            except:
                await interactions.channel.purge(limit=5, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            await interactions.channel.send(embed=em4_foot)

            try:
                cote_1 = await bot.wait_for("message", timeout=30)
            except:
                await interactions.channel.purge(limit=7, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            await interactions.channel.send(embed=em5_foot)

            try:
                cote_2 = await bot.wait_for("message", timeout=30)
            except:
                await interactions.channel.purge(limit=9, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            await interactions.channel.send(embed=em_nul)

            try:
                cote_nul = await bot.wait_for("message", timeout=30)
            except:
                await interactions.channel.purge(limit=11, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

        elif sport.content == "tennis":
            await interactions.channel.send(embed=em2_tennis)

            try:
                equipe_1 = await bot.wait_for("message", timeout=30)
            except:
                await interactions.channel.purge(limit=2, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            await interactions.channel.send(embed=em3_tennis)

            try:
                equipe_2 = await bot.wait_for("message", timeout=30)
            except:
                await interactions.channel.purge(limit=2, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            await interactions.channel.send(embed=em4_tennis)

            try:
                cote_1 = await bot.wait_for("message", timeout=30)
            except:
                await interactions.channel.purge(limit=2, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            await interactions.channel.send(embed=em5_tennis)

            try:
                cote_2 = await bot.wait_for("message", timeout=30)
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
            pari_info[str(message.id)]["player_2"] = equipe_2.content
            pari_info[str(message.id)]["cote_nul"] = cote_nul_int
            pari_info[str(message.id)]["msg_pari"] = message.id
        except KeyError:
            print(f"Il y a une erreur!")

        with open("pari.json", "w") as f:
            json.dump(pari_info, f, indent=2)

    if interactions.custom_id == "pari_1":

        await interactions.respond(type=7)

        await when_pari(message=interactions.message)
        await when_mise(interactions.user)
        pari_info = await get_pari_data()
        mise_info = await get_mise_data()

        cote_1 = pari_info[str(interactions.message.id)]["cote_1"]
        equipe_1 = pari_info[str(interactions.message.id)]["player_1"]
        equipe_2 = pari_info[str(interactions.message.id)]["player_2"]

        guild = bot.get_guild(733712051280543785)
        catego = bot.get_channel(1011236492443660309)

        author = interactions.author
        channel = interactions.channel

        ticket_channel = await guild.create_text_channel(f"🎾〡{author.name}-", category=catego)

        em_mise = discord.Embed(
            description="Quelle mise souhaité vous mettre ? **(UNIQUEMENT chiffre, SANS le $, SANS espace et la réduction)**", color=0xFF0000)

        await ticket_channel.send(embed=em_mise)

        try:
            mise = await bot.wait_for("message", timeout=300)
        except:
            await ticket_channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
            await ticket_channel.delete()
            return

        mise = await convert_int(mise.content)

        em_paiement = discord.Embed(title=f"🎾 **{equipe_1}** VS **{equipe_2}**",
                                        description=f"> Victoire : `{equipe_1}` \n > Côte : `{cote_1}` \n > Mise : `{mise}$` \n > Gain potentiel : `{mise * cote_1}$` \n \n Nous rappelons qu'en cas d'abandon, vous serez remboursé. \n \n __Screen de paiement de `{mise}$` au compte `ScaryShop` avec visible :__ \n > • Pseudo en haut à gauche \n > • Date et heure en bas à droite \n > • Paiement dans le chat \n \n <a:w_:786969896721448960> *Si le screen ne comporte pas ces informations, il sera refusé !*",
                                        color=0xFF0000)
        em_paiement.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/1012429275649015819/1012436579366740028/LOGO.png")
        em_paiement.set_footer(text="PalaBet - Made by MathieuLP (Dr3Xt3r)",
                                   icon_url="https://cdn.discordapp.com/attachments/1012429275649015819/1012436579366740028/LOGO.png")

        await interactions.channel.purge(limit=2)

        await ticket_channel.send(embed=em_paiement, components=[[
                Button(style=ButtonStyle.green, label=f"Validé !", custom_id="valide1"),
                Button(style=ButtonStyle.red, label=f"Refusé", custom_id="refuse1")]])

        try:
            mise_info[str(interactions.user.id)]["mise"] = mise
            mise_info[str(interactions.user.id)]["gain_pot"] = mise * cote_1
            mise_info[str(interactions.user.id)]["vainqueur"] = equipe_1
            mise_info[str(interactions.user.id)]["looser"] = equipe_2
            mise_info[str(interactions.user.id)]["cote"] = cote_1
        except KeyError:
            print(f"Il y a une erreur!")

        with open("mise.json", "w") as f:
            json.dump(mise_info, f, indent=2)

    if interactions.custom_id == "valide1":

        await interactions.respond(type=7)

        croupier = interactions.guild.get_role(1013095281417531517)

        if croupier in author.roles:

            await first_pari(user=interactions.user)
            pari_info = await get_pari_data()
            user_data = await get_user_data()
            user_mise = await get_mise_data()

            nbr_pari = user_data[str(interactions.user.id)]["nbr_pari"] + 1

            #ID channel dans base de donnée

            cote_1 = user_mise[str(interactions.user.id)]["cote"]
            equipe_2 = user_mise[str(interactions.user.id)]["looser"]

            mise = user_mise[str(interactions.user.id)]["mise"]
            vainqueur = user_mise[str(interactions.user.id)]["vainqueur"]

            em_paiement = discord.Embed(title=f"🎾 **{vainqueur}** VS **{equipe_2}**",
                                        description=f"> Victoire : `{vainqueur}` \n > Côte : `{cote_1}` \n > Mise : `{mise}$` \n > Gain potentiel : `{mise * cote_1}$` \n \n Nous rappelons qu'en cas d'abandon, vous serez remboursé. \n \n > ✅ Paiement validé !",
                                        color=0xFF0000)
            em_paiement.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/1012429275649015819/1012436579366740028/LOGO.png")
            em_paiement.set_footer(text="PalaBet - Made by MathieuLP (Dr3Xt3r)",
                                   icon_url="https://cdn.discordapp.com/attachments/1012429275649015819/1012436579366740028/LOGO.png")

            await interactions.message.edit(embed=em_paiement, components=None)

            match = f"**{vainqueur}** VS **{equipe_2}**"

            try:
                user_data[str(interactions.user.id)][f"match_{nbr_pari}"] = match
                user_data[str(interactions.user.id)][f"winner_{nbr_pari}"] = vainqueur
                user_data[str(interactions.user.id)][f"looser_{nbr_pari}"] = equipe_2
                user_data[str(interactions.user.id)][f"cote_{nbr_pari}"] = cote_1
                user_data[str(interactions.user.id)][f"mise_{nbr_pari}"] = mise
                user_data[str(interactions.user.id)]["nbr_pari"] = nbr_pari
            except KeyError:
                print(f"Il y a une erreur!")

            with open("user_data.json", "w") as f:
                json.dump(user_data, f, indent=2)

        else:
            em_perm = discord.Embed(description="Vous n'avez pas la permission d'appuyer sur ce bouton !", color=0xFFA500)



bot.run("MTAxMTIzNTYzOTU2MTMwMjEwMA.GeVrrj.b27o1rBftj_DdOyfFEUoor6qCDnQACLwMp1Rog")