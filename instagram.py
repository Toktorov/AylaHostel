from instabot import Bot
bot = Bot()
bot.login(username = "toktorov005",  password = "Toktorov05")

user_followers = bot.get_user_followers('toktorov005')