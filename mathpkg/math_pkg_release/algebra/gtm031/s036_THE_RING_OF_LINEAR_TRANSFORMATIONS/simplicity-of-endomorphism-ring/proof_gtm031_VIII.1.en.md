---
role: proof
locale: en
of_concept: simplicity-of-endomorphism-ring
source_book: gtm031
source_chapter: "VIII"
source_section: "1. Simplicity of $\\mathfrak{L}$"
---

**First proof (via matrix units).** Let $\mathfrak{B} \neq 0$ be a two-sided ideal in $\mathfrak{L}$. Choose $B \neq 0$ in $\mathfrak{B}$ and write $B = \sum \bar{\beta}_{ij} E_{ij}$ where not all $\bar{\beta}_{ij} = 0$. Suppose $\bar{\beta}_{pq} \neq 0$ for some $p, q$. By the coefficient formula,

$$\bar{\beta}_{pq} = \sum_k E_{kp} B E_{qk}.$$

Since $\mathfrak{B}$ is a two-sided ideal, each term $E_{kp} B E_{qk} \in \mathfrak{B}$, and therefore $\bar{\beta}_{pq} \in \mathfrak{B}$. Since the map $\alpha \mapsto \bar{\alpha}$ is an isomorphism $\Delta \cong \bar{\Delta}$, $\bar{\beta}_{pq} \neq 0$ implies that $\bar{\beta}_{pq}$ has an inverse in $\bar{\Delta}$, say $\bar{\gamma}$. Thus $\bar{\gamma} \bar{\beta}_{pq} = 1 \in \mathfrak{B}$. Hence $\mathfrak{B} = \mathfrak{L}$, proving $\mathfrak{L}$ is simple.
