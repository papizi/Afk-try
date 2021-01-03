from .. import loader, utils


def register(cb):
    cb(ArtsMod())


class ArtsMod(loader.Module):
    strings = {'name': 'Slot'}

    async def slotcmd(self, message):
        text = utils.get_args_raw(message)
        from asyncio import sleep
        await message.respond(text)
        await sleep(20)
        await message.respond(text)
        await sleep(20)
        await message.respond(text)
        await sleep(20)
        await message.respond(text)
        await sleep(20)
        await message.respond(text)
        await sleep(20)
        await message.respond(text)
        await sleep(20)
        await message.respond(text)

            
            
