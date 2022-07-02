from aiogram.dispatcher.filters.state import State, StatesGroup

class StatesAdmin(StatesGroup):
    #состояния списка и выбора команд
    wait_show_command = State()
    wait_choose_command = State()

    #Команда "Добавить заказ"
    wait_address = State()
    wait_phone_number = State()
    wait_price = State()
    wait_driver = State()
    wait_ready = State()
    wait_confirm_order = State()
    wait_confirm_complite = State()

    # Команда "Подтвердить клиентский заказ"
    wait_confirm_driver= State()
    wait_confirm_price= State()
