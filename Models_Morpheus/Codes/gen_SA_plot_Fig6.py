import numpy as np
from matplotlib import pyplot as plt
import os

sweep_file_names = ['r1', 'r2', 'beta1', 'beta2', 'lambda', 'a1', 'a2', 'n']
sweep_param_range = ['(0 ~ 0.8)', '(0 ~ 2)', '(10 ~ 30)', '(10 ~ 30)', '(0 ~ 1)', '(0 ~ 1)', '(0 ~ 1)', '(1 ~ 4)']
title_tex = [r'$r_1$',r'$r_2$', r'$\tilde{\beta}_B$', r'$\tilde{\beta}_N$', r'$\lambda$', r'$\tilde{a}_B$', r'$\tilde{a}_N$', r'$n$']
base_id = [6, 24, 10, 10, 20, 5, 5, 1]
plot_id = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3)]



radius_res = 200
# SA plot for BMP
fig, axes = plt.subplots(nrows=2, ncols=4)
for sweep_file_name, idx, id_p, param_range, tex in zip(sweep_file_names, base_id, plot_id, sweep_param_range, title_tex):
    r_BMP = np.loadtxt(os.path.join("sweep_array_"+sweep_file_name, "r_BMP.txt"), dtype=np.float16)
    f_BMP = np.loadtxt(os.path.join("sweep_array_"+sweep_file_name, "f_BMP.txt"), dtype=np.float16)

    r_BMP = np.reshape(r_BMP, (np.uint8(r_BMP.shape[0]/radius_res), radius_res))
    f_BMP = np.reshape(f_BMP, (np.uint8(f_BMP.shape[0]/radius_res), radius_res))

    r = r_BMP[0, :]


    mu1 = f_BMP.mean(axis=0)
    prop = f_BMP[idx, :]
    sigma1 = f_BMP.std(axis=0)

    # plot it!
    axes[id_p[0], id_p[1]].plot(r * 2, prop, lw=2, color='red', label="Proposed")
    axes[id_p[0], id_p[1]].fill_between(r*2, mu1+2*sigma1, mu1-2*sigma1, facecolor='yellow', alpha=0.5)
    axes[id_p[0], id_p[1]].legend(loc='lower right')
    axes[id_p[0], id_p[1]].set_xlabel('Distance to center('+r'$\mu$'+'m)')
    axes[id_p[0], id_p[1]].set_ylabel('Concentration')
    axes[id_p[0], id_p[1]].set_title('Local SA for ' + tex + param_range)


plt.subplots_adjust(wspace=0.5, hspace=0.5)


fig, axes = plt.subplots(nrows=2, ncols=4)
for sweep_file_name, idx, id_p, param_range, tex in zip(sweep_file_names, base_id, plot_id, sweep_param_range,title_tex):
    r_Nog = np.loadtxt(os.path.join("sweep_array_"+sweep_file_name, "r_Nog.txt"), dtype=np.float16)
    f_Nog = np.loadtxt(os.path.join("sweep_array_"+sweep_file_name, "f_Nog.txt"), dtype=np.float16)

    r_Nog = np.reshape(r_Nog, (np.uint8(r_Nog.shape[0]/radius_res), radius_res))
    f_Nog = np.reshape(f_Nog, (np.uint8(f_Nog.shape[0]/radius_res), radius_res))

    r = r_Nog[0, :]


    mu1 = f_Nog.mean(axis=0)
    sigma1 = f_Nog.std(axis=0)
    prop = f_Nog[idx, :]

    # plot it!
    axes[id_p[0], id_p[1]].plot(r * 2, prop, lw=2, color='red', label="Proposed")
    axes[id_p[0], id_p[1]].fill_between(r*2, mu1+2*sigma1, mu1-2*sigma1, facecolor='yellow', alpha=0.5)
    axes[id_p[0], id_p[1]].legend(loc='lower left')
    axes[id_p[0], id_p[1]].set_xlabel('Distance to center('+r'$\mu$'+'m)')
    axes[id_p[0], id_p[1]].set_ylabel('Concentration')
    axes[id_p[0], id_p[1]].set_title('Local SA for ' + tex + param_range)

plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.show()