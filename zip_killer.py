#!/usr/bin/python
# -*- coding: utf-8 -*-

# Importing Required modules

import time
import optparse
import zipfile
import os

# Banner for Zip Killer

xyz = \
    '''\033[1;35m
            /$$                 /$$       /$$ /$$ /$$                    
          |__/                | $$      |__/| $$| $$                    
 /$$$$$$$$ /$$  /$$$$$$       | $$   /$$ /$$| $$| $$  /$$$$$$   /$$$$$$ 
|____ /$$/| $$ /$$__  $$      | $$  /$$/| $$| $$| $$ /$$__  $$ /$$__  $$
   /$$$$/ | $$| $$  \ $$      | $$$$$$/ | $$| $$| $$| $$$$$$$$| $$  \__/
  /$$__/  | $$| $$  | $$      | $$_  $$ | $$| $$| $$| $$_____/| $$      
 /$$$$$$$$| $$| $$$$$$$/      | $$ \  $$| $$| $$| $$|  $$$$$$$| $$      
|________/|__/| $$____/       |__/  \__/|__/|__/|__/ \_______/|__/      
              | $$                                                      
              | $$                                                      
              |__/                
                                      
                        \033[1;31mCrack Zip File Password \033[1;33m
                +======================================+  
                #           Version : v1.0             #
	        #        ---------------------	       #
		# Developed By : Encryptor             #
		# Author       : Sathyaprakash Sahoo   #
                # Instagram    : _.encryptor._         #  
                # Website      : www.cyberbuddy.co.in  #  
                # Github       : Encryptor-Sec         #
                +======================================+  

-------OPTIONS-------

[1] Crack Zip File
[2] Exit Tool        
\033[0m                                                                          
'''
print xyz


# Main Function

def main():
    x = input('[+] Select an Option : ')
    if x == 1:

    # Input path for zip file

        file_path = raw_input('[+] Enter Zip File Path : ')
        file_path = file_path.replace(' ', '')

    # Input path for wordlist file

        word_list = raw_input('[+] Enter Wordlist Path : ') \
            or '/usr/share/wordlists/rockyou.txt'  # Default Rockyou dictionary file
        word_list = word_list.replace(' ', '')
        z_file = zipfile.ZipFile(file_path)
        pwd_list = open(word_list)
        print "\033[\n1;32m[+] Brute Force Initiated ..."
        print "\033[\n1;36m[+] Checking For Correct Password ..."
        for line in pwd_list.readlines():
            passwd = line.strip('\n')

    # Password Brute Forcing

            try:
                z_file.extractall(pwd=passwd)
                print "\033[\n1;31m[+] Congrats!! Password Found : " \
                    + passwd + "\n\033[0m"
                if passwd != '':
                    quit()
            except Exception:
                pass
        print """
\033[1;31m[+] Password Not Found in Given Wordlist 
\033[0m"""
    else:
        print """\033[1;31m
Thank You !! 
\033[0m"""
        time.sleep(1)
        quit()


if __name__ == '__main__':
    main()

