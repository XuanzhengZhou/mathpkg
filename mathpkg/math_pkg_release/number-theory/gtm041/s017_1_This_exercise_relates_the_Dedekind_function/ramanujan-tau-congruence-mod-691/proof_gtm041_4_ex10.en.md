---
role: proof
locale: en
of_concept: ramanujan-tau-congruence-mod-691
source_book: gtm041
source_chapter: "4"
source_section: "Exercises for Chapter 4, Exercise 10"
---

From Exercise 9 we have the identity
$$(504)^2 \sum_{k=0}^{n} \sigma_5(k)\sigma_5(n-k) = \tau(n+1) - 984\tau(n) + \sum_{k=1}^{n-1} c(k)\tau(n-k).$$

Using Exercise 10 of Chapter 6 together with this identity, Lehmer [20] derived the formula
$$\frac{65520}{691}\{\sigma_{11}(n) - \tau(n)\} = \tau(n+1) + 24\tau(n) + \sum_{k=1}^{n-1} c(k)\tau(n-k).$$

The right-hand side is an integer because $\tau(n)$ and $c(k)$ are integers. Therefore the left-hand side is an integer, which implies
$$\frac{65520}{691}(\sigma_{11}(n) - \tau(n)) \in \mathbb{Z}.$$

Since $\gcd(65520, 691) = 1$ (as $691$ is prime and does not divide $65520$), we must have $\sigma_{11}(n) - \tau(n)$ divisible by $691$. Hence
$$\tau(n) \equiv \sigma_{11}(n) \pmod{691}$$
for all positive integers $n$.
