import thinkstats2

def ReadFemPreg(dct_file = '2002FemPreg.dct',data_file = '2002FemPreg.dat.gz'):
  dct = thinkstats2.ReadStateDct(dct_file)
  df = dcts.ReadFixedWidth(data_file,compression = 'gzip')
  CleanFemPreg(df)
  return df

def CleanFemPreg(df):
  df.agepreg / = 100.0
  na_vals = [97,98,99]
  #df.birthwgt_lb.replace(na_vals,np.nan, inplace = True)
  df.birthwgt_lb[df.birthwgt_lb > 20] = np.nan
  df.birthwgt_oz.replace(na_vals,np.nan, inplace = True)
  df['totalwgt_lb'] = df.birthwgt_lb + df.birthwgt_oz / 16.0

def MakePregMap(df):
  d = defaultdict(list)
  
