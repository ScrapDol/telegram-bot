import asyncio
import json
from datetime import datetime

from keyboards import reply

from aiogram import Bot, Dispatcher, types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import (
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram import F

BOT_TOKEN = "6034449668:AAESbVaUdZvhA1gvHbxzEbs8Sge4ih37Oj8"
# ADMINS = [1996601646]
ADMINS = [1996601646, 794115978]
QUESTIONNAIRE_FILE = "questionnaire.json"
ANSWERS_FILE = "answers.json"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def is_admin(admin_id):
    if admin_id not in ADMINS:
        return False

    return True


def load_questionnaire():
    try:
        with open(QUESTIONNAIRE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_questionnaire(questionnaire):
    with open(QUESTIONNAIRE_FILE, "w", encoding="utf-8") as f:
        json.dump(questionnaire, f, indent=2, ensure_ascii=False)


def load_answers():
    try:
        with open(ANSWERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_answers(answers):
    with open(ANSWERS_FILE, "w", encoding="utf-8") as f:
        json.dump(answers, f, indent=2, ensure_ascii=False)


class Questionnaire(StatesGroup):
    answering = State()


class AdminActions(StatesGroup):
    adding_question = State()
    adding_options = State()
    editing_question = State()
    editing_options = State()


async def create_keyboard(buttons, row_width=2):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            buttons[i : i + row_width] for i in range(0, len(buttons), row_width)
        ]
    )


@dp.message(Command("start"))
async def cmd_start(message: types.Message):

    main_kb = ReplyKeyboardMarkup(keyboard=[])

    if is_admin(message.from_user.id):
        main_kb = reply.create_admin_keyboard()
        await message.answer(
            "Приветствую! С моей помощью вы можете подать заявку на вакансию оператора OnlyFans.",
            reply_markup=main_kb,
        )
    else:
        await message.answer(
            "Привет! Я - Lewd Bot.\n\n"
            "Если ты ищешь новую работу удаленного формата, еженедельной оплатой в долларах, то у меня есть что-то интересное для тебя.\n\n"
            "Моя задача - познакомить тебя с профессией секстера(оператора чата, чаттера) на платформе OnlyFans с агентством Lewd Media.\n\n"
            "Это отличная возможность для тех, кто хочет работать из любой точки мира и получать хороший доход.",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton(text="Далее", callback_data="next_1")]
                ]
            ),
        )


# ----------------- Страшный код


@dp.callback_query(F.data == "next_1")
async def process_callback_next(callback: types.CallbackQuery):
    message = callback.message

    await message.edit_reply_markup(
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="🟢 Далее", callback_data="next_1")]
            ]
        ),
    )

    await message.answer(
        "Давай начнем с знакомства с профессией секстера. Я объясню тебе, что это за работа и чем она особенная.",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Что такое секстинг?", callback_data="next_2"
                    )
                ]
            ]
        ),
    )


@dp.callback_query(F.data == "next_2")
async def process_callback_next(callback: types.CallbackQuery):
    message = callback.message

    await message.edit_reply_markup(
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="🟢 Что такое секстинг?", callback_data="next_1"
                    )
                ]
            ]
        ),
    )

    await message.answer(
        'Термин "секстинг" произошел от английского слова "sexting", которое объединяет "sex" и "texting". Изначально секстинг ограничивался только текстовыми сообщениями.\n\n'
        "В современный период цифровизации, секстинг развился и стал включать не только текст, но и эмодзи, мемы, видео и интимные фотографии.\n\n"
        "Раньше, когда люди обменивались полароидными фото, распространение контента сексуального характера считалось необычным. Однако сегодня, по последним исследованиям, около 48% людей делятся интимными фото, видео и сообщениями в сети, и это даже укрепляет отношения.",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Кто такой секстер?", callback_data="next_3"
                    )
                ]
            ]
        ),
    )


@dp.callback_query(F.data == "next_3")
async def process_callback_next(callback: types.CallbackQuery):
    message = callback.message

    await message.edit_reply_markup(
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="🟢 Кто такой секстер?", callback_data="next_1"
                    )
                ]
            ]
        ),
    )

    await message.answer(
        "Секстер ( также оператор чата, чаттер ) – это специалист по продажам в индустрии онлайн-развлечений. Его задача – строить и поддерживать отношения с фанатами модели, подогревая их интерес и продавая контент или услуги модели, при этом выступая от её имени.",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Что делает секстер?", callback_data="next_4"
                    )
                ]
            ]
        ),
    )


