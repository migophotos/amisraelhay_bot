from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_bot_name(bot: Bot):
    '''
        Set Name, Short description, Description, and Commands list for the given user language
        "the bot's" name. 0-64 characters,
    '''
    data = [
        (
            'Israel Lives!',
            "en",
        ),
        (
            'Israël vit !',
            "fr",
        ),
        (
            'Израиль жив!',
            "ru",
        ),
        (
            'Живе Ізраїль!',
            "uk",
        ),
        (
            'עם ישראל חי!',
            "he",
        )
    ]
    for name, language in data:
        bot_name = await bot.get_my_name(language_code=language)
        if bot_name and bot_name.name != name:
            await bot.set_my_name(name=name, language_code=language)


async def set_commands(bot: Bot):
    '''
        Set Short description, Description, and Commands list for the given user language
        "the bot's" short description, which is shown on the bot's profile page and is sent together with the link
                    when users share the bot. 0-120 characters.
        "the bot's" description, which is shown in the chat with the bot if the chat is empty. 0-512 characters.
        "A two-letter" ISO 639-1 language code"
        "the list" of the bot's commands
        "the scope" - BotCommandScope JSON-serialized object, describing scope of users for which the commands are relevant
    '''
    data = [
        (
            "Useful links during the war\n\n"
            "Contact the author: https://t.me/MigoPhotos",
            "This bot will help you quickly find the information you need during Israel's war with Hamas",
            "en",
            [
                BotCommand(command='start', description='Start bot'),
                BotCommand(command='help', description='Show help info'),
                BotCommand(command='language', description='Change UI Language'),
                BotCommand(command='profile', description='Show my profile'),
                BotCommand(command='admin', description='Change Settings (for administrator only)')
            ],
            BotCommandScopeDefault(),
        ),
        (
            "Liens utiles pendant la guerre\n\n"
            "Contacter l'auteur : https://t.me/MigoPhotos",
            "Ce bot vous aidera à trouver rapidement les informations dont vous avez besoin pendant la guerre entre Israël et le Hamas",
            "fr",
            [
                BotCommand(command='start', description='Démarrer le bot'),
                BotCommand(command='help', description='Afficher les informations et les catégories'),
                BotCommand(command='language', description="Changer la langue de l'interface utilisateur"),
                BotCommand(command='profile', description='Afficher mon profil'),
                BotCommand(command='admin', description="Modifier les paramètres (pour l'administrateur uniquement)")
            ],
            BotCommandScopeDefault(),
        ),
        (
            "Корисні посилання під час війни\n\n"
            "Зв'язатися з автором: https://t.me/MigoPhotos",
            "Цей бот допоможе вам швидко знайти потрібну інформацію під час війни Ізраїлю з ХАМАС\n\n",
            "uk",
            [
                BotCommand(command='start', description='Запустити бота'),
                BotCommand(command='help', description='Показати інформацію та категорії'),
                BotCommand(command='language', description='Змінити мову інтерфейсу'),
                BotCommand(command='profile', description='Показати мій профіль'),
                BotCommand(command='admin', description='Змінити налаштування (лише для адміністратора)')
            ],
            BotCommandScopeDefault(),
        ),
        (
            "Полезные ссылки на время войны\n\n"
            "Связаться с автором: https://t.me/MigoPhotos",
            "Этот бот поможет вам быстро найти нужную информацию во время войны Израиля с ХАМАС\n\n",
            "ru",
            [
                BotCommand(command='start', description='Запуск бота'),
                BotCommand(command='help', description='Помощь'),
                BotCommand(command='language', description='Смена языка'),
                BotCommand(command='profile', description='Показать профиль'),
                BotCommand(command='admin', description='Изменить настройки (только для администратора)')
            ],
            BotCommandScopeDefault(),
        ),
        (
            "קישורים שימושיים במהלך המלחמה\n\n"
            "צור קשר עם המחבר: https://t.me/MigoPhotos",
            "הבוט הזה יעזור לך למצוא במהירות את המידע שאתה צריך במהלך המלחמה של ישראל בחמאס",
            "he",
            [
                BotCommand(command='start', description='התחל בוט'),
                BotCommand(command='help', description='הצג מידע עזרה'),
                BotCommand(command='language', description='שנה שפת ממשק משתמש'),
                BotCommand(command='profile', description='הצג את הפרופיל שלי'),
                BotCommand(command='admin', description='שנה הגדרות (למנהל בלבד)')
            ],
            BotCommandScopeDefault(),
        )
    ]
    for short_descr, description, language, commands_list, commands_scope in data:
        await bot.set_my_short_description(short_description=short_descr, language_code=language)
        await bot.set_my_description(description=description, language_code=language)
        await bot.set_my_commands(commands=commands_list, scope=commands_scope, language_code=language)


