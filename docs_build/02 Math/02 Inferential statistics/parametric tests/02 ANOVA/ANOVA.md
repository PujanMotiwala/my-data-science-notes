*Analysis of Variance is a statistical test used to analyze the difference between the means of more than two groups.*

![[Excalidraw/anova.excalidraw.svg]]

### Types:
- one-way ANOVA: one <font color="orange">independent variable</font>
- two-way ANOVA: two <font color="orange">independent variables</font>

#### One-way ANOVA
##### Example
- As a crop researcher, you want to test the effect of three different fertilizer mixtures on crop yield. You can use a one-way ANOVA to find out if there is a difference in crop yields between the three groups.
##### When to use ?
- Use a one-way ANOVA when you have [collected data](https://www.scribbr.com/methodology/data-collection/) about <font color="orange">one categorical independent variable </font>and <font color="green">one quantitative dependent variable</font>. 
- The independent variable should have *at least three* *levels* (*i.e. at least three different groups/categories*).

- ANOVA tells you if the <font color="green">dependent variable</font> changes according to the level of the <font color="orange">independent variable</font>. For example:

	- Your <font color="orange">independent variable</font> is <u style="background-color:#6F5C00">social media use</u>, and you assign groups to *low*, *medium*, and *high* levels of social media use to find out if there is a difference in <u style="background-color:#116600">hours of sleep per night</u>.
	- Your <font color="orange">independent variable</font> is <u style="background-color:#6F5C00">brand of soda</u>, and you collect data on *Coke*, *Pepsi*, *Sprite*, and *Fanta* to find out if there is a difference in the <u style="background-color:#116600">price per 100ml</u>.
	- Your <font color="orange">independent variable</font> is <u style="background-color:#6F5C00">type of fertilizer</u>, and you treat crop fields with mixtures *1*, *2* and *3* to find out if there is a <u style="background-color:#116600">difference in crop yield</u>.

##### Mechanism 
- If any of the group means is significantly different from the overall mean, then the null hypothesis is rejected.

##### Assumptions
The assumptions of the ANOVA test are the same as the general assumptions for any parametric test:

1.  Independence of observations
2.  Normally-distributed response variable
3.  Homogeneity of variance

##### Interpreting the test
The ANOVA output provides an estimate of how much variation in the dependent variable that can be explained by the independent variable.

-   The first column lists the **independent variable** along with the model **residuals** (aka the model error).
-   The **Df** column displays the [degrees of freedom](https://www.scribbr.com/statistics/degrees-of-freedom/) for the independent variable (calculated by taking the number of levels within the variable and subtracting 1), and the degrees of freedom for the residuals (calculated by taking the total number of observations minus 1, then subtracting the number of levels in each of the independent variables).
-   The **Sum Sq** column displays the sum of squares (a.k.a. the total variation) between the group means and the overall mean explained by that variable. The sum of squares for the fertilizer variable is 6.07, while the sum of squares of the residuals is 35.89.
-   The **Mean Sq** column is the mean of the sum of squares, which is calculated by dividing the sum of squares by the degrees of freedom.
-   The **_F_ value** column is the [test statistic](https://www.scribbr.com/statistics/test-statistic/) from the _F_ test: the mean square of each independent variable divided by the mean square of the residuals. The larger the _F_ value, the more likely it is that the variation associated with the independent variable is real and not due to chance.
-   The **Pr(>F)** column is the [_p_ value](https://www.scribbr.com/statistics/p-value/) of the _F_ statistic. This shows how likely it is that the _F_ value calculated from the test would have occurred if the [null hypothesis](https://www.scribbr.com/statistics/null-and-alternative-hypotheses/) of no difference among group means were true.

Because the _p_ value of the independent variable, fertilizer, is [statistically significant](https://www.scribbr.com/statistics/statistical-significance/) (_p_ < 0.05), it is likely that fertilizer type does have a significant effect on average crop yield.

*ANOVA will tell you if there are differences among the levels of the independent variable, but not which differences are significant. To find how the treatment levels differ from one another, perform a TukeyHSD (Tukey’s Honestly-Significant Difference) post-hoc test.*

##### The Tukey test
- It runs pairwise comparisons among each of the groups, and uses a conservative error estimate to find the groups which are statistically different from one another.
- First, the table reports the model being tested (‘Fit’). Next, it lists the pairwise differences among groups for the independent variable.
- Groups B and C are statistically significant, say group A is not.

##### Reporting
- When reporting the results of an ANOVA:
	- include a brief description of the variables you tested, 
	- the  _F_ value, 
	- degrees of freedom, 
	- and _p_ values for each independent variable, 
	- and explain what the results mean.
- Example:
	- We found a statistically-significant difference in average crop yield according to fertilizer type (_F_(2)=9.073, _p_ < 0.001). 
	- A Tukey post-hoc test revealed significant pairwise differences between fertilizer types 3 and 2, with an average difference of 0.42 bushels/acre (_p_ < 0.05) and between fertilizer types 3 and 1, with an average difference of 0.59 bushels/acre (_p_ < 0.01).

#### Two-way ANOVA