from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt
# It describes the outcome of binary scenarios, e.g. toss of a coin, it will either 
# be head or tails.
# It has three parameters:
# n - number of trials.
# p - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).
# size - The shape of the returned array.


x = random.binomial(n=5, p=0.5, size=10)
# print(x)  #[1 2 0 2 4 2 5 3 1 5] --->  if this is output : 0th index vala "1" show kr rha h
# 5 times experiment kia gya or un m s just "1" time success mili,, yani if we
# consider that our experiment is tossing a coin and consider kryn k jab head aya
# to hmari success ho gi then "1" yhan y show kr rha h k "5 times" coin ko toss kia gya
# or just "1" time head aya, 1st index vala 2 y show kr rha h k "5 times" coin ko toss
# kia gya or "2 times" head aya and so on


# ploting binomial distribution
toss_coin=random.binomial(n=10, p=0.5, size=10)
# print(toss_coin)
sns.histplot(toss_coin, kde=True)
plt.show()


# difference between NORMAL and BINOMIAL DISTRIBUTION
# ---> NORMAL is continous distribution
# ---> BINOMIAL is discrete distribution

#  agar ap binomial distribution m "size" ko increase kr do to vo normal distribution ki
# trah dikhy ga

# bulb_off_on=random.binomial(n=100, p=0.5, size=2000) #yani 100 trials m dekhna hr baar m 
# # bulb kitni dfa on ho ga or kitni dfa off hi rhy ga, considering ON is our success state
# print(bulb_off_on)
# # sns.histplot(bulb_off_on, kde=True)
# # plt.show()


bulb_off_on=random.binomial(n=50, p=0.5, size=10) #yani 100 trials m dekhna hr baar m 
# bulb kitni dfa on ho ga or kitni dfa off hi rhy ga, considering ON is our success state
print(bulb_off_on)
# sns.histplot(bulb_off_on, kde=True)
# plt.show()