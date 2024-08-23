from telegram.ext import Application, CommandHandler

async def hello(update, context): # 建立 hello 指令內容
    await update.message.reply_text(f'你好，{update.message.from_user.first_name}！') # 回答你好

def main():
    application = Application.builder().token('你的 token').build() # 建立 tg bot
    application.add_handler(CommandHandler('hello', hello)) # 設定 hello 指令
    application.run_polling() #開啟程式持續訪問

if __name__ == '__main__':
    main()