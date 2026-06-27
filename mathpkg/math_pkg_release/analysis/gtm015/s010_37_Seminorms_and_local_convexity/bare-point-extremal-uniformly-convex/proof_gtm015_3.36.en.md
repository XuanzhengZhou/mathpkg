---
role: proof
locale: en
of_concept: bare-point-extremal-uniformly-convex
source_book: gtm015
source_chapter: "3"
source_section: "36"
---

# Proof of Bare points are extremal in uniformly convex spaces

Let $E$ be a uniformly convex normed space. Let $A$ be a convex subset of $E$ and let $b \in A$ be a bare point of $A$. That is, there exist $x_0 \in E$ and $r > 0$ such that $\|b - x_0\| = r$ and $\|a - x_0\| \leq r$ for all $a \in A$ (so $b$ lies on the surface of a closed ball that contains $A$).

To show $b$ is an extremal point of $A$, suppose $b = \frac{1}{2}a_1 + \frac{1}{2}a_2$ with $a_1, a_2 \in A$. Then

$$\begin{aligned}
r = \|b - x_0\| &= \left\|\frac{1}{2}(a_1 - x_0) + \frac{1}{2}(a_2 - x_0)\right\| \\
&\leq \frac{1}{2}\|a_1 - x_0\| + \frac{1}{2}\|a_2 - x_0\| \leq \frac{1}{2}r + \frac{1}{2}r = r.
\end{aligned}$$

Thus equality holds throughout, which forces $\|a_1 - x_0\| = \|a_2 - x_0\| = r$ and also $\|\frac{1}{2}(a_1 - x_0) + \frac{1}{2}(a_2 - x_0)\| = r$. By uniform convexity, for any $\varepsilon > 0$, taking $\delta = 0$ (since $\|\frac{1}{2}(a_1 - x_0) + \frac{1}{2}(a_2 - x_0)\| = r \geq r - 0$), we obtain $\|(a_1 - x_0) - (a_2 - x_0)\| \leq \varepsilon$, i.e., $\|a_1 - a_2\| \leq \varepsilon$ for all $\varepsilon > 0$, hence $a_1 = a_2 = b$. Therefore $b$ is an extremal point of $A$.
