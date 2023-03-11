#Repthon

import random

from telethon.errors.rpcbaseerrors import ForbiddenError
from telethon.errors.rpcerrorlist import PollOptionInvalidError
from telethon.tl.types import InputMediaPoll, Poll

from . import Build_Poll


@bot.on(admin_cmd(pattern="استفتاء( (.*)|$)"))
@bot.on(sudo_cmd(pattern="استفتاء( (.*)|$)", allow_sudo=True))
async def pollcreator(Repthon):
    reply_to_id = None
    if Repthon.reply_to_msg_id:
        reply_to_id = Repthon.reply_to_msg_id
    string = "".join(Repthon.text.split(maxsplit=1)[1:])
    if not string:
        options = Build_Poll(["- ايي 😊✌️", "- لاع 😏😕", "- مادري 🥱🙄"])
        try:
            await bot.send_message(
                Repthon.chat_id,
                file=InputMediaPoll(
                    poll=Poll(
                        id=random.getrandbits(32),
                        question="تحبوني ؟",
                        answers=options,
                    )
                ),
                reply_to=reply_to_id,
            )
            await Repthon.delete()
        except PollOptionInvalidError:
            await edit_or_reply(
                Repthon,
                "⌔∮ الاستفتاء المستخدم غير صالح (قد تكون المعلومات طويلة جدا).",
            )
        except ForbiddenError:
            await edit_or_reply(Repthon, "⌔∮ هذه الدردشة تحظر استطلاعات الرأي. ")
        except exception as e:
            await edit_or_reply(Repthon, str(e))
    else:
        Repthon = string.split("|")
        if len(Repinput) > 2 and len(Repinput) < 12:
            options = Build_Poll(Repinput[1:])
            try:
                await bot.send_message(
                    Rallspoll.chat_id,
                    file=InputMediaPoll(
                        poll=Poll(
                            id=random.getrandbits(32),
                            question=Repinput[0],
                            answers=options,
                        )
                    ),
                    reply_to=reply_to_id,
                )
                await Repthon.delete()
            except PollOptionInvalidError:
                await edit_or_reply(
                    icsspoll,
                    "⌔∮ الاستفتاء المستخدم غير صالح (قد تكون المعلومات طويلة جدا).",
                )
            except ForbiddenError:
                await edit_or_reply(Repthon, "⌔∮ هذه الدردشة تحظر استطلاعات الرأي. ")
            except Exception as e:
                await edit_or_reply(Repthon, str(e))
        else:
            await edit_or_reply(
                Repthon,
                "**⌔∮ انت تكتب الامر بشكل خاطئ يجب عليك كتابته بهذا الشكل** `.استفتاء السؤال | الجواب الاول | الجواب الثاني`",
            )


CMD_HELP.update(
    {
        "استفتاء": "**اسم الاضافـه :**`استفتاء`\
        \n\n**╮•❐ الامـر ⦂** `.استفتاء`\
        \n**الشـرح •• **إذا لم تقدم أي مدخلات ، فإنها ترسل استطلاعًا افتراضيًا. إذا كنت ترغب في تخصيصه ، فاستخدم بناء الجملة هذا :\
        \n `.استفتاء السؤال | الجواب الاول | الجواب الثاني`\
        \n '|' هذا الرمز يفصل بين كل خيار وسؤال \
        "
    }
)
