### What is A/B testing in [[Data Science]] ?
- Good for lifecycle testing for ML models.
- Heavily used in Ecommerce. 
- Products based on human behaviour.
- 

#### Bayesian Testing

- Experiment Definition: 
	- New webpage's effects on purchase conversion. 
	- Assumption:
		- control and treatment groups are mutually exclusive groups
	- Divide into 2 groups:
		- Control: Users that got *old* webpage
		- Treatment: Users that got *new* webpage
	- Metric to track: $$purchase Conversion = \frac{ converted\ Users}{exposed\ Users}$$
		- Exposure: A user in with control / treatment groups and interacts website for the very first time.
		- Conversion: An exposed user makes a purchase within 7 days of being first exposed.
	- Questions to ask on the test:
		- How do you think the experiment will perform ?
		- What will be actionable next step layout ?
	- Data:
	
| index | user_id | timestamp           | group     | landing_page | converted |
| ----- | ------- | ------------------- | --------- | ------------ | --------- |
| 0     | 1       | 2017-01-01 00:00:03 | treatment | new_page     | 0         |
| 1     | 2       | 2017-01-03 23:00:03 | control   | old_page     | 0         |

- EDA:
	- how many days is the collected data sample ?
	- Percentage of both the division groups.
	- Total no of users
	- landing page to compare.
	- Users who watched new and old page 
		- *Substantial %* : Find timestamp of their first exposure.
		- *insignificant %*: Filter them out
- Frequentist Approach:
	- [[treatment group]]: Conversion Rate: `11.87%`
	- [[control group]]: Conversion Rate: `12.017%`
	- Lift = `-0.144%` (in favour of [[control group]])
	- Hypothesis Test: 
		- Chi-Squared test ?
- Bayesian Approach: 
- 
