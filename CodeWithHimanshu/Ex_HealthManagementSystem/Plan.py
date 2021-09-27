print("Do you want to 1-Log or 2-Retrieve the details?")
logRet = int(input())
print("Do you want to log 1-Diet or 2-Exercise?")
dietEx = int(input())
newLog = input("Log the details") if logRet == 1 else print("Below are the required details")

if dietEx == 1:
    with open("DietHimanshu.txt", 'r+') as f:
        if logRet == 1:
            f.write(newLog)
        else:
            print(f.readlines())
else:
    with open("ExersiseHimanshu.txt", 'r+') as f:
        if logRet == 1:
            f.write(newLog)
        else:
            print(f.readlines())
