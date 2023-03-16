# Repthon - UserBot
# Copyright (C) Repthon. All Rights Reserved
# PLease read the GNU Affero General Public License in

""" Command: اوامـر حمـاية المجمـوعات والقنـوات بالمسـح والطـرد والتقييـد
Credit: @Repthon
@E_7_V - كتـابـة الملـف :  روجــر"""


import asyncio
import io
from asyncio import sleep
from datetime import datetime
from math import sqrt


from telethon import events, functions, types
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.functions.messages import EditChatDefaultBannedRightsRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetFullChatRequest, GetHistoryRequest
from telethon.tl.types import (
    ChannelParticipantAdmin,
    ChannelParticipantCreator,
    ChannelParticipantsAdmins,
    ChannelParticipantsBots,
    ChannelParticipantsKicked,
    ChatBannedRights,
    MessageActionChannelMigrateFrom,
    UserStatusEmpty,
    UserStatusLastMonth,
    UserStatusLastWeek,
    UserStatusOffline,
    UserStatusOnline,
    UserStatusRecently,
)
from telethon.errors import (
    ChatAdminRequiredError,
    UserAdminInvalidError,
)
from ..utils import is_admin
from userbot.plugins.sql_helper.locks_sql import get_locks, is_locked, update_lock
from . import BOTLOG, BOTLOG_CHATID, admin_groups, get_user_from_event
# All Rights Reserved for "Rallsthon - UserBot" "الريس"
ANTI_DDDD_RallsTHON_MODE = ChatBannedRights(
    until_date=None, view_messages=None, send_media=True, send_stickers=True, send_gifs=True
)


