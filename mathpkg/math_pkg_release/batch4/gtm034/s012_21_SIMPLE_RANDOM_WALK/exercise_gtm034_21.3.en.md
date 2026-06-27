---
role: exercise
locale: en
chapter: "V"
section: "21"
exercise_number: 3
---

Consider simple random walk $x_n$ in the plane $\mathbb{R}$. Given any positive integer $N$ we decompose $\mathbb{R}$ into the three sets
$$A_N = \{ z \mid z \in \mathbb{R}, \; z = k(1 + i) \text{ for some } k \geq N + 1 \},$$
$$B_N = \{ z \mid z \in \mathbb{R}, \; z = k(1 + i) \text{ for some } k < 0 \},$$
$$C_N = \mathbb{R} - (A_N \cup B_N).$$
Let $D$ be the entire diagonal $\{ z \mid z = n(1 + i), \; -\infty < n < \infty \}$.

It was shown in E8.3 that $P(x,y)$, defined in equation (4) of the text, is the transition function of the random walk executed by $x_n$ when it visits $D$ (the imbedded random walk associated with $D$). Show that for any real $t$, $0 < t < 1$, $R_N([Nt])$ has an interesting probability interpretation in terms of simple two-dimensional random walk $x_n$, and prove that the random walk in (4) has absorption probabilities given by
$$F_\alpha(x) = \frac{2}{\pi} \sin^{-1} \sqrt{x}, \quad 0 < x < 1.$$
