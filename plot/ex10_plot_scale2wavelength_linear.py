#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

import smplotlib
plt.rcParams["markers.fillstyle"] = "full"

# データの読み込み
data = np.loadtxt('input.data')
s, l, ds, dl, atom = data[:,0], data[:,1], data[:,2], data[:,3], data[:,4]

l0 = 589.6
xerr=np.full(len(s),1.5/l0)

# フィッティング関数
def fitting_func(x, a, b):
    return a * x + b

# フィッティング
popt, pcov = curve_fit(fitting_func, s, 1/(l/l0)**2)

# データのプロット
fig, ax = plt.subplots(figsize=(8, 5))

# 定数 a, b の値と1-sigma誤差の取得
a, b = popt
a_err, b_err = np.sqrt(np.diag(pcov))

# フィッティング曲線のプロット
xfit = np.linspace(0.0,5.0,100)
yfit = fitting_func(xfit, a, b)
ax.plot(xfit, yfit, 'r--', label=r'Fit: $(\lambda/\lambda_0)^{-2}=$ a * scale + b')
ax.errorbar(s[atom==1], 1/(l[atom==1]/l0)**2,  
	xerr=xerr[atom==1], yerr=ds[atom==1], 
	fmt='s', capsize=0, markersize=6, alpha=1.0,
	markerfacecolor='k',markeredgecolor='k',
	label='Na')
ax.errorbar(s[atom==2], 1/(l[atom==2]/l0)**2,  
	xerr=xerr[atom==2], yerr=ds[atom==2], 
	fmt='o', capsize=0, markersize=6, alpha=1.0,
	markerfacecolor='k',color='k',markeredgecolor='k',
	label='Hg')
ax.errorbar(s[atom==3], 1/(l[atom==3]/l0)**2,  
	xerr=xerr[atom==3], yerr=ds[atom==3], 
	fmt='^', capsize=0, markersize=6, alpha=1.0,
	markerfacecolor='k',color='k',markeredgecolor='k',
	label='Cd')

# 軸の範囲の設定
ax.set_xlim(0.0,5.0)
ax.set_ylim(0.0,2.0)

# ラベルの設定
ax.set_xlabel('Scale',labelpad=15)
ax.set_ylabel(r'$(\lambda/\lambda_0)^{-2}$')

# グリッドの表示
ax.grid(True)

# 凡例の表示
legend_text = f'$\lambda_0$ = {l0:.1f} nm (Na D)\na = {a:.2f} $\pm$ {a_err:.2f}\nb = {b:.2f} $\pm$ {b_err:.2f}'
ax.legend(title=legend_text)

# 保存
plt.savefig('ex10_plot_scale2wavelength_linear.pdf')

