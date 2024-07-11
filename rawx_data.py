import serial 
from pyubx2 import UBXReader
import time

ser = serial.Serial("/dev/ttyAMA0", baudrate=38400, timeout=1)
ubr = UBXReader(ser)
         
def get_rawx(parsed_data):
	print("RXM-RAWX data recieved")
	entries = list((parsed_data.__dict__).keys())
	r = int(entries[-1][-2:])
	#print(r)
	for i in range(1, r + 1):
		if i in range(1,10):
			i = f"0{i}"
		rcvTow = getattr(parsed_data, f'rcvTow')
		svId = getattr(parsed_data, f'svId_{i}')
		gnssId = getattr(parsed_data, f'gnssId_{i}')
		svId = getattr(parsed_data, f'svId_{i}')
		prMes = getattr(parsed_data, f'prMes_{i}')
		cpMes = getattr(parsed_data, f'cpMes_{i}')
		doMes = getattr(parsed_data, f'doMes_{i}')
		prStd = getattr(parsed_data, f'prStd_{i}')
		cpStd = getattr(parsed_data, f'cpStd_{i}')
		doStd = getattr(parsed_data, f'doStd_{i}')
		
		with open('rawx.txt', "a") as rawx:
			rawx.write(f"{rcvTow},{gnssId},{svId},{prMes},{cpMes},{doMes},{prStd},{cpStd},{doStd}\n")

	
def get_pvt(parsed_data):
	print("NAV-PVT data recieved")
	with open("pvt.txt", "a") as pvt:
		pvt.write(f"{time.time()},{parsed_data.lon},{parsed_data.lat},{parsed_data.hMSL},{parsed_data.velN/1000},{parsed_data.velE/1000},{parsed_data.velD/1000}\n")	
	
def read_ubx():
	while True:
		try:
			try:
				raw_data, parsed_data = ubr.read()
				if parsed_data:
					if parsed_data.identity == "RXM-RAWX":
						get_rawx(parsed_data)
					elif parsed_data.identity == "NAV-PVT":
						get_pvt(parsed_data)

			except Exception as e:
				print(f"Error: {e}")
		except KeyboardInterrupt:
			print("...Closing...")
			return
			
if __name__ == "__main__":
	read_ubx()
