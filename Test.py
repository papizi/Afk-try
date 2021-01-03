from .. import loader, utils


def register(cb):
    cb(ArtsMod())


class ArtsMod(loader.Module):
    strings = {'name': 'Slot'}

    async def vjuhcmd(self, message):
        text = utils.get_args_raw(message)
        if not text:
            await message.edit('<b>Нету текста после команды :c</b>')
            return
        else:
            vjuh =("слот 10М")
            time.sleep(20.00)
            vjuh =("слот 10М")
            time.sleep(20.00)

            
