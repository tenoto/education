#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

import smplotlib
plt.rcParams["markers.fillstyle"] = "full"

# データの読み込み
data = np.loadtxt('input.data')
x, y, dx, dy = data[:,0], data[:,1], data[:,2], data[:,3]

# フィッティング関数
def fitting_func(x, a, b):
    return a * x**(-2) + b

# フィッティング
popt, pcov = curve_fit(fitting_func, x, y)

# データのプロット
fig, ax = plt.subplots(figsize=(8, 5))

# 定数 a, b の値と1-sigma誤差の取得
a, b = popt
a_err, b_err = np.sqrt(np.diag(pcov))

# フィッティング曲線のプロット
xfit = np.linspace(1.5, 4.5, 100)
yfit = fitting_func(xfit, a, b)
ax.plot(xfit, yfit, 'r--', label='Fit: $y = ax^{-2} + b$')
ax.errorbar(x, y, xerr=dx, yerr=dy, 
	fmt='o', capsize=0, markersize=6, alpha=1.0,
	markerfacecolor=None,markeredgecolor='k',
	label='Measurement')

# 軸の範囲の設定
ax.set_xlim(1.5, 4.5)
ax.set_ylim(400, 700)

# ラベルの設定
ax.set_xlabel('Scale (cm)')
ax.set_ylabel('Wavelength (nm)',labelpad=15)

# グリッドの表示
ax.grid(True)

# 凡例の表示
legend_text = f'a = {a:.1f} $\pm$ {a_err:.1f} nm*cm$^2$\nb = {b:.1f} $\pm$ {b_err:.1f} nm'
ax.legend(title=legend_text)

# 保存
plt.savefig('sample.pdf')

"""
以下の要求を満たす python コードを出力して下さい。
- input.data というテキストデータを読み込む。このデータには、４つのデータ列 x, y, dx, dy, text が１行ごとに入っている。x, y, dx, dy は float の値とする。text は文字列である。
- (x,y) を読み取って、散布図で表示する。
- (dx,dy) を誤差として表示する。
- 出力を sample.pdf として保存する。
- x,yのラベル名はそれぞれ、"Scale (cm)" と "Wavelength (nm)"とする。
- コードの１行目に "#!/usr/bin/env python" を挿入してください。
- 図のサイズは、figsize=(8, 5) に設定してください。
- 図の中に凡例を示してください。
- 散布図のマーカーは filled circle にしてください。capsize は 0 です。
- (x,y) のデータを y = a * x**-2 + b でフィットしてください。ここで、a, b は定数とします。
- フィットした関数を図に表示してください。
- プロットにはグリッドを表示してください。
- x は (1.5, 4.5) の範囲をプロットの下限、上限としてください。
- y は (400, 700) の範囲をプロットの下限、上限としてください。
- フィットで得られる定数 a, b について1-sigma誤差も凡例に表示してください。
- プロットしたデータ点の近くに text の内容をプロットする。
"""