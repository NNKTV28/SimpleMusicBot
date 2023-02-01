import discord
import os
from dotenv import load_dotenv
import wavelink
load_dotenv()
bot = discord.Bot()
async def connect_nodes():
  """Connect to our Lavalink nodes."""
  await bot.wait_until_ready() # wait until the bot is ready

  await wavelink.NodePool.create_node(
    bot=bot,
    host='0.0.0.0',
    port=2333,
    password='youshallnotpass'
  ) # create a node
@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    await connect_nodes()  # connect to the server
@bot.event
async def on_wavelink_node_ready(node: wavelink.Node):
  print(f"{node.identifier} is ready.") # print a message
cogs_list = ['music']

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')

bot.run(os.getenv('TOKEN'))