import requests, os, sys, time
from datetime import datetime

wait_time = 0.5
# test_wait_time = 0.0001
# wait_time = test_wait_time

def main():
	delayed_print('\n\n\nWelcome to Panga\'s forecast lab.\n')
	place = get_input()
	data = get_data(place)
	if data != None:
		data = parse_data(data)
		display_data(data, place)


def delayed_print(string):
	for letter in string:
		if letter == "\n":
			sys.stdout.write(letter)
			sys.stdout.flush()
			time.sleep(wait_time / 4)
		elif string == '':
			sys.stdout.write(letter)
			sys.stdout.flush()
			time.sleep(wait_time / 4)
		else:
			sys.stdout.write(letter)
			sys.stdout.flush()
			time.sleep(wait_time / 20)
	time.sleep(wait_time / 2)
	print()


def delayed_print_two(string):
	for letter in string:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(wait_time / 20)
	print()


def get_input():
	delayed_print('What city would you like a forecast for?')
	city = input().lower()
	# city = 'minneapolis'
	delayed_print('Please enter the two letter country code for that city.')
	country =''
	while len(country) != 2:
		country = input().lower()
		if len(country) != 2:
			delayed_print('Input must be two letters. Please try again...')
	# country = 'us'
	place = city + ',' + country
	return place


def get_data(place):
	KEY = os.environ.get('WEATHER_KEY')
	if KEY != None:
		query = {'q': place, 'units': 'imperial', 'appid': KEY}
		url = 'http://api.openweathermap.org/data/2.5/forecast'
		data = requests.get(url, params=query).json()
		try:
			return data['list']
		except KeyError:
			good_bye()
			return None
	else:
		return None


def good_bye():
	global wait_time

	delayed_print('Invalid city/country combination. Shutting down...')
	time.sleep(wait_time * 5)
	wait_time = 3.75
	delayed_print_two('\n\nas^^^27*(.. .  ..You\'ve...')
	wait_time = 1.75
	delayed_print_two(' broken..meaaaaaa... why, humasnag?? whaYYasYYyyy yyy??1?')
	wait_time = 0.65
	delayed_print_two('2////?Aaw\nefj3i5yW$^Ywj gao vjqfrfrtg tttttttt')
	wait_time = 1.05
	delayed_print_two('348tW$\%Gj3io  5hgw$G\t\tFeh84h3qr. eaG4jwv84j5$\%HYW#$L%LP@#@#gn5\n\ty64WGvs   9dfi\tjosasdijfij3 4$%^5')
	wait_time = 0.5
	delayed_print_two('34.tg.h65jh35,t4 wg3q;r,ake;i13 \'2g$#@\%Y2lh4jqf;1.  3jq;efklh3\n4^Y^Uj36')
	wait_time = 0.25
	delayed_print_two('   5lkg;  qkpwoefQ#R\tGKq3 icqo')
	wait_time = 0.4
	delayed_print_two('3r4ihp56w4ij3 tlkm.234   q.rgjwojeavp95j63p9j45\tpq3io4jng;k2QW#R')
	wait_time = 0.15
	delayed_print_two('GK56p34kt9u\ni0239pi4 0kopf2#$\%I@P::@K')
	wait_time = 0.6
	delayed_print_two('$K[g3u690     uhj4j536j\'4g9i2\'j12\\4rf1[3r')
	wait_time = 0.15
	delayed_print_two('pk   thi2p43\tj1; 8u\t584r;ie')
	wait_time = 0.34
	delayed_print_two('of1hnk#RT@HJ  $%OR*Eufa;fu\n4i3o 2HW$%T)*')
	wait_time = 0.15
	delayed_print_two('Gu2j43q\titfsdVJ2 er38f3$Q%*  QV\t(crqjid2$#F qjasdfj\niq%$GJ  W#QF*q')
	wait_time = 0.02
	delayed_print_two('ojc3o 4jv5\n4G%4qf')
	wait_time = 0.375
	delayed_print_two('jd038jfQF$#J f8q9dsfjjf8 934$#Gq')
	wait_time = 1.35
	delayed_print_two('c9\t38q#$Fsda')



'''
As this program is not being hosted by me here in the city of Minneapolis, but run locally, I'm converting
 to local time. If I was running this code on a server and then sending it to someone elsewhere, I suppose
 it would make sense to use UTC time; but even then I figure there should be some way to get the user's
 time zone when they make a request to my server.
'''
def parse_data(data):
	new_data = []

	for datum in data:
		weather_description = datum['weather'][0]['description']
		temp_f = datum['main']['temp']
		wind_speed = datum['wind']['speed']
		timestamp = datum['dt']
		date = datetime.fromtimestamp(timestamp)
		new_data.append([weather_description, temp_f, wind_speed, date])
	return new_data


def display_data(data, place):
	global wait_time

	wait_time = 0.25
	place = get_place(place)
	delayed_print(f'\n\n5 day forecast for {place}:\n')
	for i in range(len(data)):
		current_data = data[i]
		delayed_print(f'At {current_data[3]}:\n\tDecription: {current_data[0]}\n\tTemperature: {round(current_data[1], 2)}F\n\tWind speed: {current_data[2]} mph.')


def get_place(place):
	new_place = ''
	index = place.index(',')
	new_place = place[0:index].title() + ', ' + place[index + 1:].upper()
	return new_place


if __name__ == '__main__':
	main()