# pip install pymodbus <- install pmodbus first if you dont have it
# pip install pymodbus –upgrade
import pymodbus
print(pymodbus)
from pymodbus.client import (
ModbusSerialClient,
ModbusTcpClient,
ModbusTlsClient,
ModbusUdpClient,
)
from pymodbus.transaction import (
ModbusAsciiFramer,
ModbusBinaryFramer,
ModbusRtuFramer,
ModbusSocketFramer,
ModbusTlsFramer,
)
client = ModbusTcpClient(host='put your ip adress here',port=502,framer=ModbusSocketFramer)
def WriteData(slave_id,address,count,value):
client.write_registers(address,[value]*count,unit=slave_id)
def ReadData(slave_id,address,count):
x = client.read_holding_registers(address,count,unit = slave_id)
print(x.registers)

Page 7 of 35

def ReadCoil(slave_id,address,count):
x = client.read_coils(address,count,unit=slave_id).bits
print(x)
def WriteCoil(slave_id,address,count,value):
if value == "ON":
status = True
else:
status = False
x = client.write_coils(address,[status]*count,unit=slave_id)
# print(x)
def WriteString(slave_id,address,count,value):
client.write_registers(address,[0]*count,unit=slave_id)
if len(value)%2 > 0:
value = value + " "
c = len(value)//2
for i in range(c):
y = value[0 + (2*i):2 + (2*i)]
print(y)
q = [ hex(ord(r))[2:4] for r in y]
print(q)
k = int(q[0]+q[1],16)
client.write_registers(address+i,k,unit=slave_id)
print(client.connect())
# WriteData(1,0,2,555)
# WriteCoil(1,0,8,"ON")
# ReadData(1,0,8)
# ReadCoil(1,0,8)
# WriteString(1,0,8,"banana")
print("on Q0: Word Address = 2 (Byte Address = 4)")
WriteData(1,2,1,0x0100) # force ID=1 WordAddr=2 nData=1Word Data = 0x0100
ReadData(1,0,4) # Read ID=1 WordAddr=0 nData=4Word
print("Off Q0: Word Address = 2 (Byte Address = 4)")
WriteData(1,2,1,0x0000) # force ID=1 WordAddr=2 nData=1Word Data = 0x0000
ReadData(1,0,4) # Read ID=1 WordAddr=0 nData=4Word
print("on Q1: Word Address = 3 (Byte Address = 6)")
WriteData(1,3,1,0x0100) # force ID=1 WordAddr=2 nData=1Word Data = 0x0100
ReadData(1,0,4) # Read ID=1 WordAddr=0 nData=4Word
print("Off Q1: Word Address = 3 (Byte Address = 6)")
WriteData(1,3,1,0x0000) # force ID=1 WordAddr=2 nData=1Word Data = 0x0000
ReadData(1,0,4) # Read ID=1 WordAddr=0 nData=4Word
