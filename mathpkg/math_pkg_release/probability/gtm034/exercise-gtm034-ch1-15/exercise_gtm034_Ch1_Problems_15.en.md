---
role: exercise
locale: en
chapter: "1"
section: "Problems"
exercise_number: 15
---

15. Coin tossing at random times (Täcklind [98]). The compound Poisson process $x(t)$ is defined as $x(t) = x_{N(t)}$, where $x_n$ is simple one-dimensional random walk with $x_0 = 0$. $N(t)$ is the simple Poisson process defined for $t \geq 0$ by $N(0) = 0$ and

$$P[N(t_1) = n_1, N(t_2) = n_2, \ldots, N(t_k) = n_k] = \prod_{j=1}^{k} \frac{e^{-a(t_j - t_{j-1})}}{(n_j - n_{j-1})!} [a(t_j - t_{j-1})]^{(n_j - n_{j-1})}$$

for real $0 = t_0 < t_1 < \cdots < t_k$ and integer valued $0 = n_0 \leq n_1 \leq \cdots \leq n_k$. Thus $x(t)$ will be a step function; its jumps are of magnitude one, and the independent, exponentially distributed time intervals between jumps have mean $1/a$. Prove that

$$P\left[ \sup_{0 \leq t \leq t} x(\tau) \geq n \right] = \sum_{k=0}^{\infty} e^{-at} \frac{(at)^k}{k!} P_0\left[ \max\{0, x_1, x_2, \ldots, x_k\} \geq n \right]$$

$$= \begin{cases} 1 \text{ for } n = 0, \\ n \int_0^t e^{-ax} \frac{I_n(ax)}{x} dx \text{ for } n \geq 1. \end{cases}$$

Here $I_n(x) = i
