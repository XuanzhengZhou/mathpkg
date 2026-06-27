---
role: proof
locale: en
of_concept: "let-then-if-leq"
source_book: gtm025
source_chapter: "Extending Functionals"
source_section: "9.4"
---

Let $\varepsilon > 0$ be fixed. Choose $f_0 \in \mathfrak{D}$ and define $A_0 = \{x \in X : f_0(x) > 0\}^-$. Since $f_0 \in \mathfrak{C}_{00}, A_0$ is compact. For each $f \in \mathfrak{D}$, let $A_f = \{x \in A_0 : f(x) \geq \varepsilon\}$. Then $\{A_f : f \in \mathfrak{D}\}$ is a family of closed subsets of the compact space $A_0$ and $\cap \{A_f : f \in \mathfrak{D}\} = \varnothing$. It follows (6.34) that this family does not have the finite intersection property, i.e., there is a finite subset $\{f_1, \ldots, f_n\}$ of $\mathfrak{D}$ such that $A_{f_1} \cap A_{f_2} \cap \cdots \cap A_{f_n} = \varnothing$. Since $\mathfrak{D}$ is directed downward, there is a function $f_\varepsilon \in \mathfrak{D}$ such that $f_\varepsilon \leq \min\{f_0, f_1, \ldots, f_n\}$; plainly $\|f_\varepsilon\|_u < \varepsilon$.

To prove (i), apply (9.5) to find a real number $\beta$ [depending only on $A_0$ and not on $\varepsilon$] such that $|I(f)| \leq \beta \|f\|_u$ for all $f

These assertions are all obvious upon a moment's reflection.
The next theorem is a counterpart of (9.6).