@bot.on(admin_cmd(pattern=r"قفل (.*)"))
@bot.on(sudo_cmd(pattern=r"قفل (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    Ralls_id = event.chat_id
    # All Rights Reserved for "Rallsthon - UserBot" "الريس"
    if not event.is_group:
        return await edit_delete(event, "**ايا مطـي! ، هـذه ليست مجموعـة لقفـل الأشيـاء**")
    chat_per = (await event.get_chat()).default_banned_rights
    if input_str == "البوتات":
        update_lock(Ralls_id, "bots", True)
        return await edit_or_reply(event, "**❈╎تـم قفـل {} بنجـاح ✅ •**\n\n**❈╎خاصيـة الطـرد والتحذيـر •**".format(input_str))
    if input_str == "المعرفات":
        update_lock(Ralls_id, "button", True)
        return await edit_or_reply(event, "**❈╎تـم قفـل {} بنجـاح ✅ •**\n\n**❈╎خاصيـة المسـح والتحذيـر •**".format(input_str))
    if input_str == "الدخول":
        update_lock(Ralls_id, "location", True)
        return await edit_or_reply(event, "**❈╎تـم قفـل {} بنجـاح ✅ •**\n\n**❈╎خاصيـة الطـرد والتحذيـر •**".format(input_str))
    if input_str == "الفارسيه":
        update_lock(Ralls_id, "egame", True)
        return await edit_or_reply(event, "**❈╎تـم قفـل {} بنجـاح ✅ •**\n\n**❈╎خاصيـة المسـح والتحذيـر •**".format(input_str))
    if input_str == "الاضافه":
        update_lock(Ralls_id, "contact", True)
        return await edit_or_reply(event, "**❈╎تـم قفـل {} بنجـاح ✅ •**\n\n**❈╎خاصيـة الطـرد والتحذيـر •**".format(input_str))
    if input_str == "التوجيه":
        update_lock(Ralls_id, "forward", True)
        return await edit_or_reply(event, "**❈╎تـم قفـل {} بنجـاح ✅ •**\n\n**❈╎خاصيـة المسـح والتحذيـر •**".format(input_str))
    if input_str == "الميديا":
        update_lock(Ralls_id, "game", True)
        return await edit_or_reply(event, "**❈╎تـم قفـل {} بنجـاح ✅ •**\n\n**❈╎خاصيـة المسـح بالتقييـد والتحذيـر •**".format(input_str))
    if input_str == "الانلاين":
        update_lock(Ralls_id, "inline", True)
        return await edit_or_reply(event, "**❈╎تـم قفـل {} بنجـاح ✅ •**\n\n**❈╎خاصيـة المسـح والتحذيـر •**".format(input_str))
    if input_str == "الفشار":
        update_lock(Ralls_id, "rtl", True)
        return await edit_or_reply(event, "**❈╎تـم قفـل {} بنجـاح ✅ •**\n\n**❈╎خاصيـة المسـح والتحذيـر •**".format(input_str))
    if input_str == "الروابط":
        update_lock(Ralls_id, "url", True)
        return await edit_or_reply(event, "**❈╎تـم قفـل {} بنجـاح ✅ •**\n\n**❈╎خاصيـة المسـح والتحذيـر •**".format(input_str))
    if input_str == "الكل":
        update_lock(Ralls_id, "bots", True)
        update_lock(Ralls_id, "location", True)
        update_lock(Ralls_id, "game", True)
        update_lock(Ralls_id, "forward", True)
        update_lock(Ralls_id, "egame", True)
        update_lock(Ralls_id, "rtl", True)
        update_lock(Ralls_id, "url", True)
        update_lock(Ralls_id, "contact", True)
        update_lock(Ralls_id, "location", True)
        update_lock(Ralls_id, "button", True)
        update_lock(Ralls_id, "inline", True)
        update_lock(Ralls_id, "video", True)
        update_lock(Ralls_id, "sticker", True)
        update_lock(Ralls_id, "voice", True)
        return await edit_or_reply(event, "**❈╎تـم قفـل {} بنجـاح ✅ •**\n\n**❈╎خاصيـة المسـح - الطـرد - التقييـد - التحذيـر •**".format(input_str))
    else:
        if input_str:
            return await edit_delete(
                event, f"**❈╎عذراً لايمكن قفل :** `{input_str}`", time=5
            )

        return await edit_or_reply(event, "`❈╎عذراً لايمكنك قفل اي شي هنا 𓆰•`")


@bot.on(admin_cmd(pattern="فتح (.*)"))
@bot.on(sudo_cmd(pattern="فتح (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    Ralls_id = event.chat_id
   # All Rights Reserved for "Rallsthon - UserBot" "الريس"
    if not event.is_group:
        return await edit_delete(event, "**ايا مطـي! ، هـذه ليست مجموعـة لقفـل الأشيـاء**")
    chat_per = (await event.get_chat()).default_banned_rights
    if input_str == "البوتات":
        update_lock(Ralls_id, "bots", False)
        return await edit_or_reply(event, "**❈╎تـم فتـح** {} **بنجـاح ✅ 𓆰•**".format(input_str))
    if input_str == "الدخول":
        update_lock(Ralls_id, "location", False)
        return await edit_or_reply(event, "**❈╎تـم فتـح** {} **بنجـاح ✅ 𓆰•**".format(input_str))
    if input_str == "الاضافه":
        update_lock(Ralls_id, "contact", False)
        return await edit_or_reply(event, "**❈╎تـم فتـح** {} **بنجـاح ✅ 𓆰•**".format(input_str))
    if input_str == "التوجيه":
        update_lock(Ralls_id, "forward", False)
        return await edit_or_reply(event, "**❈╎تـم فتـح** {} **بنجـاح ✅ 𓆰•**".format(input_str))
    if input_str == "الفارسيه":
        update_lock(Ralls_id, "egame", False)
        return await edit_or_reply(event, "**❈╎تـم فتـح** {} **بنجـاح ✅ 𓆰•**".format(input_str))
    if input_str == "الفشار":
        update_lock(Ralls_id, "rtl", False)
        return await edit_or_reply(event, "**❈╎تـم فتـح** {} **بنجـاح ✅ 𓆰•**".format(input_str))
    if input_str == "الروابط":
        update_lock(Ralls_id, "url", False)
        return await edit_or_reply(event, "**❈╎تـم فتـح** {} **بنجـاح ✅ 𓆰•**".format(input_str))
    if input_str == "الميديا":
        update_lock(Ralls_id, "game", False)
        return await edit_or_reply(event, "**❈╎تـم فتـح** {} **بنجـاح ✅ 𓆰•**".format(input_str))
    if input_str == "المعرفات":
        update_lock(Ralls_id, "button", False)
        return await edit_or_reply(event, "**❈╎تـم فتـح** {} **بنجـاح ✅ 𓆰•**".format(input_str))
    if input_str == "الانلاين":
        update_lock(Ralls_id, "inline", False)
        return await edit_or_reply(event, "**❈╎تـم فتـح** {} **بنجـاح ✅ 𓆰•**".format(input_str))
    if input_str == "الكل":
        update_lock(Ralls_id, "bots", False)
        update_lock(Ralls_id, "location", False)
        update_lock(Ralls_id, "game", False)
        update_lock(Ralls_id, "forward", False)
        update_lock(Ralls_id, "egame", False)
        update_lock(Ralls_id, "rtl", False)
        update_lock(Ralls_id, "url", False)
        update_lock(Ralls_id, "contact", False)
        update_lock(Ralls_id, "location", False)
        update_lock(Ralls_id, "button", False)
        update_lock(Ralls_id, "inline", False)
        update_lock(Ralls_id, "video", False)
        update_lock(Ralls_id, "sticker", False)
        update_lock(Ralls_id, "voice", False)
        return await edit_or_reply(event, "**❈╎تـم فتـح** {} **بنجـاح ✅ 𓆰•**".format(input_str))
    if input_str == "الفارسيه":
        update_lock(Ralls_id, "egame", False)
        return await edit_or_reply(event, "**❈╎تـم فتـح** {} **بنجـاح ✅ 𓆰•**".format(input_str))
    else:
        if input_str:
            return await edit_delete(
                event, f"**❈╎عذراً لايمكن قفل :** `{input_str}`", time=5
            )

        return await edit_or_reply(event, "`❈╎عذراً لايمكنك قفل اي شي هنا 𓆰•`")


@bot.on(admin_cmd(pattern="الحاله$"))
@bot.on(sudo_cmd(pattern="الحاله$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
   # All Rights Reserved for "Repthon - UserBot" "روجــر"
    res = ""
    current_Ralls_locks = get_locks(event.chat_id)
    if not current_Ralls_locks:
        res = "**إعدادات الحمايه في هذه الدردشة**"
    else:
        res = "- فيمـا يلي إعـدادات الحمـاية في هـذه الدردشـة: \n"
        ubots = "❌" if current_Ralls_locks.bots else "✅"
        uegame = "❌" if current_Ralls_locks.egame else "✅"
        urtl = "❌" if current_Ralls_locks.rtl else "✅"
        uforward = "❌" if current_Ralls_locks.forward else "✅"
        ubutton = "❌" if current_Ralls_locks.button else "✅"
        uurl = "❌" if current_Ralls_locks.url else "✅"
        ugame = "❌" if current_Ralls_locks.game else "✅"
        ulocation = "❌" if current_Ralls_locks.location else "✅"
        ubutton = "❌" if current_Ralls_locks.button else "✅"
        uinline = "❌" if current_Ralls_locks.inline else "✅"
        res += f"👉 `البوتات`: `{ubots}`\n"
        res += f"👉 `الدخول`: `{ulocation}`\n"
        res += f"👉 `الاضافه`: `{ucontact}`\n"
        res += f"👉 `التوجيه`: `{uforward}`\n"
        res += f"👉 `الميديا`: `{ugame}`\n"
        res += f"👉 `المعرفات`: `{ubutton}`\n"
        res += f"👉 `الفارسيه`: `{uegame}`\n"
        res += f"👉 `الفشار`: `{urtl}`\n"
        res += f"👉 `الروابط`: `{uurl}`\n"
        res += f"👉 الانلاين: {uinline}\n"
    current_chat = await event.get_chat()
    try:
        chat_per = current_chat.default_banned_rights
    except AttributeError as e:
        logger.info(str(e))
    await edit_or_reply(event, res)

@bot.on(events.MessageEdited())
@bot.on(events.NewMessage())
async def check_incoming_messages(event):
    if not event.is_private:
        chat = await event.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            return
    Rep_dev = (5502537272, 1260465030, 5502537272, 1260465030)
    admin = event.sender_id
    Ralls = await bot.get_permissions(event.chat_id, admin)
    malath = bot.uid
    hhh = event.message.text
    Ralls_id = event.chat_id
    if is_locked(Ralls_id, "rtl") and ("خرا" in hhh or "كسها" in hhh or "كسمك" in hhh or "كسختك" in hhh or "عيري" in hhh or "كسخالتك" in hhh or "خرا بالله" in hhh or "عير بالله" in hhh or "كسخواتكم" in hhh or "اختك" in hhh or "بڪسسخخت" in hhh or "كحاب" in hhh or "مناويج" in hhh or "كحبه" in hhh or " كواد " in hhh or "كواده" in hhh or "تبياته" in hhh or "تبياتة" in hhh or "فرخ" in hhh or "كحبة" in hhh or "فروخ" in hhh or "طيز" in hhh or "آإيري" in hhh or "اختج" in hhh or "سالب" in hhh or "موجب" in hhh or "فحل" in hhh or "كسي" in hhh or "كسك" in hhh or "كسج" in hhh or "مكوم" in hhh or "نيج" in hhh or "نتنايج" in hhh or "مقاطع" in hhh or "ديوث" in hhh or "دياث" in hhh or "اديث" in hhh or "محارم" in hhh or "سكس" in hhh or "مصي" in hhh or "اعرب" in hhh or "أعرب" in hhh or "قحب" in hhh or "قحاب" in hhh or "عراب" in hhh or "مكود" in hhh or "عربك" in hhh or "مخنث" in hhh or "مخنوث" in hhh or "فتال" in hhh or "زاني" in hhh or "زنا" in hhh or "لقيط" in hhh or "بنات شوارع" in hhh or "بنت شوارع" in hhh or "نيك" in hhh or "منيوك" in hhh or "منيوج" in hhh or "نايك" in hhh or "قواد" in hhh or "زب" in hhh or "اير" in hhh or "ممحو" in hhh or "بنت شارع" in hhh or " است " in hhh or "اسات" in hhh or "زوب" in hhh or "عيير" in hhh or "املس" in hhh or "مربرب" in hhh or " خول " in hhh or "عرص" in hhh or "قواد" in hhh or "اهلاتك" in hhh or "جلخ" in hhh or "ورع" in hhh or "شرمو" in hhh or "فرك" in hhh or "رهط" in hhh):
        if admin == malath or Ralls.is_admin or admin in Ralls_dev:
            return
        else:
	        try:
	            await event.delete()
	            await event.reply(
	                "**❈╎! عـذراً**  [عزيـزي⚠️](tg://user?id={})  **يُمنـع الالفـاظ البذيئـه والفشـار فـي هـذه الدردشـة 𓆰•**".format(
	                admin
	                )
	            )
	        except Exception as e:
	            await event.reply(
	                "❈╎عذراً لا املك صلاحيات المشـرف هنا 𓆰• \n`{}`".format(str(e))
	            )
	            update_lock(Ralls_id, "rtl", False)
    if is_locked(Ralls_id, "game") and event.message.media:
        if admin == malath or Ralls.is_admin or admin in Ralls_dev:
            return
        else:
	        try:
	            await event.delete()
	            await event.reply(
	                "**❈╎عـذراً**  [عزيـزي⚠️](tg://user?id={})  **يُمنـع ارسـال الوسائـط لـ هـذه الدردشـة •**\n\n**❈╎تـم تقييدك تلقائيـاً مـن ارسـال الوسائط 🛂**\n**❈╎التـزم الهـدوء .. تستطـيع ارسـال الرسـائل فقـط..**\n\nᯓ 𝗦𝗢𝗨𝗥𝗖𝗘 𝐑𝐀𝐈𝐈𝐒𝗧𝗛𝗢𝗡╎@RallsThon".format(
	                event.sender_id
	                )
	            )
	            await event.client(
	                EditBannedRequest(
	                    event.chat_id, event.sender_id, ANTI_DDDD_RallsTHON_MODE
	                )
	            )
	        except Exception as e:
	            await event.reply(
	                "❈╎عذراً لا املك صلاحيات المشـرف هنا 𓆰• \n`{}`".format(str(e))
	            )
	            update_lock(Ralls_id, "game", False)
    if is_locked(Ralls_id, "forward") and event.fwd_from:
        if admin == malath or Ralls.is_admin or admin in Rep_dev:
            return
        else:
	        try:
	            await event.delete()
	            await event.reply(
	                "**❈╎! عـذراً**  [عزيـزي⚠️](tg://user?id={})  **يُمنـع التوجيـه لهذه المجموعـة 𓆰•**".format(
	                admin
	                )
	            )
	        except Exception as e:
	            await event.reply(
	                "❈╎عذراً لا املك صلاحيات المشـرف هنا 𓆰• \n`{}`".format(str(e))
	            )
	            update_lock(Ralls_id, "forward", False)
    if is_locked(Ralls_id, "button") and "@" in hhh:
        if admin == malath or Ralls.is_admin or admin in Rep_dev:
            return
        else:
	        try:
	            await event.delete()
	            await event.reply(
	                "**❈╎! عـذراً**  [عزيـزي⚠️](tg://user?id={})  **يُمنـع تاك المعـرفات لـ هـذه الدردشـة 𓆰•**".format(
	                admin
	                )
	            )
	        except Exception as e:
	            await event.reply(
	                "❈╎عذراً لا املك صلاحيات المشـرف هنا 𓆰• \n`{}`".format(str(e))
	            )
	            update_lock(Ralls_id, "button", False)
    if is_locked(Ralls_id, "egame") and ("فارسى" in hhh or "خوببی" in hhh or "میخوام" in hhh or "کی" in hhh or "پی" in hhh or "گ" in hhh or "خسته" in hhh or "صكص" in hhh or "راحتی" in hhh or "بیام" in hhh or "بپوشم" in hhh or "گرمه" in hhh or "چ" in hhh or "چه" in hhh or "ڬ" in hhh or "ٺ" in hhh or "چ" in hhh or "ڿ" in hhh or "ڇ" in hhh or "ڀ" in hhh or "ڎ" in hhh or "ݫ" in hhh or "ژ" in hhh or "ڟ" in hhh or "۴" in hhh or "ريسن" in hhh or "دخترا" in hhh or "كسى" in hhh or "مک" in hhh or "خالى" in hhh or "ݜ" in hhh or "ڸ" in hhh or "پ" in hhh or "بند" in hhh or "عزيزم" in hhh or "برادر" in hhh or "باشى" in hhh or "ميخوام" in hhh or "خوبى" in hhh or "ميدم" in hhh or "كى اومدى" in hhh or "خوابيدين" in hhh):
        if admin == malath or Ralls.is_admin or admin in Rep_dev:
            return
        else:
	        try:
	            await event.delete()
	            await event.reply(
	                "**❈╎! عـذراً**  [عزيـزي⚠️](tg://user?id={})  **يُمنـع الكـلام الفـارسـي فـي هـذه الدردشـة 𓆰•**".format(
	                admin
	                )
	            )
	        except Exception as e:
	            await event.reply(
	                "❈╎عذراً لا املك صلاحيات المشـرف هنا 𓆰• \n`{}`".format(str(e))
	            )
	            update_lock(Ralls_id, "egame", False)
    if is_locked(Ralls_id, "url") and "http" in hhh:
        if admin == malath or Ralls.is_admin or admin in Rep_dev:
            return
        else:
	        try:
	            await event.delete()
	            await event.reply(
	                "**❈╎! عـذراً**  [عزيـزي⚠️](tg://user?id={})  **يُمنـع ارسـال الروابـط لهذه المجموعـة 𓆰•**".format(
	                admin
	                )
	            )
	        except Exception as e:
	            await event.reply(
	                "❈╎عذراً لا املك صلاحيات المشـرف هنا 𓆰• \n`{}`".format(str(e))
	            )
	            update_lock(Ralls_id, "url", False)
    if is_locked(Ralls_id, "inline") and event.message.via_bot:
        if admin == malath or Ralls.is_admin or admin in Rep_dev:
            return
        else:
	        try:
	            await event.delete()
	            await event.reply(
	                "**❈╎! عـذراً**  [عزيـزي⚠️](tg://user?id={})  **يُمنـع استخـدام الانلايـن في هذه المجموعـة 𓆰•**".format(
	                admin
	                )
	            )
	        except Exception as e:
	            await event.reply(
	                "❈╎عذراً لا املك صلاحيات المشـرف هنا 𓆰• \n`{}`".format(str(e))
	            )
	            update_lock(Ralls_id, "inline", False)


# Copyright (C) 2022 Repthon
@bot.on(events.ChatAction())
async def _(event):
    if not event.is_private:
        chat = await event.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            return
    # All Rights Reserved for "Repthon - UserBot" "ريبـــثون"
    Rep_dev = (5502537272, 1260465030, 5502537272, 1260465030)
    malath = bot.uid
    if not is_locked(event.chat_id, "contact"):
        return
    if event.user_added:
        admin_by = event.action_message.sender_id
        Ralls = await bot.get_permissions(event.chat_id, admin_by)
        is_ban_able = False
        rights = types.ChatBannedRights(until_date=None, view_messages=True)
        added_users = event.action_message.action.users
        for user_id in added_users:
            user_obj = await event.client.get_entity(user_id)
            if event.user_added:
                is_ban_able = True
                if admin_by == malath or Ralls.is_admin or admin_by in Rep_dev:
                    return
                else:
	                try:
	                    await event.client(
	                        functions.channels.EditBannedRequest(
	                            event.chat_id, user_obj, rights
	                        )
	                    )
	                    await event.reply(
	                        "**❈╎عـذراً**  [عزيـزي⚠️](tg://user?id={})  **يُمنـع اضـافة الاعضـاء لـ هـذه المجموعـة •**\n\n**❈╎تـم حظـر العضـو المضـاف .. بنجـاح 🛂**\n\nᯓ 𝗦𝗢𝗨𝗥𝗖𝗘 𝐑𝐀𝐈𝐈𝐒𝗧𝗛𝗢𝗡╎@RallsThon".format(
	                        admin_by
	                        )
	                    )
	                except Exception as e:
	                    await event.reply(
	                        "❈╎عذراً لا املك صلاحيات المشـرف هنا 𓆰• \n`{}`".format(
	                            str(e)
	                        )
	                    )
	                    update_lock(event.chat_id, "contact", False)
	                    break
        if BOTLOG and is_ban_able:
            ban_reason_msg = await event.reply(
                "❈╎! عذراً [user](tg://user?id={}) لايمكنك اضافة الاعضـاء لهذه الدردشـه 𓆰•".format(
                    admin_by
                )
            )


# Copyright (C) 2022 Repthon
@bot.on(events.ChatAction())
async def _(event):
    if not event.is_private:
        chat = await event.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            return
    # All Rights Reserved for "Rallsthon - UserBot" "الريس"
    Rep_dev = (5502537272, 1260465030, 5502537272, 1260465030)
    if not is_locked(event.chat_id, "location"):
        return
    if event.user_joined: 
        Rallsy = await event.client.get_entity(event.user_id)
        is_ban_able = False
        rights = types.ChatBannedRights(until_date=None, view_messages=True)
        if event.user_joined:
            is_ban_able = True
            if Rallsy.id in Rep_dev:
                return
            else:
	            try:
	                await event.client(
	                        functions.channels.EditBannedRequest(
	                            event.chat_id, Rallsy.id, rights
	                        )
	                    )
	                await event.reply(
	                    "**❈╎عـذراً**  [عزيـزي⚠️](tg://user?id={})  **يُمنـع الانضمـام لـ هـذه المجموعـة •**\n\n**❈╎تـم حظـرك .. بنجـاح 🛂**\n\nᯓ 𝗦𝗢𝗨𝗥𝗖𝗘 𝐑𝐀𝐈𝐈𝐒𝗧𝗛𝗢𝗡╎@RallsThon".format(
	                    Rallsy.id
	                    )
	                )
	            except Exception as e:
	                await event.reply(
	                    "❈╎عذراً لا املك صلاحيات المشـرف هنا 𓆰• \n`{}`".format(
	                        str(e)
	                    )
	                )
	                update_lock(event.chat_id, "location", False)
	                return
        if BOTLOG and is_ban_able:
            ban_reason_msg = await event.reply(
                "❈╎! عذراً [user](tg://user?id={}) لايمكنك الانضمـام لهذه الدردشـه 𓆰•".format(
                    Rallsy.id
                )
            )


# Copyright (C) 2022 Rallsthon
@bot.on(events.ChatAction())
async def _(event):
    if not event.is_private:
        chat = await event.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            return
    # All Rights Reserved for "Rallsthon - UserBot" "الريس"
    Rep_dev = (5502537272, 1260465030, 5502537272, 1260465030)
    malath = bot.uid
    if not is_locked(event.chat_id, "bots"):
        return
    # bots are limited Telegram accounts,
    # and cannot join by themselves
    if event.user_added:
        admin_by = event.action_message.sender_id
        Ralls = await bot.get_permissions(event.chat_id, admin_by)
        is_ban_able = False
        rights = types.ChatBannedRights(until_date=None, view_messages=True)
        added_users = event.action_message.action.users
        for user_id in added_users:
            user_obj = await event.client.get_entity(user_id)
            if user_obj.bot:
                is_ban_able = True
                if admin_by == malath or admin_by in Rep_dev:
                    return
                else:
	                try:
	                    await event.client(
	                        functions.channels.EditBannedRequest(
	                            event.chat_id, user_obj, rights
	                        )
	                    )
	                    await event.reply(
	                        "**❈╎! عـذراً**  [عزيـزي⚠️](tg://user?id={})  **يُمنـع اضـافة البـوتـات لـ هـذه الدردشـة 𓆰•**".format(
	                        admin_by
	                        )
	                    )
	                except Exception as e:
	                    await event.reply(
	                        "❈╎عذراً لا املك صلاحيات المشـرف هنا 𓆰• \n`{}`".format(
	                            str(e)
	                        )
	                    )
	                    update_lock(event.chat_id, "bots", False)
	                    break
        if BOTLOG and is_ban_able:
            ban_reason_msg = await event.reply(
                "❈╎! عذراً [user](tg://user?id={}) لايمكنك اضافة بوتات لهذه الدردشـه 𓆰•".format(
                    admin_by
                )
            )


# Copyright (C) 2022 Repthon
@bot.on(admin_cmd(pattern=f"البوتات ?(.*)"))
@bot.on(sudo_cmd(pattern="البوتات ?(.*)", allow_sudo=True))
async def admin(Ralls):
    con = Ralls.pattern_match.group(1).lower()
    del_u = 0
    del_status = "**❈╎مجمـوعتك/قناتـك في أمـان ✅.. لاتوجـد بوتـات في هذه الدردشـة ༗**"
    if con != "طرد":
        event = await edit_or_reply(Ralls, "**❈╎جـاري البحـث عن بوتات في هـذه الدردشـة ...🝰**")
        async for user in Ralls.client.iter_participants(Ralls.chat_id):
            if user.bot:
                del_u += 1
                await sleep(0.5)
        if del_u > 0:
            del_status = f"🛂**┊كشـف البـوتات -** 𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻\
                           \n\n**❈╎تم العثور على** **{del_u}**  **بـوت**\
                           \n**❈╎لطـرد البوتات استخدم الامـر التالي ⩥** `.البوتات طرد`"
        await event.edit(del_status)
        return
    # All Rights Reserved for "Rallsthon - UserBot" "الريس"
    chat = await Ralls.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_delete(Ralls, "**❈╎عـذراً .. احتـاج الى صلاحيـات المشـرف هنـا**", 5)
        return
    event = await edit_or_reply(Ralls, "**❈╎جـارِ طـرد البوتـات من هنـا ...⅏**")
    del_u = 0
    del_a = 0
    async for user in Ralls.client.iter_participants(Ralls.chat_id):
        if user.bot:
            try:
                await Ralls.client.kick_participant(Ralls.chat_id, user.id)
                await sleep(0.5)
                del_u += 1
            except ChatAdminRequiredError:
                await edit_delete(event, "**❈╎اووبس .. ليس لدي صلاحيـات حظـر هنـا**", 5)
                return
            except UserAdminInvalidError:
                del_a += 1
    if del_u > 0:
        del_status = f"**❈╎تم طـرد  {del_u}  بـوت .. بنجـاح🚮**"
    if del_a > 0:
        del_status = f"❇️**┊طـرد البـوتات -** 𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻\
                           \n\n**❈╎تم طـرد  {del_u}  بـوت بنجـاح** 🚮 \
                           \n**❈╎لـم يتـم طـرد  {del_a}  بـوت لانـها اشـراف ..⅏** \
                           \n\n**❈╎الان لـ الحفـاظ علـى كروبك/قناتك من التصفيـر ارسـل ⩥** `.قفل البوتات`"
    await edit_delete(event, del_status, 50)
    if BOTLOG:
        await Ralls.client.send_message(
            BOTLOG_CHATID,
            f"#طـرد_البوتـات\
            \n ❈╎{del_status}\
            \n ❈╎الدردشه: {Ralls.chat.title}(`{Ralls.chat_id}`)",
        )




CMD_HELP.update(
    {
        "بوت الحمايه": "**اسم الاضافـه : **`بوت الحمايه`\
    \n\n**╮•❐ الامـر ⦂ **`.البوتات` + `.البوتات طرد`\
    \n**الوصـف •• **__**تنظيف مجموعتـك من البوتات .. لمنع التصفير والتفليش والتخريب**_\
    \n\n**╮•❐ الامـر ⦂ **`.قفل البوتات` / `.فتح البوتات`\
    \n**الوصـف •• **__**قفـل البوتـات بالطـرد التلقائـي .. الامر يمنع المشـرفين من اضافـة البوتات .. في حـال اراد احد المشرفين رفـع بوت وتصفير مجموعتك بـ غيابـك.**__\
    \n\n**╮•❐ الامـر ⦂ **`.قفل الاضافه` / `.فتح الاضافه`\
    \n**الوصـف •• **__**قفـل اضافـة الاعضـاء بالطـرد .. مـع تحذيـر صاحـب الاضـافه.**__\
    \n\n**╮•❐ الامـر ⦂ **`.قفل الدخول` / `.فتح الدخول`\
    \n**الوصـف •• **__**قفـل الدخـول بالرابـط بالطـرد التلقائـي .. حيث يقـوم بطـرد المنضم تلقائيـاً .. مـع ارسـال رسـاله تحذيريـه.**__\
    \n\n**╮•❐ الامـر ⦂ **`.قفل الميديا` \ `.فتح الميديا`\
    \n**الوصـف •• **__**قفـل الوسائـط بالمسـح + تقييـد المرسـل من صلاحيـة ارسال الوسائط تلقائيـاً .. مع السمـاح له بارسـال الرسـائل فقـط .. يفيدكـم بـ منـع التفليـش الاباحـي في حال غيابكـم او انشغـالكم .. يسمـح للمشـرفين فقـط بارسـال الوسائـط.**__\
    \n\n**╮•❐ الامـر ⦂ **`.قفل التوجيه` / `.فتح التوجيه`\
    \n**الوصـف •• **__**قفـل التوجيـه بالمسـح التلقائـي .. مـع تحذيـر الشخـص .. يسمـح للمشرفين فقط بالتوجيه.** __\
    \n\n**╮•❐ الامـر ⦂ **`.قفل الفشار` / `.فتح الفشار`\
    \n**الوصـف •• **__**لـ مسـح رسـائل الفشار والسب والتكفير تلقائيـاً .. مـع تحذيـر الشخـص المرسـل.**__\
    \n\n**╮•❐ الامـر ⦂ **`.قفل الفارسيه` / `.فتح الفارسيه`\
    \n**الوصـف •• **__**لـ مسـح رسـائل الايرانيين وبوتات الاعلانات الفارسيه تلقائيـاً.. مـع تحذيـر الشخـص المرسـل.**__\
    \n\n**╮•❐ الامـر ⦂ **`.قفل الروابط` / `.فتح الروابط`\
    \n**الوصـف •• **__**قفـل الروابـط بالمسـح التلقائـي .. مع تحذير الشخص المرسل.**__\
    \n\n**╮•❐ الامـر ⦂ **`.قفل المعرفات` / `.فتح المعرفات`\
    \n**الوصـف •• **__**قفـل المعرفـات بالمسـح التلقائـي .. مع تحذير الشخص المرسل.**__\
    \n\n**╮•❐ الامـر ⦂ **`.قفل الانلاين` / `.فتح الانلاين`\
    \n**الوصـف •• **__**قفـل رسائل الانلايـن والهمسـات بالمسـح التلقائـي .. مع تحذير الشخص .. يسمـح للمشرفين فقـط بارسال الانلايـن.**__\
    \n\n**╮•❐ الامـر ⦂ **`.قفل الكل` / `.فتح الكل`\
    \n**الوصـف •• **__**لـ قفـل او فتـح كـل الاوامـر السابقـه.**__"
    }
)
