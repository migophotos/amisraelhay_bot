from shared.config import Config
from database.sql import DataBase


MESSAGES_RU = {
    "hello": "Здравствуйте",
    "your_role": "Ваша роль",
    "your_lang": "Язык общения",
    "your_id": "Ваш код",
    "about_bot": 'Этот бот содержит ссылки на онлайн ресурсы, которые могут быть полезны вам во время войны Израиля против Хамаса',
    "help_text": 'Нажмите на кнопку "Показать категории" внизу экрана или используйте команду /help',
    "lang_text": 'Используйте команду /language для выбора языка общения и отображения иинформации',
    "admin_text": 'Используйте команду /admin для установки времени отправки сообщений и управления сообщениями\n'
                  '- cmd:users отображает список пользователей',
    "bombshelters": 'Карта бомбоубежищ по всей стране',
    "preferred_language": 'Вы выбрали Русский язык, теперь перезапустите бота /start',
    "change_language": 'Выберите Язык Общения',
    "no_rights": '<b>Здравствуйте {0}!</b>\nК сожалению у вас нет прав доступа к этой команде....\n<b>Досвидания!</b>',
    "update_db_msg": '<b>Здравствуйте {0}!</b>\nБаза данных бота обновлена.\nВыполните команду /start для перезапуска бота.',
    "admin_panel": 'Панель администратора',
    "scheduler_manage": 'Планировщик...',
    "content_manage": 'Контент...',
    "start_scheduler": 'Запустить планировщик',
    "restart_scheduler": 'Перезапустить планировщик',
    "stop_scheduler": 'Остановить планировщик',
    "unknown_cmd": 'Неизвестная команда, проверьте синтаксис!',
    "show_categories": 'Показать категории',
    "select_content_type": 'Выберите тип контента',
    "openai": 'Автоматически генерировать с помощью OpenAI',
    "external_csv": 'Внешний CSV-файл',
    "external_json": 'Внешний JSON файл',
    "back_to_admin": 'Вернуться в панель администратора',
    "ru_prompt": 'Обновить Русский промпт',
    "en_prompt": 'Обновить Английский промпт',
    "he_prompt": 'Обновить промпт для Иврита',
    "load_csv_file__prompt": 'Загрузите ваш CSV файл со ссылками в формате:\n'
                             'cat_ru, cat_en, cat_he, descr_ru, descr_en, descr_he, link\n, cat_uk, descr_uk, car_fr, descr_fr'
                             '<b>ваш файл должен содержать название колонок в первой строке!</b>\n',
}

