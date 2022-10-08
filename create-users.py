#!/usr/bin/python3
import os
import re
import sys
def main():
    for line in sys.stdin:
        m = re.match('^\s*#.*$',line)
        print(m)
        fields = line.strip().split(':')
        if m or len(fields) != 5:
            continue
        username = fields[0]
        password = fields[1]
        gecos = "{f3} {f2},,,".format(f3=fields[3], f2=fields[2])
        groups = fields[4].split(",")

        print("==> Creating account for {username}...".format(username=username))
        cmd = "usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}".format(gecos=gecos, username=username)
        print(cmd)
        os.system(cmd)

        print("==> Setting the password for {username}...".format(username=username))
        cmd = "/bin/echo -ne {password}\n{password} | /usr/bin/sudo /usr/bin/passwd {username}".format(password=password)
        print(cmd)
        os.system(cmd)

        for group in groups:
            if group != "-":
                print("==> Assigning {username} to the {group} group...".format(username=username, group=group))
                cmd = "/usr/sbin/adduser {username} {group}".format(username=username, group=group)
                print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()

