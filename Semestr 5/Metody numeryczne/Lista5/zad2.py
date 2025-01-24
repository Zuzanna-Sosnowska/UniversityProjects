import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import interpolation


def main():
    re_lst = [0.2, 2, 20, 200, 2000, 20000]
    cd_lst = [103, 13.9, 2.72, 0.8, 0.401, 0.433]
    cs = make_interp_spline(x=re_lst, y=cd_lst, bc_type="natural")
    points = [(re_lst[i], cd_lst[i]) for i in range(len(re_lst))]
    poly = interpolation.polynomial_interpolation(points)

    x_lst = np.linspace(0, 20000, 100000)
    y1_lst = cs(x_lst)
    y2_lst = poly(x_lst)

    plt.plot(x_lst, y1_lst, label='Cubic Spline')
    plt.plot(x_lst, y2_lst, label='Interpolation')
    plt.scatter(re_lst, cd_lst, label='Points', color='red')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
