[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> 
import scipy.stats

dist = scipy.stats.norm(loc=178, scale=7.7)
dist.cdf(mu-sigma)

import thinkstats2
import thinkplot
import brfss

five_eleven = dist.cdf(177.8)
six_one = dist.cdf(185.4)

five_eleven, six_one, six_one-five_eleven

<!-- tried it using thinkstats2/thinkplot -->
df = brfss.ReadBrfss()
weights = df.wtkg2.dropna()

weight_cdf = thinkstats2.Cdf(weights)
my_plot = thinkplot.cdf(weight_cdf)
my_plot