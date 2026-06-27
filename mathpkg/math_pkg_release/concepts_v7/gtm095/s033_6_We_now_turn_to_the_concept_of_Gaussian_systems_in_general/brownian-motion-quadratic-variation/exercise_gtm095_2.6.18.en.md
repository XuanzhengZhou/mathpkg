---
role: exercise
locale: en
chapter: "2"
section: "6"
exercise_number: 18
---

# Exercise 18

Give a detailed proof that the processes $(B_t)_{0 \leq t \leq 1}$ defined by

$$B_t = \frac{\sqrt{2}}{\pi} \sum_{n=1}^{\infty} \frac{\xi_n}{n+1/2} \sin((n+1/2)\pi t), \quad t \in [0, 1],$$

and by

$$B_t = \sum_{n=1}^{\infty} \xi_n \int_0^t H_n(u) \, du, \quad t \in [0, 1],$$

(where $\xi_n$ are independent $\mathcal{N}(0,1)$ random variables and $H_n$ are the Haar functions) are standard Brownian motions.

*Hint.* For the first construction, use the "two series" theorem (Theorem 2 in Sect. 3, Chap. 4, Vol. 2) to establish almost-sure uniform convergence of the series, which yields continuous paths. Then apply Theorem 1(b) and the preservation of Gaussianity under limits in probability to conclude that the finite-dimensional distributions are Gaussian. Finally, compute the covariance function and verify that it equals $\min(s, t)$.
