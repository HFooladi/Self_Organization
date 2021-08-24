import matplotlib.pyplot as plt
import numpy as np
import os
from SALib.analyze import morris
from SALib.sample.morris import sample
from SALib.plotting.morris import horizontal_bar_plot

problem = {
    'num_vars':
        7,
    'names': [
        r'$\tilde{a}_B$', r'$\tilde{a}_N$', r'$\tilde{\beta}_B$',
        r'$\tilde{\beta}_N$', r'$\lambda$', r'$r_1$', r'$r_2$'
    ],
    'groups':
        None,
    'bounds': [[0.01, 2], [0.01, 2], [5, 40], [5, 40], [0.1, 4], [0.01, 2],
               [0.5, 1.5]]
}
# Generate samples
param_values = sample(problem, N=100, num_levels=4, grid_jump=2, \
                      optimal_trajectories=None)

saved_param_values = np.zeros_like(param_values)
saved_param_values[:, 0] = np.loadtxt("a1.txt", dtype=np.float32, delimiter=';')
saved_param_values[:, 1] = np.loadtxt("a2.txt", dtype=np.float16, delimiter=';')
saved_param_values[:, 2] = np.loadtxt("beta1.txt",
                                      dtype=np.float16,
                                      delimiter=';')
saved_param_values[:, 3] = np.loadtxt("beta2.txt",
                                      dtype=np.float16,
                                      delimiter=';')
saved_param_values[:, 4] = np.loadtxt("lambda.txt",
                                      dtype=np.float16,
                                      delimiter=';')
saved_param_values[:, 5] = np.loadtxt("r1.txt", dtype=np.float16, delimiter=';')
saved_param_values[:, 6] = np.loadtxt("r2.txt", dtype=np.float16, delimiter=';')

r_Nog = np.loadtxt(os.path.join("sweep_array_all_morris", "r_Nog.txt"),
                   dtype=np.float32)
r_BMP = np.loadtxt(os.path.join("sweep_array_all_morris", "r_BMP.txt"),
                   dtype=np.float32)
f_BMP = np.loadtxt(os.path.join("sweep_array_all_morris", "f_BMP.txt"),
                   dtype=np.float32)
f_Nog = np.loadtxt(os.path.join("sweep_array_all_morris", "f_Nog.txt"),
                   dtype=np.float32)

Y = (np.max(f_BMP, axis=1) - np.min(f_BMP, axis=1)) / (
    np.argmax(f_BMP, axis=1) - np.argmin(f_BMP, axis=1))

Si = morris.analyze(problem,
                    saved_param_values,
                    Y,
                    conf_level=0.95,
                    print_to_console=True,
                    num_levels=4,
                    grid_jump=2,
                    num_resamples=100)

fig, ax1 = plt.subplots(1, 1)
horizontal_bar_plot(ax1, Si, {}, sortby='mu_star')

plt.show()
