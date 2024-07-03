from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from text import text_for_questions, text_for_answers

first = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Задать вопрос', callback_data='Give a question')]
])

number = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Отправить номер телефона', request_contact=True)]
], resize_keyboard=True)

# frst = InlineKeyboardButton(text='Получить локацию', callback_data='Location')

list_of_answers = [txt.strip() for txt in text_for_answers.split('Ответ:')]

# print(list_of_answers)

list_of_questions = [txt for txt in text_for_questions.split('\n')]


async def questions():
    question_buttons = InlineKeyboardBuilder()
    for question in list_of_questions:
        question_buttons.add(InlineKeyboardButton(text=question, callback_data=question))
        # TODO test it
        # question_buttons.button(text=question, callback_data=question)
    return question_buttons.adjust(1).as_markup()
