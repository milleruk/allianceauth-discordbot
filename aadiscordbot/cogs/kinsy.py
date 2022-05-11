# Cog Stuff
from discord.ext import commands
from discord.embeds import Embed
from discord.colour import Color
from ..app_settings import mumble_active, discord_active
# AA Contexts
from aadiscordbot.app_settings import get_site_url, get_admins

from django.conf import settings

import logging
logger = logging.getLogger(__name__)


class Kinsy(commands.Cog):
    """
    The Kinsy Video
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def auth(self, ctx):
        """
        Returns the Kinsy Video
        """
        await ctx.trigger_typing()

        embed = Embed(title="AllianceAuth")
        embed.set_thumbnail(
            url="https://images.evetech.net/characters/1630472146/portrait?size=128"
        )
        embed.colour = Color.blue()

        embed.description = "Just Jump In Anw WARP TO ME!!"

        url = get_site_url()

        embed.add_field(
            name="The Link", value="https://cdn.discordapp.com/attachments/685827175626440735/949349523774398565/My_Movie.mp4".format(url, url), inline=False
        )

        return await ctx.send(embed=embed)

    @commands.slash_command(name='auth', guild_ids=[int(settings.DISCORD_GUILD_ID)])
    async def auth_slash(self, ctx):
        """
        Returns the Kinsy Video
        """
        embed = Embed(title="Kinsy")
        embed.set_thumbnail(
            url="https://images.evetech.net/characters/1630472146/portrait?size=128"
        )
        embed.colour = Color.blue()

        embed.description = "Just Jump In Anw WARP TO ME!!"

        url = get_site_url()

        embed.add_field(
            name="The Link", value="https://cdn.discordapp.com/attachments/685827175626440735/949349523774398565/My_Movie.mp4".format(url, url), inline=False
        )

        return await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(Auth(bot))
