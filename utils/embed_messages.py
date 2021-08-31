from discord.embeds import Embed
from datetime import datetime

def easyembed(title, _type, message, footer = None):
    _type = _type.lower()

    color = 0xE2E3E5

    if _type == "info":
        color = 0xD1ECF1
    elif _type == "error":
        color = 0xC50707
    elif _type == "warning":
        color = 0xFFF3CD
    elif _type == "success":
        color = 0xD4EDDA

    e = Embed(
        description=message,
        color=color,
        timestamp=datetime.utcnow()
    )

    e.set_author(
        name=title,
        icon_url="https://cdn.discordapp.com/attachments/545533157131288587/876658614553686016/slp.png"
    )

    if footer:
        e.set_footer(
            text=footer
        )

    return e