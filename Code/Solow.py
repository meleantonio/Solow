# This file will contain the class for the Solow model
class Solow:
  def __init__(self, a=1/3, g=0, n=0, d=0.02, s=0.1, K_0=1, A_0=1, L_0=1):
    self.a = a # 'a' is the share of output that will be attributed to capital, '(1 - a)' will be that attributed to effective labour 
    self.g = g # 'g' is the growth rate of tfp per time period
    self.n = n # 'n' is the population growth rate 
    self.d = d # 'd' is the year to year depreciation rate of capital 
    self.s = s # 's' is the saving rate
    self.K = K_0 # 'K' is the total capital in the economy, L_0 being the initial value
    self.A = A_0 # 'A' is the total tfp of the economy, A_0 being the initial value   
    self.L = L_0 # 'L' is the total level of labour in the economy, K_0 being the inital value
    self.Y = self.K ** self.a * (self.A * self.L) ** (1 - self.a) # The output level of the Solow model economy
    self.I = self.s * self.Y # 'I' is the investment level when a rate s of total level of capital is saved
    self.C = (1 - self.s) * self.Y # 'C' is the aggregate consumption level
    self.D = self.d * self.K # 'D' is the aggregate depreciation level
    self.ke = self.K / (self.A * self.L) # 'ke' is the level of capital per effective unit of labour
    self.k = self.K / self.L # 'k' (lowercase) is the level of perworker capital
    self.y = self.Y / self.L # 'y' (lowercase) is the level of perworker output
    self.i = self.I / self.L # 'i' (lowercase) is the level of perworker investment
    self.c = self.C / self.L # 'c' (lowercase) is the level of perworker consumption
    self.k_star = 0
    try: # Checking if we don't divide by zero
      self.k_star = (self.s / (self.g + self.n + self.d + self.g * self.n))**(1/(1-self.a)) #'k_star' is the steady state level of per worker capital, where capital in the next period is equal to capital in the current period
    except:
      if s > 0:
        print('Great, you will have sustained economic growth!')

  # A function that gives the change in the aggregate capital for one time step
  def capital_change(self):
    return self.I - self.D

  # A function that changes the capital for one time step
  def update_capital(self):
    self.K += self.capital_change()

  # A function that gives the change in the tfp for one time step
  def tfp_change(self):
    return self.g * self.A

  # A function that changes the tfp for one time step
  def update_tfp(self):
    self.A += self.tfp_change()

  # A function that gives the change in the aggregate labour for one time step
  def labour_change(self):
    return self.n * self.L

  # A function that changes the labour for one time step
  def update_labour(self):
    self.L += self.labour_change()

  # A function that gives the change in economy output according to the Solow model
  def output_change(self):
    return (self.K ** self.a) * ((self.A * self.L) ** (1 - self.a)) - self.Y

  # A function that updates the economy output according to the Solow model
  def update_output(self):
    self.Y += self.output_change()

  # A function that gives the change in the aggregate investment level for one time step
  def investment_change(self):
    return self.s * self.Y - self.I

  # A function that updates the investment
  def update_investment(self):
    self.I += self.investment_change()

  # A function that gives the change in the aggregate consumption level for one time step
  def consumption_change(self):
    return (1 - self.s) * self.Y - self.C

  # A function that updates the consumption
  def update_consumption(self):
    self.C += self.consumption_change()

  # A function that gives the change in the aggregate depreciation level for one time step
  def depreciation_change(self):
    return self.d * self.K - self.D

  # A function that updates the depreciation
  def update_depreciation(self):
    self.D += self.depreciation_change()

  # A function that gives the change in the level of capital per effective unit of labour
  def capital_per_effective_labour_change(self):
    return self.K / (self.A * self.L) - self.ke

  # A function that updates the capital per effective unit of labour
  def update_capital_per_effective_labour(self):
    self.ke += self.capital_per_effective_labour_change()

  # A function that gives the change in the capital per capita level for one time step
  def capital_per_capita_change(self):
    return self.K / self.L - self.k

  # A function that updates the capital per capita
  def update_capital_per_capita(self):
    self.k += self.capital_per_capita_change()

  # A function that gives the change in the capital per capita level for one time step
  def output_per_capita_change(self):
    return self.Y / self.L - self.y

  # A function that updates the output per capita
  def update_output_per_capita(self):
    self.y += self.output_per_capita_change()

  # A function that gives the change in the investment per capita level for one time step
  def investment_per_capita_change(self):
    return self.I / self.L - self.i

  # A function that updates the investment per capita
  def update_investment_per_capita(self):
    self.i += self.investment_per_capita_change()

  # A function that gives the change in the consumption per capita level for one time step
  def consumption_per_capita_change(self):
    return self.C / self.L - self.c

  # A function that updates the consumption per capita
  def update_consumption_per_capita(self):
    self.c += self.consumption_per_capita_change()

  # A function that updates the properties of the class for one time step
  def step(self):
    # Getting output determinant changes
    capital_change = self.capital_change()
    tfp_change = self.tfp_change()
    labour_change = self.labour_change()

    # Updating the variables that determine the output
    self.update_capital()
    self.update_tfp()
    self.update_labour()

    # Getting output variable change
    output_change = self.output_change()

    # Updating output
    self.update_output()

    # Getting other variable changes
    investment_change = self.investment_change()
    consumption_change = self.consumption_change()
    depreciation_change = self.depreciation_change()

    capital_per_effective_labour_change = self.capital_per_effective_labour_change()
    capital_per_capita_change = self.capital_per_capita_change()
    output_per_capita_change = self.output_per_capita_change()
    investment_per_capita_change = self.output_per_capita_change()
    consumption_per_capita_change = self.consumption_per_capita_change()

    # Updating other variable changes
    self.update_investment()
    self.update_consumption()
    self.update_depreciation()

    self.update_capital_per_effective_labour()
    self.update_capital_per_capita()
    self.update_output_per_capita()
    self.update_investment_per_capita()
    self.update_consumption_per_capita()

    # Returning a row of data to be inserted in the dataset of the simulation
    return [self.Y, self.K, self.A, self.L, self.I, self.C, self.D, output_change, capital_change, tfp_change, labour_change, investment_change, consumption_change, depreciation_change, self.y, self.ke, self.k, self.i, self.c, output_per_capita_change, capital_per_effective_labour_change, capital_per_capita_change, investment_per_capita_change, consumption_per_capita_change]

  def simulate(self, steps):
    title = f'Solow model simulation with the parameter values of a={self.a}, g={self.g}, n={self.n}, d={self.d}, s={self.s}.'
    dataset = [['Output', 'Capital', 'TFP', 'Labour', 'Investment', 'Consumption', 'Depreciation', 'Output Change', 'Capital Change', 'TFP Change', 'Labour Change', 'Investment Change', 'Consumption Change', 'Depreciation Change', 'Output / Capita', 'Capital / Effective Labour', 'Capital / Capita', 'Investment / Capita', 'Consumption / Capita', 'Output / Capita Change', 'Capital / Effective Labour Change', 'Capital / Capita Change', 'Investment / Capita Change', 'Consumption / Capita Change']]
    dataset.append([self.Y, self.K, self.A, self.L, self.I, self.C, self.D, 0, 0, 0, 0, 0, 0, 0, self.y, self.ke, self.k, self.i, self.c, 0, 0, 0, 0, 0])
    for i in range(steps):
      dataset.append(self.step())
    return title, dataset
  
  # A function that permanently updates the parameter values that are put in
  def update_parameters(self, a=None, g=None, n=None, d=None, s=None, K=None, A=None, L=None):    
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