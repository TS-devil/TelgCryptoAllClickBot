#Creating session for telegram bots connection
import asyncio
import logging
import re
import time
import os
import sys

logging.basicConfig(level=logging.ERROR)

from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from datetime import datetime
from colorama import Fore, init as color_ama
color_ama(autoreset=True)

os.system('cls' if os.name=='nt' else 'clear')

# Get your own values from my.telegram.org
api_id = 800812
api_hash = 'db55ad67a98df35667ca788b97f771f5'

def print_msg_time(message):
	print('[' + Fore.CYAN + f'{datetime.now().strftime("%H:%M:%S")}' + Fore.RESET + f'] {message}')

async def main():
	print(Fore.MAGENTA + '__      _____ _    ___ ___  __  __ ___ ')
	print(Fore.MAGENTA + '\ \    / / __| |  / __/ _ \|  \/  | __|')
	print(Fore.MAGENTA + ' \ \/\/ /| _|| |_| (_| (_) | |\/| | _| ')
	print(Fore.MAGENTA + '  \_/\_/ |___|____\___\___/|_|  |_|___|\n' + Fore.RESET)
	print(Fore.GREEN + '    -   BY THUNDER SOUL   -   \n' + Fore.RESET)
                                
	# Check if phone number is not specified
	if len(sys.argv) < 2:
		print('Usage: python start.py phone_number')
		print('-> Input number in international format (example: +639162995600)\n')
		e = input('Press any key to exit...')
		exit(1)
		
	phone_number = sys.argv[1]
	
	if not os.path.exists("session"):
		os.mkdir("session")
   
	# Connect to client
	client = TelegramClient('session/' + phone_number, api_id, api_hash)
	await client.start(phone_number)
	me = await client.get_me()
	
	print(f'Current account: {me.first_name}({me.username})\n')
	print(f'Successfully created session file for: {phone_number} | directory: /session/{phone_number}.session')
	print(f'______________________________________________________________________')
	#print (f'Press Ctrl + Z for exit | Enter')
	# val = input("You want to add number in list.txt? yes/no: ")
	# if (val == "yes"):
	#     print(f'{phone_number} add in list.txt')
	#     #with open('list.txt', 'w') as f:
	#     #for item in my_list:
	#         #f.write("\n" phone_number)
	# else:
	#     exit()

	content = True
	i = 1
	with open("Numbers.txt") as f:
		while content:
			content = f.read()
			i+=1
			if phone_number in content.lower():
				print(f'{phone_number} is present on "Numbers.txt" line no. {i}')
				f.close()
				exit()
			else:
				f.close()
				val = input("You want to add number in Numbers.txt? yes/no: ")
				if (val == "yes"):
					print(f'{phone_number} add in Numbers.txt')
					m = open('Numbers.txt', 'a')
					m.write("\n"+phone_number)
					m.close()
					exit()
				else:
					exit()
	
	await client.run_until_disconnected()
	
asyncio.get_event_loop().run_until_complete(main())
