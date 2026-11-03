"""User-facing copy (Lithuanian). Admin-side strings stay in English."""

# ---- user side (LT) ----

WELCOME = (
    "👋 Labas! Ačiū už žinutę ir susidomėjimą <b>{vip_name} grupe</b>.\n\n"
    "<b>Pasirink savo šalį:</b>"
)

CHOOSE_REGION = "<b>Pasirink savo šalį:</b>"

REGION_SELECTED = (
    "Kad prisijungtum prie VIP kanalo <b>NEMOKAMAI</b>, užsiregistruok pas vieną iš "
    "partnerių žemiau ir įnešk bent <b>{min_deposit}</b>. "
    "Taip galėsi sekti ir statyti tuos pačius statymus kartu su manimi. "
    "Už prieigą prie VIP kanalo <b>papildomai mokėti nereikia</b>.\n\n"
    "👇 <b>Pasirink partnerį, pas kurį nori užsiregistruoti, ir gauk "
    "nemokamą VIP prieigą:</b>"
)

BRAND_CARD = (
    "🎰 <b>Partneris:</b> {brand}\n\n"
    "💰 <b>Minimalus įnašas:</b> {min_deposit}\n"
    "🔗 <b>Nuoroda:</b> <a href=\"{link}\">Registruokis čia</a>\n"
    "{note}"
    "\n<b>Instrukcija:</b> užsiregistruok per nuorodą aukščiau, įnešk bent "
    "{min_deposit}, tada atsiųsk čia ekrano nuotrauką kaip patvirtinimą."
)

PENDING_HINT = (
    "⏳ Laukiame tavo ekrano nuotraukos dėl <b>{brand}</b>. "
    "Atsiųsk nuotrauką arba parašyk /cancel, jei nori atšaukti."
)

ALL_BRANDS_STARTED = (
    "📋 Atidarytos užklausos: <b>{brands}</b>\n\n"
    "Siųsk ekrano nuotraukas po vieną — kiekvieną priskirsiu kitam partneriui eilėje."
)

ALREADY_REQUESTED = (
    "ℹ️ Jau turi atidarytą užklausą dėl <b>{brand}</b>. "
    "Atsiųsk ekrano nuotrauką arba spausk ❌ Atšaukti užklausas ir pradėk iš naujo."
)

ALREADY_APPROVED = "✅ <b>{brand}</b> tavo paskyrai jau patvirtintas."

NO_OPEN_REQUESTS = "Atidarytų užklausų neturi. Pasirink šalį žemiau ir pradėk."

OPEN_REQUESTS_HEADER = "📋 <b>Tavo užklausos:</b>\n\n"

REQ_WAITING = "laukia tavo ekrano nuotraukos"
REQ_REVIEW = "tikrinama"

CANCELLED = "❌ Atšaukta užklausų: {count}."

SCREENSHOT_RECEIVED = (
    "📨 Ekrano nuotrauka dėl <b>{brand}</b> gauta ir išsiųsta patikrinti.\n"
    "Parašysime tau čia, kai tik ją peržiūrėsime."
)

SCREENSHOT_NEXT = "\n\n⏳ Kitas eilėje: <b>{brand}</b>. Atsiųsk tą nuotrauką, kai galėsi."

NO_PENDING_FOR_PHOTO = (
    "Šiuo metu ekrano nuotraukos nelaukiu. Pasirink šalį ir partnerį žemiau, "
    "o nuotrauką atsiųsk po įnašo."
)

APPROVED_USER = (
    "✅ <b>Patvirtinta!</b> Tavo įnašas pas <b>{brand}</b> patvirtintas.\n\n"
    "Štai tavo asmeninė nuoroda į {vip_name} (galioja 24 valandas, vienkartinė):\n"
    "{invite}\n\n"
    "Lauksime tavęs grupėje! 🎉"
)

APPROVED_USER_UNTIL = (
    "✅ <b>Patvirtinta!</b> Tavo įnašas pas <b>{brand}</b> patvirtintas.\n\n"
    "Štai tavo asmeninė nuoroda į {vip_name} (galioja 24 valandas, vienkartinė):\n"
    "{invite}\n\n"
    "Tavo prieiga galioja iki <b>{until}</b>."
)

APPROVED_NO_LINK = (
    "✅ <b>Patvirtinta!</b> Tavo įnašas pas <b>{brand}</b> patvirtintas.\n\n"
    "Nepavyko sukurti nuorodos — administratorius atsiųs ją tau rankiniu būdu."
)

REJECTED_USER = (
    "❌ Tavo ekrano nuotraukos dėl <b>{brand}</b> nepavyko patvirtinti.\n\n"
    "Patikrink, kad nuotraukoje matytųsi įnašas paskyroje, atidarytoje per mūsų nuorodą. "
    "Naują nuotrauką gali atsiųsti — tiesiog parašyk /start.{support}"
)

VIP_EXPIRED = (
    "⌛ Tavo nemokama prieiga prie {vip_name} grupės baigėsi.\n\n"
    "Parašyk /start, užsiregistruok pas kitą partnerį ir atnaujink prieigą."
)

SUPPORT_SUFFIX = "\n\nKlausimų? Rašyk @{username}."

RELAYED = (
    "📨 Tavo žinutė perduota mūsų komandai. "
    "Atsakymą gausi čia, šiame pokalbyje."
)

REGION_GONE = "Ši šalis nebepasiekiama. Pasirink kitą:"
BRAND_GONE = "Šis partneris nebepasiekiamas. Pasirink kitą:"

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
