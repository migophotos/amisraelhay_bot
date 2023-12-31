import io
import re

from aiogram import Bot, Router, F, types
from aiogram.enums import ContentType
from aiogram.types import Message, File
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
async def cmd_start(msg: Message):
    db: DataBase = msg.bot.db
    ui = UserInfo(db)
    await ui.init_user_info(msg)  # init user info
    msg.bot.ml.set_lang(ui.get_language())

    start_message = tools.build_start_message(ui, msg.bot.ml)

    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text=msg.bot.ml.msg("show_categories")))
    builder.adjust(1)

    await msg.answer(start_message, reply_markup=builder.as_markup(resize_keyboard=True))


@router.message(Command("help"))
async def cmd_help(msg: Message, edit_message=False):
    db: DataBase = msg.bot.db
    ui = UserInfo(db)
    await ui.init_user_info(msg)  # init user info
    lang = ui.get_language()
    msg.bot.ml.set_lang(lang)

    help_msg = tools.build_help_message(ui, msg.bot.ml)
    content = await db.get_all_content()

    builder = ReplyKeyboardBuilder()
    categories_index = {
        "ru": 0, "en": 1, "he": 2, "uk": 7, "fr": 9
    }
    categories_list = []
    for co in content:
        cat = co[categories_index[lang]]
        if cat:
            if cat in categories_list:
                pass
            else:
                categories_list.append(cat)
                builder.add(types.KeyboardButton(text=co[categories_index[lang]]))
    builder.adjust(2)
    if edit_message:
        await msg.answer("* * * * *", reply_markup=builder.as_markup(resize_keyboard=True))
    else:
        await msg.answer(help_msg, reply_markup=builder.as_markup(resize_keyboard=True))


@router.message(Command("profile"))
async def cmd_profile(msg: Message):
    db: DataBase = msg.bot.db
    ui = UserInfo(db)
    await ui.init_user_info(msg)  # init user info
    msg.bot.ml.set_lang(ui.get_language())

    profile = tools.build_profile_text(ui, msg.bot.ml)
    await msg.answer(profile)


@router.message(F.document)
async def load_document(message: types.Message):
    bot = message.bot
    db: DataBase = bot.db
    ui = UserInfo(db)
    await ui.init_user_info(message)  # init user info
    bot.ml.set_lang(ui.get_language())

    if message.chat.id != Config.admin_id:
        await message.answer(bot.ml.msg("no_rights").format(ui.get_first_name()))
        return False

    if message.content_type == ContentType.DOCUMENT and message.document.mime_type.startswith('text/'):
        doc = message.document
        doc_data = await bot.download(doc)
        doc_data.seek(0)
        cat_list_csv = str(doc_data.read(), encoding='utf-8')
        # print(cat_list_csv)
        cat_list = re.findall(r'.*\n', cat_list_csv)
        cat_list.pop(0)
        await bot.db.delete_content()
        await bot.db.import_from_csv(cat_list)

        await message.answer(f"{len(cat_list)} rows were loaded into the database")
        return True


async def check_admin_rights(message: Message, name: str) -> bool:
    if message.from_user.is_bot or message.from_user.id != Config.admin_id:
        warning = message.bot.ml.msg("no_rights").format(name)
        await message.answer(warning)
        return False
    return True


# Attention! This message handler should always remain last!
@router.message(F.text)
async def cmd_all_messages(msg: Message):
    db: DataBase = msg.bot.db
    ui = UserInfo(db)
    await ui.init_user_info(msg)  # init user info
    lang = ui.get_language()
    msg.bot.ml.set_lang(lang)

    cmd = msg.text.lower()
    if cmd.startswith("cmd:sc"):
        if await check_admin_rights(msg, ui.get_first_name()):
            await set_new_scheduler(msg.text, msg)
            return True

    if cmd == 'exit:sc':
        if await check_admin_rights(msg, ui.get_first_name()):
            await show_admin_keyboard(msg)
            return True

    if cmd == 'cmd:users':
        if await check_admin_rights(msg, ui.get_first_name()):
            data = await db.get_users()
            text = ""
            for key in data:
                text += f'{key[0]}: {key[1]}, lang: {key[2]}\n'
            await msg.answer(text)
            return True

    if msg.text == msg.bot.ml.msg("show_categories"):
        await cmd_help(msg, edit_message=True)
        return True

    content = await db.get_content_by_cat(msg.text, lang)
    if len(content):
        descr_index = {"ru": 3, "en": 4, "he": 5, "uk": 8, "fr": 10}
        link_index = 6
        message = f"<b>{msg.text}</b>:\n\n"
        for co in content:
            if co[descr_index[lang]]:
                # await msg.answer(f"{co[descr_index[lang]]} - {co[link_index]}\n\n", disable_web_page_preview=True)
                message += f"{co[descr_index[lang]]} - {co[link_index]}\n\n"
        await msg.answer(message, disable_web_page_preview=True)
        return True

    await msg.answer(msg.bot.ml.msg("unknown_cmd"))


