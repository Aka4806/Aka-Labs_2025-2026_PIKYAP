import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
from config import BOT_TOKEN, POPULAR_CURRENCIES
from currency_data import converter

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class CurrencyBot:
    def __init__(self, token):
        self.application = Application.builder().token(token).build()
        self.setup_handlers()

    def setup_handlers(self):
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CommandHandler("help", self.help_command))
        self.application.add_handler(CommandHandler("convert", self.convert_command))
        self.application.add_handler(CommandHandler("currencies", self.list_currencies))
        self.application.add_handler(CallbackQueryHandler(self.button_handler))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.effective_user
        welcome_text = f"""
 Привет, {user.first_name}!

Я бот для конвертации валют 

Доступные команды:
/start - Начать работу
/convert - Конвертировать валюту
/currencies - Список доступных валют
/help - Помощь

Или просто напишите сумму и валюты для конвертации, например:
"100 USD to EUR"
        """
        await update.message.reply_text(welcome_text)

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        help_text = """
  Как пользоваться ботом:

1. **Быстрая конвертация:**
   Напишите в чат: `[сумма] [из валюты] to [в валюту]`
   Пример: `100 USD to EUR`

2. Команда /convert:
   Пошаговая конвертация с выбором из списка

3. Команда /currencies:
   Показать список доступных валют

  Примеры использования:
- 100 USD to EUR
- 50 EUR to RUB
- 1000 JPY to USD
        """
        await update.message.reply_text(help_text)

    async def convert_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        keyboard = [
            [InlineKeyboardButton(currency, callback_data=f"from_{currency}")
             for currency in POPULAR_CURRENCIES[i:i + 3]]
            for i in range(0, len(POPULAR_CURRENCIES), 3)
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            "Выберите исходную валюту:",
            reply_markup=reply_markup
        )

    async def list_currencies(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        currencies = converter.get_available_currencies()
        if currencies:
            currencies_text = "Доступные валюты:\n\n"
            for i in range(0, len(currencies), 8):
                currencies_text += " ".join(currencies[i:i + 8]) + "\n"
            await update.message.reply_text(currencies_text)
        else:
            await update.message.reply_text("Не удалось загрузить список валют")

    async def button_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()

        data = query.data

        if data.startswith("from_"):
            from_currency = data[5:]
            context.user_data['from_currency'] = from_currency

            keyboard = [
                [InlineKeyboardButton(currency, callback_data=f"to_{currency}")
                 for currency in POPULAR_CURRENCIES[i:i + 3]]
                for i in range(0, len(POPULAR_CURRENCIES), 3)
            ]

            reply_markup = InlineKeyboardMarkup(keyboard)
            await query.edit_message_text(
                f"Исходная валюта: {from_currency}\nВыберите целевую валюту:",
                reply_markup=reply_markup
            )

        elif data.startswith("to_"):
            to_currency = data[3:]
            from_currency = context.user_data.get('from_currency')

            if from_currency:
                context.user_data['to_currency'] = to_currency
                await query.edit_message_text(
                    f"Конвертация: {from_currency} → {to_currency}\n"
                    f"Введите сумму для конвертации:"
                )

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = update.message.text.strip()

        try:
            parts = text.upper().split()
            if len(parts) >= 4 and parts[2] == 'TO':
                amount = float(parts[0])
                from_currency = parts[1]
                to_currency = parts[3]

                result = await self.perform_conversion(amount, from_currency, to_currency)
                await update.message.reply_text(result)
                return

        except (ValueError, IndexError):
            pass

        if 'from_currency' in context.user_data and 'to_currency' in context.user_data:
            try:
                amount = float(text)
                from_currency = context.user_data['from_currency']
                to_currency = context.user_data['to_currency']

                result = await self.perform_conversion(amount, from_currency, to_currency)
                await update.message.reply_text(result)

                context.user_data.clear()
                return

            except ValueError:
                pass

        await update.message.reply_text(
            "Не удалось распознать запрос.\n\n"
            "Используйте формат: `100 USD to EUR`\n"
            "Или команду /convert для пошаговой конвертации"
        )

    async def perform_conversion(self, amount: float, from_currency: str, to_currency: str) -> str:
        converted_amount = converter.convert_currency(amount, from_currency, to_currency)

        if converted_amount is not None:
            return (
                f" Результат конвертации:\n\n"
                f" {amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}\n"
                f" Курс: 1 {from_currency} = {converted_amount / amount:.4f} {to_currency}"
            )
        else:
            return "Ошибка при конвертации. Проверьте правильность введенных валют."

    def run(self):
        print("Бот запущен...")
        self.application.run_polling()


def main():
    if BOT_TOKEN == 'YOUR_BOT_TOKEN_HERE':
        print("Пожалуйста, установите BOT_TOKEN в config.py")
        return

    bot = CurrencyBot(BOT_TOKEN)
    bot.run()


if __name__ == '__main__':
    main()