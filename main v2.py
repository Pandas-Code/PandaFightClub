from asyncio import exceptions
import discord
from discord import client
from dataclasses import dataclass
import io
import json
import os
import random
from discord import message
from discord.ext import commands
from discord.utils import _unique
from discord_components import *
import asyncio

class Character:
    name = "Name"
    level = 1
    race = "normal"
    User = "None"
    Inv = []
    Helmet = ""
    Chestplate = ""
    Boots = ""
    Accessory = ""
    Shield = ""
    Weapon = ""
Char1 = Character()

def int_to_roman(num):
    val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
    syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

items={
    "unique" : ["Sharp Bamboo","Stick","Stone","Leather Tunic","Normal Ring","Leather Boots","Ordinary Hat","Defensive Stick"],
    "rare" : ["Wooden Spear","Rusty Axe","Bow and Arrow","Broken Chestplate","Golden Earrings","Boots of the Rambler","Rusty Helmet","Wooden Shield"],
    "epic" : ["Steal Sword","Battleaxe","Crossbow","Roman Chestplate","Emerald Bracelet","Tiger Claws","Legionaire Helmet","Viking Shield"],
    "legendary" : ["Blade of the Pigs","Axe of Peace","The Magicians Wand","Holy Protector","The Necklace of the Ocean","Steps of the Ancestors","The Masters Helmet","Shield of the Golem"],
    "mythic" : ["Eden's Spear","Thor's Hammer","Poseidon's Trident","Obsidian Chestplate","Rind of the Widdow","Giant's Step","Crown of Anarchie","Ragnar's Skjöldur"]
}

def exp(n):
    n=int((n-int(n))*10)
    out=""
    if n!=0:
        for i in range(n):
            out+="⬜"
    for i in range(10-n):
        out+="⬛"
    
    return out

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Beep Boop")
    DiscordComponents(client)
    welcome_channel=client.get_channel(880537990181552198)
    print(str(welcome_channel))
    message=await welcome_channel.send("React with ur pronouns, or dont idc, if ur pronouns are on there, ping an admin, theyll love you and tell them they suck and ur pronouns, he/him💙, she/her💜, they/them💛")
    await message.add_reaction("💛")
    await message.add_reaction("💜")
    await message.add_reaction("💙")
@client.event
async def on_reaction_add(reaction, user):
    he=discord.utils.get(user.guild.roles, name="He/Him")
    she=discord.utils.get(user.guild.roles, name="She/Her")
    they=discord.utils.get(user.guild.roles, name="They/Them")
    print("He")
    if str(reaction.emoji)=="💙":
        await user.add_roles(he)
    if str(reaction.emoji)=="💜":
        await user.add_roles(she)
    if str(reaction.emoji)=="💛":
        await user.add_roles(they)


@client.command()
async def moin(ctx):
    await ctx.send("Moinsen")

@client.command()
async def register(ctx, name, race):
    await ctx.send("Ur "+name+" "+race+" Pandabear has been succesfully created and saved!")
    Char1.name=name
    Char1.race=race
    Char1.level=1
    Char1.User=str(ctx.author.id)
    Char1.Inv=[]
    Char1.Helmet="Standard Hat"
    Char1.Chestplate="Standard Chestplate"
    Char1.Boots="Standard Boots"
    Char1.Accessory="Standard Ring"
    Char1.Shield="Standard Shield"
    Char1.Weapon="Standard Stick"
    Jason=json.dumps(Char1.__dict__)
    print(Jason)
    with io.open(os.path.join("D:\\Hacking\\python\\PandaFightClub\\", str(ctx.author.id) + '.json'), 'w') as db_file:
        db_file.write(json.dumps(Char1.__dict__))

@client.command()
async def start(ctx):
    await ctx.send("""U can use the following commands to interact with me:
                        !create will let you create your first Fighter!
                        !levelup is for debugging purposes only
                        !info will tell you the stats of your Panda
                        !get will give you something
                        !inv will give you the information about your Inventory
                        !crate will open a crate giving you a random Item
                        !inv will show ur Inventory
                        !equip will equip a item if its in ur Inventory
                        !equipment will show the gear ur currently fighting with
                        !details will tell u everything about an item
                        
                                            """)
