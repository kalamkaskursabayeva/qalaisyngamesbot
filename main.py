from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
from telegram.ext import ConversationHandler

ASKING = 1
questions = [
    "Какая самая неловкая ситуация произошла с тобой при незнакомцах?",
    "Какой запах вызывает у тебя ностальгию? Почему именно он?",
    "На какие рискованные поступки (по типу прыжка с парашютом) ты бы решился? Откуда у тебя появилось желание попробовать это?",
    "О чём ты мечтал(а) в детстве и почему это было важно?",
    "Что в тебе ценят твои друзья, по твоему мнению?",
    "Какой фильм или книга когда-то сильно повлияли на тебя?",
    "Какое своё качество ты любишь больше всего?",
    "Если бы ты мог(ла) вернуться в одно событие своей жизни и прожить его ещё раз, что бы это было?",
    "Что ты понял(а) о себе за последний год?",
    "Кто оказал на тебя большое влияние и почему?",
    "Какой самый большой комплимент ты получал(а)?",
    "Какие привычки из детства до сих пор с тобой?",
    "О чём тебе не хватает смелости рассказать близким?",
    "Чего ты стыдишься, но это часть твоей истории?",
    "Какое воспоминание заставляет тебя улыбаться каждый раз, когда ты его вспоминаешь?",
    "Что для тебя значит «доверие»?",
    "С чем тебе было сложно справиться в этом году?",
    "Когда ты чувствовал(а) себя по-настоящему живым/живой?",
    "Какое твое достижение не оценили, но ты гордишься им?",
    "Что ты хотел(а) бы услышать от любимого человека?",
    "В какой момент ты чувствовал(а) поддержку и запомнил(а) это на всю жизнь?",
    "Какие слова тебе запомнились от родителей больше всего?",
    "Какой твой страх кажется тебе сейчас нелепым?",
    "Когда ты в последний раз плакал(а)? Почему?",
    "Что для тебя значит «быть настоящим»?",
    "Что ты никогда никому не говорил(а), но сейчас готов(а)?",
    "Какие три слова тебя точно описывают?",
    "Какие слова ты хотел(а) бы чаще слышать от других?",
    "Когда ты в последний раз чувствовал(а) себя неуверенно?",
    "Что в себе ты научился(ась) принимать не сразу?",
    "Какую часть себя ты прячешь от мира?",
    "Какая твоя черта отталкивает людей, но ты не хочешь её менять?",
    "Какой вопрос ты хотел(а) бы, чтобы тебе задали, но тебе его никогда не задавали?",
    "С кем бы ты хотел(а) провести один день из прошлого?",
    "Какой момент в своей жизни ты хочешь забыть?",
    "Чего тебе не хватает прямо сейчас?",
    "О чём ты часто молчишь?",
    "Что для тебя «дом»?",
    "Когда ты в последний раз испытывал(а) благодарность?",
    "Какие свои чувства тебе сложно выражать?",
    "Что бы ты изменил(а) в своей истории, если бы мог(ла)?",
    "Что бы ты хотел(а) подарить себе в будущем?",
    "О чём ты жалеешь?",
    "Что тебя наполняет энергией?",
    "Когда ты чувствуешь любовь?",
    "Как ты проявляешь любовь к другим?",
    "Что тебе помогает возвращаться к себе?",
    "Что ты хотел(а) бы сказать себе в трудный момент?",
    "Чего ты хочешь на самом деле, но боишься признаться?",
    "Какая часть жизни кажется тебе недожитой?",
    "Какую часть себя ты хотел(а) бы показать миру, но не решаешься?",
    "О чём ты хочешь говорить чаще?",
    "Когда ты чувствуешь вдохновение?",
    "Что бы ты хотел(а) отпустить?",
    "Когда ты чувствуешь свободу?",
    "Что для тебя значит быть сильным?",
    "Какие мечты ты давно откладываешь?",
    "Когда ты в последний раз чувствовал(а) счастье?",
    "Что делает тебя по-настоящему живым/живой?",
    "Что ты готов(а) начать сначала?",
    "Как бы ты хотел(а) быть запомненным(ой)?",
    "Какие слова ты сказал(а) бы себе, глядя в зеркало?",
    "Какой совет ты дал(а) бы себе 10 лет назад?",
    "Чем ты гордишься больше всего?",
    "Какие моменты тебе хочется запомнить навсегда?",
    "Когда ты в последний раз смеялся(ась) до слёз?",
    "Что ты любишь делать, когда остаёшься наедине с собой?",
    "Что тебе помогает справляться с трудностями?",
    "Что ты понял(а) о жизни, когда потерял(а) что-то важное?",
    "Кого тебе не хватает?",
    "Что для тебя значит прощение?",
    "Что бы ты хотел(а) сказать своим родителям, но не говоришь?",
    "Чем ты хочешь поделиться прямо сейчас?",
    "Когда ты чувствовал(а), что ты — на своём месте?",
    "Какие моменты в жизни ты считаешь волшебными?",
    "Что ты по-настоящему ценишь в себе?",
    "Что ты хотел(а) бы передать будущему поколению?",
    "Как ты понимаешь, что тебе нужно перезагрузиться?",
    "Какой твой самый тёплый спонтанный момент?",
    "Что бы ты хотел(а) отпраздновать, но пока не решаешься?",
    "Когда ты чувствуешь себя собой?",
    "Какое чувство для тебя самое трудное?",
    "С каким вопросом ты бы хотел(а) остаться сегодня?",
]


