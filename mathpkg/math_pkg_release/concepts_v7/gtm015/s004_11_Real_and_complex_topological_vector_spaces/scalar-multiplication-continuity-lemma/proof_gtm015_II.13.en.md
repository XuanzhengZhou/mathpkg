---
role: proof
locale: en
of_concept: scalar-multiplication-continuity-lemma
source_book: gtm015
source_chapter: "Chapter 2 – Topological Vector Spaces"
source_section: "13. Spaces of type (F)"
---

# Proof of Scalar Multiplication Continuity Lemma

**Lemma (13.3).** Let $E$ be a vector space over $\mathbb{K}$, with a metrizable topology such that (i) the topology is compatible with the additive group structure, (ii) for each $x \in E$, the mapping $\lambda \mapsto \lambda x$ is continuous at $\lambda = 0$, and (iii) for each $\lambda \in \mathbb{K}$, the mapping $x \mapsto \lambda x$ is continuous at $x = \theta$. Then the topology is compatible with the vector space structure, i.e., $E$ is a TVS.

*Proof.* By (11.3), it suffices to show that the mapping $(\lambda, x) \mapsto \lambda x$ is continuous at $(0, \theta)$. Let $d$ be an invariant metric compatible with the additive group structure. Let $\varepsilon > 0$ be given; we seek $\delta > 0$ and a neighborhood $V$ of $\theta$ such that $|\lambda| < \delta$ and $x \in V$ imply $d(\lambda x, \theta) < \varepsilon$.

Choose a symmetric neighborhood $U$ of $\theta$ with $U + U \subset \{y : d(y, \theta) < \varepsilon\}$ (possible by continuity of addition at $(\theta, \theta)$). Define

$$C_k = \{\lambda \in \mathbb{K} : |\lambda| \leq 1/k\},$$

and suppose to the contrary that for each $k$ there exist $\lambda_k$ with $|\lambda_k| < 1/k$ and $x_k \in U$ such that $\lambda_k x_k \notin U$. We derive a contradiction.

By (ii), $\lambda \mapsto \lambda x_k$ is continuous at 0, so for each $k$ there exists $\delta_k > 0$ with the property that $|\lambda| < \delta_k$ implies $\lambda x_k \in U$. But $\lambda_k \to 0$, so for sufficiently large $k$, $|\lambda_k| < \delta_k$, which would give $\lambda_k x_k \in U$, contradicting the choice of $x_k$.

More precisely, let $A = \{\mu : |\mu| < \delta\}$ be a symmetric neighborhood of $0$ in $\mathbb{K}$ such that $\lambda_0 + A \subset C_k$. Choose $n$ large enough that $\lambda_i \in A$ for all $i \geq n$ (possible since $\lambda_i \to 0$) and $\lambda_0 x_i \in U$ for all $i \geq n$ (possible by (iii)). Let $m = \max\{k, n\}$. Then $\lambda_0 + \lambda_m \in C_k$, hence $(\lambda_0 + \lambda_m)x_m \in U$. Also $\lambda_0 x_m \in U$ and $-\lambda_0 x_m \in -U = U$. Writing $x = -\lambda_0 x_m$ and $y = (\lambda_0 + \lambda_m)x_m$, we have $x, y \in U$ and $x + y = \lambda_m x_m$, so $d(\lambda_m x_m, \theta) = d(x + y, \theta) < \varepsilon$ by the definition of $U$, contrary to the assumption. This contradiction establishes the continuity of $(\lambda, x) \mapsto \lambda x$ at $(0, \theta)$. $\square$
