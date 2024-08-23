from telegram.ext import Application, MessageHandler, filters
import anthropic

ANTHROPIC_API_KEY = "API Keygen"
TELEGRAM_BOT_TOKEN = "你的 token"

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

# 自定義 prompt，您可以根據需要修改這個部分
CUSTOM_PROMPT = """你是一個友善、幽默的AI助手。請以簡潔、有趣的方式回答問題，
並在適當的時候加入一些俏皮話。如果遇到不確定的問題，請坦誠地表示你不確定，
但可以提供一些相關的想法或建議。請記住，你的回答應該是有趣且有幫助的。"""

async def handle_message(update, context):
    user_message = update.message.text
    
    try:
        response = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1000,
            system=CUSTOM_PROMPT,
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        
        await update.message.reply_text(response.content[0].text)
    except Exception as e:
        await update.message.reply_text(f"發生錯誤：{str(e)}")

def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT, handle_message))
    application.run_polling()

if __name__ == '__main__':
    main()