async def play_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["question_index"] = 0
    text = f"1⃣ Вопрос\n💬 {questions[0]}"
    keyboard = [
        [InlineKeyboardButton("➡️ Далее", callback_data="next_question")],
        [InlineKeyboardButton("🔙 Назад", callback_data="prev_question")],
    ]
    await update.callback_query.message.edit_text(
        text=text, reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def next_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    index = context.user_data.get("question_index", 0) + 1

    if index >= len(questions):
        await query.edit_message_text("✨ Все вопросы закончились. Спасибо за игру!")
        return

    context.user_data["question_index"] = index
    text = f"💬 {questions[index]}"
    keyboard = [
        [InlineKeyboardButton("➡️ Далее", callback_data="next_question")],
        [InlineKeyboardButton("🔙 Назад", callback_data="prev_question")],
    ]
    await query.edit_message_text(
        text=text, reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def prev_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    index = context.user_data.get("question_index", 0) - 1
    if index < 0:
        index = 0  # не уходим за пределы
        text = f"1⃣ Вопрос\n💬 {questions[index]}"
    else:
        text = f"💬 {questions[index]}"

    context.user_data["question_index"] = index

    keyboard = [
        [InlineKeyboardButton("➡️ Далее", callback_data="next_question")],
        [InlineKeyboardButton("🔙 Назад", callback_data="prev_question")],
    ]
    await query.edit_message_text(
        text=text, reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def back_to_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)


# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🎉 Поздравляем с покупкой игры!\n"
        "🥰 Верим, что вы отлично провели время играя в игру!\n\n"
        "Сейчас у вас в руках — ДОПОЛНЕНИЕ! Или наш способ сказать вам спасибо еще раз :)\n\n"
        "Внутри дополнения:\n"
        "🔹 300+ отобранных вопросов на сближение\n"
        "🔹 Три раздела: Прошлое, Настоящее и Будущее\n"
        "🔹 Действия, которые помогут разрядить и еще больше проникнуться в атмосферу игры!\n\n"
        "💬 Играть в дополнение нужно после прохождения физической карточной игры!"
    )

    keyboard = [
        [
            InlineKeyboardButton(
                "🎁 Получить персональную скидку -15% ", callback_data="discount"
            )
        ],
        [
            InlineKeyboardButton(
                "🃏 Приступить к игре в Дополнение", callback_data="play_soon"
            )
        ],
        [InlineKeyboardButton("💬 Связаться с Тех.поддержкой", callback_data="support")],
        [InlineKeyboardButton("📰 Новости Qalaisyn Games", callback_data="news")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        await update.message.reply_text(text=text, reply_markup=reply_markup)
    elif update.callback_query:
        await update.callback_query.edit_message_text(
            text=text, reply_markup=reply_markup
        )


# Обработка кнопок
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "discount":
        text = (
            "🎁 У нас сейчас в наличии 4 вида игр и 2 книги.\n"
            "Подскажите, на какой продукт вы хотели бы получить скидку лояльного клиента?"
        )

        keyboard = [
            [
                InlineKeyboardButton(
                    "🃏 Игра для друзей «Укрепление связей»",
                    callback_data="friends_game",
                )
            ],
            [
                InlineKeyboardButton(
                    "🧡 Игра для пар «Первая связь»", callback_data="couples_game"
                )
            ],[InlineKeyboardButton("🩵 Связь с Собой", callback_data="self_connection")],

            [InlineKeyboardButton("🩵 Өзімен байланыс", callback_data="self_game")],
            [
                InlineKeyboardButton(
                    "📘 Книга «Мама, как это было?»", callback_data="mom_book"
                )
            ],
            [
                InlineKeyboardButton(
                    "📙 Книга «Папа, как это было?»", callback_data="dad_book"
                )
            ],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=text, reply_markup=reply_markup)

    elif query.data == "friends_game":
        text = (
            "💛 Укрепление связей — уникальная игра, которая подходит для друзей, пар, семьи, коллег, а также на любые праздники 🎉\n\n"
            "Состоит из 3 уровней, которые постепенно выведут ваши отношения на новый уровень общения 🤍\n\n"
            "Игра также является прекрасным подарком! ❤️\n\n"
            "⬇️ Смотрите видео обзор продукта:\n"
            "https://www.instagram.com/p/CpDX0zTjv0C/"
        )
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛍️ Я посмотрел(а) обзор, хочу получить скидку",
                        callback_data="watched",
                    )
                ],
                [InlineKeyboardButton("🔙 Назад", callback_data="discount")],
            ]
        )
        await query.edit_message_text(text=text, reply_markup=reply_markup)

    elif query.data == "couples_game":
        text = (
            "❤️ Первая связь — романтическая игра, подходящая для пар.\n\n"
            "Состоит из 4 уровней (начнем?, прошлое, настоящее, будущее), "
            "в каждом блоке вы сможете обсудить беспокоящие вас вопросы, а также прийти к их решению через диалог 🩵\n\n"
            "Даря эту игру, вы показываете партнёру, что ваши отношения значимы вам!\n\n"
            "⬇️ Смотрите видео обзор продукта:\n"
            "https://www.instagram.com/p/CpNOEKoD2ZK/"
        )
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛍️ Я посмотрел(а) обзор, хочу получить скидку",
                        callback_data="watched",
                    )
                ],
                [InlineKeyboardButton("🔙 Назад", callback_data="discount")],
            ]
        )
        await query.edit_message_text(text=text, reply_markup=reply_markup)
    elif query.data == "self_connection":
        text = (
            "🩵 Связь с Собой  - это игра-саморефлексия, созданная совместно с психологом, для игры одной/одному.\n\n"
        "❔В игре 130+ вопросов и практик, которые помогут вам обрести внутренний покой и уверенность в себе! \n\n"
        "🫂Игра для тех, кто:\n"
        "Ищет себя, работает над уверенностью/самоценностью, хочет перестать критиковать себя и желает принять себя полностью! "
        "Для тех, кто готов к трансформации 🩵"
            "https://www.instagram.com/p/C8rbgO-IWtC/"
        )
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛍️ Я посмотрел(а) обзор, хочу получить скидку",
                        callback_data="watched",
                    )
                ],
                [InlineKeyboardButton("🔙 Назад", callback_data="discount")],
            ]
        )
        await query.edit_message_text(text=text, reply_markup=reply_markup)
    elif query.data == "self_game":
        text = (
            "🩵 Өзімен байланыс — бұл психологпен бірге бір/бір ойнау үшін жасалған өзін-өзі көрсету ойыны.\n\n"
            "❔ Ойында 130-дан астам сұрақтар мен тәжірибелер бар, олар сізге ішкі тыныштық пен сенімділікті табуға көмектеседі!\n\n"
            "🫂 Ойын кім үшін:\n"
            "Өзін іздейді, сенімділік/өзін-өзі бағалау бойынша жұмыс істейді, өзін сынауды тоқтатқысы келеді және өзін толығымен қабылдағысы келеді!\n"
            "Трансформацияға дайын адамдар үшін 🩵\n\n"
            "Қазақша, орысша нұсқасы бар\n"
            "Өнімнің бейне шолуын қараңыз ⬇️\n"
            "https://www.instagram.com/reel/C9HvTobseMB/"
        )
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛍️ Я посмотрел(а) обзор, хочу получить скидку",
                        callback_data="watched",
                    )
                ],
                [InlineKeyboardButton("🔙 Назад", callback_data="discount")],
            ]
        )
        await query.edit_message_text(text=text, reply_markup=reply_markup)

    elif query.data == "mom_book":
        text = (
            "🫂 «Мама, как это было?» — дневник воспоминаний, который сохранит самые важные моменты и истории из жизни вашей мамы.\n"
            "Книга хранит воспоминания лучше, чем мы, ведь они остаются навсегда ♾️\n\n"
            "📖 Что внутри?\n"
            "✔️ 14 разделов и 320+ глубоких вопросов, где вы узнаете всё о маме, начиная с её детства\n"
            "✔️ Раздел «Настоящее время» — узнаете, о чём мечтает мама сейчас 💭\n"
            "✔️ Место для фотографий важных моментов\n\n"
            "Это не просто 🎁 , а возможность провести тёплое время вместе\n\n"
            "⬇️ Смотрите видео обзор продукта:\n"
            "https://www.instagram.com/p/DHTV9NRtYGT/"
        )
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛍️ Я посмотрел(а) обзор, хочу получить скидку",
                        callback_data="watched",
                    )
                ],
                [InlineKeyboardButton("🔙 Назад", callback_data="discount")],
            ]
        )
        await query.edit_message_text(text=text, reply_markup=reply_markup)

    elif query.data == "dad_book":
        text = (
            "📙 «Папа, как это было?» ❤️ — это уникальный шанс услышать истории отца, узнать о его трудностях и как он всё преодолевал.\n\n"
            "О первых ошибках на работе, сложностях в жизни и о светлых моментах, о первых свиданиях с вашей мамой 🫶🏻\n\n"
            "🖤 320+ вопросов и 14 разделов о жизни папы\n"
            "🖤 десятки душевных вечеров вместе\n"
            "🖤 сохраните память о папе — для ваших внуков 🫶🏻\n\n"
            "Это не просто книга — это знак внимания о том, что Папа вам важен 💔\n\n"
            "⬇️ Смотрите видео обзор продукта:\n"
            "https://www.instagram.com/p/DK2REPBo5S7/"
        )
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛍️ Я посмотрел(а) обзор, хочу получить скидку",
                        callback_data="watched",
                    )
                ],
                [InlineKeyboardButton("🔙 Назад", callback_data="discount")],
            ]
        )
        await query.edit_message_text(text=text, reply_markup=reply_markup)

    elif query.data == "watched":
        text = (
            "Спасибо! 🛍️\n"
            "Напишите нам в Instagram и отправьте скрин с этим сообщением, чтобы получить персональную скидку!\n\n"
            "👇 Нажмите на кнопку ниже, чтобы открыть чат:"
        )
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔗 Написать в Instagram", url="https://ig.me/m/qalaisyn.games"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔙 Вернуться в начало", callback_data="back_to_start"
                    )
                ],
            ]
        )
        await query.edit_message_text(
            text=text, reply_markup=reply_markup
        )  # <--- этого не хватает

    elif query.data == "support":
        text = (
            "💬 Свяжитесь с нашей командой поддержки — мы с радостью поможем!\n\n"
            "👇 Нажмите на кнопку ниже, чтобы написать нам в WhatsApp:"
        )
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔗 Написать в WhatsApp", url="https://wa.me/77755007264"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔙 Назад",
                         callback_data="back_to_start",
                    )
                ],
            ]
        )
        await query.edit_message_text(text=text, reply_markup=reply_markup)

    elif query.data == "news":
        text = (
            "📰 Все новости, отзывы и анонсы наших новых продуктов — в социальных сетях!\n\n"
            "Подпишись, чтобы не пропустить!\n"
            "(Эксклюзивные предложения публикуем только в сториз)"
        )
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔗 Перейти в Instagram",
                        url="https://www.instagram.com/qalaisyn.games/",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔙 Назад",
                         callback_data="back_to_start",
                    )
                ],
            ]
        )
        await query.edit_message_text(text=text, reply_markup=reply_markup)

    elif query.data == "play_soon":
        await play_game(update, context)

    elif query.data == "next_question":
        await next_question(update, context)

    elif query.data == "prev_question":
        await prev_question(update, context)

    elif query.data == "back_to_start":
        await back_to_start(update, context)


# Запуск приложения
app = (
    ApplicationBuilder().token("7638033518:AAECvpZhCyRSqetmJbqE8jWHqkjbGHYwOYo").build()
)
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))


app.run_polling()




app.run_polling()
