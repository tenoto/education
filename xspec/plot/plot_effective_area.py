#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

import smplotlib
plt.rcParams["markers.fillstyle"] = "full"

def running_average(data, window_size):
    """
    2次元データのrunning averageを計算する関数
    :param data: 2次元データ (ndarray)
    :param window_size: 移動平均のウィンドウサイズ (int)
    :return: running averageを計算した2次元データ (ndarray)
    """
    # 移動平均を計算するために、2次元データを転置する
    data_T = np.transpose(data)

    # 移動平均を計算する
    rolling_mean = np.convolve(data_T[1], np.ones(window_size) / window_size, mode='valid')

    # 結果を格納するための2次元データを作成する
    result = np.zeros((2, len(rolling_mean)))

    # 2次元データに移動平均の結果を格納する
    result[0] = data_T[0][(window_size - 1):]
    result[1] = rolling_mean

    # 結果を転置して返す
    return np.transpose(result)

# データの読み込み
data = np.loadtxt('data/CsI5x15x5cm3_Al2000umCoated_FlatRadiation_EffectiveArea.qdp',skiprows=2)

# 移動平均を計算する
window_size = 2**4
data_ave = running_average(data, window_size)

energy_keV, area_cm2 = data_ave[:,0], data_ave[:,1],
#print(energy_keV)
#print(area_cm2)

# データのプロット
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(energy_keV, area_cm2, 'r-')

# 軸の範囲の設定
ax.set_xlim(0.12,40.0)
ax.set_ylim(30.0,80.0)

# ラベルの設定
ax.set_xlabel('Energy (MeV)')
ax.set_ylabel(r'Effective Area (cm$^2$)')

# グリッドの表示
plt.xscale('log')
ax.grid(True)
plt.xticks([0.2,0.4,1.0,2.0,4.0,10.0,40.0],["0.2","0.4","1.0","2.0","4.0","10.0","40.0"])

# 凡例の表示
legend_text = r'Cogamo CsI(Tl) 5x5x15 cm$^3$'
ax.legend(title=legend_text)

# 保存
plt.savefig('CsI5x15x5cm3_Al2000umCoated_FlatRadiation_EffectiveArea.pdf')

"""



# フィッティング曲線のプロット
xfit = np.linspace(0.0,5.0,100)
yfit = fitting_func(xfit, a, b)
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


"""
