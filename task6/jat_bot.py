import discord
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

AUTHORIZED_ROLES = ["Faculty", "Administrator"]
ANNOUNCEMENT_CHANNEL_ID = 1416110696713818165
DELETE_AFTER_SECONDS = 86400

@client.event
async def on_ready():
    print(f"Bot is ready as {client.user}") 

@client.event
async def on_member_join(member):
    print(f"New member joined: {member.name}")
    channel_id = 1087643008276639807
    channel = client.get_channel(channel_id)
    if channel:
        await channel.send(f"Welcome to the server, {member.mention}! 🎉")
    else:
        print("Welcome channel not found.")
    role_name = "Aspiring Hero"
    role = discord.utils.get(member.guild.roles, name=role_name)
    if role:
        await member.add_roles(role)
        print(f"Assigned role '{role.name}' to {member.name}")
    else:
        print(f"Role '{role_name}' not found.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!wisdom rules"):
        await message.channel.send("1. Be respectful to all members.\n2. No spamming \n3.No bullying others")
    if message.content.startswith("!wisdom resources"):
        await message.channel.send("1. https://www.w3schools.com/python/\n2. https://realpython.com/\n3. https://docs.python.org/3/tutorial/")
    if message.content.startswith("!wisdom contact"):
        await message.channel.send("You can contact the admin at shreyas lab which is avaiable from 9am to 5pm \n Contact this mail id faculty1234@gmail.com")

    keywords = ["villainous spam", "unauthorized link", "off topic disruption", "menacing threats"]
    if any(kw in message.content.lower() for kw in keywords):
        await message.delete()
        await message.channel.send(f"{message.author.mention}, violated the rule of code of conduct of midtown tech")

    if message.content.startswith("!bugle "):
        if any(role.name in AUTHORIZED_ROLES for role in message.author.roles):
            announcement = message.content[len("!bugle "):]
            channel = client.get_channel(ANNOUNCEMENT_CHANNEL_ID)
            if channel:
                sent_msg = await channel.send(f"📣 **Announcement:** {announcement}")
                async def delete_if_not_pinned():
                    await asyncio.sleep(DELETE_AFTER_SECONDS)
                    try:
                        refreshed_msg = await channel.fetch_message(sent_msg.id)
                        if not refreshed_msg.pinned:
                            await refreshed_msg.delete()
                            print("Announcement deleted after timeout.")
                        else:
                            print("Announcement retained (pinned).")
                    except discord.NotFound:
                        print("Message already deleted.")
                asyncio.create_task(delete_if_not_pinned())
            else:
                await message.channel.send("Announcements channel not found.")
        else:
            await message.channel.send("You are not authorized to post announcements.")

client.run(os.getenv('TOKEN'))