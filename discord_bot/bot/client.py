from discord import Message
from discord.ext import commands
from googlesearch import search

from discord_bot.bot.bot_storage import BotStorage, initialize_schema
from discord_bot.settings import DISCORD_TOKEN

bot = commands.Bot(command_prefix="!")


@bot.command()
async def google(ctx: commands.context.Context, keyword: str):
    """
    A Bot command that provides 5 top results from google search and saves the keyword in the DB.
    For example: "!google apple" will search apple in the google and provides results.
    """
    results = search(keyword, num=5, stop=5)
    message = "\n".join(list(results))
    with BotStorage() as storage:
        storage.save_keyword(ctx.author.id, keyword)
    await ctx.send(message)


@bot.command()
async def recent(ctx: commands.context.Context, keyword: str):
    """
    A Bot command that provides results through the user history.
    For example: "!recent apple" will look for apple keyword in user searched keywords.
    """
    with BotStorage() as storage:
        results = storage.get_matched_keywords(ctx.author.id, keyword)
        if results:
            message = "\n".join([result[0] for result in results])
        else:
            message = f'Oops, not found any match for "{keyword}"'
    await ctx.send(message)


@bot.event
async def on_message(msg: Message):
    """
    Handles the event when someone sends a message
    """
    # Return if message is sent by bot itself
    if msg.author == bot.user:
        return

    if msg.content.lower() == "hi":
        await msg.channel.send("hey")

    # Process the commands for the sent message
    await bot.process_commands(msg)


@bot.event
async def on_ready():
    """
    Handles the event when bot is ready for the actions
    """
    print("Bot is now ready")


if __name__ == "__main__":
    initialize_schema()
    bot.run(DISCORD_TOKEN)
