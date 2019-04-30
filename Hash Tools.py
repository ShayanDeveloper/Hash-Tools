import os, random, time, sys
from hashlib import *
from datetime import datetime

dirs = ['Results','Results/Generator','Results/Cracker','Results/Type','Results/Generator/MD5','Results/Generator/SHA1','Results/Generator/SHA224','Results/Generator/SHA256','Results/Generator/SHA384','Results/Cracker/MD5','Results/Cracker/SHA1','Results/Cracker/SHA224','Results/Cracker/SHA256','Results/Cracker/SHA384']
for Dir in dirs:
    try:
        os.mkdir(Dir)
    except:
        pass

CrackedHashes = []
Colors = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m', '\033[39m']
def Print_Logo():
    Logo = '''

                        '##::::'##::::'###:::::'######::'##::::'##:
                         ##:::: ##:::'## ##:::'##... ##: ##:::: ##:
                         ##:::: ##::'##:. ##:: ##:::..:: ##:::: ##:
                         #########:'##:::. ##:. ######:: #########:
                         ##.... ##: #########::..... ##: ##.... ##:
                         ##:::: ##: ##.... ##:'##::: ##: ##:::: ##:
                         ##:::: ##: ##:::: ##:. ######:: ##:::: ##:
                                ---------------------------
                                +  Powered By ZetaTech_iR +
                                +     TG: @ZetaTech_iR    +
                                +  Coded By .::Shayan::.  +
                                ---------------------------                                   
                    '########::'#######:::'#######::'##::::::::'######::
                    ... ##..::'##.... ##:'##.... ##: ##:::::::'##... ##:
                    ::: ##:::: ##:::: ##: ##:::: ##: ##::::::: ##:::..::
                    ::: ##:::: ##:::: ##: ##:::: ##: ##:::::::. ######::
                    ::: ##:::: ##:::: ##: ##:::: ##: ##::::::::..... ##:
                    ::: ##:::: ##:::: ##: ##:::: ##: ##:::::::'##::: ##:
                    ::: ##::::. #######::. #######:: ########:. ######::

                                  [*]Choose an option :

                          [1]Hash Generator | [2]Hash Cracker
                                       [3]Hash Type
                  '''
    for Line in Logo.split('\n'):
        time.sleep(0.1)
        print(random.choice(Colors)+Line)
def Clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def C():
    return random.choice(Colors)

def MainCrack(Word,Hash,Type,Date):
    Htype = None
    Name = ''
    if Type == 1:#MD5
        Htype = md5()
        Name = 'MD5'
    elif Type == 2:#SHA1
        Htype = sha1()
        Name = 'SHA1'
    elif Type == 3:#SHA224
        Htype = sha224()
        Name = 'SHA224'
    elif Type == 4:#SHA256
        Htype = sha256()
        Name = 'SHA256'
    elif Type == 5:#SHA384
        Htype = sha384()
        Name = 'SHA384'
    Htype.update(bytes(Word,'utf-8'))
    PassHashed = Htype.hexdigest()
    if PassHashed == Hash:
        print(C()+Name+C()+' -> '+C()+Word+C()+':'+C()+Hash)
        CrackedHashes.append(Hash)
        with open('Results/Cracker/'+Name+'/Cracked['+Date+'].txt','a') as op:
            op.write(Word+'\n')
        print('\n')

def Type():
    f_name = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    Clear()
    try:
        os.mkdir('Results/Type/'+f_name)
    except:
        pass
    print(C()+' Please Enter Hashes Path To Check Types')
    path = input(C()+'  > ')
    read = open(path,'r').read().splitlines()
    Clear()
    time.sleep(5)
    for Hash in read:
        if len(Hash) == 32:#MD5
            print(C()+Hash+C()+' -> '+C()+'MD5!')
            with open('Results/Type/'+f_name+'/MD5.txt','a') as op:
                op.write(Hash+'\n')
            print('\n')
        elif len(Hash) == 40:#SHA1
            print(C()+Hash+C()+' -> '+C()+'SHA1!')
            with open('Results/Type/'+f_name+'/SHA1.txt','a') as op:
                op.write(Hash+'\n')
            print('\n')
        elif len(Hash) == 56:#SHA224
            print(C()+Hash+C()+' -> '+C()+'SHA224!')
            with open('Results/Type/'+f_name+'/SHA224.txt','a') as op:
                op.write(Hash+'\n')
            print('\n')
        elif len(Hash) == 64:#SHA256
            print(C()+Hash+C()+' -> '+C()+'SHA256!')
            with open('Results/Type/'+f_name+'/SHA256.txt','a') as op:
                op.write(Hash+'\n')
            print('\n')
        elif len(Hash) == 96:#SHA384
            print(C()+Hash+C()+' -> '+C()+'SHA384!')
            with open('Results/Type/'+f_name+'/SHA384.txt','a') as op:
                op.write(Hash+'\n')
            print('\n')
        else:
            print(C()+Hash+C()+' -> '+C()+'Not Found!')
            with open('Results/Type/'+f_name+'/Not Found.txt','a') as op:
                op.write(Hash+'\n')
            print('\n')
    print(C()+'\n\n\nFinished!')
    input(C()+'Press `Enter` To Continue...')

def Generator():
    f_name = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    Clear()
    print(C()+' Please Enter Texts Path To Convert')
    path = input(C()+'  > ')
    read = open(path,'r').read().splitlines()
    print('''
    {C1}Choose The Hash Type To Convert:
    {C2}[{C3}1{C4}]{C5}MD5    {C6}|{C7} [{C8}2{C9}]{C10}SHA1   {C11}|{C12} [{C13}3{C14}]{C15}SHA224
    {C16}[{C17}4{C18}]{C20}SHA256 {C21}|{C22} [{C23}5{C24}]{C25}SHA384
    
    '''.format(C1=C(),C2=C(),C3=C(),C4=C(),C5=C(),C6=C(),C7=C(),C8=C(),C9=C(),C10=C(),C11=C(),C12=C(),C13=C(),C14=C(),C15=C(),C16=C(),C17=C(),
    C18=C(),C19=C(),C20=C(),C21=C(),C22=C(),C23=C(),C24=C(),C25=C(),C26=C(),C27=C(),C28=C(),C29=C(),C30=C(),))
    Type = input(C()+'> ')
    if int(Type) <= 6:
        pass
    else:
        sys.exit(0)
    Clear()
    time.sleep(3)
    for text in read:
        Htype = None
        Name = ''
        if int(Type) == 1:#MD5
            Htype = md5()
            Name = 'MD5'
        elif int(Type) == 2:#SHA1
            Htype = sha1()
            Name = 'SHA1'
        elif int(Type) == 3:#SHA224
            Htype = sha224()
            Name = 'SHA224'
        elif int(Type) == 4:#SHA256
            Htype = sha256()
            Name = 'SHA256'
        elif int(Type) == 5:#SHA384
            Htype = sha384()
            Name = 'SHA384'
        Htype.update(bytes(text,'utf-8'))
        myHash = Htype.hexdigest()
        print(C()+Name+C()+' -> '+C()+text+C()+':'+C()+myHash)
        with open('Results/Generator/'+Name+'/Generated['+f_name+'].txt','a') as op:
            op.write(myHash+'\n')
        print('\n')
    print(C()+'\n\n\nFinished!')
    input(C()+'Press `Enter` To Continue...')

def Cracker():
    Clear()
    print(C()+' Please Enter Hashes Path To Crack')
    path = input(C()+'  > ')
    read_hashes = open(path,'r').read().splitlines()
    print(C()+' Please Enter Wordlist Path To Crack')
    path = input(C()+'  > ')
    read_wordlist = open(path,'r').read().splitlines()
    print('''
    {C1}Choose The Hash Type To Crack:
    {C2}[{C3}1{C4}]{C5}MD5    {C6}|{C7} [{C8}2{C9}]{C10}SHA1   {C11}|{C12} [{C13}3{C14}]{C15}SHA224
    {C16}[{C17}4{C18}]{C20}SHA256 {C21}|{C22} [{C23}5{C24}]{C25}SHA384
    
    '''.format(C1=C(),C2=C(),C3=C(),C4=C(),C5=C(),C6=C(),C7=C(),C8=C(),C9=C(),C10=C(),C11=C(),C12=C(),C13=C(),C14=C(),C15=C(),C16=C(),C17=C(),
    C18=C(),C19=C(),C20=C(),C21=C(),C22=C(),C23=C(),C24=C(),C25=C(),C26=C(),C27=C(),C28=C(),C29=C(),C30=C(),))
    Type = input(C()+'> ')
    if int(Type) <= 6:
        pass
    else:
        sys.exit(0)
    Clear()
    time.sleep(3)
    f_name = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')    
    for Hash in read_hashes:
        if not Hash in CrackedHashes:
            for Word in read_wordlist:
                if not Hash in CrackedHashes:
                    MainCrack(Word,Hash,int(Type),f_name)
            
    print(C()+'\n\n\nFinished!')
    input(C()+'Press `Enter` To Continue...')

while True:
    Clear()
    Print_Logo()
    op = int(input(C()+'                    > '))
    del CrackedHashes[:]
    if op == 1:
        Generator()
    elif op == 2:
        Cracker()
    elif op == 3:
        Type()
    else:
        sys.exit(0)