import random
import wifi_qrcode_generator.generator


names = ['SSID']

def main():
	SSID = random.choice(names)
	PASS = random.randrange(10000000000)
	text = f"""
Wi-Fi
SSID: {SSID}
Password: {PASS}
	"""
	print(text)

	with open('Wifi.txt', 'a') as file:
		file.write(text)

	qr_code = wifi_qrcode_generator.generator.wifi_qrcode(
    ssid=SSID, hidden=False, authentication_type='WPA', password=PASS
	)
	qr_code.print_ascii()
	qr_code.make_image().save('wifi_qr.png')