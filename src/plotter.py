#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec


class Plotter:
    def __init__(self, data):
        self.data = data
        self.fig = plt.figure(figsize=(10, 4))
        self.spec = gridspec.GridSpec(ncols=2, nrows=1, width_ratios=[3,1], wspace=0.3)

        self.add_percentages()
        self.data = data.groupby('SIZE').agg(['mean'])

    def add_percentages(self):
        self.data['LOAD_TIME_P'] = (
            self.data['LOAD_TIME'] / self.data['TIME'] * 100)
        self.data['GROUND_TIME_P'] = (
            self.data['GROUND_TIME'] / self.data['TIME'] * 100)
        self.data['SOLUTION_TIME_P'] = (
            self.data['SOLUTION_TIME'] / self.data['TIME'] * 100)

    def add_time_plot(self):
        line_plot_data = data.groupby('SIZE').agg(['mean'])
        line_plot_data['ESTIMATION'] = 2.3 * 10**(-9) * line_plot_data.index**(1.7)

        plot = self.fig.add_subplot(self.spec[0])
        plot.plot(line_plot_data.index, line_plot_data['TIME']['mean'])
        plot.plot(line_plot_data.index, line_plot_data['ESTIMATION'], '--')

        plot.set_title('Execution Time')
        plot.set_ylabel("Time (s)")
        plot.set_xlabel("Size")
        plot.grid()

    def add_time_distribution_plot(self):
        plot = self.fig.add_subplot(self.spec[1])
        bar_plot_data = self.data.loc[[114, 850114, 15300114]]

        plot.bar(
            bar_plot_data.index.astype(str),
            bar_plot_data['LOAD_TIME_P']['mean'],
            bottom=0, width=0.4,
            color='C1',
            label='Load')

        plot.bar(
            bar_plot_data.index.astype(str),
            bar_plot_data['GROUND_TIME_P']['mean'],
            bottom=bar_plot_data['LOAD_TIME_P']['mean'],
            width=0.3,
            color='C0',
            label='Ground')

        plot.bar(
            bar_plot_data.index.astype(str),
            bar_plot_data['SOLUTION_TIME_P']['mean'],
            bottom=bar_plot_data['LOAD_TIME_P']['mean'] + bar_plot_data['GROUND_TIME_P']['mean'],
            width=0.2,
            color='C2',
            label='Solution')

        plot.set_title('Time Distribution')
        plot.set_ylabel("Time (%)")
        plot.set_xlabel("Size (K)")
        plot.set_xticklabels((bar_plot_data.index/1000).astype(int))


data = pd.read_csv('evaluation.csv', delimiter='; ')
plotter = Plotter(data)
plotter.add_time_plot()
plotter.add_time_distribution_plot()

plt.savefig('evaluation.pdf')
