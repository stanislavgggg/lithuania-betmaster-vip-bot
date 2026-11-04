"""User-facing copy (Lithuanian). Admin-side strings stay in English."""

# ---- user side (LT, formal "jūs") ----

WELCOME = (
    "👋 Sveiki, dėkojame už žinutę ir susidomėjimą <b>{vip_name} VIP kanalu</b>.\n\n"
    "<b>Pasirinkite savo šalį:</b>"
)

CHOOSE_REGION = "<b>Pasirinkite savo šalį:</b>"

REGION_SELECTED = (
    "Norėdami <b>NEMOKAMAI</b> prisijungti prie <b>Mūsų Statymai Matas VIP kanalo</b>, "
    "užsiregistruokite pas vieną iš žemiau pateiktų partnerių ir atlikite bent "
    "<b>{min_deposit}</b> įmoką. Už prieigą prie VIP kanalo <b>papildomai mokėti nereikia</b>.\n\n"
    "👇 <b>Pasirinkite partnerį, pas kurį norite užsiregistruoti, ir gaukite "
    "nemokamą VIP prieigą:</b>"
)

BRAND_CARD = (
    "🎰 <b>Bendrovė:</b> {brand}\n\n"
    "💰 <b>Minimali įmoka:</b> {min_deposit}\n"
    "🔗 <b>Nuoroda:</b> <a href=\"{link}\">Registruotis čia</a>\n"
    "{note}"
    "\nUžsiregistruokite per aukščiau pateiktą nuorodą, atlikite bent 40-50€ įmoką "
    "ir čia atsiųskite ekrano nuotrauką, patvirtinančią įmoką."
)

PENDING_HINT = (
    "⏳ Laukiame jūsų <b>{brand}</b> įmokos patvirtinimo. "
    "Atsiųskite ekrano nuotrauką arba įveskite /cancel, jei norite atšaukti."
)

ALL_BRANDS_STARTED = (
    "📋 Atidarytos užklausos: <b>{brands}</b>\n\n"
    "Siųskite ekrano nuotraukas po vieną — kiekvieną priskirsime kitam partneriui eilėje."
)

ALREADY_REQUESTED = (
    "ℹ️ Jau turite atidarytą užklausą dėl <b>{brand}</b>. "
    "Atsiųskite ekrano nuotrauką arba spauskite ❌ Atšaukti užklausas ir pradėkite iš naujo."
)

ALREADY_APPROVED = "✅ <b>{brand}</b> jūsų paskyrai jau patvirtintas."

NO_OPEN_REQUESTS = "Atidarytų užklausų neturite. Pasirinkite šalį žemiau ir pradėkite."

OPEN_REQUESTS_HEADER = "📋 <b>Jūsų užklausos:</b>\n\n"

REQ_WAITING = "laukiama jūsų ekrano nuotraukos"
REQ_REVIEW = "tikrinama"

CANCELLED = "❌ Atšaukta užklausų: {count}."

SCREENSHOT_RECEIVED = (
    "📨 Ekrano nuotrauka dėl <b>{brand}</b> gauta ir išsiųsta patikrinti.\n"
    "Parašysime jums čia, kai tik ją peržiūrėsime."
)

SCREENSHOT_NEXT = "\n\n⏳ Kitas eilėje: <b>{brand}</b>. Atsiųskite tą nuotrauką, kai galėsite."

NO_PENDING_FOR_PHOTO = (
    "Šiuo metu ekrano nuotraukos nelaukiame. Pasirinkite šalį ir partnerį žemiau, "
    "o nuotrauką atsiųskite po įmokos."
)

APPROVED_USER = (
    "✅ <b>Patvirtinta!</b> Jūsų įmoka pas <b>{brand}</b> patvirtinta.\n\n"
    "Štai jūsų asmeninė nuoroda į {vip_name} VIP kanalą (galioja 24 valandas, vienkartinė):\n"
    "{invite}\n\n"
    "Laukiame jūsų kanale! 🎉"
)

APPROVED_USER_UNTIL = (
    "✅ <b>Patvirtinta!</b> Jūsų įmoka pas <b>{brand}</b> patvirtinta.\n\n"
    "Štai jūsų asmeninė nuoroda į {vip_name} VIP kanalą (galioja 24 valandas, vienkartinė):\n"
    "{invite}\n\n"
    "Jūsų prieiga galioja iki <b>{until}</b>."
)

APPROVED_NO_LINK = (
    "✅ <b>Patvirtinta!</b> Jūsų įmoka pas <b>{brand}</b> patvirtinta.\n\n"
    "Nepavyko sukurti nuorodos — administratorius atsiųs ją jums rankiniu būdu."
)

REJECTED_USER = (
    "❌ Jūsų ekrano nuotraukos dėl <b>{brand}</b> nepavyko patvirtinti.\n\n"
    "Patikrinkite, kad nuotraukoje matytųsi įmoka paskyroje, atidarytoje per mūsų nuorodą. "
    "Naują nuotrauką galite atsiųsti įvedę /start.{support}"
)

VIP_EXPIRED = (
    "⌛ Jūsų nemokama prieiga prie {vip_name} VIP kanalo baigėsi.\n\n"
    "Įveskite /start, užsiregistruokite pas kitą partnerį ir atnaujinkite prieigą."
)

SUPPORT_SUFFIX = "\n\nKlausimų? Rašykite @{username}."

RELAYED = (
    "📨 Jūsų žinutė perduota mūsų komandai. "
    "Atsakymą gausite čia, šiame pokalbyje."
)

REGION_GONE = "Ši šalis nebepasiekiama. Pasirinkite kitą:"
BRAND_GONE = "Šis partneris nebepasiekiamas. Pasirinkite kitą:"

ADMIN_ONLY = "This command is for admins only."

# ---- admin side (EN) ----

ADMIN_REQUEST = (
    "🆕 <b>VIP request #{rid}</b>\n\n"
    "👤 {name} (<code>{user_id}</code>) {username}\n"
    "🌍 Country: {region}\n"
    "🎰 Brand: <b>{brand}</b>\n"
    "🔖 Source: {source}\n"
    "🕒 {created}"
)

ADMIN_DECIDED = "\n\n{icon} <b>{status}</b> by {admin} at {when}"

ADMIN_HELP = (
    "<b>Admin panel</b>\n\n"
    "/stats — users, requests, active VIPs\n"
    "/brands — request breakdown per brand\n"
    "/pending — open requests awaiting review\n"
    "/user &lt;id&gt; — look up a user\n"
    "/note &lt;request_id&gt; &lt;text&gt; — message the user about a request\n"
    "/msg &lt;user_id&gt; &lt;text&gt; — message any user by Telegram ID\n"
    "↩️ <b>Reply</b> to a request card or a forwarded user message to chat with that user\n"
    "/grant &lt;user_id&gt; [days] — grant VIP manually\n"
    "/revoke &lt;user_id&gt; — end VIP access and remove from the channel\n"
    "/broadcast &lt;text&gt; — send to all users\n"
    "/reload — reload brands.json without redeploy\n"
    "/id — show this chat's ID"
)
