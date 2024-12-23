from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import requests
from urllib.parse import urlparse, urlencode, parse_qs

TOKEN = '7783516470:AAE1yXKYGEUn6kJF5WpkKVEjFbCuH7GGZzo'

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('Hello! Send me a URL to check for reflected XSS vulnerabilities.')

async def check_xss(update: Update, context: CallbackContext):
    url = update.message.text.strip()
    critical_payloads = [
        "'\"><script>alert('XSS1')</script>",
        "<iframe src='javascript:alert(\"XSS2\")'></iframe>",
        "</script><script>alert('XSS3')</script>",
        "<img src='x' onerror='alert(1)'>",
        "<svg/onload=alert(1)>"
    ]

    encoded_payloads = [
        "%27%22%3E%3Cscript%3Ealert%28%27XSS4%27%29%3C%2Fscript%3E",
        "%3Ciframe%20src%3D%27javascript%3Aalert%28%22XSS5%22%29%27%3E%3C%2Fiframe%3E",
        "%3C%2Fscript%3E%3Cscript%3Ealert%28%27XSS6%27%29%3C%2Fscript%3E"
    ]

    try:
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)

        for payload in critical_payloads + encoded_payloads:
            query_params['query'] = payload  # Inject payload into the 'query' parameter
            full_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}?{urlencode(query_params)}"

            response = requests.get(full_url, timeout=5)

            if payload in response.text:
                await update.message.reply_text(f'Potential XSS vulnerability found at: {full_url}')
                return

        await update.message.reply_text('No XSS vulnerability found.')

    except requests.exceptions.RequestException as e:
        await update.message.reply_text(f'Error: Could not fetch the URL. {e}')
    except Exception as e:
        await update.message.reply_text(f'Error: {e}')

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_xss))

    application.run_polling()

if __name__ == '__main__':
    main()