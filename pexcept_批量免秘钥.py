#!/usr/bin/env python3.6
# -*- coding:utf8 -*-
## 放在mac环境执行成功，但是命令行跳转还是需要密码，
###放到linux环境执行此脚本完全OK.

import sys
import pexpect

user = 'dada'
password = 'dada'
expect_list = ['(yes/no)', 'password:']
with open('/tmp/IPs.txt','r')as f:
    for ip in f.readlines():
        p = pexpect.spawn('ssh-copy-id %s@%s' % (user,ip))
        try:
            while True:
                idx = p.expect(expect_list)
                # print (p.before + expect_list[idx])
                if idx == 0:
                    print ("yes")
                    p.sendline('yes')
                elif idx == 1:
                    print ('password:',password)
                    p.sendline(password)
        except pexpect.TIMEOUT:
            print (sys.stderr, 'timeout')
        except pexpect.EOF:
            print (p.before)
            print (sys.stderr, '<the end>')




#####------#####

import sys
import pexpect


google_auth = str(input("Pls enter google auth code here :"))
if len(google_auth) == 6 and google_auth.isdigit():
    user = 'chen.qingyan'
    password = 'xxxxxx '+google_auth
    ip = "192.168.0.1"
    expect_list = ['(yes/no)', 'password:']
    p = pexpect.spawn('ssh %s@%s' % (user, ip))
    try:
        while True:
            idx = p.expect(expect_list)
            # print (p.before + expect_list[idx])
            if idx == 0:
                print ("yes")
                p.sendline('yes')
            elif idx == 1:
                print ('password:',password)
                p.sendline(password)
    except pexpect.TIMEOUT:
        print (sys.stderr, 'timeout')
    except pexpect.EOF:
        print (p.before)
        print (sys.stderr, '<the end>')
else:
    print("google auth code error !")
    sys.exit(500)
