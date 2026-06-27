---
role: proof
locale: en
of_concept: product-bound-spaces-ulam
source_book: gtm036
source_chapter: "19"
source_section: "19.8"
---

If there is an Ulam measure $m$ on $A$, one can construct a bounded linear functional on the product which is not continuous, showing the product topology is not bound. For each $t$ in $A$ choose $f_t$ in $E_t^*$ not identically zero. For $x$ in $\bigwedge \{E_t : t \in A\}$ let $g(x) = \int_A f_t(x_t) \, dm(t)$. Then $g$ is linear. Each bounded subset of the product is contained in a set of the form $B = \bigwedge \{B_t : t \in A\}$ with each $B_t$ bounded in $E_t$. Then $\sup\{|g(x)| : x \in B\} \leq \int_A \sup\{|f_t(x_t)| : x_t \in B_t\} \, dm(t)$, and this integral of a scalar-valued function exists, so $g$ is bounded on bounded subsets. However, $g$ is not continuous: if it were, there would be a finite subset $C$ of $A$ such that $g(x) = 0$ whenever $x_t = 0$ for all $t \in C$ (by 14.6). But choosing $x$ with $x_t = 0$ for $t \in C$ and $f_t(x_t) = 1$ for $t \in A \setminus C$ gives $g(x) = m(A \setminus C) = 1$, contradiction.

Conversely, if no Ulam measure exists on $A$, then every bounded linear functional on the product is continuous. The proof uses the lemma that any bounded linear functional determines a countably additive two-valued measure. Since the index set has no Ulam measure, any such measure must be supported on a finite set, which implies continuity of the functional. Thus the product topology is bound.
