# APRS_byebye
Ever had that one guy on APRS who just likes to list fake repeaters? No worries , I Got you covered. 
# The scenario
You have a list of repeaters that you want to use in your APRS network. But you have that one “ham” who just likes to list fake repeaters on APRS, so they can get attention. The problem is that even though this is a bit harmless, it's not a good idea to have a bunch of fake repeaters on APRS, as it will confuse a lot of people thinking that a repeater is actually there. Which in an emergency scenario could be a life or death situation. A real-world example of this is the Beirut explosion that happened in the year of 2020. Many people were killed, and many others were injured. Furthermore, many people were not aware of the explosion, and they were not aware of the fact that it was happening. Communications were down and the only thing that was working was radio. Many ham radio operators used repeaters from neighbouring countries to communicate with each other, such as Cyprus, Israel and Turkey. Many of these operators used Yagi antennas to point in the direction of the Repeaters, now imagine if the repeaters were not actually what would happen. 
# APRS security issues
One of the major security issues of the APRS network is the ability to compute the authentication password for any user of the APRS network. 
This is obvious why once we look at the code used for password generation:
```
<?php

function aprspass ($callsign) { 
	$stophere = strpos($callsign, '-'); 
	if ($stophere) $callsign = substr($callsign, 0, $stophere); 
	$realcall = strtoupper(substr($callsign, 0, 10)); 

	// initialize hash 
	$hash = 0x73e2; 
	$i = 0; 
	$len = strlen($realcall); 

	// hash callsign two bytes at a time 
	while ($i < $len) { 
		$hash ^= ord(substr($realcall, $i, 1))<<8; 
		$hash ^= ord(substr($realcall, $i + 1, 1)); 
		$i += 2; 
	} 

	// mask off the high bit so number is always positive 
	return $hash & 0x7fff; 
} 

?>
```
Due to regulations in the HAM radio licence, encryption is not allowed. But authentication is allowed. That is why password are used to distinguish  between users. 

# How to use 

First open up [https://apps.magicbug.co.uk/passcode/] and generate a password for the callsign you want to use. Open up the aprssend.py file and add the credentials include the location, symbol you want to use.

For added effect you can add this to a crontab to run at specified time frames. 

# Disclaimer

This is for educational purposes only. It is to show the fundamental flaw of the APRS network. It is not meant to be "used" in a real world scenario. 