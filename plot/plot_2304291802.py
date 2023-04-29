#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

import smplotlib
plt.rcParams["markers.fillstyle"] = "full"

# データの読み込み
data = np.loadtxt('input.data')
s, l, ds, dl = data[:,0], data[:,1], data[:,2], data[:,3]

l0 = 589.6
xerr=np.full(len(s),1.5/l0)

# フィッティング関数
def fitting_func(x, a, b):
    return a * x + b

# フィッティング
popt, pcov = curve_fit(fitting_func, 1/(l/l0)**2, s)

# データのプロット
fig, ax = plt.subplots(figsize=(8, 5))

# 定数 a, b の値と1-sigma誤差の取得
a, b = popt
a_err, b_err = np.sqrt(np.diag(pcov))

# フィッティング曲線のプロット
xfit = np.linspace(0.0,2.0,100)
yfit = fitting_func(xfit, a, b)
ax.plot(xfit, yfit, 'r--', label=r'Fit: scale$ = a(\lambda/\lambda_0)^{-2} + b$')
ax.errorbar(1/(l/l0)**2, s, xerr=xerr, yerr=ds, 
	fmt='o', capsize=0, markersize=6, alpha=1.0,
	markerfacecolor=None,markeredgecolor='k',
	label='Measurement')

# 軸の範囲の設定
ax.set_xlim(0.0,2.0)
ax.set_ylim(0.0,5.0)

# ラベルの設定
ax.set_xlabel(r'$(\lambda/\lambda_0)^{-2}$')
ax.set_ylabel('Scale (cm)',labelpad=15)

# グリッドの表示
ax.grid(True)

# 凡例の表示
legend_text = f'$\lambda_0$ = {l0:.1f} nm\na = {a:.2f} $\pm$ {a_err:.2f} cm\nb = {b:.2f} $\pm$ {b_err:.2f} cm'
ax.legend(title=legend_text)

# 保存
plt.savefig('sample2.pdf')

