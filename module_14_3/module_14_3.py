from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

token = "5124618412:AAGv62So6kpLWe7zwz7RROqxj6klKLlITck"
bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рассчитать'),
            KeyboardButton(text='Информация')
        ],
        [KeyboardButton(text='Купить')]
    ], resize_keyboard=True
)

inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Рассчитать норму калорий', callback_data="calories"),
            InlineKeyboardButton(text='Формулы расчёта', callback_data="formulas")
        ],
    ]
)

inline_kb_buy = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Продукт 1', callback_data="product_buying"),
            InlineKeyboardButton(text='Продукт 2', callback_data="product_buying"),
            InlineKeyboardButton(text='Продукт 3', callback_data="product_buying"),
            InlineKeyboardButton(text='Продукт 4', callback_data="product_buying")
        ],
    ]
)


@dp.message_handler(text="Купить")
async def get_buying_list(message):
    for number in range(1, 5):
        await message.answer(f"Название: Product{number} | Описание: описание {number} | Цена: {number * 100}")
        with open(f'files/product{number}.png', "rb") as img:
            await message.answer_photo(img, parse_mode='HTML')

    await message.answer("Выберите продукт для покупки:", reply_markup=inline_kb_buy)

@dp.callback_query_handler(text='product_buying')
async def get_formulas(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=inline_kb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 x вес (кг) + 6,25 x рост (см) - 5 x возраст (г) - 161', reply_markup=start_kb)
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = 10 * float(data["weight"]) + 6.25 * float(data["growth"]) - 5 * int(data["age"]) - 161
    await message.answer(f"Ваша норма калорий {calories:.2f}", reply_markup=start_kb)
    await state.finish()


@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=start_kb)


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
