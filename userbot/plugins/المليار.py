#by Roger For Repthon
# يمنع منعاً باتاً تخمط الملف خلي عندك كرامه ولتسرقة
from userbot import bot
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
import asyncio
from telethon import events
c = requests.session()
bot_username = '@t06bot'
repthon = ['yes']


@bot.on(admin_cmd(pattern="(تجميع النقاط|تجميع نقاط)"))
async def _(event):
    if repthon[0] == "yes":
        await event.edit("**᯽︙سيتم تجميع النقاط , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await bot.get_entity(bot_username)
        await bot.send_message('@t06bot', '/start')
        await asyncio.sleep(5)
        msg0 = await bot.get_messages('@t06bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await bot.get_messages('@t06bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if repthon[0] == 'no':
                break
            await asyncio.sleep(5)

            list = await bot(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await bot.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await bot(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await bot(ImportChatInviteRequest(bott))
                msg2 = await bot.get_messages('@t06bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await bot.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await bot.send_message(event.chat_id, f"**خطأ , ممكن تبندت**")
                break
        await bot.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")
