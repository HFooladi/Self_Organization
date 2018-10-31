import numpy as np
from matplotlib import pyplot as plt
import os

sweep_file_names = ['radius']
sweep_param_range = ['(150' + r'$\mu m$'+ ' ~ 300' + r'$\mu m$' + ')']
title_tex = ['radius']
base_id = [10]
plot_id = [(0, 0)]


radius_res = 200
# SA plot for BMP
fig, axes = plt.subplots(nrows=2, ncols=1)
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
    axes[0].plot(r / np.max(r), prop, lw=2, color='red', label="Proposed")
    axes[0].fill_between(r/ np.max(r), mu1+2*sigma1, mu1-2*sigma1, facecolor='yellow', alpha=0.5)
    axes[0].legend(loc='lower right')
    axes[0].set_xlabel('normalized distance to center')
    axes[0].set_ylabel('Concentration(BMP)')
    axes[0].set_title('Local SA for ' + tex + param_range)

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
    axes[1].plot(r / np.max(r), prop, lw=2, color='red', label="Proposed")
    axes[1].fill_between(r/ np.max(r), mu1+2*sigma1, mu1-2*sigma1, facecolor='yellow', alpha=0.5)
    axes[1].legend(loc='lower left')
    axes[1].set_xlabel('normalized distance to center')
    axes[1].set_ylabel('Concentration(Noggin)')
    axes[1].set_title('Local SA for ' + tex + param_range)

plt.subplots_adjust(hspace=0.6)
plt.show()