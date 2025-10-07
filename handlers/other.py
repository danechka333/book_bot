from aiogram import Router
from aiogram.types import Message

other_router = Router()


@other_router.message()
async def send_echo(message: Message):
    await message.answer('Эта команда мне непонятна. Пожалуйста, воспользуйтесь /help для получения списка команд.')