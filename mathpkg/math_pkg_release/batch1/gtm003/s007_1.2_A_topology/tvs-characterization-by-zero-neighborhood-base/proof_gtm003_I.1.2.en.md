---
role: proof
locale: en
of_concept: tvs-characterization-by-zero-neighborhood-base
source_book: gtm003
source_chapter: "I"
source_section: "1.2"
---

We first prove the existence, in every t.v.s., of a $0$-neighborhood base having the listed properties. Given a $0$-neighborhood base $\mathfrak{V}$ in a t.v.s. $L$, by $(LT)_1$ the map $(x, y) \mapsto x + y$ is continuous at $(0, 0)$, so for each $V \in \mathfrak{V}$ there exists $U \in \mathfrak{V}$ with $U + U \subset V$, proving (a). By continuity of scalar multiplication $(\lambda, x) \mapsto \lambda x$ at $(0, 0)$, each $V$ is radial; by continuity at $(\lambda, 0)$ for $|\lambda| \leq 1$, each $V$ contains a circled neighborhood, so (b) holds after replacing $\mathfrak{V}$ by a circled base. For (c), the continuity of $\lambda \mapsto \lambda x$ at $\lambda = 0$ for fixed $x$ yields the required $\lambda$.

Conversely, suppose $\mathfrak{T}$ is translation-invariant with a $0$-neighborhood base $\mathfrak{V}$ satisfying (a)--(c). Translation invariance gives $(LT)_1$. To prove $(LT)_2$, let $(\lambda_0, x_0) \in K \times L$ and let $V \in \mathfrak{V}$. Choose $U \in \mathfrak{V}$ such that $U + U \subset V$. Since $U$ is radial, there exists $\varepsilon > 0$ such that $|\lambda - \lambda_0| \leq \varepsilon$ implies $(\lambda - \lambda_0) x_0 \in U$.

Let $\mu \in K$ satisfy (c); then there exists an integer $n \in \mathbb{N}$ such that $|\mu^{-n}| = |\mu|^{-n} \geq |\lambda_0| + \varepsilon$; let $W \in \mathfrak{V}$ be defined by $W = \mu^n U$. Now since $U$ is circled, the relations $x - x_0 \in W$ and $|\lambda - \lambda_0| \leq \varepsilon$ imply that $\lambda(x - x_0) \in U$, and hence the identity

$$\lambda x = \lambda_0 x_0 + (\lambda - \lambda_0)x_0 + \lambda(x - x_0)$$

implies that $\lambda x \in \lambda_0 x_0 + U + U \subset \lambda_0 x_0 + V$, which proves $(LT)_2$.

Finally, if $K$ is an Archimedean valuated field, then $|2| > 1$ for $2 \in K$. Hence $|2^n| = |2|^n > |\lambda_0| + \varepsilon$ (notation of the preceding paragraph) for a suitable $n \in \mathbb{N}$. By repeated application of (b), we can select a $W_1 \in \mathfrak{V}$ such that $2^n W_1 \subset W_1 + \cdots + W_1 \subset U$, where the sum has $2^n$ summands ($2 \in \mathbb{N}$). Since $W_1$ (and hence $2^n W_1$) is circled, $W_1$ can be substituted for $W$ in the preceding proof of $(LT)_2$, and hence (c) is dispensable in this case. This completes the proof of (1.2).
