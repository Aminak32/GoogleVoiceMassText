
#!/usr/bin/python

import sys
import time

from googlevoice import Voice
from googlevoice.util import input

voice = Voice()
voice.login()

# Jeff K
voice.send_sms(6163253722, sys.argv[1])

# Matt P
voice.send_sms(5172701948, sys.argv[1])

# Alec S
voice.send_sms(6023171077, sys.argv[1])

# Sam M
voice.send_sms(6512696132, sys.argv[1])

# Mike S
voice.send_sms(6162998711, sys.argv[1])

#Pause to avoid flood protection
time.sleep(10)

#Alex O
voice.send_sms(2316763291, sys.argv[1])

#Josh M
voice.send_sms(2483967666, sys.argv[1])

#Brett B
voice.send_sms(2484622725, sys.argv[1])

#Ryan H
voice.send_sms(5862193245, sys.argv[1])

#Jermey C
voice.send_sms(9892255512, sys.argv[1])

#Pause
time.sleep(10)

#Eric R
voice.send_sms(8103946039, sys.argv[1])

#Cam S
voice.send_sms(9063609011, sys.argv[1])

#Noah R
voice.send_sms(2484590883, sys.argv[1])

#Richard Taglione
voice.send_sms(9063690239, sys.argv[1])
