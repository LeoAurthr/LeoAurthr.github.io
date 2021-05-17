def DNA_complemnet (seq):
    seq = seq.upper()
    seq = seq.replace('A','T')
    seq = seq.replace('T','A')
    seq = seq.replace('C','G')
    seq = seq.replace('G','C')
    seq = seq.replace('a','t')
    seq = seq.replace('t','a')
    seq = seq.replace('c','g')
    seq = seq.replace('g','c')
    return seq

def DNA_reverse(seq):
    seq = seq.upper()
    return seq[::-1]

def DNA_revcomp(seq):
    seq = seq.upper()
    return DNA_complement(seq)[::-1]

def read_seq(inputfile):
    file = open(inputfile,"r")
    seq = file.read()
    seq = seq.replace("\n","")
    seq = seq.replace("\r","")
    return seq

if __name__ == '__main__':
    DNA = read_seq(XXXXX) #file
    print(DNA)  #原DNA序列
    print(DNA_complemnet(DNA))  #DNA互补序列
    print(DNA_reverse(DNA))  #DNA反向序列
    print(DNA_revcomp(DNA))  #DNA反向互补序列






class Students(object):
    def __init__(self,full_name,undergraduate_programme):
        self.full_name = read_self(XXXXXX)  #inputfile
        self.undergraduate_programme = read_self(XXXXXX)  #inputfile
        self.full_name = full_name
        self.undergraduate_programme = undergraduate_programme
        return (self.full_name,self.undergraduate_programme)
    print(self.full_name,self.undergraduate_programme)






def calculator(name,code,poster,final):
    code = int(code)
    poster = int(poster)
    final = int(final)
    all = ((code/100)*40 + (poster/100)*30 + (final/100)*30)
    return (name + ''''s Score for IBI1 is'''+ all)

print(calculator('Yuefeng','90','90','90'))








