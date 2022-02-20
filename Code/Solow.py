# This file will contain the class for the Solow model
class Solow:
  def __init__(self, a, g, n, d, s, K_0, A_0, L_0):
    # 'a' is the share of output that will be attributed to capital, '(1 - a)' will be that attributed to 
    self.a = a
    
    # 'g' is the growth rate of tfp per time period
    self.g = g
    
    # 'n' is the population growth rate 
    self.n = n

    # 'd' is the year to year depreciation rate of capital 
    self.d = d
    
    # 's' is the saving rate
    self.s = s

    # 'K' is the total capital in the economy, L_0 being the initial value
    self.K = K
    
    # 'A' is the total tfp of the economy, A_0 being the initial value
    self.A = A
    
    # 'L' is the total level of labour in the economy, K_0 being the inital value
    self.L = L

    # The Solow model economy output
    self.Y = K ** a * (A * L) ** (1 - a)

    # 'I' is the investment level when a rate s of total level of capital is saved, I_0 is the inital value
    self.I = s * self.Y

  # Todo: A function that changes the capital after one time step
  def capital(self):
    return self

  # Todo: A function that changes the labour after one time step
  def labour(self):
    return self
  
  # A function that updates the parameter values that are put in
  def update(self, a=None, g=None, n=None, d=None, s=None, K=None, A=None, L=None):    
    # If the argument is not none, change the parameter value of the class
    if a:
      self.a = a
    if g:
      self.g = g
    if n:
      self.n = n
    if d:
      self.d = d
    if s:
      self.s = s
    if K:
      self.K = K
    if A:
      self.A = A
    if L:
      self.L = L
    
  # A function that updates the properties of the class for one time step
  def step(self):
    return self