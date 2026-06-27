---
role: proof
locale: en
of_concept: nilpotency-properties-of-lie-algebras
source_book: gtm009
source_chapter: "I"
source_section: "3.2"
---
(a) Imitate the proof of the solvability property: if $K$ is a subalgebra, then $K^i \subset L^i$, and if $\phi: L \to M$ is an epimorphism, then $\phi(L^i) = M^i$ by induction.

(b) Suppose $L^n \subset Z(L)$. Then $L^{n+1} = [L L^n] \subset [L Z(L)] = 0$, so $L$ is nilpotent.

(c) If $L$ is nilpotent, consider the descending central series $L^1 \supset L^2 \supset \cdots \supset L^k = 0$ with $L^k = 0$ but $L^{k-1} \neq 0$. By definition, $[L L^{k-1}] = L^k = 0$, so every element of $L^{k-1}$ commutes with all of $L$, i.e., $L^{k-1} \subset Z(L)$. Since $L^{k-1} \neq 0$, the center is nontrivial.
