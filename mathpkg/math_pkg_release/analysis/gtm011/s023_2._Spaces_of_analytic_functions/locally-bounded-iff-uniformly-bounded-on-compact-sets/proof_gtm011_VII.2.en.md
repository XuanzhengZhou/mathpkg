---
role: proof
locale: en
of_concept: locally-bounded-iff-uniformly-bounded-on-compact-sets
source_book: gtm011
source_chapter: "VII"
source_section: "2"
---

The proof is left to the reader in the text, but the equivalence follows by a standard compactness argument:

($\Leftarrow$) If $\mathcal{F}$ is uniformly bounded on compact sets, then in particular for each $a \in G$, the closed disk $\overline{B}(a; r)$ for sufficiently small $r > 0$ is a compact subset of $G$, so $\mathcal{F}$ is uniformly bounded on this disk, hence locally bounded.

($\Rightarrow$) Suppose $\mathcal{F}$ is locally bounded. Let $K \subset G$ be compact. For each $a \in K$, there exist $r_a > 0$ and $M_a$ such that $|f(z)| \leq M_a$ for all $f \in \mathcal{F}$ and $z \in B(a; r_a)$. The open cover $\{B(a; r_a) : a \in K\}$ of $K$ has a finite subcover $B(a_1; r_{a_1}), \ldots, B(a_n; r_{a_n})$. Set $M = \max\{M_{a_1}, \ldots, M_{a_n}\}$. Then $|f(z)| \leq M$ for all $f \in \mathcal{F}$ and $z \in K$.
