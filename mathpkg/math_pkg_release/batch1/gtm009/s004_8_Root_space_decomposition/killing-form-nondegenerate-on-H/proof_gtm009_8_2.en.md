---
role: proof
locale: en
of_concept: killing-form-nondegenerate-on-H
source_book: gtm009
source_chapter: "8"
source_section: "8.2 Centralizer of H"
---

Let $C = C_L(H)$. One proves in succession (using the lemma that $\kappa(n, C) = 0$ for any nilpotent $n \in C$, properties of the Jordan decomposition, and Corollary 8.1):

(1) $C$ contains the semisimple and nilpotent parts of all its elements.
(2) All semisimple elements of $C$ lie in $H$.
(3) $\kappa$ restricts nondegenerately to $H \times H$.
(4) $C$ is nilpotent (by Engel's Theorem).
(5) $H \cap [C C] = 0$ (using associativity of $\kappa$ and (3)).
(6) $C$ is abelian. Otherwise $[C C] \neq 0$; by nilpotence of $C$, $Z(C) \cap [C C] \neq 0$. Let $z \neq 0$ lie in this intersection. By (2) and (5), $z$ cannot be semisimple. Its nilpotent part $n$ is nonzero, lies in $C$ by (1), and lies in $Z(C)$ by Proposition 4.2. The lemma then implies $\kappa(n, C) = 0$, contradicting Corollary 8.1.
(7) $C = H$. Otherwise $C$ contains a nonzero nilpotent element $x$ by (1) and (2). According to the lemma and (6), $\kappa(x, y) = \mathrm{Tr}(\mathrm{ad} x \, \mathrm{ad} y) = 0$ for all $y \in C$, contradicting Corollary 8.1.

Since $C = H$, Corollary 8.1 implies that $\kappa$ restricted to $H$ is nondegenerate.
