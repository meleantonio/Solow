from re import A
from tkinter import N


class Model:
  def __init__(self, a, g, n, d, s, A, K, L):
    self.a = a
    self.g = g
    self.n = n
    self.d = d
    self.s = s
    self.A = A
    self.K = K
    self.L = L
    self.I = s * K
    self.Y = K ** a * (A * L) ** (1 - a)

  def capital(self):
    # Todo: write function of changes to capital
    return self

  def labour(self):
    # Todo: write function for changes to the labour force
    return self