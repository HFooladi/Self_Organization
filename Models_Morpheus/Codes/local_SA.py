import numpy as np
import os

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
    f, r = circle_to_rect((x_center, y_center), radius, field_cur)

    return f, r*radius

sweep_file_names = ['r1', 'r2', 'beta1', 'beta2', 'lambda', 'a1', 'a2', 'n', 'radius']

for sweep_file_name in sweep_file_names:
    r_BMP = []
    r_Nog = []
    f_BMP = []
    f_Nog = []
    runs_string = os.listdir("sweep_"+sweep_file_name)
    runs_index = []
    for rr in runs_string:
        if rr.startswith('Model'):
            runs_index.append(np.uint16(rr.split('_')[-1]))

    runs_index = sorted(runs_index)
    for run in runs_index:
        if os.path.isdir(os.path.join("sweep_"+sweep_file_name, "Model_new_test_" + str(run))):

            f1, r1 = radial_plot(os.path.join("sweep_"+sweep_file_name, "Model_new_test_" + str(run), "BMP.txt"))
            f2, r2 = radial_plot(os.path.join("sweep_" + sweep_file_name, "Model_new_test_" + str(run), "Nog.txt"))

            r_BMP = r_BMP + r1.tolist()
            r_Nog = r_Nog + r2.tolist()

            f_BMP = f_BMP + f1.tolist()
            f_Nog = f_Nog + f2.tolist()

    r_Nog = np.array(r_Nog)
    r_BMP = np.array(r_BMP)
    f_BMP = np.array(f_BMP)
    f_Nog = np.array(f_Nog)

    os.makedirs("sweep_array_"+sweep_file_name)
    np.savetxt(os.path.join("sweep_array_"+sweep_file_name, "r_Nog.txt"), r_Nog)
    np.savetxt(os.path.join("sweep_array_"+sweep_file_name, "r_BMP.txt"), r_BMP)
    np.savetxt(os.path.join("sweep_array_"+sweep_file_name, "f_BMP.txt"), f_BMP)
    np.savetxt(os.path.join("sweep_array_"+sweep_file_name, "f_Nog.txt"), f_Nog)

