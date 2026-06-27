---
role: exercise
locale: en
chapter: "1"
section: "Problems"
exercise_number: 6
---

6. For each $n \geq 1$, prove that $E[X_k] = 0$ and $E|X_k|^{n+1} = m_{n+1} < \infty$ imply $E[Z^n] < \infty$. Hint:

$$E[Z^n] = \sum_{k=1}^{\infty} k^n \sum_{k=1}^{0} g_{(0,\infty)}(0,x)P(x,k)$$

$$\leq \sum_{k=1}^{\infty} k^n \sum_{k=-\infty}^{0} g

$$E[Z^n] \leq M \sum_{k=1}^{\infty} k^n \sum_{z=-\infty}^{0} P(x,k) < \infty$$

when $m_{n+1} < \infty$. (Due to H. Kesten.)
