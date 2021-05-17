import re
import os
import sys
os.chdir("/Users/likaixuan/Documents/IBI1_2020-21/IBI1_2020-21/Practical8\\via")
file1 = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
file2 = open('unknown_function.fa','w')
line = next(file1,'0')
while True:
    if line.startswith('>'):
        if re.search(r'unknow function',line):
            m = re.findall(r'>(\S+)_',line)
            s = ''

            while True:
                line = next(file1,'0')
                if line.startswith('>') or (line == '0'):
                    break
                line1 = line.replace('\n','')
                s = s + line1
            f = ">>"+m[0]
            file2.write(f'{f:14}')
            file2.write(str(int(len(s))))
            file2.write('\n')
            file2.write(s)
            file2.write('\n')

    if line == '0':
        break
    line = next(file1,'0')
    file1.close()
    file2.close()





