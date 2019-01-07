[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)


<!--
Exercise 2.4 Using the variable totalwgt_lb, investigate whether first ba-
bies are lighter or heavier than others. Compute Cohen's d to quantify the
difference between the groups. How does it compare to the difference in
pregnancy length?
-->
>> CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb) = -0.088672927072602 This number represents the difference between the means deviation between both groups (firsts and others). The difference in means is also quite small,
firsts.totalwgt_lb.mean(), others.totalwgt_lb.mean() = (7.201094430437772, 7.325855614973262)


Cohen's D for pregnancy length -> CohenEffectSize(firsts.prglngth, others.prglngth) = 0.028879044654449883
Raw difference of means -> firsts.prglngth.mean() - others.prglngth.mean() = 0.07803726677754952

It appears that effect size on total weight is higher than the effect size for pregnancy length (after taking the absolute value). However, overall these effects seem to be quite small in the larger picture.

