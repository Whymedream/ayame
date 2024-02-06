from flask_discord_interactions import cog, Member, Embed
from utils.database import get_currency, get_user, task
from datetime import datetime as dt


class BalanceCog:
    def __init__(self, interactions):
        self.interactions = interactions
        self.register()

    def register(self):

        @self.interactions.command()
        def balance(ctx, member: Member = None):
            currency = get_currency(ctx.guild)
            if member is None:
                member = ctx.author
            user = get_user(member.id, ctx.guild)
            emb = Embed(color=0x2b2d31)
            emb.add_field(name='Баланс:', value=f"{task(user['balance'])} {currency}")
            emb.add_field(name='Банк:', value=f"{task(user['bank'])} {currency}")
            emb.set_thumbnail(url=ctx.author.display_avatar.url)
            emb.timestamp = dt.now()
            return emb.to_dict()