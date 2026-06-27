---
role: exercise
locale: en
chapter: "1"
section: "12"
exercise_number: 4
---

# Exercise 4

Consider a homogeneous Markov chain $\xi = (\xi_0, \xi_1, \ldots, \xi_n)$ taking values in $\{0, 1\}$ with transition matrix

$$
\mathbb{P} = \begin{pmatrix}
1-p & p \\
q & 1-q
\end{pmatrix},
$$

where $0 < p < 1$ and $0 < q < 1$. Let $S_n = \xi_0 + \xi_1 + \cdots + \xi_n$.

(a) As a generalization of the de Moivre--Laplace theorem (see Section 6), show that

$$
\mathrm{P}\left\{\frac{S_n - \frac{p}{p+q}\,n}{\sqrt{\frac{npq(2-p-q)}{(p+q)^3}}} \leq x\right\} \longrightarrow \Phi(x), \qquad n \to \infty,
$$

where $\Phi(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{x} e^{-u^2/2} \, du$ is the standard normal distribution function.

(b) Verify that in the special case $p + q = 1$, the random variables $\xi_0, \xi_1, \ldots, \xi_n$ are independent and the above statement reduces to the classical de Moivre--Laplace theorem:

$$
\mathrm{P}\left\{\frac{S_n - pn}{\sqrt{npq}} \leq x\right\} \longrightarrow \Phi(x), \qquad n \to \infty.
$$
