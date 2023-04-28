from aiogram import Bot, Dispatcher, types,executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
def bot(usd):
    # Инициализация бота и хранилища состояний
    bot = Bot(token="6139653937:AAF66dx70T0t60ZspDVrv5acbMtB_4rQH9o")
    dp = Dispatcher(bot, storage=MemoryStorage())
    # Обработчик команды /start
    @dp.message_handler(commands="start")
    async def cmd_start(message: types.Message):
        # Приветственное сообщение и инструкции по использованию бота
        await message.reply("Привет!\n"
                            "Я бот, который поможет тебе узнать курс доллара.\n"
                            "Для продолжения нажми /course")
    # Обработчик команды /course
    @dp.message_handler(commands="course")
    async def cmd_course(message: types.Message):
        # Запрашиваем нижнюю границу
        await message.answer("Введите нижнюю границу:")
        await dp.current_state(user=message.from_user.id).set_state('wait_down')
    # Обработчик сообщений в состоянии wait_down
    @dp.message_handler(state='wait_down')
    async def process_down(message: types.Message):
        # Получаем значение нижней границы и запрашиваем верхнюю
        global down
        down = message.text
        await message.reply("Введите верхнюю границу:")
        await dp.current_state(user=message.from_user.id).set_state('wait_up')
    # Обработчик сообщений в состоянии wait_up
    @dp.message_handler(state='wait_up')
    async def process_up(message: types.Message, state):
        # Получаем значение верхней границы и отправляем курс доллара
        up = message.text
        await state.finish()
        if usd<down or usd>up:
            await message.reply(f"Курс доллара вышел за границы")
        else: await message.reply(f"курс доллара {usd} рубль")
    executor.start_polling(dp, skip_updates=True)
