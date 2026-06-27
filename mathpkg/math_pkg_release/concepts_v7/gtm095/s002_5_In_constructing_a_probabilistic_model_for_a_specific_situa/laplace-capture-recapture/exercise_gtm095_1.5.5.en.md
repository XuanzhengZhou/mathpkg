---
role: exercise
locale: en
chapter: "1"
section: "5"
exercise_number: "5"
---

# Exercise 5 — Laplace Capture-Recapture Method

Suppose we want to estimate the size $N$ of a population without a complete census. Such a question may be of interest, for example, when we try to estimate the population of a country, or a town, etc.

In 1786 Laplace proposed the following method to estimate the number $N$ of inhabitants of France.

Draw a sample of size $M$, say, from the population and mark its elements. Then return them into the initial population and assume that they become "well mixed" with unmarked elements. Then draw $n$ elements from the "mixed" population. Suppose there are $X$ marked elements among them.

**1.** Show that the corresponding probability $\mathrm{P}_{N,M;n}\{X = m\}$ is given by the formula for the hypergeometric distribution (cf. formula (4)):

$$\mathrm{P}_{N,M;n}\{X = m\} = \frac{\binom{M}{m} \binom{N-M}{n-m}}{\binom{N}{n}}.$$

**2.** For fixed $M$, $n$ and $m$, find $N$ maximizing this probability, i.e., find the "most likely" size of the whole population (for fixed $M$ and $n$) given that the number $X$ of marked elements in the repeated sample is equal to $m$.

Show that the "most likely" value (to be denoted by $\hat{N}$) is given by the formula (with $[\cdot]$ denoting the integral part):

$$\hat{N} = \left\lfloor \frac{Mn}{m} \right\rfloor.$$

The estimator $\hat{N}$ for $N$ obtained in this way is called the **maximum likelihood estimator**.

*(This problem is continued in Section 7, Problem 4.)*
