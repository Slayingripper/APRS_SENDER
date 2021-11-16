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

AIS.sendall(f"{callsign}-R>APU25N,TCPIP*,qAC,T2GREECE:;RV59-Rpt *{thedate}z3440.80N/03256.50E!REPORTED FOR VIOLATION OF TOS")
AIS.sendall(f"{callsign}-R>APU25N,TCPIP*,qAC,T2GREECE:;R5b_Rpt  *{thedate}z3440.81N/03256.51E!REPORTED FOR VIOLATION OF TOS")
AIS.sendall(f"{callsign}-R>APU25N,TCPIP*,qAC,T2GREECE:;RV59=Rpt *{thedate}z3440.82N/03256.52E!REPORTED FOR VIOLATION OF TOS")
AIS.sendall(f"{callsign}-R>APU25N,TCPIP*,qAC,T2GREECE:;RV59_Rpt *{thedate}z3440.83N/03256.53E!REPORTED FOR VIOLATION OF TOS")
AIS.sendall(f"{callsign}-R>APU25N,TCPIP*,qAC,T2GREECE:;RV59*Rpt *{thedate}z3440.84N/03256.54E!REPORTED FOR VIOLATION OF TOS")
AIS.sendall(f"{callsign}-R>APU25N,TCPIP*,qAC,T2GREECE:;R5b-Rpt  *{thedate}z3440.85N/03256.55E!REPORTED FOR VIOLATION OF TOS")


