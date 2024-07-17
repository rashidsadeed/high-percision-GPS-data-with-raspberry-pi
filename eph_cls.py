import serial
from pyubx2 import UBXMessage, UBXReader, POLL

# Configure the serial port (adjust the port and baudrate as needed)
serial_port = '/dev/ttyUSB0'  # Replace with your serial port
baudrate = 9600

# Open the serial port
ser = serial.Serial(serial_port, baudrate, timeout=3)

import math

class Ephemeris_data():
	def __init__(self, parsed_data):
		self.parsed_data = parsed_data
        
	def get_eccentricity(self):
		try:
			d3 = bin(self.parsed_data.sf2d3_01)[-8:]
			d4 = bin(self.parsed_data.sf2d4_01)[2:10]
			eccentricity = int(d3 + d4,2) * pow(2, -33)
			return eccentricity
		except Exception as e:
			return("eccentricity data missing or invalid") 
    
	def get_IODC(self):
		try:
			d1 = bin(self.parsed_data.sf1d1_01)[4:6]
			d8 = bin(self.parsed_data.sf1d8_01)[-8:]
			iodc = int(d1+d8,2)
			return iodc
		except Exception as e:
			return("IODC data missing or invalid") 
			

	def get_T_oc(self):
		try:
			d8 = bin(self.parsed_data.sf1d8_01)[2:18]
			T_oc = int(d8,2) * pow(2,4)
			return T_oc
		except Exception as e:
			return("T_oc data missing or invalid") 
			
	def get_a_f0_a_f1_a_f2(self):
		try:
			#second/second^2
			a_f2 = int(bin(self.parsed_data.sf1d7_01)[2:10], 2) * pow(2, -55)
			d7 = bin(self.parsed_data.sf1d7_01)[-8:]
			d8 = bin(self.parsed_data.sf1d8_01)[2:10]
			#seconds/second
			a_f1 = int(d7+d8,2) * (2,-43)
			#seconds
			a_f0 = int(bin(self.parsed_data.sf1d8_01)[5:25],2) * pow(2,-31)
			return f"a_f0, a_f1, a_f2"
		except Exception as e:
			return("a_f--0-2-- data missing or invalid") 
        
	def get_iode(self):
		try:
			d1 = bin(self.parsed_data.sf2d1_01)[-8:]
			iode = int(d1,2)
			return iode
		except Exception as e:
			return("IODE data missing or invalid") 
	
	def get_C_rs(self):
		try:
			d1 = bin(self.parsed_data.sf2d1_01)[-8:]
			d2 = bin(self.parsed_data.sf2d2_01)[2:10]
			C_rs = int(d1 + d2,2) * pow(2,-5)
			#meters
			return C_rs
		except Exception as e:
			return("C_rs data missing or invalid") 

	def get_Delta_n(self):
		try:
			d4 = bin(self.parsed_data.sf2d4_01)[-8:]
			d5 = bin(self.parsed_data.sf2d5_01)[2:10]
			Delta_n = int(d4 + d5,2) * pow(2,-43) * math.pi
			#radians per second
			return Delta_n
		except Exception as e:
			return("Delta_n data missing or invalid") 
			
	def get_M_0(self):
		try:
			d5 = bin(self.parsed_data.sf2d5_01)[-16:]
			d6 = bin(self.parsed_data.sf2d6_01)[2:18]
			M_0 = int(d5 + d6,2) * pow(2,-31) * math.pi
			#radians
			return M_0
		except Exception as e:
			return("M-0 data missing or invalid") 
    
	def get_C_uc(self):
		try:
			d7 = bin(self.parsed_data.sf2d7_01)[-8:]
			d8 = bin(self.parsed_data.sf2d7_01)[2:10]
			C_uc = int(d7 + d8,2) * pow(2,-29)
			#radians
			return C_uc
		except Exception as e:
			return("C_uc data missing or invalid") 
			
	def get_C_us(self):
		try:
			d8 = bin(self.parsed_data.sf2d8_01)[-16]
			C_us = int(d8,2) * pow(2,-29)
			#radians
			return C_us
		except Exception as e:
			return("C_us data missing or invalid") 
			
	def get_sqrt(self):
		try:
			d6 = bin(self.parsed_data.sf2d6_01)[-8:]
			d7 = bin(self.parsed_data.sf2d7_01)[-24:]
			sqrt = (int(d6 + d7,2) * pow(2,-19))^(1/2)
			meters
			return sqrt
		except Exception as e:
			return("sqrt data missing or invalid") 

	def get_C_ic(self):
		try:
			d1 = bin(self.parsed_data.sf3d1_01)[-8:]
			d2 = bin(self.parsed_data.sf3d2_01)[2:10]
			C_ic = int(d1+d2,2) * pow(2, -29)
			#radians
			return C_ic
		except Exception as e:
			return("C_ic data missing or invalid") 	
		
	def get_C_is(self):
		try:
			d2 = bin(self.parsed_data.sf3d2_01)[-8:]
			d3 = bin(self.parsed_data.sf3d3_01)[2:10] 
			C_is = int(d2+d3,2) * pow(2, -29)
			radians
			return C_is
		except Exception as e:
			return("C_is data missing or invalid") 
			
	def get_Omega_0(self):
		try:
			d3 = bin(self.parsed_data.sf3d3_01)[-16:]
			d4 = bin(self.parsed_data.sf3d4_01)[2:18]
			Omega_0 = int(d3+d4, 2) * pow(2, -31) * math.pi
			#radians
			return Omega_0
		except Exception as e:
			return("omega-0 data missing or invalid") 
    
	def get_i_0(self):
		try:
			d5 = bin(self.parsed_data.sf3d5_01)[-16:]
			d6 = bin(self.parsed_data.sf3d6_01)[2:18]
			i_0 = int(d5+d6,2) * pow(2, -31) * math.pi
			#radians
			return i_0
		except Exception as e:
			return("i-0 data missing or invalid") 
			
	def get_C_rc(self):
		try:
			d2 = bin(self.parsed_data.sf2d2_0)[-8:]
			d3 = bin(self.parsed_data.sf2d3_01)[2:10]
			C_rc = int(d2+d3, 2) * pow(2, -5)
			#meters
			return C_rc
		except Exception as e:
			return("C-rc data missing or invalid") 
			
	def get_omega(self):
		try:
			d7 = bin(self.parsed_data.sf3d7_01)[-24:]
			d8 = bin(self.parsed_data.sf3d8_01)[2:10]
			omega = int(d7+d8, 2) * pow(2, -31) * math.pi
			#radians
			return omega
		except Exception as e:
			return("omega data missing or invalid") 

	def get_omega_dot(self):
		try:
			d6 = bin(self.parsed_data.sf3d6_01)[-16:]
			d7 = bin(self.parsed_data.sf3d7_01)[2:10]
			omega_dot = int(d6+d7,2) * pow(2,-43) * math.pi
			#radians per second
			return omega_dot
		except Exception as e:
			return("omega-dot data missing or invalid")
			 
	def get_IDOT(self):
		try:
			d8 = bin(self.parsed_data.sf3d8_01)[8:22]
			idot = int(d8,2) * pow(2,-43) * math.pi
			#radians per second
			return idot
		except Exception as e:
			return("IDOT data missing or invalid") 
			
	def __str__(self):
		return(f"{self.parsed_data.svid},{self.parsed_data.how},{self.get_IODC()},{self.get_T_oc()},{self.get_a_f0_a_f1_a_f2()},{self.get_iode()},{self.get_C_rs()},{self.get_Delta_n()},{self.get_M_0},{self.get_C_uc()},{self.get_C_us()},{self.get_eccentricity()},{self.get_sqrt()},{self.get_C_ic()},{self.get_C_is()},{self.get_Omega_0()},{self.get_i_0()},{self.get_C_rc()},{self.get_omega()},{self.get_omega_dot()},{self.get_IDOT()}\n")

	def out(self):
		with open("ephemeris.txt", "a") as eph:
			eph.write(f"{self.parsed_data.svid},{self.parsed_data.how},{self.get_IODC()},{self.get_T_oc()},{self.get_a_f0_a_f1_a_f2()},{self.get_iode()},{self.get_C_rs()},{self.get_Delta_n()},{self.get_M_0()},{self.get_C_uc()},{self.get_C_us()},{self.get_eccentricity()},{self.get_sqrt()},{self.get_C_ic()},{self.get_C_is()},{self.get_Omega_0()},{self.get_i_0()},{self.get_C_rc()},{self.get_omega()},{self.get_omega_dot()},{self.get_IDOT()}\n")

    
    
try:
    # Create the UBX poll message for UBX-MGA-DBD
	msg_class = "AID"  # MGA class
	msg_id = "AID-EPH"  # MGA-DBD ID (you can use other IDs based on your needs)
	payload = b''    # No payload for the poll message

    # Create the UBX message
	msg = UBXMessage(msg_class, msg_id, payload=payload, msgmode=POLL)

    # Convert the message to binary
	msg_bin = msg.serialize()
	while True:
        # Send the message to the GPS module
		ser.write(msg_bin)

        # Read the response
		ubr = UBXReader(ser)
		for raw_data, parsed_data in ubr:
			if parsed_data.identity == 'AID-EPH':
				print("Ephemeris recieved")
				eph = Ephemeris_data(parsed_data)
				eph.out()
                #break  # Exit after receiving the MGA-DBD response


except Exception as e:
	print(f"An error occurred: {e}")
