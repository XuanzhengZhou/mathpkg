---
role: proof
locale: en
of_concept: measurability-criterion-by-ray
source_book: gtm018
source_chapter: "IV"
source_section: "18"
---
**Proof.** If $M = \{t : t < c\}$ is the open ray to $-\infty$, then $M$ is a Borel set and $f^{-1}(M) = \{x : f(x) < c\}$, so the condition is necessary.

Conversely, suppose the condition holds. For $c_1 \leq c_2$,
$$\{x : f(x) < c_2\} - \{x : f(x) < c_1\} = \{x : c_1 \leq f(x) < c_2\}.$$
Thus for any semiclosed interval $M$, $N(f) \cap f^{-1}(M)$ is the difference of two measurable sets, hence measurable. Let $\mathbf{E}$ be the class of all subsets $M$ of the extended real line for which $N(f) \cap f^{-1}(M)$ is measurable. Since $\mathbf{E}$ is a $\sigma$-ring containing all semiclosed intervals, it contains all Borel sets, completing the proof.
