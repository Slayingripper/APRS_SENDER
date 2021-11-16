# Intro
![alt](https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fqrznow.com%2Fwp-content%2Fuploads%2F2015%2F11%2Faprsfi-largerlogo-blog-scaled.png&f=1&nofb=1)
Ever had that one guy on APRS who just likes to list fake repeaters? No worries, I Got you covered. 
# The scenario
You have a list of repeaters that you want to use in your APRS network. But you have that one “ham” who just likes to list fake repeaters on APRS, so they can get attention. The problem is that even though this is a bit harmless, it's not a good idea to have a bunch of fake repeaters on APRS, as it will confuse a lot of people thinking that a repeater is actually there. Which in an emergency scenario could be a life or death situation. A real-world example of this is the Beirut explosion that happened in the year of 2020. Many people were killed, and many others were injured. Furthermore, many people were not aware of the explosion, and they were not aware of the fact that it was happening. Communications were down and the only thing that was working was radio. Many ham radio operators used repeaters from neighbouring countries to communicate with each other, such as Cyprus, Israel and Turkey. Many of these operators used Yagi antennas to point in the direction of the Repeaters, now imagine if the repeaters were not actually there what would happen. 
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
The password is generated using a known hash function, and the callsign is hashed using the same hash function. The result is a number between 0 and 32767. The password is then the result of the hash function, and the callsign is hashed again, and the result is the password.
Due to regulations in the HAM radio license, encryption is not allowed. But authentication is allowed. That is why passwords are used to distinguish  between users. 
# Requirments 
1. Python 3.7 +
2. Aprslib


# How to use 

1. First open up [https://apps.magicbug.co.uk/passcode/] and generate a password for the callsign you want to use. 
2. Open up the aprssend.py file and add the credentials include the location, symbol you want to use.
3. Reference the image bellow for symbols to use.
   ![alt](http://www.aprs.org/symbols/Icon-set.gif)
3. For added effect you can add this to a crontab to run at specified time frames. 
4. Use this responsibly 

# Improvements to security

# Disclaimer
This is for educational purposes only. It is to show the fundamental flaw of the APRS network. It is not meant to be "used" in a real world scenario. Doing this to cause harm to others is not the purpose of this project. Sometimes people are not aware of the damage they are doing, and they are not aware of the consequences. Educate them on why what they are doing is wrong. If that then fails, and they persist, more appropriate action should be taken to prevent harm to others.