@dp.callback_query(F.data == "next_4")
async def process_callback_next(callback: types.CallbackQuery):
    message = callback.message

    await message.edit_reply_markup(
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="🟢 Что делает секстер?", callback_data="next_1"
                    )
                ]
            ]
        ),
    )

    await message.answer(
        "Ежедневное общение: Секстер регулярно взаимодействует с клиентами через профили моделей на платформах, таких как OnlyFans (OF).\n\n"
        "Выполнение продаж: Он обязан выполнять установленные квоты продаж, увеличивая доходы профиля.\n\n"
        "Следование правилам: Секстер действует в соответствии с нормами и правилами, указанными в обучающих материалах агентства, а также следует указаниям администратора.",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Зачем нужны секстеры?", callback_data="next_5"
                    )
                ]
            ]
        ),
    )


@dp.callback_query(F.data == "next_5")
async def process_callback_next(callback: types.CallbackQuery):
    message = callback.message

    await message.edit_reply_markup(
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="🟢 Зачем нужны секстеры?", callback_data="next_1"
                    )
                ]
            ]
        ),
    )

    await message.answer(
        "Усиление Продаж: Секстеры играют ключевую роль в увеличении продаж контента модели, используя стратегии маркетинга и общения.\n\n"
        "Управление Временем: Они позволяют моделям освободить время для создания контента, беря на себя задачи коммуникации и продаж.",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Cколько зарабатывают секстеры?", callback_data="next_6"
                    )
                ]
            ]
        ),
    )


@dp.callback_query(F.data == "next_6")
async def process_callback_next(callback: types.CallbackQuery):
    message = callback.message

    await message.edit_reply_markup(
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="🟢 Cколько зарабатывают секстеры?", callback_data="next_1"
                    )
                ]
            ]
        ),
    )

    await message.answer(
        "Заработок секстеров зависит от нескольких факторов, таких как количество и качество продаж.\n\n"
        "К примеру, в нашей команде  заработок секстеров варьируется от 100 до 500 долларов в среднем каждую неделю.",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Нажми на меня", callback_data="next_7")]
            ]
        ),
    )


@dp.callback_query(F.data == "next_7")
async def process_callback_next(callback: types.CallbackQuery):
    message = callback.message

    await message.edit_reply_markup(
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="🟢 Нажми на меня", callback_data="next_1")]
            ]
        ),
    )

    await message.answer(
        "Итак, я рассказал тебе о професии секстера и познакомил тебя с нашей чудесной организацией. Надеюсь тебе был интересен мой рассказ.\n\n"
        "Теперь я должен задать тебе вопрос. Хочешь ли ты рабоать с нами и стать частью нашей семьи ?\n\n"
        'Если ты выберешь "Да", то я расскажу тебе про условия и правила нашего агентства. Если же ты выберешь "Нет", на этом наш разговор закончится.',
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Да", callback_data="next_yes"),
                    InlineKeyboardButton(text="Нет", callback_data="next_no"),
                ]
            ]
        ),
    )


@dp.callback_query(F.data == "next_yes")
async def process_callback_next(callback: types.CallbackQuery):
    main_kb = reply.create_main_keyboard()

    message = callback.message

    await message.answer(
        "Приветствую, с моей помощью вы можете подать заявку на вакансию оператора OnlyFans.",
        reply_markup=main_kb,
    )


# ----------------- Конец стращного кода


@dp.message(F.text == "Подать заявку")
async def start_questionnaire(message: types.Message, state: FSMContext):
    questionnaire = load_questionnaire()

    user = message.from_user

    await state.update_data(
        question_index=0,
        answers={},
        user_id=user.id,
        username=user.username,
        full_name=user.full_name,
    )

    if not questionnaire:
        await message.answer("Извините, анкета сейчас недоступна.")
        return

    await state.update_data(question_index=0)
    await ask_question(message, state)
    await state.set_state(Questionnaire.answering)


async def ask_question(message: types.Message, state: FSMContext):
    data = await state.get_data()
    question_index = data.get("question_index", 0)
    questionnaire = load_questionnaire()

    if question_index < len(questionnaire):
        question = questionnaire[question_index]
        if question["type"] == "button":
            keyboard = await create_keyboard(
                [
                    InlineKeyboardButton(text=option, callback_data=f"answer_{option}")
                    for option in question["options"]
                ]
            )
            await message.answer(question["text"], reply_markup=keyboard)
        else:
            await message.answer(question["text"])
    else:
        await save_and_notify(message, state)


