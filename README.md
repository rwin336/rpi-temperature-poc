# rpi-temperature-poc
Raspberry PI temperature monitor POC

Basic code examples for Proof of Concept temperature monitoring.

Two different types of temperature monitors are connected to the GPIO bus on a Raspberry PI. 
This code is just example PoC code to show how to gather the temperture data.

Sensor 1:
---------

Weewooday 4 Sets DS18B20 Temperature Sensor Module Kit with 
1 m/ 3.2 Ft Waterproof Digital Stainless Steel Probe -55 to +125 Degrees Celsius, 
Compatible with Raspberry Pi


When plugged into the Raspberry Pi GPIO the readings can be found at
a directory similar to:

  /sys/bus/w1/devices/w1_bus_master1

in that directory you will find the identy of the slave devices.  Look at the number 
of slaves and then the slave IDs.

  $ cat w1_master_slave_count 
  1

  $ cat w1_master_slaves
  28-49710087a97f

  $ cd 28-49710087a97f/
  $ ls
  alarms     driver  ext_power  hwmon  name   resolution  temperature  w1_slave
  conv_time  eeprom  features   id     power  subsystem   uevent


  ## The temperature can be found in the w1_slave or teh temperature file.
  $ cat w1_slave 

  20 01 00 00 7f e1 3c aa 7a : crc=7a YES
  20 01 00 00 7f e1 3c aa 7a t=18000

  t=18000 is the temperature in C * 1000 so it needs to be devided by 1000 to get degrees C


  $ cat temperature
  18000  
