# Normal Traffic Generator
import os, time, random
from scipy.stats import genpareto

# FlowDuration Generator - Generalzed Pareto Distribution
location = 0;
scale = 6.12258; # scale
shape = 0.577699; # shape
# FlowDelay Generator - Weibull distribution
a = 541.895   # scale
b = 0.643293  # shape
Xn = [];
n = 20000;    # number of generated flows

for i in range (0,n):
	flowDuration = genpareto.rvs(shape, loc=location, scale = scale, size=1)+1; 
	flowDuration = round(flowDuration[0]) + 1; # +1 helps to flowDuration > 1
	flowDelay = (random.weibullvariate(a,b))/1000; # in seconds
	time.sleep(flowDelay);     
	print('./ITGSend -a 10.0.0.1 -rp 10001 -V 1.55558 0.0093942 -w 1.74315 86.9597 -T TCP -z '+f'{flowDuration}'+' -d '+ f'{flowDelay}' +' -l sender.log')
	os.system('./ITGSend -a 10.0.0.1 -rp 10001 -V 1.55558 0.0093942 -w 1.74315 86.9597 -T TCP -z '+f'{flowDuration}'+' -d 0 -l sender.log')
