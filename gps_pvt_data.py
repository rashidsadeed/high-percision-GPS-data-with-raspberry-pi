from ublox_gps import UbloxGps
import serial
import time

port = serial.Serial("/dev/ttyAMA0", baudrate = 9600, timeout=1)
gps = UbloxGps(port)

#38400


def get_data():
	try:
		print("Listening for UBX Messages")
		while True:
			try:
				coords = gps.geo_coords()
				#get_gps_data_pre(coords)
				get_gps_data_org(coords)
			except (ValueError, IOError, AttributeError) as err:
				print(err)
	finally:
		port.close()
		
def get_gps_data_pre(coords):
	headers = ["longitude", "latitude", "altitude", "velNorth", "velEast", "velDown"]
	required_data = [coords.lon, coords.lat, coords.height, coords.velN, coords.velE, coords.velD]
	for index, i in enumerate(required_data):
		print(f"{headers[index]}: {required_data[index]}\t")
		if index == len(required_data)-1:
			print("\n")

def get_gps_data_org(coords):
	#scaled the longitude and latitude coordinates and converted velocities to meters
	print(f"{coords.lon},{coords.lat},{coords.height},{coords.velN/1000},{coords.velE/1000},{coords.velD/1000}")
	with open("data.txt","a") as data:
		data.write(f"{time.time()},{coords.lon},{coords.lat},{coords.height},{coords.velN/1000},{coords.velE/1000},{coords.velD/1000}\n")
		


			
if __name__ == "__main__":
	get_data()
	
