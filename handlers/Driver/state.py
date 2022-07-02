from aiogram.dispatcher.filters.state import State, StatesGroup

class StatesDriver(StatesGroup):
    # состояния списка и выбора команд
    wait_show_command = State()
    wait_choose_command = State()

    wait_add_order = State()
    wait_new_address = State()
    wait_new_tel_num = State()
    wait_new_price = State()
    wait_new_driver = State()
    wait_new_ready = State()
