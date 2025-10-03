# IS211_Assignment5 – Network Request Simulation

For this project, I simulated network requests being handled by either a single server or multiple servers using a load balancer. The goal was to see how adding more servers affects the average wait time and requests are processed using a queue.

The project includes two files: `simulation.py`, which runs the simulation, and `requests.csv`, which has the sample requests in the format `timestamp,file,processing_time`.

To run it:  
- For one server: `python simulation.py requests.csv`  
- For multiple servers: `python simulation.py requests.csv 2` (or however many servers you want)

Here are my outcomes I got when I ran the simulation with my sample requests:

Servers   Avg Wait Time (s)  
1         1.33  
2         0.33  
3         0.00  
4         0.00  

Basically, what I got is that the more servers you add, the faster requests get handled, so the wait time goes down. With three or more servers, almost all requests are processed immediately.
