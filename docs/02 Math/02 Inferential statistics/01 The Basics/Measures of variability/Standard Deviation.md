- Example:
	- We have different tasks taking different time for each agent
	- We have data for last 7 days
	- Solution:
		- Find mean time taken by an agent (sample mean)
		- Find mean time taken by all agents (population mean)
		- Min: 1 min
		- Max: 60 mins
		- Bucket time: 12 buckets : 5 mins
			- 0- 5 min: a
			- 6-10 min: b
			- ...
		- For an agent:
| Agent | actual time taken | ticket/task | bucket |
| ----- | ----------------- | ----------- | ------ |
| A     | 6 mins            | t1          | b      |
| A     | 4 mins            | t2          | a      |
| A     | 15 mins           | t3          | c      |
| A     | 43 mins           | t5          | h      |
| A     | 32 mins           | t4          | f      |
| A     | 3 mins            | t8          | a       |

For Agent A, 

| bucket name (bn) | frequency (f) | tn * f | (tn-mean_tn)^2 | (tn-mean_tn)^2 * f | # tickets (t) |
| ---------------- | ------------- | ------ | -------------- | ------------------ | ------------- |
| 5                | 2             |        |                |                    |               |
| 5-10             | 1             |        |                |                    |               |
| 10-15            | 1             |        |                |                    |               |
| 15-20            | 0             |        |                |                    |               |
| e                | 0             |        |                |                    |               |
| f                | 1             |        |                |                    |               |
| g                | 0             |        |                |                    |               |
| h                | 1             |        |                |                    |               |



For all agents & tasks:



