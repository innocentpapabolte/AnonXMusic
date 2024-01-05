from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_[˹ᴊᴧᴧɴɪ ꭙ ᴍᴜsɪᴄ˼], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_[˹𝑺υᴘᴘꪮят•₲ꪹᴏɾρ˼], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_[˹ᴊᴧᴧɴɪ ꭙ ᴍᴜsɪᴄ˼],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_[˹𝑯ҽʅᴘ•ᨶꪮꪑмαиĐ˼], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_[˹⭕ғͦғᷱɪᷡᴄͤ͢ɪᷢᴀʟ˼], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_[˼𝑺υᴘᴘꪮят•₲ꪹᴏɾρ˼], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text=_[w˹𝑺υᴘᴘꪮят•₵нαɴɴҽʅ˼], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_[˹𝑵ᴀʜɪ•ɱιʅҽɠα•ƙυ¢н˼], url=f"https://telegra.ph/file/141d5f105f321012aa839.mp4",
            ),
        ],
    ]
    return buttons
