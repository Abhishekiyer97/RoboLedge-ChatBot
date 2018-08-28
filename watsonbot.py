from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
from watson_developer_cloud import ConversationV1
import json
import sqlite3


context = None

conn = sqlite3.connect('budget.db', check_same_thread=False, timeout=10)
c=conn.cursor()


#query = "SELECT date FROM expenditure1 WHERE userID = 'arjun' and amount=500"
#c.execute(query)
#r=c.fetchall()
#r1=r[1][1]
    

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    print('Received /start command')
    update.message.reply_text('Hola!\nI\'m here to help you save some money.\nPlease enter your name to continue :) ')
    #update.message.reply_text(r[0][0])


def help(bot, update):
    print('Received /help command')
    update.message.reply_text('Help!')


def message(bot, update):
    print('Received an update')
    global context

    conversation = ConversationV1(username='usernamehere',  # TODO
                                  password='passwordhere',  # TODO
                                  version='2018-02-16')

    # get response from watson
    response = conversation.message(
        workspace_id='workspaceidhere',  # TODO
        input={'text': update.message.text},
        context=context)
    print(json.dumps(response, indent=2))
    context = response['context']

    # build response
    resp = ''
    for text in response['output']['text']:
        resp += text
    #update.message.reply_text(resp)
	
    if len(response['entities'])>0:    	
	entity = response['entities'][0]['entity']
 	value = response['entities'][0]['value']
    
    # handle no intents
    if len(response['intents'])>0:
    	intent=response['intents'][0]['intent']
        print(intent)
    

    context = response['context']
    # build response

    #print(response['entities'][4]['metadata']['numeric_value'])
	 	
    if intent == 'enter_name':
    	global name
    	name = response['input']['text']
    	print(name)
    	update.message.reply_text(response['output']['text'][0])
    	
    	
    if intent == 'Set_budget':
    	print(name)
        budg=response['entities'][2]['metadata']['numeric_value']
        date = response['entities'][0]['value']
        #print(date)
        #print(response['entities'][4]['metadata']['numeric_value'])
	update.message.reply_text(response['output']['text'][0])
        query = 'INSERT INTO expenditure1 (userID,date,budget) VALUES("%s","%s",%d)'%(name,date,budg)
	print(query)
	try:
		c.execute(query)
		conn.commit()
	except Exception as e:
		print(e)
	#c.execute("SELECT * FROM expenditure1")
	#r=c.fetchall()	
	#print(r)
	#print(response['entities'][4]['metadata']['numeric_value'])

    if intent == 'Money_Spent':
    	print('aaa')
    	update.message.reply_text(response['output']['text'][0])

    if intent == 'Spent_money_on':
	spent=response['entities'][1]['metadata']['numeric_value']
	item=response['context']['item']
	#print(response['entities'][1]['metadata']['numeric_value'])
	update.message.reply_text(response['output']['text'][0])
	query= 'UPDATE expenditure1 SET amount=%d , item="%s" WHERE userID = "%s" '%(spent,item,name)
	query2= 'UPDATE expenditure1 SET budget=budget-%d WHERE userID = "%s"'%(spent , name)
	#query3='SELECT budget FROM expenditure1 WHERE userID="%s"'%(name)
	print(query2)
	try:
		#print(c.execute(query))		
		c.execute(query)
		c.execute(query2)
		#c.execute(query3)
		conn.commit()
		#r=c.fetchall()
		#print(r)
		
	except Exception as e:
		print(e)
	


    if intent == 'Remaining_budget':
	outp=response['output']['text'][0]
	query='SELECT budget FROM expenditure1 WHERE userID="%s"'%(name)
	print(query)
	try:
		#print(c.execute(query))		
		c.execute(query)
		conn.commit()
		r=c.fetchall()
		print(r[0][0])
		budg=str(r[0][0]) 
		if r[0][0] > 0:
			update.message.reply_text(outp+" "+budg)
		else:
			update.message.reply_text("Oops! You have already exceeded your budget")
	except Exception as e:
		print(e)
	
		


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater('your token here')  # TODO

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, message))

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blockin
    # g and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