@client.command()
async def create(ctx):
    await ctx.send(
                    """To Create your own, personal fight Panda:
                    answer with a message starting with !register, then name[No Spaces, max of 32 characters], then seperated by a space his Race[Brown, normal, red, old]
                    and you shall recieve a Panda for you!
                    """)
@client.command()
async def levelup(ctx, lvl):
    lvl=float(lvl)
    with open("D:\\Hacking\\python\\PandaFightClub\\" + str(ctx.author.id)+".json") as f: 
        data = json.load(f)
    Char1.name=data["name"]
    Char1.level = data["level"]
    Char1.race = data["race"]
    Char1.User = data["User"]
    Char1.Inv = data["Inv"]
    Char1.Weapon = data["Weapon"]
    Char1.Accessory = data["Accessory"]
    Char1.Boots = data["Boots"]
    Char1.Chestplate = data["Chestplate"]
    Char1.Helmet = data["Helmet"]
    Char1.Shield = data["Shield"]
    print(Char1.level)
    Char1.level=Char1.level+lvl
    with io.open(os.path.join("D:\\Hacking\\python\\PandaFightClub\\", data["User"] + '.json'), 'w') as db_file:
        db_file.write(json.dumps(Char1.__dict__))
@client.command()
async def info(ctx):
    with open("D:\\Hacking\\python\\PandaFightClub\\" + str(ctx.author.id)+".json") as f: 
        data = json.load(f)
    await ctx.send(str(ctx.author)[:len(data["User"])-8]+"'s "+data["name"])
    await ctx.send("Level: "+int_to_roman(int(data["level"]))+"  "+exp(data["level"])+" "+int_to_roman(int(data["level"])+1))
@client.command()
async def get(ctx, *, thing):
    with open("D:\\Hacking\\python\\PandaFightClub\\" + str(ctx.author.id)+".json") as f: 
        data = json.load(f)
    print(type(data))
    print(data)
    Char1.name=data["name"]
    Char1.level = data["level"]
    Char1.race = data["race"]
    Char1.User = data["User"]
    Char1.Inv = data["Inv"]
    Char1.Weapon = data["Weapon"]
    Char1.Accessory = data["Accessory"]
    Char1.Boots = data["Boots"]
    Char1.Chestplate = data["Chestplate"]
    Char1.Helmet = data["Helmet"]
    Char1.Shield = data["Shield"]
    Char1.Inv.append(thing)
    print(Char1.Inv[:])
    with io.open(os.path.join("D:\\Hacking\\python\\PandaFightClub\\", data["User"] + '.json'), 'w') as db_file:
        db_file.write(json.dumps(Char1.__dict__))
@client.command()
async def inv(ctx):
    with open("D:\\Hacking\\python\\PandaFightClub\\" + str(ctx.author.id)+".json") as f: 
        data = json.load(f)
    data["Inv"]=list(filter(None, data["Inv"]))
    print(data["Inv"])
    if data["Inv"]==[]:
        await ctx.send("Your backpack is empty")
    else:
        await ctx.send("Whats in ur backback? "+", ".join(data["Inv"]))
@client.command()
async def crate(ctx):
    get=""
    rnd=random.randint(1,100)
    if rnd<=30:
        get=items["unique"][random.randint(0,7)]
    elif rnd<=55:
        get=items["rare"][random.randint(0,7)]
    elif rnd<=100:
        get=items["epic"][random.randint(0,7)]
    elif rnd<=90:
        get=items["legendary"][random.randint(0,7)]
    else:
        get=items["mythic"][random.randint(0,7)]
    with open("D:\\Hacking\\python\\PandaFightClub\\" + str(ctx.author.id)+".json") as f: 
        data = json.load(f)
    Char1.name=data["name"]
    Char1.level = data["level"]
    Char1.race = data["race"]
    Char1.User = data["User"]
    Char1.Inv = data["Inv"]
    Char1.Weapon = data["Weapon"]
    Char1.Accessory = data["Accessory"]
    Char1.Boots = data["Boots"]
    Char1.Chestplate = data["Chestplate"]
    Char1.Helmet = data["Helmet"]
    Char1.Shield = data["Shield"]
    Char1.Inv.append(get)
    print(data["Inv"])
    with io.open(os.path.join("D:\\Hacking\\python\\PandaFightClub\\", str(ctx.author.id) + '.json'), 'w') as db_file:
        db_file.write(json.dumps(Char1.__dict__))
    print("New Crate:")
    await ctx.send("Wow! you got:"+get)
    with open("D:\\Hacking\\python\\PandaFightClub\\" + get+".json") as f: 
        data = json.load(f)
    print(str(data))
    await ctx.send("Its a "+str(data["rarity"])+" "+str(data["Type"])+" You need to be a minimum of "+str(data["level"])+" it will Increase ur Damage by "+str(data["Damage"])+" Ur Health will get a Bonus of "+str(data["Health"])+" and ur Range will be boosted by " +str(data["Range"]))
