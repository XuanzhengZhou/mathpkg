---
role: proof
locale: en
of_concept: d-metric-completeness-on-measurable-quotient
source_book: gtm015
source_chapter: "Chapter 2 – Topological Vector Spaces"
source_section: "15. The space (S)"
---

# Proof of Completeness of $d$ on $[\mathcal{M}]$

**Lemma (15.5).** $d$ is a complete metric on $[\mathcal{M}]$.

*Proof.* Let $u_n$ be a Cauchy sequence in $[\mathcal{M}]$, say $u_n = [f_n]$. According to (15.4), $f_n$ is fundamental in measure; by the Riesz-Weyl theorem, there exists $f \in \mathcal{M}$ with $f_n \to f$ in measure [10, p. 67, Th. 4]. Writing $u = [f]$, we have $u_n \to u$ by (15.4). Thus every Cauchy sequence converges, proving completeness. $\square$
