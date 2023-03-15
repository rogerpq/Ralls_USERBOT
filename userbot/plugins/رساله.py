import os
from PIL import Image, ImageDraw, ImageFont
from . import *
from . import ALIVE_NAME, *


def text_set(text):
    lines = []
    if len(text) <= 55:
        lines.append(text)
    else:
        all_lines = text.split("\n")
        for line in all_lines:
            if len(line) <= 55:
                lines.append(line)
            else:
                k = int(len(line) / 55)
                for z in range(1, k + 2):
                    lines.append(line[((z - 1) * 55) : (z * 55)])
    return lines[:25]
    

@bot.on(baqir_cmd(pattern="رساله ?(.*)"))
async def writer(e):
    if e.reply_to:
        reply = await e.get_reply_message()
        text = reply.message
    elif e.pattern_match.group(1):
        text = e.text.split(maxsplit=1)[1]
    else:
        return await e.edit("**- بالـرد على نص او .رساله + النص**")
    img = Image.open("Zilzal/malath/ppho.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Zilzal/malath/zarz.ttf", 30)
    x, y = 150, 140
    lines = text_set(text)
    line_height = font.getsize("hg")[1]
    for line in lines:
        draw.text((x, y), line, fill=(1, 22, 55), font=font)
        y = y + line_height - 5
    file = "{ALIVE_NAME}.jpg"
    img.save(file)
    await e.reply(file=file)
    os.remove(file)
    await e.delete()
