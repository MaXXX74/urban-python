from aiogram import Bot, Dispatcher, executor

token = "TELEGRAM_CHANNEL_TOKEN"

bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_massages(message):
    print('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)