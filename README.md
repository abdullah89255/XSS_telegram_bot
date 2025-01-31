# XSS Bot

🔒 **Secure your web applications with our XSS detection bot!** 🔒

## Overview

This project aims to create a Telegram bot that helps you check for reflected Cross-Site Scripting (XSS) vulnerabilities in web applications. By sending a URL to the bot, it will attempt to inject common XSS payloads and report any potential vulnerabilities.

## Features

- 🔍 **XSS Detection**: Automatically checks for reflected XSS vulnerabilities.
- 📱 **Telegram Integration**: Interact with the bot directly through Telegram.
- 🛡️ **Security Testing**: Helps secure web applications by identifying potential security flaws.

## Setup Instructions

### Prerequisites

- Python 3.x
- Telegram Bot Token

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/abdullah89255/XSS_telegram_bot
   cd XSS_telegram_bot
   ```

2. **Install dependencies**:
   ```sh
   pip install python-telegram-bot requests
   ```

### Configuration

1. **Set up your Telegram Bot**:
   - Create a new bot on Telegram and get your Bot Token.
   - Replace `TOKEN` in `xss_bot.py` with your Bot Token.

### Running the Bot

1. **Run the bot**:
   ```sh
   python xss_bot.py
   ```

2. **Interact with the bot**:
   - Open Telegram and search for your bot.
   - Send a URL to check for XSS vulnerabilities.

## Usage

1. **Start the bot**:
   - Send `/start` to initiate the bot.

2. **Check for XSS**:
   - Send a URL to the bot to check for reflected XSS vulnerabilities.

## Payloads

The bot uses a combination of critical and encoded XSS payloads to test for vulnerabilities.

### Critical Payloads

- `"'\"><script>alert('XSS1')</script>"`
- `"<iframe src='javascript:alert(\"XSS2\")'></iframe>"`
- `"</script><script>alert('XSS3')</script>"`
- `"<img src='x' onerror='alert(1)'>"`
- `"<svg/onload=alert(1)>"`

### Encoded Payloads

- `"%27%22%3E%3Cscript%3Ealert%28%27XSS4%27%29%3C%2Fscript%3E"`
- `"%3Ciframe%20src%3D%27javascript%3Aalert%28%22XSS5%22%29%27%3E%3C%2Fiframe%3E"`
- `"%3C%2Fscript%3E%3Cscript%3Ealert%28%27XSS6%27%29%3C%2Fscript%3E"`

## Contributing

Contributions are welcome! 🤝

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push to the branch.
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please reach out to [your email](mailto:your.email@example.com).

---

🔒 **Stay secure!** 🔒
```

### Explanation

- **Overview**: Provides a brief description of the project.
- **Features**: Lists the main features of the bot.
- **Setup Instructions**: Step-by-step guide to set up and run the bot.
- **Usage**: Explains how to use the bot.
- **Payloads**: Lists the critical and encoded XSS payloads used by the bot.
- **Contributing**: Guidelines for contributing to the project.
- **License**: Specifies the license under which the project is distributed.
- **Contact**: Provides contact information for questions or issues.

The emojis make the `README.md` more visually appealing and easier to read.