@client.command()
async def details(ctx, *, item):
    with open("D:\\Hacking\\python\\PandaFightClub\\" + item+".json") as f: 
        data = json.load(f)
    await ctx.channel.send("Its a "+str(data["rarity"])+" "+str(data["Type"])+" You need to be a minimum of "+str(data["level"])+" it will Increase ur Damage by "+str(data["Damage"])+" Ur Health will get a Bonus of "+str(data["Health"])+" and ur Range will be boosted by " +str(data["Range"]))
@client.command()
async def equipment(ctx):
    with open("D:\\Hacking\\python\\PandaFightClub\\" + str(ctx.author.id)+".json") as f: 
        data = json.load(f)
    tosend=str("You are fighting with: "+data["Weapon"]+" While defending urself with "+data["Shield"]+" And U are wearing "+data["Chestplate"]+", "+data["Boots"]+" and " +data["Helmet"]+" and a " +data["Accessory"]+" for the style!")
    await ctx.channel.send(tosend)
    end={
    "Damage": 1,
    "Health": 10,
    "Range": 1
    }
    liste=[data["Weapon"],data["Accessory"],data["Boots"],data["Chestplate"],data["Helmet"],data["Shield"]]
    for i in liste :
        with open("D:\\Hacking\\python\\PandaFightClub\\" + str(i)+".json") as f: 
            item = json.load(f)
            end["Damage"]+=item["Damage"]
            end["Health"]+=item["Health"]
            end["Range"]+=item["Range"]
            print(str(end))
    await ctx.channel.send(str("With this setup u can deal "+str(end["Damage"]) + " Damage, got a total of "+str(end["Health"])+" Health and a Range of " +str(end["Range"])))
@client.command()
async def equip(ctx, *, item):
    print(item)
    with open("D:\\Hacking\\python\\PandaFightClub\\" + str(ctx.author.id)+".json") as f: 
        data = json.load(f)
    print(data)
    Char1.level = data["level"]
    Char1.race = data["race"]
    Char1.User = data["User"]
    Char1.Inv = data["Inv"]
    Char1.Weapon = data["Weapon"]
    Char1.Accessory = data["Accessory"]
    Char1.Boots = data["Boots"]
    Char1.Chestplate = data["Chestplate"]
    Char1.Helmet = data["Helmet"]
    Char1.Shield = data["Shield"]
    Char1.name=data["name"]
    with open("D:\\Hacking\\python\\PandaFightClub\\" + item+".json") as f: 
        item_data = json.load(f)
    item_type=item_data["Type"]
    if item in data["Inv"] and int(item_data["level"])<=data["level"]:
        if item_type=="Weapon":
            Char1.Inv.append(Char1.Weapon)
            Char1.Weapon=item
            Char1.Inv.remove(item)
        elif item_type=="Shield":
            print("SHIELD")
            Char1.Inv.append(Char1.Shield)
            Char1.Shield=item
            Char1.Inv.remove(item)
        elif item_type=="Helmet":
            Char1.Inv.append(Char1.Helmet)
            Char1.Helmet=item
            Char1.Inv.remove(item)
        elif item_type=="Boots":
            Char1.Inv.append(Char1.Boots)
            Char1.Boots=item
            Char1.Inv.remove(item)
        elif item_type=="Chestplate":
            Char1.Inv.append(Char1.Chestplate)
            Char1.Chestplate=item
            Char1.Inv.remove(item)
        elif item_type=="Accessory":
            Char1.Inv.append(Char1.Accessory)
            Char1.Accessory=item
            Char1.Inv.remove(item)
        
    with io.open(os.path.join("D:\\Hacking\\python\\PandaFightClub\\", str(ctx.author.id) + '.json'), 'w') as db_file:
        db_file.write(json.dumps(Char1.__dict__))
