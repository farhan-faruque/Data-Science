from thinkstats import Mean

def Pumpkin(seq):
  mean = Mean(seq)
  print "mean -",mean

def main(name, data_dir='.'):
    Pumpkin([1,2,3,4,5])

if __name__ == '__main__':
    import sys
    main(*sys.argv)
