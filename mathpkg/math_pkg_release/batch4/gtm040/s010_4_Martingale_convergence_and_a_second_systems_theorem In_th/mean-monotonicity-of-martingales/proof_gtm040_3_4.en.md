---
role: proof
locale: en
of_concept: mean-monotonicity-of-martingales
source_book: gtm040
source_chapter: "3"
source_section: "4"
---

The result is immediate from Lemma 3-6 when $R_k$ is taken as $\Omega$. Indeed, Lemma 3-6 gives the integral identity for conditional expectations on cells of the partition, and taking the whole space $\Omega$ (which is the union of all cells of $\mathcal{R}_n$) yields the unconditional mean. For a martingale, $M[f_n \mid \mathcal{R}_{n-1}] = f_{n-1}$ implies $M[f_n] = M[f_{n-1}]$; for a supermartingale, $M[f_n \mid \mathcal{R}_{n-1}] \leq f_{n-1}$ implies $M[f_n] \leq M[f_{n-1}]$; and for a submartingale, $M[f_n \mid \mathcal{R}_{n-1}] \geq f_{n-1}$ implies $M[f_n] \geq M[f_{n-1}]$.
