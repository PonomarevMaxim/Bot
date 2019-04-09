import requests
import time


def main():
	url = 'https://api.exmo.com/v1/order_book/?pair=LTC_RUB,WAVES_RUB,XRP_RUB'
	
	response = requests.get(url).json()
	LTC_RUB = str(response['LTC_RUB']['ask_top']) +' ' + str(response['LTC_RUB']['bid_top'])
	
	WAVES_RUB = str(response['WAVES_RUB']['ask_top']) +' ' + str(response['WAVES_RUB']['bid_top'])
	XRP_RUB = str(response['XRP_RUB']['ask_top']) +' ' + str(response['XRP_RUB']['bid_top'])
	response = str(LTC_RUB + ' '+ WAVES_RUB+' '+ XRP_RUB)
	f = open("exmo_data.txt", "a")
	print(response)
	try:
		f.write(response +'\n')
		f.close()
	except:
		f.write('0'+'\n')
		f.close()
	return

while(True):
    main()
    time.sleep(60)




	



if __name__ == '__main__':
	main()
