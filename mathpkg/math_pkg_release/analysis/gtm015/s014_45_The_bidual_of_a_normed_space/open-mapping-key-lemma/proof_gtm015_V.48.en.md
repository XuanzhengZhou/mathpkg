---
role: proof
locale: en
of_concept: open-mapping-key-lemma
source_book: gtm015
source_chapter: "V"
source_section: "48"
---

# Proof of the Key Lemma for the Open Mapping Theorem

Let $V$ be a neighborhood of $\theta$ in $E$. Choose a balanced neighborhood $W$ of $\theta$ such that $W + W \subset V$, and fix a scalar $\lambda$ with $|\lambda| > 1$ (e.g., $\lambda = 2$). We first show that
$$E = \bigcup_{n=1}^{\infty} \lambda^n W.$$

Let $x \in E$. By (17.11), $\mu x \in W$ for a suitable nonzero scalar $\mu$. Choose $n$ so that $|\lambda^{-n}\mu^{-1}| \leq 1$; since $W$ is balanced,
$$\lambda^{-n}x = (\lambda^{-n}\mu^{-1})(\mu x) \in W,$$
thus $x \in \lambda^n W$.

Since $T$ is surjective and linear, we have
$$F = T(E) = \bigcup_{1}^{\infty} T(\lambda^n W) = \bigcup_{1}^{\infty} \lambda^n T(W).$$

Since $F$ is a Baire space (being a complete, metrizable TVS; cf. 46.6), there exists an index $m$ such that $\overline{\lambda^m T(W)}$ has nonempty interior. It follows that $\overline{T(W)}$ has nonempty interior (because $y \mapsto \lambda^m y$ is a homeomorphism of $F$). Let $A = \operatorname{int}(\overline{T(W)}) \neq \varnothing$. Since $T(W)$ is symmetric ($-T(W) = T(-W) = T(W)$), it follows that $\overline{T(W)}$ is symmetric, hence $-A = A$.

Then $\theta \in A - A = A + A \subset \overline{T(W)} + \overline{T(W)} \subset \overline{T(W) + T(W)} = \overline{T(W + W)} \subset \overline{T(V)}$,
using the continuity of addition. Since $A + A$ is an open set (as the sum of open sets; 2.10), $\overline{T(V)}$ is a neighborhood of $\theta$ in $F$. $\square$
