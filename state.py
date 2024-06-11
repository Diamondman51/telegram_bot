from aiogram.fsm.state import StatesGroup, State


class Sign_up(StatesGroup):
    name = State()
    phone_number = State()
