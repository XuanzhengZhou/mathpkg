---
role: exercise
locale: en
chapter: "VI"
section: "32"
exercise_number: 7
---

The mean square distance of a random walk $x_n$ from the origin, subject to the condition of no return to the origin in time $n$, is
$$D_n = E_0[|x_n|^2 \mid T > n] = \frac{1}{R_n} E_0[|x_n|^2; T > n].$$

Suppose that the random walk is genuinely $d$-dimensional, with mean vector zero and second moment $m_2 = E_0[|x_1|^2] < \infty$. When the dimension $d = 1$, prove that
$$D_n \sim 2n m_2 = 2E_0[|x_n|^2] \text{ as } n \to \infty,$$
whereas for dimension $d \geq 2$,
$$D_n \sim n m_2 = E_0[|x_n|^2] \text{ as } n \to \infty.$$

Hint: To obtain these asymptotic relations, first derive the identity
$$E_0[|x_n|^2; T > n] = (R_0 + R_1 + \cdots + R_{n-1}) m_2, \quad n \geq 1.$$
