[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

<!-- Exercise 3.1 Something like the class size paradox appears if you survey 
children and ask how many children are in their family. Families with many
children are more likely to appear in your sample, and families with no chil-
dren have no chance to be in the sample.
Use the NSFG respondent variable NUMKDHH to construct the actual distribu-
tion for the number of children under 18 in the household.
Now compute the biased distribution we would see if we surveyed the children
and asked them how many children under 18 (including themselves) are in
their household.
Plot the actual and biased distributions, and compute their means. As a
starting place, you can use chap03ex.ipynb. -->

>> 
%matplotlib inline

import numpy as np
import nsfg
resp = nsfg.ReadFemResp()

pmf = thinkstats2.Pmf(resp.numkdhh, label='numkdhh')

thinkplot.Pmf(pmf)
thinkplot.Config(xlabel='Number of children', ylabel='PMF')
pmf

biased = BiasPmf(pmf, label='biased')
biased

thinkplot.Pmfs([pmf, biased])
thinkplot.Config(xlabel='Number of children', ylabel='PMF')

pmf.Mean()
<!-- 1.024205155043831 -->

biased.Mean()
<!-- 2.403679100664282 -->
