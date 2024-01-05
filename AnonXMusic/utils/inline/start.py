from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["◄𝆺𝅥اـ꯭ـ꯭🥀˹ᴊᴧᴧɴɪ ꭙ ᴍᴜsɪᴄ˼᭄. ⃟⃟⃝⃪⃟⚚‎"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["◄𝆺𝅥اـ꯭ـ꯭🥀𝑺υᴘᴘꪮят✦₲ꪹᴏɾρ᭄. ⃟⃟⃝⃪⃟⚚‎"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["◄𝆺𝅥اـ꯭ـ꯭🥀˹ᴊᴧᴧɴɪ ꭙ ᴍᴜsɪᴄ˼᭄. ⃟⃟⃝⃪⃟⚚‎"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["◄𝆺𝅥اـ꯭ـ꯭🥀𝑯ҽʅᴘ✦ᨶꪮꪑмαиĐ᭄. ⃟⃟⃝⃪⃟⚚‎"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["◄𝆺𝅥اـ꯭ـ꯭🥀⭕ғͦғᷱɪᷡᴄͤ͢ɪᷢᴀʟ᭄. ⃟⃟⃝⃪⃟⚚‎"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["◄𝆺𝅥اـ꯭ـ꯭🥀𝑺υᴘᴘꪮят✦₲ꪹᴏɾρ᭄. ⃟⃟⃝⃪⃟⚚‎"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text=_["◄𝆺𝅥اـ꯭ـ꯭🥀𝑺υᴘᴘꪮят✦₵нαɴɴҽʅ᭄. ⃟⃟⃝⃪⃟⚚‎"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["◄𝆺𝅥اـ꯭ـ꯭🥀𝑵ᴀʜɪ•ɱιʅҽɠα•ƙυ¢н᭄. ⃟⃟⃝⃪⃟⚚‎"], url=f"https://telegra.ph/file/141d5f105f321012aa839.mp4",
            ),
        ],
    ]
    return buttons
