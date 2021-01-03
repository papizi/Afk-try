# made by @PapichX


from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.ff(?: |$)(.*)')
async def typewriter(typew):
    await typew.edit("Слот 20М")
    sleep(20.00)
    await typew.print("Слот 20М")
    sleep(20.00)
    await typew.print("Слот 20М")
    sleep(20.00)
