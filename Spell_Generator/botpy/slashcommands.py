import disnake
from disnake.ext import commands
import random
import requests
import json

class utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def spell(self, inter: disnake.CommandInteraction):

        #setup harry potter spells
        url = "https://hp-api.onrender.com/api/spells"
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print("Harry potter setup complete")
            spells = json.loads(response.text)

        else:
            print("Harry potter setup Failed")
            print(response.text)
            spells = {'error':"error"}
        spell = random.choice(spells)
        print(spell)
        await inter.response.send_message("Spell: " + spell["name"] + " Description: " +  spell["description"])

