# This file will contain the class for the Solow model
class Solow:
  def __init__(self, a, g, n, d, s, K_0, A_0, L_0):
    self.a = a # 'a' is the share of output that will be attributed to capital, '(1 - a)' will be that attributed to effective labour 
    self.g = g # 'g' is the growth rate of tfp per time period
    self.n = n # 'n' is the population growth rate 
    self.d = d # 'd' is the year to year depreciation rate of capital 
    self.s = s # 's' is the saving rate
    self.K = K_0 # 'K' is the total capital in the economy, L_0 being the initial value
    self.A = A_0 # 'A' is the total tfp of the economy, A_0 being the initial value   
    self.L = L_0 # 'L' is the total level of labour in the economy, K_0 being the inital value
    self.Y = self.K ** self.a * (self.A * self.L) ** (1 - self.a) # The output level of the Solow model economy
    self.I = self.s * self.Y # 'I' is the investment level when a rate s of total level of capital is saved, I_0 is the inital value
    
  # Todo: A function that changes the capital after one time step
  def capital_next_period(self):
    return self

  # Todo: A function that changes the labour after one time step
  def labour_next_period(self):
    return self
  
  # A function that permanently updates the parameter values that are put in
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