from discord.ext.ui import Component, Button, View, ObservedObject, Published, Message
import discord
import os

client = discord.Client()


class SampleViewModel(ObservedObject):
    def __init__(self):
        super().__init__()
        self.num = Published(0)

    def countup(self):
        self.num += 1

    def countdown(self):
        self.num -= 1


class SampleView(View):
    def __init__(self):
        super().__init__()
        self.viewModel = SampleViewModel()

    async def delete(self, interaction: discord.Interaction):
        await interaction.message.delete()
        await self.stop()

    async def add_reaction(self):
        await self.discord_message.add_reaction("\U0001f44d")

    async def body(self):
        return Message(
            content=f"test! {self.viewModel.num}",
            component=Component(
                buttons=[
                    [
                        Button("+1")
                        .on_click(lambda x: self.viewModel.countup())
                        .style(discord.ButtonStyle.blurple),

                        Button("-1")
                        .on_click(lambda x: self.viewModel.countdown())
                        .style(discord.ButtonStyle.blurple)
                    ],
                    [
                        Button("終わる")
                        .on_click(self.delete)
                        .style(discord.ButtonStyle.danger)
                    ]
                ]
            )
        ).on_appear(self.add_reaction)


@client.event
async def on_message(message):
    if message.content != "!test":
        return
    await SampleView().start(client, message.channel)


client.run(os.environ["DISCORD_BOT_TOKEN"])
