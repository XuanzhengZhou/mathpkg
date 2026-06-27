---
role: proof
locale: en
of_concept: measurable-function-simple-approximation
source_book: gtm055
source_chapter: "6"
source_section: "8"
---

(Sketch, see Problem S.) (iii)$\Rightarrow$(ii)$\Rightarrow$(i) is immediate. For (i)$\Rightarrow$(iii): decompose $f = f^+ - f^-$ with $f^\pm \ge 0$ measurable. For a nonnegative measurable $g$, define $s_n(x) = \sum_{k=0}^{n2^n-1} \frac{k}{2^n} \chi_{E_{n,k}}(x) + n \chi_{F_n}(x)$ where $E_{n,k} = \{x: k/2^n \leq g(x) < (k+1)/2^n\}$ and $F_n = \{x: g(x) \ge n\}$. Then $0 \leq s_n \leq g$, $s_n \uparrow g$ pointwise, with uniform convergence on bounded sets. Apply to $f^+$ and $f^-$.
