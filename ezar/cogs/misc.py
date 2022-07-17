from typing import Literal

from disnake import CommandInter, Member, User
from disnake.ext.commands import Cog, slash_command

from ezar import Ezar
from ezar.backend.config import Colors
from ezar.utils.embed import Embeb


class Miscellaneous(Cog):
    """Miscellaneous/not-important commands"""

    def __init__(self, bot: Ezar):
        self.bot = bot

    @slash_command()
    async def icon(self, itr: CommandInter):
        """Icon/Profile-Picture-related commands"""

    @icon.sub_command()
    async def server(self, itr: CommandInter):
        """Returns the server icon URL."""
        avatar_embed = Embeb()
        avatar_embed.set_image(url=itr.guild.icon.with_size(1024).url)
        avatar_embed.set_author(
            name=itr.guild.name,
            icon_url=itr.guild.icon if itr.guild.icon else itr.guild.gen,
        )
        await itr.response.send_message(embed=avatar_embed)

    @icon.sub_command()
    async def user(
        self,
        itr: CommandInter,
        user: User = None,
        type: Literal["global", "local"] = "local",
    ):
        """Returns a user's avatar.

        Parameters
        ----------
        user: The user to get the avatar of.
        type: The type of avatar to get."""
        if user is None:
            user = itr.user
        elif user in itr.guild.members:
            user: Member = await itr.guild.getch_member(user.id)

        avatar_embed = Embeb(
            color=user.color if user in itr.guild.members else Colors.purple
        )
        if type == "global":
            avatar_embed.set_image(url=user.avatar.url or user.default_avatar.url)
            avatar_embed.set_author(
                name=user.name, icon_url=user.avatar.url or user.default_avatar.url
            )
            await itr.send(embed=avatar_embed)
        elif type == "local":
            avatar_embed.set_author(name=user.name, icon_url=user.display_avatar.url)
            avatar_embed.set_image(url=user.display_avatar.url)
            await itr.send(embed=avatar_embed)


def setup(bot: Ezar):
    bot.add_cog(Miscellaneous(bot))
