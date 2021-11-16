import aprslib
import time
from datetime import datetime
#grab the current time and date in zulu time
thedate = datetime.now().strftime('%d%H%M')
#add their callsign and the password for aprs here
callsign = ""
password = ""
AIS = aprslib.IS("{callsign}", passwd="{password}", port=14580)
AIS.connect()
#add the message to send here
comment = ""
#add the location here (latitude and longitude)
latitude = "" #example: "3440.80N"
longitude = "" #example: "03256.50E"
#add the symbol here
#refer to http://www.aprs.org/symbols.html for a list of symbols
symbol = ""
AIS.sendall(f"{callsign}-R>APU25N,TCPIP*,qAC,T2GREECE:;RV59-Rpt *{thedate}z{latitude}/{longitude}{symbol}{comment}")
AIS.sendall(f"{callsign}-R>APU25N,TCPIP*,qAC,T2GREECE:;R5b_Rpt  *{thedate}z{latitude}/{longitude}{symbol}{comment}")
AIS.sendall(f"{callsign}-R>APU25N,TCPIP*,qAC,T2GREECE:;RV59=Rpt *{thedate}z{latitude}/{longitude}{symbol}{comment}")
AIS.sendall(f"{callsign}-R>APU25N,TCPIP*,qAC,T2GREECE:;RV59_Rpt *{thedate}z{latitude}/{longitude}{symbol}{comment}")
AIS.sendall(f"{callsign}-R>APU25N,TCPIP*,qAC,T2GREECE:;RV59*Rpt *{thedate}z{latitude}/{longitude}{symbol}{comment}")
AIS.sendall(f"{callsign}-R>APU25N,TCPIP*,qAC,T2GREECE:;R5b-Rpt  *{thedate}z{latitude}/{longitude}{symbol}{comment}")


