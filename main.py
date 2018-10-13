'''
BOT MANAGER
allows bots to be selected then deployed
'''

#import brit_bot
#import ras_bot
import test_bot

def main():
    bot_list = ["Test Bot", "Brit"]

    print("-----BOT MANAGER-----")
    print("Available bots:")

    for x in range(len(bot_list)):
        print(str(x + 1) + ". " + bot_list[x])
    choice = str(input(":"))

    if choice == "1":
        successful = test_bot.start()
        if not successful:
            print("Bot failed to start")
            main();
            pass

    elif choice == "2":
        pass


main()
