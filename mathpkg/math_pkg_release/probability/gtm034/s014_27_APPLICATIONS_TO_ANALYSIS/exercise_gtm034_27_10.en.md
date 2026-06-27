---
role: exercise
locale: en
chapter: "27"
section: "APPLICATIONS TO ANALYSIS"
exercise_number: 10
---

Continuation. If $x \to \infty$ in the direction of the mean vector $\mu$, use the Local Central Limit Theorems P7.9 and P7.10 to show that
$$\lim_{x \to \infty} \frac{G(x,y)}{G(x,0)} = 1, \quad y \in R.$$

If $x \to \infty$ in the direction $p$, choose $a = a(p) \in A$ as in problem 9, and observe that the random walk with transition function
$$Q(x,y) = P(x,y)e^{a \cdot (y-x)}$$
has its mean vector along $p$. Using this idea, P. Ney and the author proved
$$\lim_{|x| \to \infty} \left| \frac{G(y,x)}{G(0,x)} - e^{a(x)\cdot y} \right| = 0$$
for every $y \in R$. Now one can imitate the method of E27.5 to conclude that the regular functions of a random walk subject to the conditions in problem 9 have the representation
$$f(x) = \int_A e^{a \cdot x} d\mu(a), \quad x \in R,$$
where $\mu$ is a Lebesgue-Stieltjes measure on $A$.