async def fight(arena, oponent, ctx, Panda1health, Panda1damage, Panda2health, Panda2damage):
    await arena.send(content="CHOOSE WISELY WHAT ATTACK YOU WILL CAST!", components=[[Button(style=ButtonStyle.green, label="Normal Hit"), Button(style=ButtonStyle.blue, label="Block"),Button(style=ButtonStyle.red, label="Charge ur hit")]])
    Panda1=str(oponent)
    Panda2=str(ctx.author)
    Panda1choice=""
    Panda2choice=""
    def check(res):
        return True
        ######################################
    try: 
        res=await client.wait_for("button_click", check=check, timeout=15)
        player=res.component.label
        user=str(res.user)
        print("user="+user)
        print("oponent="+str(oponent))
        print("CTX.author="+str(ctx.author))
        if Panda1choice!="" and user==str(oponent):
            await arena.send("Stop clicking Twice on buttons or you will get Banned by the Gods(Admins)")
            print("idiot")
        elif Panda2choice!="" and user==str(ctx.author):
            await arena.send("Stop clicking Twice on buttons or you will get Banned by the Gods(Admins)")
        else:
            print(user)
            if player=="Normal Hit":
                print(user+" Choose the Normal hit!")  
                if user==Panda1:
                    Panda1choice="Normal Hit"
                elif user==Panda2:
                    Panda2choice="Normal Hit"
            elif player=="Block":
                print(user+" Choose the Block!")  
                if user==Panda1:
                    Panda1choice="Block"
                elif user==Panda2:
                    Panda2choice="Block"
            elif player=="Charge ur hit":
                print(user+"Choose to Charge their hit")  
                if user==Panda1:
                    Panda1choice="Charge"
                elif user==Panda2:
                    Panda2choice="Charge"
            if Panda2choice!=""and Panda1choice!="":
                await arena.send("**"+Panda1+" chose to "+Panda1choice+" and "+Panda2+" choose to "+Panda2choice+"**")
            else:
                res=await client.wait_for("button_click", check=check, timeout=60)
                player=res.component.label
                user=str(res.user)
                if Panda1choice!="" and user==str(oponent):
                    await arena.send("Stop clicking Twice on buttons or you will get Banned by the Gods(Admins)")
                    print("idiot")
                elif Panda2choice!="" and user==str(ctx.author):
                    await arena.send("Stop clicking Twice on buttons or you will get Banned by the Gods(Admins)")
                else:
                    print(user)
                    if player=="Normal Hit":
                        print(user+" Choose the Normal hit!")  
                        if user==Panda1:
                            Panda1choice="Normal Hit"
                        elif user==Panda2:
                            Panda2choice="Normal Hit"
                    elif player=="Block":
                        print(user+" Choose the Block!")  
                        if user==Panda1:
                            Panda1choice="Block"
                        elif user==Panda2:
                            Panda2choice="Block"
                    elif player=="Charge ur hit":
                        print(user+"Choose to Charge their hit")  
                        if user==Panda1:
                            Panda1choice="Charge"
                        elif user==Panda2:
                            Panda2choice="Charge"
                    if Panda2choice!=""and Panda1choice!="":
                        await arena.send(Panda1+" chose to "+Panda1choice+" and "+Panda2+" choose to "+Panda2choice)
                        if Panda1choice == "Normal Hit" and Panda2choice=="Normal Hit":
                            print("double normal hit")
                            Panda1health-=Panda2damage
                            Panda2health-=Panda1damage
                            await arena.send("Both of you have choosen to normal hit! "+Panda1+" has taken "+str(Panda2damage)+" damage and is now on Health "+str(Panda1health)+" while "+Panda2+" has taken "+str(Panda1damage)+" damage and is now on "+str(Panda2health))
                        elif Panda1choice == "Normal Hit" and Panda2choice=="Block":
                            print("Panda1 hit Panda2 block")
                            Panda1health-=Panda1damage*0.5
                            await arena.send(Panda1+" has tryed hitting but "+Panda2+" has blocked dealing "+str(Panda1damage*0.5)+" to "+Panda1)
                        elif Panda1choice=="Block" and Panda2choice=="Normal Hit":
                            print("Panda2 hit, Panda1 block")
                            Panda2health-=Panda2damage*0.5
                            await arena.send(Panda2+" has tryed hitting but "+Panda1+" has blocked dealing "+str(Panda2damage*0.5)+" to "+Panda2)
                        elif Panda1choice=="Block"and Panda2choice=="Block":
                            await arena.send("Both choose to Block, nothing happens, Cowards -_-")
                        elif Panda1choice=="Block" and Panda2choice=="Charge":
                            print("Panda1 blcok Panda2 charge")
                            Panda1health-=Panda2damage
                            await arena.send(Panda1+" has blocked, but "+Panda2+" has charge hitted destoying the barrier and dealing "+str(Panda2damage)+" damage to "+Panda1+" meaning their health is dow to "+str(Panda1health))
                        elif Panda2choice=="Block" and Panda1choice=="Charge":
                            print("Panda2 blcok Panda1 charge")
                            Panda2health-=Panda1damage
                            await arena.send(Panda2+" has blocked, but "+Panda1+" has charge hitted destoying the barrier and dealing "+str(Panda1damage)+" damage to "+Panda2+" meaning their health is dow to "+str(Panda2health))
                        elif Panda1choice=="Charge"and Panda2choice=="Charge":
                            print("double charge hit")
                            Panda1health-=Panda2damage*2
                            Panda2health-=Panda1damage*2
                            await arena.send("Both of you have choosen to charge hit! "+Panda1+" has taken "+str(Panda2damage*2)+" damage and is now on Health "+str(Panda1health)+" while "+Panda2+" has taken "+str(Panda1damage*2)+" damage and is now on "+str(Panda2health))
                        elif Panda1choice=="Charge" and Panda2choice=="Normal Hit":
                            print("Panda1 charge, Panda2 hit")
                            Panda1health-=Panda2damage
                            await arena.send(Panda1+"tryed charging their hit but since "+Panda2+"hitted normal and with that faster, "+Panda2+" deals "+str(Panda2damage)+" Damage to "+Panda1+" meaning "+Panda1+" is left on "+str(Panda1health)+" Health!")
                        elif Panda2choice=="Charge" and Panda1choice=="Normal Hit":
                            print("Panda1 charge, Panda2 hit")
                            Panda2health-=Panda1damage
                            await arena.send(Panda2+"tryed charging their hit but since "+Panda1+"hitted normal and with that faster, "+Panda1+" deals "+str(Panda1damage)+" Damage to "+Panda2+" meaning "+Panda2+" is left on "+str(Panda2health)+" Health!")
                    if Panda1health<=0 and Panda2health<=0:
                        await arena.send("OMG A DRAW BOTH OF YOU ARE AT 0 HP!")
                    elif Panda2health<=0:
                        await arena.send(Panda2+" is at 0 hp and with that they LOST!")
                    elif Panda1health<=0:
                        await arena.send(Panda1+" is at 0 hp and with that they LOST!")
                    else:
                        await fight(arena, oponent, ctx, Panda1health, Panda1damage, Panda2health, Panda2damage)
    except asyncio.exceptions.TimeoutError:
        print("ye...")
