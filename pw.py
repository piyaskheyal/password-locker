import sys
import pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
'luggage': '12345'}

if(len(sys.argv)<2):
    print("Usage: python3 [account_name]")
    sys.exit(1)
else:
    if(sys.argv[1] in PASSWORDS):
        pyperclip.copy(PASSWORDS[sys.argv[1]])
        print("Email passwored is copied to the clipboard")
    else:
        print("Entry is absent!")