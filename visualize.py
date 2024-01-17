import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

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
