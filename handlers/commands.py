from aiogram import Bot, Router, F, types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from shared.config import Config
from database.sql import DataBase
from database.user_info import UserInfo
from shared import tools
from handlers.scheduler_manage import set_new_scheduler
from handlers.admin_panel import show_admin_keyboard

router = Router()


@router.message(Command("start"))
async def cmd_start(msg: Message, bot: Bot):
    db: DataBase = bot.db
    ui = UserInfo(db)
    await ui.init_user_info(msg)  # init user info
    bot.ml.set_lang(ui.get_language())

    start_message = tools.build_start_message(ui, bot.ml)
    await msg.answer(start_message)


@router.message(Command("help"))
async def cmd_start(msg: Message, bot: Bot):
    db: DataBase = bot.db
    ui = UserInfo(db)
    await ui.init_user_info(msg)  # init user info
    lang = ui.get_language()
    bot.ml.set_lang(lang)

    help_msg = tools.build_help_message(ui, bot.ml)
    content = await db.get_all_content()

    builder = ReplyKeyboardBuilder()
    categories_index = {
        "ru": 1, "en": 2, "he": 3
    }
    for co in content:
        if co[categories_index[lang]]:
            builder.add(types.KeyboardButton(text=co[categories_index[lang]]))
    builder.adjust(4)
    await msg.answer(help_msg, reply_markup=builder.as_markup(resize_keyboard=True))


@router.message(Command("profile"))
async def cmd_profile(msg: Message, bot: Bot):
    db: DataBase = bot.db
    ui = UserInfo(db)
    await ui.init_user_info(msg)  # init user info
    bot.ml.set_lang(ui.get_language())

    profile = tools.build_profile_text(ui, bot.ml)
    await msg.answer(profile)


# @router.message(F.text.lower() == "номера телефонов")
# async def call_numbers(message: Message):
#     db: DataBase = message.bot.db
#     ui = UserInfo(db)
#     await ui.init_user_info(message)  # init user info
#     lang = ui.get_language()
#     message.bot.ml.set_lang(lang)
#
#     content = await db.get_content_by_cat(message.text, lang)
#     descr_index = {"ru": 4, "en": 5, "he": 6}
#     link_index = 7
#     msg = f"<b>{message.text}</b>:\n\n"
#     for co in content:
#         if co[descr_index[lang]]:
#             msg += f"{co[descr_index[lang]]} {co[link_index]}"
#     await message.answer(msg)
#

# Attention! This handler should always remain last!
@router.message(F.text)
async def cmd_all_messages(msg: Message, bot: Bot):
    db: DataBase = bot.db
    ui = UserInfo(db)
    await ui.init_user_info(msg)  # init user info
    lang = ui.get_language()
    bot.ml.set_lang(lang)

    if msg.from_user.is_bot or msg.from_user.id != Config.admin_id:
        warning = bot.ml.msg("no_rights").format(ui.get_first_name())
        await msg.answer(warning)
        return False

    cmd = msg.text.lower()
    if cmd.startswith("cmd:sc"):
        await set_new_scheduler(msg.text, msg)
        return True

    if cmd == 'exit:sc':
        await show_admin_keyboard(msg)
        return True

    content = await db.get_content_by_cat(msg.text, lang)
    if len(content):
        descr_index = {"ru": 4, "en": 5, "he": 6}
        link_index = 7
        message = f"<b>{msg.text}</b>:\n\n"
        for co in content:
            if co[descr_index[lang]]:
                message += f"{co[descr_index[lang]]} {co[link_index]}"
        await msg.answer(message)
        return True

    await msg.answer(bot.ml.msg("unknown_cmd"))
