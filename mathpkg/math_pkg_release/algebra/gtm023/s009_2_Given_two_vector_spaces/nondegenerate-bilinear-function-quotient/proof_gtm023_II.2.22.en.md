---
role: proof
locale: en
of_concept: nondegenerate-bilinear-function-quotient
source_book: gtm023
source_chapter: "II"
source_section: "2.22"
---

To show that $\bar{\Phi}$ is well defined, suppose that $x' \in E$ and $y' \in F$ are two other vectors such that $\pi_E x = \pi_E x'$ and $\pi_F y = \pi_F y'$. Then $x' - x \in N_E$ and $y' - y \in N_F$, hence we can write $x' = x + u$, $u \in N_E$ and $y' = y + v$, $v \in N_F$. It follows that
$$\Phi(x', y') = \Phi(x + u, y + v)$$
$$= \Phi(x, y) + \Phi(x, v) + \Phi(u, y) + \Phi(u, v) = \Phi(x, y).$$
The terms $\Phi(x, v)$, $\Phi(u, y)$, and $\Phi(u, v)$ vanish because $u \in N_E$ and $v \in N_F$.

Clearly $\bar{\Phi}$ is bilinear. It remains to be shown that $\bar{\Phi}$ is non-degenerate. Assume that
$$\bar{\Phi}(\pi_E x, \pi_F y) = 0$$
for a fixed $\pi_E x$ and every $\pi_F y$. Then $\Phi(x, y) = 0$ for every $y \in F$. It follows that $x \in N_E$, whence $\pi_E x = 0$. Similarly, if the equality holds for a fixed $\pi_F y$ and every $\pi_E x$, then $\pi_F y = 0$. Hence $\bar{\Phi}$ is non-degenerate.
