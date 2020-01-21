import numpy as np

print(np.fv(0.05/12, 10*12, -100, -100))

'''
numpy.fv(rate, nper, pmt, pv[, when='end'])
#参数：
rate：每一期的利率（rate of interest）。数值或矩阵(M, )。
nper：期数。
pmt：payment。
pv：present value，现值。
when：{{‘begin’, 1}, {‘end’, 0}}, {string, int}, optional.
'''