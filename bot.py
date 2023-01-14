import discord
import random
import responses
import bot



def run_discord_bot():
    TOKEN = 'MTA2MzU2MTA5ODQ3NDgxOTYwNg.GYtoo8.kTlPyw7Lag9AKADK6VXoDy2AlJrLTGckw6UpGM'
    
    client = discord.Client(intents=is_)

   
    @client.event
    async def on_ready():
        print ('{0.user} is now running!'.format(client))



    @client.event
    async def on_message(message):

        username = str(message.author).split("#")[0]
        user_message = str(message.content)   
        channel = str(message.channel.name)


        print(f"{username} said: '{user_message}' ({channel})")

        if message.channel.name == "general":

            if message.author == client.user:
                return

            if user_message.lower() == "hello":
                await message.channel.send(f"Hey there pidaras")    
                return

            elif user_message.lower() ==  "roll":
                await message.channel.send(random.randint(1, 15))
                return
     
            elif user_message.lower() ==  "play":
                await message.channel.send(f"you are first pidar on this planet {username} ahahhaha")
                return    




    client.run(TOKEN)

while True:
    bot.run_discord_bot()