async def save_and_notify(message: types.Message, state: FSMContext):
    data = await state.get_data()

    answers = data.get("answers", {})
    user_id = data.get("user_id")
    username = data.get("username")
    full_name = data.get("full_name")

    user_info = {
        "id": user_id,
        "username": username,
        "full_name": full_name,
    }

    timestamp = datetime.now().isoformat()

    completed_questionnaire = {
        "user_id": user_info["id"],
        "username": user_info["username"],
        "full_name": user_info["full_name"],
        "timestamp": timestamp,
        "answers": answers,
        "status": "pending",
    }

    all_answers = load_answers()
    all_answers.append(completed_questionnaire)
    save_answers(all_answers)

    await message.answer(
        "Спасибо за заполнение анкеты! Мы свяжемся с вами в ближайшее время."
    )

    # Уведомление администраторов
    admin_message = f"Новая заполненная анкета!\n\n"
    admin_message += (
        f"Пользователь: {user_info['full_name']} (@{user_info['username']})\n"
    )
    admin_message += f"ID: {user_info['id']}\n"
    admin_message += f"Время заполнения: {timestamp}\n\n"
    admin_message += "Ответы на вопросы:\n"
    for question, answer in answers.items():
        admin_message += f"{question}: {answer}\n"

    for admin_id in ADMINS:
        try:
            await bot.send_message(admin_id, admin_message)
        except Exception as e:
            print(f"Не удалось отправить уведомление администратору {admin_id}: {e}")

    await state.clear()


# @dp.message(Command("check_applications"))
@dp.message(F.text == "Обработка заявок")
async def cmd_check_applications(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer("У вас нет прав для выполнения этой команды.")
        return

    all_answers = load_answers()
    pending_answers = [a for a in all_answers if a["status"] == "pending"]

    if not pending_answers:
        await message.answer("Нет новых анкет для проверки.")
        return

    application = pending_answers[0]
    await send_application_for_review(message, application)


async def send_application_for_review(message: types.Message, application):
    review_text = f"Анкета от пользователя {application['full_name']} (@{application['username']}):\n\n"
    for question, answer in application["answers"].items():
        review_text += f"{question}: {answer}\n"

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Принять", callback_data=f"accept_{application['user_id']}"
                ),
                InlineKeyboardButton(
                    text="Отклонить", callback_data=f"reject_{application['user_id']}"
                ),
            ]
        ]
    )

    await message.answer(review_text, reply_markup=keyboard)


@dp.callback_query(F.data.startswith("accept_"))
async def process_accept(callback: types.CallbackQuery):
    user_id = int(callback.data.split("_")[1])
    await process_application_decision(callback, user_id, "accepted")


@dp.callback_query(F.data.startswith("reject_"))
async def process_reject(callback: types.CallbackQuery):
    user_id = int(callback.data.split("_")[1])
    await process_application_decision(callback, user_id, "rejected")


async def process_application_decision(
    callback: types.CallbackQuery, user_id: int, decision: str
):
    all_answers = load_answers()
    for answer in all_answers:
        if answer["user_id"] == user_id and answer["status"] == "pending":
            answer["status"] = decision
            save_answers(all_answers)

            # Отправка уведомления пользователю
            if decision == "accepted":
                await bot.send_message(
                    user_id,
                    "Поздравляем! Ваша анкета была принята. Мы свяжемся с вами для дальнейших инструкций.",
                )
            else:
                await bot.send_message(
                    user_id,
                    "К сожалению, ваша анкета была отклонена. Спасибо за интерес к нашей вакансии.",
                )

            await callback.message.edit_text(f"Анкета пользователя была {decision}.")
            await callback.answer("Решение по анкете принято")

            pending_answers = [a for a in all_answers if a["status"] == "pending"]
            if pending_answers:
                await send_application_for_review(callback.message, pending_answers[0])
            else:
                await callback.message.answer("Все анкеты проверены.")
            return

    await callback.answer("Анкета не найдена или уже обработана")


@dp.callback_query(F.data.starswith("answer_"))
async def process_callback_answer(callback: types.CallbackQuery, state: FSMContext):
    await process_answer(callback.message, state, callback.data.split("_")[1])


@dp.message(Questionnaire.answering)
async def process_text_answer(message: types.Message, state: FSMContext):
    await process_answer(message, state, message.text)


async def process_answer(message, state: FSMContext, answer):
    data = await state.get_data()
    question_index = data.get("question_index", 0)

    answers = data.get("answers", {})
    questionnaire = load_questionnaire()

    answers[questionnaire[question_index]["text"]] = answer

    await state.update_data(
        # {f"answer_{question_index}": answer, "question_index": question_index + 1}
        answers=answers,
        question_index=question_index + 1,
    )
    await ask_question(message, state)


# @dp.message(Command("add_question"))
@dp.message(F.text == "Создание вопросов")
async def cmd_add_question(message: types.Message, state: FSMContext):
    if message.from_user.id not in ADMINS:
        return

    await message.answer("Введите текст вопроса:")
    await state.set_state(AdminActions.adding_question)


