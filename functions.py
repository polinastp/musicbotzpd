from distutils.command.config import LANG_EXT
from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler, CommandHandler
from telegram import ReplyKeyboardMarkup
import settings

def start(update, context):
    print("User called /start")
    my_keyboard = ReplyKeyboardMarkup([['music', 'podcast']])
    update.message.reply_text("Hello! 🎵 MusicBot here! Do you want to listen to 🎶music or 🎙podcast?", reply_markup=my_keyboard)
    return 1


    # Choosing music or podcast
def first_response(update, context):
    answer = update.message.text
    if answer.lower() == 'music':
        update.message.reply_text('How are you feeling? Tired , sad, happy or focused?')
        return 2
    elif answer.lower() == 'podcast':
        update.message.reply_text('Leisure or education?')
        return 3
    else:
        update.message.reply_text('Invalid input!')
        return ConversationHandler.END

 
    # Choosing mood for music playlist
def second_response(update, context):
    answer_music = update.message.text
    if answer_music.lower() == 'tired':
        update.message.reply_text('Do you want to wake up? yes/no?')
        return 4
    elif answer_music.lower() == 'sad':
        update.message.reply_text('Do you want to cheer up? yes/no?')
        return 5
    elif answer_music.lower() == 'happy':
        update.message.reply_text('That is great! Keep it up! Choose - indie or pop?')
        return 6
    elif answer_music.lower() == 'focused':
        update.message.reply_text('Ok. Choose - piano or lo-fi?')
        return ConversationHandler.END
    else:
        update.message.reply_text('Invalid input!')
        return ConversationHandler.END

  
    # Asking what kind of podcast user wants to hear
def third_response(update, context):
    answer_podcast = update.message.text
    if answer_podcast.lower() == 'leisure':
        update.message.reply_text(f'Here is a link to leisure podcast {settings.LEISURE_PODCAST} ')
        update.message.reply_text(settings.LAST_MESSAGE)
        return ConversationHandler.END  
    if answer_podcast.lower() == 'education':
        update.message.reply_text(f'Here is a link to educational podcast {settings.EDUCATIONAL_PODCAST} ')
        update.message.reply_text(settings.LAST_MESSAGE)
        return ConversationHandler.END 
    else:
        update.message.reply_text('Invalid input!')
    return ConversationHandler.END


    # Asking tired user if he wans to wake up
def fourth_response(update, context): 
    answer_tired = update.message.text
    if answer_tired.lower() == 'yes':
        update.message.reply_text(f'Here is the upbeat music playlist {settings.UPBEAT_PLAYLIST}')
        update.message.reply_text(settings.LAST_MESSAGE)
    elif answer_tired.lower() == 'no':
        update.message.reply_text(f'Here is the meditation music playlist {settings.MEDITATION_PLAYLIST}')
        update.message.reply_text(settings.LAST_MESSAGE)
    else:
        update.message.reply_text('Invalid input!')
    return ConversationHandler.END


    #Asking sad user if he wants to cheer up
def fifth_response(update, context):
    answer_sad = update.message.text
    if answer_sad.lower() == 'yes':
        update.message.reply_text(f'Here is the party music playlist {settings.PARTY_PLAYLIST}')
        update.message.reply_text(settings.LAST_MESSAGE)
    elif answer_sad.lower() == 'no':
        update.message.reply_text(f'Here is the sad music playlist {settings.SAD_PLAYLIST}')
        update.message.reply_text(settings.LAST_MESSAGE)
    else:
        update.message.reply_text('Invalid input!')
    return ConversationHandler.END


    #Suggesting music playlist genre for a happy user
def six_response(update, context):
    answer_happy = update.message.text
    if answer_happy.lower() == 'pop':
        update.message.reply_text(f'Here is the pop music playlist {settings.POP_PLAYLIST} ')
        update.message.reply_text(settings.LAST_MESSAGE)
    elif answer_happy.lower() == 'indie':
        update.message.reply_text(f'Here is the indie music playlist {settings.INDIE_PLAYLIST}')
        update.message.reply_text(settings.LAST_MESSAGE)
    else:
        update.message.reply_text('Invalid input!')
    return ConversationHandler.END        


    #Suggesting music playlist genre for a focused user
def seven_response(update, context):
    answer_focused = update.message.text
    if answer_focused.lower() == 'lofi' or answer_focused.lower() == "lo-fi":
        update.message.reply_text(f'Here is the lo-fi music playlist {settings.LOFI_PLAYLIST}')
        update.message.reply_text(settings.LAST_MESSAGE)
    elif answer_focused.lower() == 'piano':
        update.message.reply_text(f'Here is the piano music playlist {settings.PIANO_PLAYLIST}')
        update.message.reply_text(settings.LAST_MESSAGE)
    else:
        update.message.reply_text('Invalid input!')
    return ConversationHandler.END        


    # /stop command
def stop(update, context):
    update.message.reply_text('Bye!')
    return ConversationHandler.END


conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],

    states={
        # Function reads first question and asks second.
        1: [MessageHandler(Filters.text, first_response, pass_user_data=True)],
        # Function reads second question
        2: [MessageHandler(Filters.text, second_response, pass_user_data=True)],
        3: [MessageHandler(Filters.text, third_response, pass_user_data=True)],
        4: [MessageHandler(Filters.text, fourth_response, pass_user_data=True)],
        5: [MessageHandler(Filters.text, fifth_response, pass_user_data=True)],
        6: [MessageHandler(Filters.text, six_response, pass_user_data=True)],
        7: [MessageHandler(Filters.text, seven_response, pass_user_data=True)]
    },

    fallbacks = [CommandHandler('stop', stop)]
)

