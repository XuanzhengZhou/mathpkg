---
role: proof
locale: en
of_concept: uniqueness-of-limit
source_book: gtm012
source_chapter: "3"
source_section: "3. Sequences of real and complex numbers"
---

# Proof of Uniqueness of the limit

Suppose $(z_n)_{n=1}^{\infty}$ is a sequence in $\mathbb{C}$ such that $z_n \to z$ and also $z_n \to w$. We shall show that $z = w$.

Given any $\varepsilon > 0$, since $z_n \to z$ there exists $N_1$ such that $|z_n - z| < \varepsilon$ for all $n \geq N_1$. Similarly, since $z_n \to w$ there exists $N_2$ such that $|z_n - w| < \varepsilon$ for all $n \geq N_2$. Take $N = \max\{N_1, N_2\}$. Then for any $n \geq N$ we have both $|z_n - z| < \varepsilon$ and $|z_n - w| < \varepsilon$. By the triangle inequality,

$$|z - w| \leq |z - z_n| + |z_n - w| < \varepsilon + \varepsilon = 2\varepsilon.$$

Thus $|z - w| < 2\varepsilon$ for every $\varepsilon > 0$. Since $\varepsilon > 0$ is arbitrary, it follows that $|z - w| = 0$, hence $z = w$. $\square$

*Remark.* The same argument works in any metric space (or any normed vector space). This shows that limits of sequences are unique whenever the underlying space is Hausdorff.
