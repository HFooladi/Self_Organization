import numpy as np
import os
from SALib.sample.morris import sample

def circle_to_rect(center, radius, Image):
    normalHeight = 201
    normalWidth = 360
    polCol = 0
    theta = 0
    polarImg = np.zeros((normalHeight, normalWidth), dtype=np.float16)
    while(theta<=359):

        xptet = center[0]
        yptet = center[1]

        xitet = np.int16(xptet + radius * np.cos(theta * np.pi / 180.0))
        yitet = np.int16(yptet + radius * np.sin(theta * np.pi / 180.0))

        r = 0.0
        polRow = 0
        while r <= 1:
            polarImg[polRow, polCol] = Image[np.int16((1.0-r)*yptet+r*yitet), np.int16((1.0-r)*xptet+r*xitet)]
            r += 1.0/(normalHeight-1.0)
            polRow += 1
        theta += 360.0/normalWidth
        polCol += 1

        radiusArray = np.linspace(0, 1, normalHeight-1)
        polarField = np.mean(polarImg, axis=1)
    return polarField[:-1], radiusArray

def radial_plot(fileName):
    # colunms = "time","l.x","l.y","b"
    field = np.loadtxt(fileName, delimiter=',', dtype=np.float16, skiprows=1)
    lastTime = np.max(field[:, 0])
    n_pixel_x = np.uint16(np.max(field[:, 1]) + 1)
    n_pixel_y = np.uint16(np.max(field[:, 2]) + 1)
    all_fields = []
    x_center = n_pixel_x /2.0
    y_center = n_pixel_y /2.0
    radius   = 240 - x_center

    field_cur = np.reshape(field[field[:, 0] == lastTime, -1],(n_pixel_x, n_pixel_y))
    all_fields.append(field_cur)
    # plt.figure()
    # plt.imshow(field_cur)
    f, r = circle_to_rect((x_center, y_center), radius, field_cur)

    return f, r*radius

is_analyze = True
is_generate_samples = False

# Read the parameter range file and generate samples
# or define manually without a parameter file:
problem = {
 'num_vars': 7,
 'names': ['a1', 'a2', 'beta1', 'beta2', 'lambda', 'r1', 'r2'],
 'groups': None,
 'bounds': [[0.01, 2],
            [0.01, 2],
            [5, 40],
            [5, 40],
            [0.1, 4],
            [0.01, 2],
            [0.5, 1.5]]
}

# Generate samples
param_values = sample(problem, N=100, num_levels=4, grid_jump=2, optimal_trajectories=None)
if is_generate_samples:
    np.savetxt("a1.txt", param_values[:, 0], delimiter=';', newline=';')
    np.savetxt("a2.txt", param_values[:, 1], delimiter=';', newline=';')
    np.savetxt("beta1.txt", param_values[:, 2], delimiter=';', newline=';')
    np.savetxt("beta21.txt", param_values[:, 3], delimiter=';', newline=';')
    np.savetxt("lambda.txt", param_values[:, 4], delimiter=';', newline=';')
    np.savetxt("r1.txt", param_values[:, 5], delimiter=';', newline=';')
    np.savetxt("r2.txt", param_values[:, 6], delimiter=';', newline=';')

if is_analyze:

    saved_param_values = np.zeros_like(param_values)
    saved_param_values[:, 0] = np.loadtxt("a1.txt", dtype=np.float32, delimiter=';')
    saved_param_values[:, 1] = np.loadtxt("a2.txt", dtype=np.float16, delimiter=';')
    saved_param_values[:, 2] = np.loadtxt("beta1.txt", dtype=np.float16, delimiter=';')
    saved_param_values[:, 3] = np.loadtxt("beta2.txt", dtype=np.float16, delimiter=';')
    saved_param_values[:, 4] = np.loadtxt("lambda.txt", dtype=np.float16, delimiter=';')
    saved_param_values[:, 5] = np.loadtxt("r1.txt", dtype=np.float16, delimiter=';')
    saved_param_values[:, 6] = np.loadtxt("r2.txt", dtype=np.float16, delimiter=';')

    sweep_file_name = 'SA_General'
    r_BMP = []
    r_Nog = []
    f_BMP = []
    f_Nog = []
    runs_string = os.listdir(sweep_file_name)
    runs_index = []
    for rr in runs_string:
        if rr.startswith('Model'):
            runs_index.append(np.uint16(rr.split('_')[-1]))
    runs_index = sorted(runs_index)

    for run in runs_index:
        print run
        if os.path.isdir(os.path.join(sweep_file_name, "Model_new_test_" + str(run))):
            f1, r1 = radial_plot(os.path.join(sweep_file_name, "Model_new_test_" + str(run), "BMP.txt"))
            f2, r2 = radial_plot(os.path.join(sweep_file_name, "Model_new_test_" + str(run), "Nog.txt"))

            r_BMP.append(r1.tolist())
            r_Nog.append(r2.tolist())

            f_BMP.append(f1.tolist())
            f_Nog.append(f2.tolist())

    r_Nog = np.array(r_Nog)
    r_BMP = np.array(r_BMP)
    f_BMP = np.array(f_BMP)
    f_Nog = np.array(f_Nog)

    os.makedirs("sweep_array_all_morris")
    np.savetxt(os.path.join("sweep_array_all_morris", "r_Nog.txt"), r_Nog)
    np.savetxt(os.path.join("sweep_array_all_morris", "r_BMP.txt"), r_BMP)
    np.savetxt(os.path.join("sweep_array_all_morris", "f_BMP.txt"), f_BMP)
    np.savetxt(os.path.join("sweep_array_all_morris", "f_Nog.txt"), f_Nog)
