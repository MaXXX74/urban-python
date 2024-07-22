# -*- coding: utf-8 -*-
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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
