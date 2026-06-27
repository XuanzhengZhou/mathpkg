---
role: proof
locale: en
of_concept: sigma-equals-convex-hull-spectrum
source_book: gtm015
source_chapter: "61"
source_section: "Positivity in C*-algebras"
---

# Proof of Numerical status equals convex hull of spectrum

Proof. We know that $\sigma(a)$ is real (58.4); let $m$ be the smallest element of $\sigma(a)$, $M$ the largest. Thus $[m, M] = \text{conv} \sigma(a)$. Evidently $m1 \leq a \leq M1$ in the sense of (61.12); citing (ii) of (61.13), we have $m \leq f(a) \leq M$ for all $f \in \Sigma$, thus $\Sigma(a) \subset [m, M]$.

On the other hand, $\sigma(a) \subset \Sigma(a)$ by the proof of (61.10), therefore $\text{conv} \sigma(a) \subset \Sigma(a)$ by the convexity of $\Sigma(a)$.
