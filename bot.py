import discord

client = discord.Client()
channel1id = 848906341183258628
channel2id = 884754157502881832

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(message):
    if message.channel.id == channel1id:
        channeltosend = client.get_channel(channel2id)
        await channeltosend.send(message.content, embed=message.embeds[0])

client.run("ODg0NzUyOTI0NjEyMzcwNDMy.YTdEXw.OUbidaVtJx54ePTDJDrkS3Uzmhw")