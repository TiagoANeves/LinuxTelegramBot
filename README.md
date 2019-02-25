LinuxTelegramBot

Run any commands on Linux machine using Telegram

## Getting Ready
![Print](https://core.telegram.org/file/811140763/1/PihKNbjT8UE/03b57814e13713da37)

Create a new bot using [TheBotFather](https://telegram.me/botfather) the get your bot token.

Edit the LinuxTelegramBot.py script and set your Bot token and your Telegram Username.

If you don't remember your Telegram Username, you can send /whoami to your new bot to get it after starting it.

## Installing

Clone this repository:
``` sh
git clone https://github.com/TiagoANeves/LinuxTelegramBot.git
```

Now, install the required packages:
``` sh
pip3 install -r requirements.txt
```

Run the Bot!
``` sh
python3 LinuxTelegramBot.py 
```

### Commands

All commands start with "/" like: /whoami , /help or /start

/whoami : The bot will answer with your Telegram Username.

/help or /start : The bot will answer with all available commands.

If you set your Username and send any messages without "/", the bot will run it direct in the linux machine, so be careful. If you don't wanna this feature, just comment this line:

``` sh
dp.add_handler(MessageHandler(Filters.text, opencmd))
```

You can add or remove any commands to fit you needs.


That's all folks!

## License

LinuxTelegramBot is licensed under the GNU GPL license. take a look at the [LICENSE](https://github.com/TiagoANeves/TDTLinuxPWD/blob/master/LICENSE) for more information.

## Version
**Current version is 1.0.0**

## Credits
- [Tiago Neves](https://github.com/TiagoANeves)
