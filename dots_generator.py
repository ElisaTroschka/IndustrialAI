import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rd
import pandas as pd

x = np.empty((0, 1))
y = np.empty((0, 1))
area = np.array([])

# add new points and shifts the existing ones with random noise
def update_points(i, x, y, area):
    new_points = 1 if i < 2 else i // 3
    delta_x = rd.default_rng().normal(0, 2, x.shape)
    delta_y = rd.default_rng().normal(0, 2, y.shape)
    x += delta_x
    y += delta_y
    area = (10 + 2 * i * rd.default_rng().uniform(0, 1, x.shape)) ** 2
    
    # adding new points
    x = np.vstack((x, rd.default_rng().normal(50, 15, (new_points, 1))))
    y = np.vstack((y, rd.default_rng().normal(50, 15, (new_points, 1))))
    area = np.vstack((area, (10 + 2 * rd.default_rng().uniform(0, 1, (new_points, 1))) ** 2))
    return x, y, area

# plots and saves the images
def get_image(x, y, area, path):
    fig, ax = plt.subplots(1, 1, figsize=(20, 12))

    plt.scatter(x, y, s=area, alpha=0.5, c='royalblue', marker='o', edgecolors='None')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    ax.spines['left'].set_color('white')      
    ax.spines['top'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.spines['bottom'].set_color('white')

    fig.savefig(f'{path}img{i}.jpg')

n_img = 30
for i in range(n_img):
    x, y, area = update_points(i, x, y, area)
    get_image(x, y, area, 'img/')


