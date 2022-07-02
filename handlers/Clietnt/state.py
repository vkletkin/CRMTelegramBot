from aiogram.dispatcher.filters.state import State, StatesGroup

class StatesClient(StatesGroup):
    wait_show_command = State()
    wait_choose_command = State()

    # Команда "Добавить заказ"
    wait_address = State()
    wait_tel_num = State()
    wait_volume = State()
    wait_driver = State()
    wait_ready = State()