MESSAGES_EN = {
    "hello": "Hello",
    "your_role": "Your role",
    "your_lang": "Your language",
    "your_id": "Your ID",
    "about_bot": "This bot contains links to online resources that may be useful to you during Israel's war against Hamas",
    "help_text": 'Click on the "Show Categories" button at the bottom of the screen or use the /help command',
    "lang_text": 'Use the /language command to select a language for communication and display information.',
    "admin_text": 'Use the /admin command to set the time of sending messages and to manage messages\n'
                  '- cmd:users show active users list',
    "bombshelters": 'Map of air raid shelters across the country',
    "preferred_language": 'You have selected an English language, please restart bot - /start',
    "change_language": 'Select Language of Communication',
    "no_rights": '<b>Hello {0}!</b>\nUnfortunately, you do not have access rights to this command....\n<b>Goodbye!</b>',
    "update_db_msg": "<b>Hello {0}!</b>\nThe bot's database has been updated.\nRun the /start command to restart the bot.",
    "admin_panel": 'Admin Panel',
    "scheduler_manage": 'Scheduler...',
    "content_manage": 'Content...',
    "start_scheduler": 'Start Scheduler',
    "restart_scheduler": 'Restart Scheduler',
    "stop_scheduler": 'Stop Scheduler',
    "unknown_cmd": 'Unknown command, check the syntax!',
    "show_categories": 'Show categories',

    "select_content_type": 'Select content type',
    "openai": 'Automatically generate with OpenAI',
    "external_csv": 'External CSV file',
    "external_json": 'External JSON file',
    "back_to_admin": 'Return to Admin panel',
    "ru_prompt": 'Update Russian Prompt',
    "en_prompt": 'Update English Prompt',
    "he_prompt": 'Update Hebrew Prompt',
    "load_csv_file__prompt": 'Upload your CSV file with links in the following format:\n'
                             'cat_ru, cat_en, cat_he, descr_ru, descr_en, descr_he, link\n, cat_uk, descr_uk, car_fr, descr_fr'
                             '<b>Note: your file must contain the names of the columns in the first line!</b>\n',
}
MESSAGES_FR = {
    "hello": "Bonjour",
    "your_role": "Ton rôle",
    "your_lang": "Votre langue",
    "your_id": "Votre identifiant",
    "about_bot": "Ce bot contient des liens vers des ressources en ligne qui pourraient vous être utiles pendant la guerre d'Israël contre le Hamas.",
    "help_text": """Cliquez sur le bouton "Afficher les catégories" en bas de l'écran ou utilisez la commande /help""",
    "lang_text": 'Utilisez la commande /language pour sélectionner une langue de communication et afficher les informations.',
    "admin_text": """Utilisez la commande /admin pour définir l'heure d'envoi des messages et gérer les messages""",
    "bombshelters": """Carte des abris anti-aériens à travers le pays""",
    "preferred_language": """Vous avez sélectionné une langue anglaise, veuillez redémarrer le bot - /start""",
    "change_language": """Sélectionnez la langue de communication""",
    "no_rights": """<b>Bonjour {0} !</b>\n Malheureusement, vous n'avez pas les droits d'accès à cette commande....\n<b>Au revoir!</b>""",
    "update_db_msg": "<b>Bonjour {0}!</b>\nLa base de données du bot a été mise à jour.\nExécutez la commande /start pour redémarrer le bot.",
    "show_categories": 'Afficher les catégories',
    "admin_panel": 'Admin Panel',
    "scheduler_manage": 'Scheduler...',
    "content_manage": 'Content...',
    "start_scheduler": 'Start Scheduler',
    "restart_scheduler": 'Restart Scheduler',
    "stop_scheduler": 'Stop Scheduler',
    "unknown_cmd": 'Unknown command, check the syntax!',

    "select_content_type": 'Select content type',
    "openai": 'Automatically generate with OpenAI',
    "external_csv": 'External CSV file',
    "external_json": 'External JSON file',
    "back_to_admin": 'Return to Admin panel',
    "ru_prompt": 'Update Russian Prompt',
    "en_prompt": 'Update English Prompt',
    "he_prompt": 'Update Hebrew Prompt',
    "load_csv_file__prompt": 'Upload your CSV file with links in the following format:\n'
                             'cat_ru, cat_en, cat_he, descr_ru, descr_en, descr_he, link\n, cat_uk, descr_uk, car_fr, descr_fr'
                             '<b>Note: your file must contain the names of the columns in the first line!</b>\n',
}

MESSAGES_UK = {
    "hello": "Привіт",
    "your_role": "Ваша роль",
    "your_lang": "Твоя мова",
    "your_id": "Ваше посвідчення особи",
    "about_bot": "Цей бот містить посилання на онлайн-ресурси, які можуть бути корисними під час війни Ізраїлю проти ХАМАС",
    "help_text": 'Натисніть кнопку «Показати категорії» внизу екрана або скористайтеся командою /help',
    "lang_text": 'Використовуйте команду /language, щоб вибрати мову для спілкування та відображення інформації.',
    "admin_text": 'Використовуйте команду /admin, щоб встановити час надсилання повідомлень і керувати повідомленнями',
    "bombshelters": 'Карта бомбосховищ по Ізраїлю',
    "preferred_language": 'Ви вибрали українську мову, перезапустіть бота - /start',
    "change_language": 'Виберіть мову спілкування',
    "no_rights": '<b>Привіт, {0}!</b>\nНа жаль, ви не маєте прав доступу до цієї команди...\n<b>До побачення!</b>',
    "update_db_msg": "<b>Привіт, {0}!</b>\nБазу даних бота оновлено.\nВиконайте команду /start, щоб перезапустити бота.",
    "admin_panel": 'Панель адміністратора',
    "scheduler_manage": 'Планувальник...',
    "content_manage": 'Зміст...',
    "start_scheduler": 'Запустіть планувальник',
    "restart_scheduler": 'Перезапустіть планувальник',
    "stop_scheduler": 'Зупинити планувальник',
    "unknown_cmd": 'Невідома команда, перевірте синтаксис!',
    "show_categories": 'Показати категорії',

    "select_content_type": 'Виберіть тип вмісту',
    "openai": 'Автоматично генерувати за допомогою OpenAI',
    "external_csv": 'Зовнішній файл CSV',
    "external_json": 'Зовнішній файл JSON',
    "back_to_admin": 'Повернутися до панелі адміністратора',
    "ru_prompt": 'Update Russian Prompt',
    "en_prompt": 'Update English Prompt',
    "he_prompt": 'Update Hebrew Prompt',
    "load_csv_file__prompt": 'Завантажте файл CSV із посиланнями в такому форматі:\n'
                             'cat_ru, cat_en, cat_he, descr_ru, descr_en, descr_he, link\n, cat_uk, descr_uk, car_fr, descr_fr'
                             '<b>Примітка: ваш файл повинен містити назви стовпців у першому рядку!</b>\n',

}

