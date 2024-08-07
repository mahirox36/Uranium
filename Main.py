from rich import print
from rich.console import Console
from rich.traceback import install
from Lib.richer import *
install()
try:
    import nextcord
    from nextcord.ext import commands
    from requests import request
    from Lib.Side import *
    import Lib.Data as Data
    from Lib.Logger import *
    import os
    from nextcord import Interaction as init
    from datetime import datetime
    import threading
    import time

    intents = nextcord.Intents.all()
    client = commands.Bot(command_prefix=prefix, intents=intents)

    global Bot
    Bot = client

    clear()
    



    #On Bot Start
    @client.event
    async def on_ready():
        await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f"Over {len(client.guilds)} Servers"))
        print(Rule(f'{client.user.display_name}  Is Online',style="bold green")) # type: ignore
        if send_to_owner_enabled:
            user = client.get_user(owner_id)
            channel = await user.create_dm()
            await channel.send("Running ✅",embeds=[
                info_embed("Bot is Online")])
    #End

    #Classes
    initial_extension = []
    core_extension = []

    for filename in os.listdir("./classes"):
        if filename.endswith(".py"):
            if "." in filename[:-3]: raise Exception("You can't have a dot in the class name")
            if (DisableAiClass == True) and (filename[:-3] == "AI"):
                continue
            initial_extension.append("classes." + filename[:-3])


    print(f"and These All The Extension {initial_extension} ")
    for extension in initial_extension:
        if (extension == "classes.Welcome") and (Welcome_enabled == False):
            continue
        client.load_extension(extension)

    if __name__ == '__main__':
        try:
            client.run(token)
        except nextcord.errors.LoginFailure:
            print(Panel(f"""Here's the step to check if you Have put your Token right:
            1- Add your token in the config file in {config_path}
            2- see if it didn't change back to "Your Bot Token" and if is change it to your token
            3- Reset your token in https://discord.com/developers/applications""",
            title="Invalid Token",style="bold red",border_style="bold red"))
except Exception as e:
    console.print_exception()