---
role: proof
locale: en
of_concept: generalized-hahn-banach-circled-variant
source_book: gtm036
source_chapter: "3"
source_section: "3.9"
---

(a) The definition $g(x) = \inf \{ p(x + \sum R_i(y_i)) : y_i \in E, R_i \in \mathcal{L}_1, k \in \mathbb{N} \}$ yields a functional satisfying the stated properties by standard arguments using the absolute convexity of $p$ and the fact that $\mathcal{L}_1$ consists of linear operators.

(b) If $f(x) \leq g(x)$ for all $x \in F$, then applying the classical Hahn-Banach theorem to $f$ (dominated by the subadditive, positively homogeneous functional $g$) yields an extension $\bar{f}$ with $\bar{f} \leq g \leq p$ on $E$. The condition $\bar{f} \circ R = 0$ for $R \in \mathcal{L}_1$ follows from the definition of $g$. Conversely, if such an extension exists, then $f(x) = \bar{f}(x) \leq g(x)$ for $x \in F$.

(c) The equivalence of (i), (ii), and (iii) follows from a compactness argument on finite subsets of $\mathcal{L}$ together with the characterization in part (b). The proof is omitted in the source text.
