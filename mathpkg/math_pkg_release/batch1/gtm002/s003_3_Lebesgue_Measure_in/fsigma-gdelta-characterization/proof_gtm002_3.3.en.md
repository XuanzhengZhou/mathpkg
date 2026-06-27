---
role: proof
locale: en
of_concept: fsigma-gdelta-characterization
source_book: gtm002
source_chapter: "3"
source_section: "3. Lebesgue Measure in r-Space"
---

If $A$ is measurable, then for each $n$ there exists a closed set $F_n$ and an open set $G_n$ such that $F_n \subset A \subset G_n$ and $m^*(G_n - F_n) < 1/n$. Put $E = \bigcup_{n=1}^{\infty} F_n$ and $N = A - E$. Then $E$ is an $F_{\sigma}$ set. $N$ is a nullset, since $N \subset G_n - F_n$ and $m^*(N) < 1/n$ for every $n$. Moreover, $A$ is the disjoint union of $E$ and $N$. It follows by complementation that $A$ can also be represented as a $G_{\delta}$ set minus a nullset.

Conversely, any set that can be so represented is measurable, by Lemma 3.12 and the fact that the class $S$ of measurable sets is a $\sigma$-algebra.
