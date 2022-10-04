import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np
import itertools

means = [100, 105]
std_devs = [5, 6]

num_to_sim = 500

data = [
    np.random.randn(num_to_sim) * s + mu for mu, s in zip(means, std_devs)
]

plt.hist(data[0])
plt.xlabel('Value')
plt.ylabel('Count')
plt.savefig('imgs/basic_histogram.png')

plt.figure()
plt.hist(data[0])
plt.hist(data[1], alpha=0.5)
plt.xlabel('Value')
plt.ylabel('Count')
plt.savefig('imgs/two_distributions.png')


pp = sm.ProbPlot(data[0])
pp2 = sm.ProbPlot(data[1])
fig = pp.probplot()
pp2.probplot(ax=fig.gca())
plt.grid(True)

colors = itertools.cycle(plt.rcParams['axes.prop_cycle'].by_key()['color'])

for l in fig.gca().get_lines():
    c = next(colors)
    l.set_markerfacecolor(c)
    l.set_color(c)

plt.tight_layout()
plt.savefig('imgs/probplot.png')