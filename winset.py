import subprocess
import os

help="classic apps:\n1. classic settings (control)\n2. classic uninstall (appwiz.cpl)\n3. system properties (sysdm.cpl)\n4. device amanger (diskmgmt.msc)\n5. classic network-connections (ncpa.cpl)\n6. firewall advanced settings (wf.msc)\n7. local group policy editor (pro/enterprise) (gpedit.msc)\n8. task scheduler (taskschd.msc)\n9. service manager (services.msc)\n10. performance manager (perfmon)\n11. windows memory diagnostic (mdsched.exe)\n12. User Accounts (netplwiz) L. list again\nQ. exit"
print(help)
while True:
    uinput=input(":")
    if not uinput:
        print("no input")
        continue
    if uinput=="1":
        subprocess.run("control", shell=True)
    elif uinput=="2":
        subprocess.run("control appwiz.cpl", shell=True)
    elif uinput=="3":
        subprocess.run("sysdm.cpl", shell=True)
    elif uinput=="4":
        subprocess.run("devmgmt.msc", shell=True)
    elif uinput=="5":
        subprocess.run("ncpa.cpl", shell=True)
    elif uinput=="6":
        subprocess.run("wf.msc", shell=True)
    elif uinput=="7":
        subprocess.run("gpedit.msc", shell=True)
    elif uinput=="8":
        subprocess.run("taskschd.msc", shell=True)
    elif uinput=="9":
        subprocess.run("services.msc", shell=True)
    elif uinput=="10":
        subprocess.run("perfmon", shell=True)
    elif uinput=="11":
        subprocess.run("mdsched.exe", shell=True)
    elif uinput=="12":
        subprocess.run("netplwiz", shell=True)
    elif uinput.upper()=="L":
        print(help)
    elif uinput.upper()=="Q":
        os._exit(0)
    else:
        print("invalid input")