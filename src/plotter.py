#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec


class Plotter:
    def __init__(self, data):
        self.data = data
        self.fig = plt.figure(figsize=(10, 4))
        self.spec = gridspec.GridSpec(ncols=2, nrows=1, width_ratios=[1,1], wspace=0.3)

        self.add_time_percentages()

    def add_time_percentages(self):
        for time in ['LOAD_TIME', 'GROUND_TIME', 'SOLUTION_TIME']:
            self.data[time + '_P'] = (
                self.data[time] / self.data['TIME'] * 100
            )

    def plot_time_growth(self):
        estimation = {
            'SIZE': [i*850000+114 for i in range(25, 35)],
        }
        line_plot_data = self.data.append(pd.DataFrame(estimation))

        line_plot_data = line_plot_data.groupby('SIZE').agg(['mean'])
        line_plot_data['ESTIMATION'] = 2.4 * 10**(-9) * line_plot_data.index**(1.7)

        plot = self.fig.add_subplot(self.spec[0])

        plot.plot(
            line_plot_data.index,
            line_plot_data['ESTIMATION'],
            '--',
            linewidth='3',
            color='C1',
            label='Estimation')

        plot.plot(
            line_plot_data.index,
            line_plot_data['TIME']['mean'],
            linewidth='3',
            color='C0',
            label='Data')

        plot.set_title('Execution Time')
        plot.set_ylabel("Time (s)")
        plot.set_xlabel("Atoms (solution size)")
        plot.legend()
        plot.grid()

    def plot_time_distribution(self):
        plot = self.fig.add_subplot(self.spec[1])
        bar_plot_data = data.groupby('SIZE').agg(['mean'])
        bar_plot_data = bar_plot_data.loc[[114, 850114, 1700114, 20400114]]

        plot.bar(
            bar_plot_data.index.astype(str),
            bar_plot_data['LOAD_TIME_P']['mean'],
            bottom=0, width=0.5,
            color='C1',
            label='Load')

        plot.bar(
            bar_plot_data.index.astype(str),
            bar_plot_data['GROUND_TIME_P']['mean'],
            bottom=bar_plot_data['LOAD_TIME_P']['mean'],
            width=0.4,
            color='C0',
            label='Ground')

        plot.bar(
            bar_plot_data.index.astype(str),
            bar_plot_data['SOLUTION_TIME_P']['mean'],
            bottom=bar_plot_data['LOAD_TIME_P']['mean'] + bar_plot_data['GROUND_TIME_P']['mean'],
            width=0.3,
            color='C2',
            label='Solution')

        plot.set_title('Time Distribution')
        plot.set_ylabel("Time (%)")
        plot.set_xlabel("Atoms (solution size)")
        plot.set_xticklabels(['114', '850K', '1M', '20M'])


data = pd.read_csv('evaluation.csv', delimiter='; ')
plotter = Plotter(data)
plotter.plot_time_growth()
plotter.plot_time_distribution()

plt.savefig('evaluation.pdf')
