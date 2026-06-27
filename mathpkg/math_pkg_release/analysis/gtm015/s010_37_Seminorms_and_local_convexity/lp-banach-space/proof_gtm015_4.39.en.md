---
role: proof
locale: en
of_concept: lp-banach-space
source_book: gtm015
source_chapter: "4"
source_section: "39"
---

# Proof of $L^p$ is a Banach space

Let $(X, \mathcal{S}, \mu)$ be a measure space and $p \geq 1$. Recall $\mathcal{L}^p$ is the set of all measurable functions $f: X \to \mathbb{C}$ with $|f|^p$ integrable, equipped with the seminorm $\|f\|_p = (\int |f|^p d\mu)^{1/p}$.

Let $\mathcal{N} = \{f \in \mathcal{L}^p : \|f\|_p = 0\}$, the set of functions vanishing almost everywhere. By (39.7), $L^p = \mathcal{L}^p/\mathcal{N}$ is a normed space with $\|f + \mathcal{N}\| = \|f\|_p$.

To show $L^p$ is complete, let $(u_n)$ be a Cauchy sequence in $L^p$. Choose representatives $f_n \in \mathcal{L}^p$ with $u_n = f_n + \mathcal{N}$. Then $\|f_m - f_n\|_p \to 0$ as $m, n \to \infty$. By (39.6) (the Riesz-Fischer completeness theorem for $\mathcal{L}^p$), there exists $f \in \mathcal{L}^p$ such that $\|f_n - f\|_p \to 0$. Setting $u = f + \mathcal{N}$, we have $\|u_n - u\| = \|f_n - f\|_p \to 0$. Hence $L^p$ is complete, i.e., a Banach space.
