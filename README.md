# Intro
![alt](https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fqrznow.com%2Fwp-content%2Fuploads%2F2015%2F11%2Faprsfi-largerlogo-blog-scaled.png&f=1&nofb=1)
Ever had that one guy on APRS who just likes to list fake repeaters? No worries, I Got you covered. If anything you can always use this little script to update your location via APRS-IS using python. Just fill in your details and away you go.  
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
One time passwords could be used to further authenticate the users. The hash could be computed unique to each user and can be used in conjunction with apps like Google Authenticator. 
When creating your own APRS applications you can implement OTP to be included using only a few lines of code. 

Here is an example : 
```
import onetimepass as otp
def otpcheck(my_token):
    my_secret = "insert md5 hash here"
    #my_token = 662120
    is_valid = otp.valid_totp(token=my_token, secret=my_secret)
    print(is_valid)

if __name__ == '__main__':
    otpcheck("")
```
Now when coding up your APRS decoder you can use a simple check to see if the token is valid. Example from previous project which use an RTLsdr dongle for APRS decoding:

```
  def log_warn(self, log_message):
        """Logs a warning message to console, file.
        Args:
            log_message: The string message to log.
        """
        self.__log_any(Colors.YELLOW, self.WRN_PREFIX, log_message)
        logging.warning(log_message)
        packetexecute(log_message)
```

Inside the log packetexecute function which reads the raw packet
```
        newpacket = packetstring[packetstring.find("(")+1 : packetstring.find(")")]
```
This is just a proof of concept that could be implemented to allow for a more authentication method. 
# Notes
This is not something new. This is just a simple script to help you get started with APRS. In many cases I have found that the documentation surrounding APRS can be confusing as its a bit too detailed sometimes. This is a known security "issue" and has been abused plenty of times.
You don't need bulky programs to send out your fixed location, just fire up the script and add it to your crontab or scheduled task. 


# Disclaimer
This is for educational purposes only. It is to show the fundamental flaw of the APRS network. It is not meant to be "used" in a real world scenario. Doing this to cause harm to others is not the purpose of this project. Sometimes people are not aware of the damage they are doing, and they are not aware of the consequences. Educate them on why what they are doing is wrong. If that then fails, and they persist, more appropriate action should be taken to prevent harm to others.