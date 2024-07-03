from aiogram import Router, F, Bot
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from buttons import first, questions, number
from state import Sign_up
from text import dict_for_answers

router = Router()


@router.message(CommandStart())
async def start_and_reg(message: Message, state: FSMContext):
    await message.answer(f'Здравствуйте <b>{message.from_user.first_name}</b>, Добро пожаловать '
                         f'в бот <b>logistics</b> "название компании cargo"')
    await state.set_state(Sign_up.name)
    await message.answer('Введите ваше имя:')


@router.message(Sign_up.name)
async def reg_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Sign_up.phone_number)
    global phone_button
    phone_button = await message.answer('Отправьте свой номер телефона нажав на кнопку:', reply_markup=number)


@router.message(Sign_up.phone_number, F.contact)
async def reg_number(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(phone_number=message.contact.phone_number)
    await phone_button.delete()
    data = await state.get_data()
    # print(data.get('name'), data.get('phone_number'))
    # await message.send_copy(chat_id=1454665869, message_effect_id=f'{data.get('name')}, {data.get('phone_number')}')
    await bot.send_message(chat_id=566195506, text=f"{data['name']}, {data['phone_number']}")
    await bot.send_message(chat_id=1454665869, text=f"{data['name']}, {data['phone_number']}")
    await message.send_copy(chat_id=566195506)
    await message.send_copy(chat_id=1454665869)
    # await
    # print(data['name'], data['phone_number'])
    # await Bot.send_message(self=Bot, chat_id=1454665869, text=f'Имя: {data.get('name')}\nТелефон номер: {data.get('phone_number')}')
    await message.answer('Спасибо, регистрация завершена', reply_markup=first)
    await state.clear()


# @router.message()
# async def send_me(message: Message):
#     await message.send_copy(chat_id=1454665869)
    # await message.answer_contact(phone_number=message.contact.phone_number)


@router.callback_query(F.data == 'Give a question')
async def answer(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text='Задайте интересующий вас вопрос:', reply_markup=await questions())


# print(type(F.data.text))


@router.callback_query(F.data == F.data)
async def send_text(callback: CallbackQuery):
    await callback.answer()
    # await callback.message.answer(f'{text_for_answers_2[int(callback.data) - 1]}')
    await callback.message.answer(f'{callback.data}:\n{dict_for_answers[callback.data]}')


# @router.message(F.text == 'location')
# async def send_loc(message: Message):
#     await message.answer_location(latitude=41.877382, longitude=60.526287)
