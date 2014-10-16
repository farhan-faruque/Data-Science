
class Complex:

  def __init__(self,real,imagin):
    self.real = real;
    self.imagin = imagin;

  def toString(self):
    return str(self.real)+'+'+str(self.imagin)+'i'

class ReComplex(Complex):
  

x = Complex(2,5);
print x.toString()
