import os
from flask import Flask
from flask_discord_interactions import DiscordInteractions
app = Flask(__name__)
interactions = DiscordInteractions(app)

app.config["DISCORD_CLIENT_ID"] = ""
app.config["DISCORD_PUBLIC_KEY"] = ""
app.config["DISCORD_CLIENT_SECRET"] = ""

interactions.set_route("/interactions")

cogs = ['balance']

for cog in cogs:
    interactions.load_cog(cog)

interactions.update_commands()

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
