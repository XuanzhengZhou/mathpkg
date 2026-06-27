---
role: proof
locale: en
of_concept: elementarily-definable-subsets-nonempty
source_book: gtm037
source_chapter: "13"
source_section: "Decidable Theories"
---

By the decision method for $\Gamma_3$ (Theorem 13.12), a subset $B$ of $A$ is elementarily definable iff there is a formula $\varphi(x)$ in the pure language of equality such that $B = \{a \in A : \varphi(a) \text{ holds in } A\}$. The decision method shows that any such formula $\varphi(x)$ is equivalent in the pure theory of equality to a Boolean combination of formulas of the form $\varepsilon_m$ (asserting "there are at least $m$ elements"). In a nonempty set $A$, such formulas can only distinguish between "there is at least one element" (always true) and "there are at least $m$ elements" for $m > |A|$ (false on $A$). Thus $\varphi(x)$ can only define either the empty set or the whole set $A$.
