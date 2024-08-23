from telegram.ext import Application, CommandHandler
import random

async def hello(update, context): # 建立 hello 指令內容
    await update.message.reply_text(f'你好，{update.message.from_user.first_name}！') # 回答你好

async def guess_start(update, context):
    await update.message.reply_text(f'遊戲開始，請輸入 /guess 開始猜數字')
    global number 
    number = random.randint(1, 100)

async def guess(update, context):
    global number
    if number == None:
        await update.message.reply_text('遊戲還沒開始，請輸入 /guess_start 開始')
        return
    
    try:
        guess_num = int(update.message.text.split(' ')[1])
        if guess_num < number:
            await update.message.reply_text('太小了~!')
        if guess_num > number:
            await update.message.reply_text('太大了~!')
        ## 這裡好像還少了什麼?

    except ValueError:
        await update.message.reply_text('請輸入有效數字!!')

def main():
    application = Application.builder().token('你的 token').build() # 建立 tg bot
    application.add_handler(CommandHandler('hello', hello)) # 設定 hello 指令
    application.add_handler(CommandHandler('guess_start', guess_start))
    application.add_handler(CommandHandler('guess', guess))
    application.run_polling() #開啟程式持續訪問

if __name__ == '__main__':
    main()