@dp.message(AdminActions.adding_question)
async def process_question_text(message: types.Message, state: FSMContext):
    await state.update_data(new_question_text=message.text)
    keyboard = await create_keyboard(
        [
            InlineKeyboardButton(text="Текстовый ответ", callback_data="type_text"),
            InlineKeyboardButton(text="Кнопки", callback_data="type_button"),
        ]
    )
    await message.answer("Выберите тип ответа:", reply_markup=keyboard)


@dp.callback_query(AdminActions.adding_question, F.data.startswith("type_"))
async def process_question_type(callback: types.CallbackQuery, state: FSMContext):
    question_type = callback.data.split("_")[1]
    await state.update_data(new_question_type=question_type)

    if question_type == "button":
        await callback.message.answer("Введите варианты ответов, разделенные запятой:")
        await state.set_state(AdminActions.adding_options)
    else:
        data = await state.get_data()
        questionnaire = load_questionnaire()
        questionnaire.append({"text": data["new_question_text"], "type": "text"})
        save_questionnaire(questionnaire)
        await callback.message.answer("Текстовый вопрос добавлен в анкету.")
        await state.clear()


@dp.message(AdminActions.adding_options)
async def process_question_options(message: types.Message, state: FSMContext):
    data = await state.get_data()
    questionnaire = load_questionnaire()
    questionnaire.append(
        {
            "text": data["new_question_text"],
            "type": "button",
            "options": [option.strip() for option in message.text.split(",")],
        }
    )
    save_questionnaire(questionnaire)
    await message.answer("Вопрос с кнопками добавлен в анкету.")
    await state.clear()


# @dp.message(Command("edit_question"))
@dp.message(F.text == "Редактирование вопросов")
async def cmd_edit_question(message: types.Message):
    if message.from_user.id not in ADMINS:
        return

    questionnaire = load_questionnaire()
    keyboard = await create_keyboard(
        [
            InlineKeyboardButton(
                text=f"Вопрос {i+1}: {question['text'][:30]}...",
                callback_data=f"edit_{i}",
            )
            for i, question in enumerate(questionnaire)
        ],
        row_width=1,
    )
    await message.answer("Выберите вопрос для редактирования:", reply_markup=keyboard)


@dp.callback_query(F.data.startswith("edit_"))
async def process_edit_callback(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(edit_question_index=int(callback.data.split("_")[1]))
    await callback.message.answer("Введите новый текст вопроса:")
    await state.set_state(AdminActions.editing_question)


@dp.message(AdminActions.editing_question)
async def process_edit_question_text(message: types.Message, state: FSMContext):
    data = await state.get_data()
    questionnaire = load_questionnaire()
    question_index = data["edit_question_index"]
    questionnaire[question_index]["text"] = message.text

    if questionnaire[question_index]["type"] == "button":
        await message.answer("Введите новые варианты ответов, разделенные запятой:")
        await state.set_state(AdminActions.editing_options)
    else:
        save_questionnaire(questionnaire)
        await message.answer("Вопрос успешно отредактирован.")
        await state.clear()


@dp.message(AdminActions.editing_options)
async def process_edit_question_options(message: types.Message, state: FSMContext):
    data = await state.get_data()
    questionnaire = load_questionnaire()
    question_index = data["edit_question_index"]
    questionnaire[question_index]["options"] = [
        option.strip() for option in message.text.split(",")
    ]
    save_questionnaire(questionnaire)
    await message.answer("Вопрос успешно отредактирован.")
    await state.clear()


# @dp.message(Command("delete_question"))
@dp.message(F.text == "Удаление вопросов")
async def cmd_delete_question(message: types.Message):
    if message.from_user.id not in ADMINS:
        return

    questionnaire = load_questionnaire()
    buttons = [
        InlineKeyboardButton(
            text=f"Удалить вопрос {i+1}: {question['text'][:30]}...",
            callback_data=f"delete_{i}",
        )
        for i, question in enumerate(questionnaire)
    ]
    buttons.append(InlineKeyboardButton(text="Удалить всё", callback_data="delete_all"))
    keyboard = await create_keyboard(buttons, row_width=1)
    await message.answer("Выберите вопрос для удаления:", reply_markup=keyboard)


@dp.callback_query(F.data.startswith("delete_"))
async def process_delete_callback(callback: types.CallbackQuery):
    question_index = callback.data.split("_")[1]
    questionnaire = load_questionnaire()

    if question_index == "all":
        questionnaire.clear()
        await callback.message.answer("Все вопросы удалены.")
    else:
        del questionnaire[int(question_index)]
        await callback.message.answer(f"Вопрос {int(question_index) + 1} удален.")

    save_questionnaire(questionnaire)


async def main():

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
