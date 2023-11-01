from dataclasses import dataclass
import private.tokens as SECRET


@dataclass
class Config:
    bot_token: str = SECRET.CLIENT_BOT_TOKEN
    bot_name: str = "AmIsraelHay"
    db_path: str = './database/amisraelhay_bot.db'
    admin_id: int = 565542529

    bombshelters_link = "https://www.google.com/maps/d/edit?mid=1-moD7zpSwpSFLVzdoODYrhnBLq--m2I"

    known_languages = ("ru", "en", "he")
    channels_list = {
    }

    #                month, day, day of week, hour, minute, jitter (+- seconds)
    def_scheduler = ("", "*", "", "10", "", "")