@client.command()
async def duel(ctx, oponent: discord.Member):
    print(str(oponent))
    print(ctx.message.channel.category)
    m = await ctx.send(content=oponent.name+" You have been dueled by: "+ctx.author.name, components=[Button(style=ButtonStyle.blue, label="Accept"), Button(style=ButtonStyle.red, label="Decline")])
    def check(res):
        print(res.user)
        return res.channel == ctx.channel and res.user == oponent
    try: 
        res=await client.wait_for("button_click", check=check, timeout=15)
        player=res.component.label
        if player=="Accept":
            await ctx.send("Accept")
            guild = ctx.guild
            arena = await guild.create_text_channel(["Battle Arena of the red dragon","Fight pit of the holy Hund","Valley of the Volcano"][random.randint(0, 2)], overwrites={oponent:discord.PermissionOverwrite(read_messages=True),ctx.author: discord.PermissionOverwrite(read_messages=True),guild.default_role:discord.PermissionOverwrite(read_messages=False),guild.me: discord.PermissionOverwrite(read_messages=True)}, category=discord.utils.get(ctx.guild.categories, name='ARENAS') ,position=1)
            await arena.send(oponent.mention+" "+ctx.author.mention)
            starter="""
Welcome dear fighters to this arena! Here are the rules, you will both be presented with a Multiple Choice Option field!
You can choose between a normal hit, the option to block or charge a powerfull attack, 
if you choose hit and your oponent does too, both deal the damage created by their Pandas to the other one!
if you choose to hit and your oponent choses to block, YOU will take half of the damage you would have dealt to them!
if you choose to hit and your oponent decides to charge their hit, you hit faster meaning you deal the damage your Panda usually deals directly to them and they dont deal any to you!
if both of you decide to charge a hit, both of you will deal twice the normal dmage to eachother!
if you charge and your oponent blocks, your powerful hit destroys their barrier dealing the normal amount of damge to them!
if both of you block, nothing happens and the next round begins!
The first Panda down loses!
            """
            await arena.send(starter)
            await arena.send("""```diff\n-MAY THE BLOODTHIRSTIEST WIN!```""")
        ############################################
            #await arena.send(str(ctx.author)+" has "+str(Panda1health)+" HP and deals "+str(Panda1damage)+" damage, on the other hand "+str(oponent)+" has "+str(Panda2health)+" HP and deals "+str(Panda2damage)+" damage!")
            ################################
            Panda1health=0
            Panda2health=0
            Panda1damage=0
            Panda2damage=0
            with open("D:\\Hacking\\python\\PandaFightClub\\" + str(ctx.author.id)+".json") as f: 
                data = json.load(f)
            end={
            "Damage": 1,
            "Health": 10,
            "Range": 1
            }
            liste=[data["Weapon"],data["Accessory"],data["Boots"],data["Chestplate"],data["Helmet"],data["Shield"]]
            for i in liste :
                with open("D:\\Hacking\\python\\PandaFightClub\\" + str(i)+".json") as f: 
                    item = json.load(f)
                    end["Damage"]+=item["Damage"]
                    end["Health"]+=item["Health"]
                    end["Range"]+=item["Range"]
            Panda1damage=end["Damage"]+(end["Range"]*end["Damage"]*0.1)
            Panda1health=end["Health"]
        ############################################
            with open("D:\\Hacking\\python\\PandaFightClub\\" + str(oponent.id)+".json") as f: 
                    data = json.load(f)
            end={
            "Damage": 1,
            "Health": 10,
            "Range": 1
            }
            liste=[data["Weapon"],data["Accessory"],data["Boots"],data["Chestplate"],data["Helmet"],data["Shield"]]
            for i in liste :
                with open("D:\\Hacking\\python\\PandaFightClub\\" + str(i)+".json") as f: 
                    item = json.load(f)
                    end["Damage"]+=item["Damage"]
                    end["Health"]+=item["Health"]
                    end["Range"]+=item["Range"]
            Panda2damage=end["Damage"]+(end["Range"]*end["Damage"]*0.1)
            Panda2health=end["Health"]
            await fight(arena, oponent, ctx, Panda1health, Panda1damage, Panda2health, Panda2damage)#
            ##############################
        elif player=="Decline":
            await ctx.send("Decline")
    except asyncio.exceptions.TimeoutError:
        await ctx.send("somewhere went beep boop wrong ):")



client.run("ODQ1MzM0NzQ3Nzk3NzgyNTU5.YKfdVQ.oem6KccZj-Sv7YCrLzL7N2LIfOI")

"""
TODO:
duel urself no good
"""


#BambooTest123
#Im changing stuff rn
#Baum
#another Baum
#Change 123