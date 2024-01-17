import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Function to plot a line chart
def plot_line(data, x, y, xlabel, ylabel, title):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=x, y=y, data=data)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

# Function to plot a scatter plot
def plot_scatter(data, x, y, xlabel, ylabel, title):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=x, y=y, data=data)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

# Function to plot a bar chart
def plot_bar(data, x, y, xlabel, ylabel, title):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=x, y=y, data=data)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

# Function to plot a histogram
def plot_histogram(data, column, bins, xlabel, title):
    plt.figure(figsize=(10, 6))
    plt.hist(data[column], bins=bins)
    plt.xlabel(xlabel)
    plt.title(title)
    plt.show()

# Function to plot a heatmap
def plot_heatmap(data, title):
    plt.figure(figsize=(10, 8))
    sns.heatmap(data, annot=True)
    plt.title(title)
    plt.show()

# Function to plot a boxplot
def plot_boxplot(data, x, y, xlabel, title):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=x, y=y, data=data)
    plt.xlabel(xlabel)
    plt.title(title)
    plt.show()

# Function to plot a violin plot
def plot_violin(data, x, y, xlabel, ylabel, title):
    plt.figure(figsize=(10, 6))
    sns.violinplot(x=x, y=y, data=data)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

# Function to plot a time series
def plot_timeseries(data, x, y, xlabel, ylabel, title):
    plt.figure(figsize=(10, 6))
    plt.plot(data[x], data[y])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

# Function to plot pair plots
def plot_pairplot(data):
    sns.pairplot(data)
    plt.show()

# Function to plot 3D scatter plot
def plot_3d_scatter(data, x, y, z, xlabel, ylabel, zlabel, title):
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(data[x], data[y], data[z])
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(title)
    plt.show()

# Function to save a plot
def save_plot(fig, filename):
    fig.savefig(filename)

# Example usage of save_plot
# fig = plt.figure()
# plot_line(data, 'x', 'y', 'X Axis', 'Y Axis', 'Line Plot')
# save_plot(fig, 'line_plot.png')



def create_animation(setup_func, update_func, frames=100, interval=20, save_path=None):
    """
    Create and save a generalized animation.

    Parameters:
    - setup_func: A function to set up the initial state of the animation.
    - update_func: A function to update the animation for each frame.
    - frames (int): The total number of frames in the animation.
    - interval (int): The time (in ms) between each frame.
    - save_path (str): The file path to save the animation. If None, the animation is not saved.

    Returns:
    - ani: The created animation object.
    """

    # Set up the figure and apply the setup function
    fig, ax = plt.subplots()
    elements = setup_func(ax)

    # Create the animation
    ani = FuncAnimation(fig, lambda frame: update_func(frame, *elements), frames=frames, interval=interval)

    # Save the animation if a save path is provided
    if save_path:
        ani.save(save_path, writer='ffmpeg', fps=30)

    return ani

# # Example of how to use this function

# # Define the setup function
# def setup_plot(ax):
#     ax.set_xlim(0, 2*np.pi)
#     ax.set_ylim(-1, 1)
#     line, = ax.plot([], [], lw=2)
#     return line,

# # Define the update function
# def update_line(frame, line):
#     x = np.linspace(0, 2*np.pi, 200)
#     y = np.sin(x + frame / 10)
#     line.set_data(x, y)
#     return line,

# # Create and save the animation
# ani = create_animation(
#     setup_func=setup_plot,
#     update_func=update_line,
#     frames=100,
#     interval=20,
#     save_path=None
# )
