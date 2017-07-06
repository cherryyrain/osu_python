import requests


urls = {
	'beatmaps' : 'https://osu.ppy.sh/api/get_beatmaps',
	'user' : 'https://osu.ppy.sh/api/get_user',
	'scores' : 'https://osu.ppy.sh/api/get_scores',
	'user_best' : 'https://osu.ppy.sh/api/get_user_best',
	'user_recent' : 'https://osu.ppy.sh/api/get_user_recent',
	'match' : 'https://osu.ppy.sh/api/get_match', 'replay' :
	'https://osu.ppy.sh/api/get_replay'
}


class mods(): #the bitwise notation of each mod
	none = [0, 'No Mods']
	no_fail = [1, 'NF']
	easy = [2, 'EZ']
	no_video = [4, 'NO VIDEO MOD: POST BUG REPORT'] #this should never show
	hidden = [8, 'HD']
	hard_rock = [16, 'HR']
	sudden_death = [32, 'SD']
	double_time = [64, 'DT']
	relax = [128, 'RX']
	half_time = [256, 'HT']
	nightcore = [512, 'NC']
	flashlight = [1024, 'FL']
	autoplay = [2048, 'AT']
	spun_out = [4096, 'SO']
	relax2 = [8192, 'AP'] #autopilot, i think
	perfect = [16384, 'PF']
	key4 = [32768, '4K'] #lol who uses mania mods
	key5 = [65536, '5K']
	key6 = [131072, '6K']
	key7 = [262144, '7K']
	key8 = [524288, '8K']
	fade_in = [1048576, 'FI']
	random = [2097152, 'RD'] #i honestly had to google the shorthand for Random
	last_mod = [4194304, 'LM'] #the fuck is a last mod
	key9 = [16777216, '9K']
	key10 = [33554432, '10K']
	key1 = [67108864, '1K']
	key3 = [134217728, '3K']
	key2 = [268435456, '2K']
	modslist = [none,no_fail,easy,no_video,hidden,hard_rock,sudden_death,double_time,relax,half_time,nightcore,flashlight,autoplay,spun_out,relax2,perfect,key4,key5,key6,key7,fade_in,random,last_mod,key9,key10,key1,key3,key2]


parameters = {
	#required is TRUE, not required is FALSE
	#defaults are in the comment below each dictionary
	#note that ALL "utype"s just make a guess based on "u", and can therefore fuck up if the username is *just* digits
	'beatmaps' : {'k':True,'since':False,'s':False,'b':False,'u':False,'utype':False,'m':False,'a':False,'h':False,'limit':False}
	#m: all modes | a: 0 | limit: 500 (range 1-500)
	'user' : {'k':True,'u':True,'m':False,'utype':False,'event_days':False}
	#m: 0 | event_days: 1
	'scores' : {'k':True,'b':True,'u':False,'m':False,'mods':False,'utype':False,'limit':False}
	#m: 0 | limit: 50 (range 1-100)
	'user_best' : {'k':True,'u':True,'m':False,'limit':False,'utype':False}
	#m: 0 | limit: 10 (range 1-100)
	'user_recent' : {'k':True,'u':True,'m':False,'limit':False,'utype':False}
	#m: 0 | limit: 10 (range 1-50)
	'match' : {'k':True,'mp':True}
	#none
	'replay' : {'k':True,'m':True,'b':True,'u':True}
	#none
}
def make_request(req_type,req_parameters): #parameters should be a dictionary in the form {'parameter':'value','parameter':'value'}
	if urls.has_key(req_type):
		with req_parameters.keys() as req_parameters_list:
			if parameters[req_type].has_key(req_parameters_list):
				request = requests.get(req_type,params=req_parameters).json()[0]
				