MESSAGES_HE = {
    "hello": "שלום",
    "your_role": "התפקיד שלך",
    "your_lang": "שפת התקשורת",
    "your_id": "הקוד שלך",
    "about_bot": 'בוט זה מכיל קישורים למשאבים מקוונים שעשויים להיות שימושיים עבורך במהלך המלחמה של ישראל נגד חמאס',
    "help_text": 'לחץ על הלחצן "הצג קטגוריות" בתחתית המסך או השתמש בפקודה /help',
    "lang_text": 'השתמש בפקודה /language כדי לבחור את שפת התקשורת ולהציג מידע',
    "admin_text": 'השתמש בפקודה /admin כדי להגדיר את שעת שליחת ההודעות ולניהול הודעות',
    "bombshelters": 'מפה של מקלטי תקיפות אוויר ברחבי הארץ',
    "preferred_language": 'בחרת שפה עברית, אנא הפעל מחדש את הבוט - /start',
    "change_language": 'בחר שפת תקשורת',
    "no_rights": '<b>שלום {0}!</b>\nלמרבה הצער, אין לך זכויות גישה לפקודה זו...\n<b>להתראות!</b>',
    "update_db_msg": '<b>שלום {0}!</b>\nמסד הנתונים של הבוט עודכן.\nהפעל את הפקודה /start כדי להפעיל מחדש את הבוט.',
    "admin_panel": 'פאנל ניהול',
    "scheduler_manage": 'מתזמן...',
    "content_manage": 'ניהול תוכן...',
    "start_scheduler": 'התחל את מתזמן',
    "restart_scheduler": 'לחדש מתזמן',
    "stop_scheduler": 'עצור את מתזמן',
    "unknown_cmd": 'פקודה לא ידועה, בדוק את התחביר!',
    "show_categories": 'הצג קטגוריות',
    "select_content_type": 'בחר סוג תוכן',
    "openai": 'הפק באופן אוטומטי עם OpenAI',
    "external_csv": 'קובץ CSV חיצוני',
    "external_json": 'קובץ JSON חיצוני',
    "back_to_admin": 'חזור ללוח הניהול',
    "ru_prompt": 'עדכון הנחיה לרוסית',
    "en_prompt": 'עדכון הנחיה לאנגלית',
    "he_prompt": 'עדכון הנחיה לעברית',
    "load_csv_file__prompt": 'העלה את קובץ ה-CSV שלך עם קישורים בפורמט הבא:\n'
                             'cat_ru, cat_en, cat_he, descr_ru, descr_en, descr_he, link\n, cat_uk, descr_uk, car_fr, descr_fr'
                             'הקובץ שלך חייב (!) להכיל את שמות העמודות בשורה הראשונה!\n',
}


default_languages = MESSAGES_RU


class MultiLang:
    def __init__(self, db: DataBase, lang: str = Config.default_language):
        self.lang = lang
        self.db = db

    def get_lang(self):
        return self.lang

    def set_lang(self, lang):
        self.lang = lang if lang in Config.known_languages else Config.default_language

    def msg(self, msg_id, lang: str = ""):
        lang_selector = self.lang if lang == "" else lang
        if lang_selector == "ru":
            msg_text = MESSAGES_RU.get(msg_id)
        elif lang_selector == "uk":
            msg_text = MESSAGES_UK.get(msg_id)
        elif lang_selector == "fr":
            msg_text = MESSAGES_FR.get(msg_id)
        elif lang_selector == "he":
            msg_text = MESSAGES_HE.get(msg_id)
        else:
            msg_text = MESSAGES_EN.get(msg_id)

        if msg_text is None:
            msg_text = default_languages.get(msg_id)

        return msg_text
