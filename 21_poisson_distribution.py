# Poisson Distribution is a Discrete Distribution.
# It estimates how many times an event can happen in a specified time. (yani based on 
# the previous data, koi bhi ek event kitni dfa ho ga) e.g: If someone eats twice a day 
# what is the probability he will eat thrice?
# It has two parameters:
# lam - rate or known number of occurrences e.g. 2 for above problem.
# size - The shape of the returned array. size: This specifies the number of intervals
#  for which we want to generate data. Here, size=10 means we are simulating 10 intervals.

from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt
d=random.poisson(lam=2, size=10)  #lam=2 yani on average vo din m 2 dfa khata h, ap btao k
# kia probabilioty h k agly 10 din m vo 2 dfa s ziada khata h ya kam khata h ya khata hi nhi
# ya 2 dfa hi khay ga,,,,, y just ek simulation h, actual scenerio k outcome
# different ho skty hn
print(d)



# considering another example:
# ek store m on average 3 customers ek minute m visit krty hn, ap btao k agly 10 
# minutes m customers k any ki kia probability h?
customer=random.poisson(lam=3, size=10)
print(customer)
sns.histplot(customer, kde=True)
plt.show()


# DIFFERENCE BETWEEN NORMAL AND POISSON DISTRIBUTION:

# Normal distribution is continuous whereas poisson is discrete.
# poisson m size increase kr do to normal ki trah ka curve ay ga
# sns.histplot((random.normal(50,7,1000)),kde=True , label="normal")
# sns.histplot((random.poisson(lam=50, size=1000)),kde=True, label="poisson")
# plt.show()



# DIFFERENCE BETWEEN BINOMIAL AND POISSON DISTRIBUTION:
# in binomial, there are only 2 possible outcomes while in poisson there are many
# possible outcomes

# But for very large n and near-zero p binomial distribution is near identical to 
# poisson distribution such that n * p is nearly equal to lam. then the curve
# of poisson and binomial will same
sns.histplot((random.binomial(n=1000, p=0.01, size=1000)),kde=True , label="normal")
sns.histplot((random.poisson(lam=10, size=1000)),kde=True, label="poisson")
plt.show()
