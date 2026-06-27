---
role: proof
locale: en
of_concept: completeness-of-bounded-linear-operators
source_book: gtm015
source_chapter: "IV"
source_section: "40"
---

# Proof of Completeness of the space of continuous linear mappings when the codomain is Banach

**Theorem (40.7).** Let $E$ and $F$ be normed spaces over $\mathbb{K}$. If $F$ is a Banach space, then the space $\mathcal{L}(E, F)$ of continuous linear mappings from $E$ to $F$, equipped with the operator norm, is also a Banach space.

**Proof.**

Let $(T_n)$ be a Cauchy sequence in $\mathcal{L}(E, F)$. We must show that $(T_n)$ converges to some $T \in \mathcal{L}(E, F)$.

For each fixed $x \in E$, the inequality

$$\|T_m x - T_n x\| = \|(T_m - T_n)x\| \leq \|T_m - T_n\| \cdot \|x\|$$

shows that $(T_n x)$ is a Cauchy sequence in $F$. Since $F$ is complete, the limit

$$Tx = \lim_{n \to \infty} T_n x$$

exists in $F$. This defines a mapping $T: E \to F$.

*Linearity of $T$.* For $x, y \in E$ and $\lambda \in \mathbb{K}$,

$$T(x + y) = \lim T_n(x + y) = \lim(T_n x + T_n y) = \lim T_n x + \lim T_n y = Tx + Ty,$$

$$T(\lambda x) = \lim T_n(\lambda x) = \lim \lambda(T_n x) = \lambda \lim T_n x = \lambda Tx.$$

*Continuity of $T$.* Since $(T_n)$ is Cauchy, $(\|T_n\|)$ is a bounded sequence; let $M = \sup_n \|T_n\| < \infty$. For any $x \in E$,

$$\|Tx\| = \lim_{n \to \infty} \|T_n x\| \leq \limsup_{n \to \infty} \|T_n\| \cdot \|x\| \leq M\|x\|.$$

Thus $T$ is continuous (by Theorem 40.1) with $\|T\| \leq M$.

*Convergence in operator norm.* Given $\varepsilon > 0$, choose $N$ such that $\|T_m - T_n\| \leq \varepsilon$ for all $m, n \geq N$. For any $x \in E$ with $\|x\| \leq 1$ and any $m, n \geq N$,

$$\|T_m x - T_n x\| \leq \|T_m - T_n\| \cdot \|x\| \leq \varepsilon.$$

Fixing $n \geq N$ and letting $m \to \infty$, we obtain

$$\|Tx - T_n x\| \leq \varepsilon \quad \text{for all } x \text{ with } \|x\| \leq 1.$$

Hence $\|T - T_n\| \leq \varepsilon$ for all $n \geq N$. This shows $T_n \to T$ in the operator norm. Since $T = (T - T_n) + T_n$ and both terms are continuous, $T \in \mathcal{L}(E, F)$.

Therefore, every Cauchy sequence in $\mathcal{L}(E, F)$ converges, so $\mathcal{L}(E, F)$ is a Banach space.
