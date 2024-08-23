'''This code is pretty rudimentary for now, supposed to get smarter, the really hard work is (manually) writing the data with the jumps
But that's also the FUN part a bit because you get to play with the interactive NF so much, which you rarely get to do (with work/achievements tied into it)'''

import argparse, base64, time, sys
import requests
from requests.auth import HTTPBasicAuth
from pick import pick
from copy import copy

host_port = 'localhost:8080'
lua_pw = '1234'

movie = 'choose-love'

'''P.S: If someone wants to provide high quality files for this project... just kidding...
there's no one out there. (Probably nobody out there. Open an issue, idk lol)'''

auth = HTTPBasicAuth('', lua_pw)

# Probably wanna refactor this later or figure out a way to allow seperate .json files from a folder or something...
#~ But json is "dumber" (mainly... doesn't allow comments), so might just stick with .py-files
from interactive import movies

my_choices = {}

def check_above_remaining(ot, nt):
	global my_choices
	
	if nt > ot:
		movie_choices = movies['choose-love']['choices']
		
		#~ print('Checking for choices...', end = '', flush = True)
		
		for idx, choice in enumerate(movie_choices):
			human_idx = idx+1
			if str(human_idx) not in my_choices:
				#~ print('Choice #{0} has not been made yet.'.format(idx))
			
				# condition to present the choice
				if (nt >= choice[0]) and (nt < choice[0]+15):
					
					title = 'Your choice:'
					options = list(choice[1].keys())
					option, index = pick(options, title)
					print('You chose: {0} for choice #{1}'.format(option, human_idx))
					
					my_choices[str(human_idx)] = {'choice':option, 'idx': index}
					
					what_to_do = choice[1].get(option)
					
					print(what_to_do)
					
					if 'jump_to' in what_to_do:
						where_to_jump = what_to_do.get('jump_to')
						when_to_jump = what_to_do.get('jump_at')
						jump_back = what_to_do.get('jump_back')
						return when_to_jump, where_to_jump, jump_back
					elif 'display_message' in what_to_do:
						msg_to_display = what_to_do.get('display_message')
						print('Message: {0}'.format(msg_to_display))


def seek_to(value):
	jump_url = 'http://{0}/requests/status.json'.format(host_port)
	params = {'command':'seek','val': value}
	r = requests.get(jump_url, params = params, auth = auth)
	return r
	
old_time = 0	
sleep_interval = 1
jump_when = None
jump_where = None
jump_back = None
playing_right_file = False

while True:
	r = requests.get('http://{0}/requests/status.json'.format(host_port), auth = auth)
	r.encoding = 'utf-8'
	
	result = r.json()
	
	info = result.get('information')
	if info:
		info_cat = info.get('category')
		meta = info_cat.get('meta')
		fname = meta.get('filename')
	else:
		print('FAILURE: Seems like VLC might not be playing anything right now, please check.')
		sys.exit(3)
	
	length = result['length']
	
	if not playing_right_file is True:
		# check only if not yet checked
		encoded_fname = base64.b64encode(bytes(fname, 'utf-8'))
		if encoded_fname.decode() in movies[movie]['fnames']:
			if length == movies['choose-love']['length']:
				print('SUCCESS: You seem to be playing the right file.')
				playing_right_file = True
			else:
				print('FAILURE: We seem to be looking for a different file (wrong media length).')
				sys.exit(2)
		else:
			print('FAILURE: We seem to be looking for a different file (wrong name).')
			sys.exit(2)
	
	the_time = result['time']
	
	position = result['position']
	
	time_position = position*length
	print(the_time, 'vs.', time_position)
	time.sleep(sleep_interval)
	
	jump_data = check_above_remaining(old_time, time_position)
	
	if jump_data:
		jump_when, jump_where, jump_back = jump_data
		print('Got jump data: {0}'.format(jump_data))
		sleep_interval = 0.1
		
	if jump_when:
		# If we are waiting... CHECK if the current time is greater (than the "jump_at" time)
		if time_position > jump_when:
			seek_to(jump_where) # Technically this has a result, but we can definetly ignore it
			# Reset after seeking
			jump_when = None
			jump_where = None
			
			if jump_back:
				print('Still need to "jump back" (just sit back and relax)...')
				jump_when = jump_back.get('jump_at')
				jump_where = jump_back.get('jump_to')
				jump_back = None
			else:
				print('All jumped.')
				sleep_interval = 1
			
	old_time = copy(time_position)