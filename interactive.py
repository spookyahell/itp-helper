# "all_scenes" is mainly a helper thing for now... it doesn't have any actual effect on the program (yet)

all_scenes = {
	'choose-love':
		{
			'intro':
				{
					'description':
						'The Netflix logo sequence and the title sequence.',
					'starts':
						0,
					'ends':
						40
				},
			'cami_at_the_psychic_default': # Use _default extension only for scenes... that have the parts for making choices
				{
					'starts':
						40,
					'ends':
						206
				},
			'game_night_default':
				{
					'starts':
						206,
					'ends':
						333
				},
			'cami_paul_invitation_to_dinner_default':
				{
					'starts':
						333,
					'ends':
						427
				},
			'cami_chooses_to_hear_bad_news_first':
				{
					'description':'Cami decides to hear bad news first from the psychic.',
					'starts':4064,
					'ends':4064
				},
			'game_night_cami_goes_for_the_kill': {
				'description':'Cami will win the game like a pro.',
				'starts':4102,
				'ends':4170
				},
			
			'cami_and_jack_at_school_scene_default':
				{
					'description':'The default scene for letting user choose option when Cami drops kid off for school; ',
					'starts':4170,
					'ends': 4525,
					'sub_scenes':
						{
							'default_scene_choice_about_what_to_tell_kid':
								{
									'starts':4170,
									'ends':4261
								},
								
							'telling_kid_to_be_brave':
								{
									'starts':4261,
									#~ 'ends':
								}
						}
				},
				
				
		}
	}


#~ Rethinking the interactive movie data might be a good idea... later.
#~ But this is what I'm going with... for now.

movies = {
	'choose-love':
		{'choices':[
				[
					156.7229996062818, 
					{
						'Good News':
							{
								'display_message':
									'This is boring... nothing to do for me.'
							},
						
						'Bad News':
							{
								'jump_to':
									4064, 
								'jump_at':
									172.23975867033016
							}
					},
					[] # which choice indexes to skip (for most other choices, although not the 2nd one either)
				],
				
				[
					253.13805971294386, 
					{
						'Throw in the Game':
							{
								'display_message':
									'This is boring... nothing to do for me.'
							},
						'Go for the Kill':	
							{
								'jump_to':4102, 
								'jump_at':268.41688288376184,
								'jump_back': 
									{
										'jump_to':333, 
										'jump_at':4169
									}
							
							}
					},
					[] # choice indexes to skip
				],
				
				[
					4313.790398836144,
					{
						'Yes To Lunch':
							{
								'display_message':
									'YES to lunch action.'
							},
						'No To Lunch':
							{
								'display_message':
									'NO to lunch action.'
							}
						}
				
				
				]
				
				
			],
			
			'fnames':['Q2hvb3NlLkxvdmUuMjAyMy4xMDgwcC5XRUItREwuRERQNS4xLngyNjQtQU9DLm1rdg=='],
			'length': 17420,
			#~ 'scene-changes':
				#~ '

				
		}
	}