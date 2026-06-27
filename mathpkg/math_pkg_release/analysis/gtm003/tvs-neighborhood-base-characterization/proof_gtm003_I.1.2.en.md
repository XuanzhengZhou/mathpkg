---
role: proof
locale: en
of_concept: tvs-neighborhood-base-characterization
source_book: gtm003
source_chapter: "I. Topological Vector Spaces"
source_section: "1.2"
---

**Proof.** We first prove the existence, in every t.v.s., of a 0-neighborhood base having the listed properties. Given a 0-neighborhood $V$ in a t.v.s., there exists a 0-neighborhood $U$ and a real number $\varepsilon > 0$ such that $\lambda U \subset V$ whenever $|\lambda| \leq \varepsilon$. Since the scalar field is non-discrete, we can pick $\mu \in K$ with $0 < |\mu| \leq \varepsilon$. Then $\mu U$ is a 0-neighborhood which is contained in $V$ and satisfies (c) with $\lambda = \mu$. Moreover, by continuity of addition at $(0,0)$, for each 0-neighborhood $V$ there exists a 0-neighborhood $U$ with $U + U \subset V$, giving condition (a). Finally, every 0-neighborhood contains a circled 0-neighborhood, and the radial property follows from continuity of scalar multiplication $(\lambda, x) \mapsto \lambda x$ at $(0,0)$.

Conversely, assume $\mathfrak{T}$ is translation-invariant and possesses a 0-neighborhood base $\mathfrak{V}$ satisfying (a), (b), (c). Translation-invariance implies $(LT)_1$ (continuity of addition) is equivalent to: for each $V \in \mathfrak{V}$ there exists $U \in \mathfrak{V}$ with $U + U \subset V$, which is precisely condition (a).

For $(LT)_2$ (continuity of scalar multiplication), let $(\lambda_0, x_0) \in K \times L$ and let $V \in \mathfrak{V}$. By (a), choose $U \in \mathfrak{V}$ with $U + U \subset V$. Let $\mu \in K$ satisfy (c); then there exists an integer $n \in \mathbb{N}$ such that $|\mu^{-n}| = |\mu|^{-n} \geq |\lambda_0| + \varepsilon$; let $W \in \mathfrak{V}$ be defined by $W = \mu^n U$. Now since $U$ is circled, the relations $x - x_0 \in W$ and $|\lambda - \lambda_0| \leq \varepsilon$ imply that $\lambda(x - x_0) \in U$, and hence the identity

$$\lambda x = \lambda_0 x_0 + (\lambda - \lambda_0)x_0 + \lambda(x - x_0)$$

implies that $\lambda x \in \lambda_0 x_0 + U + U \subset \lambda_0 x_0 + V$, which proves $(LT)_2$.

Finally, if $K$ is an Archimedean valuated field, then $|2| > 1$ for $2 \in K$. Hence $|2^n| = |2|^n > |\lambda_0| + \varepsilon$ (notation of the preceding paragraph) for a suitable $n \in \mathbb{N}$. By repeated application of (b), we can select a $W_1 \in \mathfrak{V}$ such that $2^n W_1 \subset W_1 + \cdots + W_1 \subset U$, where the sum has $2^n$ summands $(2 \in \mathbb{N})$. Since $W_1$ (and hence $2^n W_1$) is circled, $W_1$ can be substituted for $W$ in the preceding proof of $(LT)_2$, and hence (c) is dispensable in this case. This completes the proof.
