---
role: proof
locale: en
of_concept: gelfand-theorem-commutative-cstar
source_book: gtm003
source_chapter: "VI"
source_section: "2"
---

By the Gelfand-Mazur theorem and the lemma of Section 1, $A/J$ is isometrically isomorphic to $\mathbf{C}$ for each maximal (necessarily closed) proper ideal $J$ of $A$. The composition $f: A \to A/J \to \mathbf{C}$ is a contractive, multiplicative linear form on $A$ of norm 1, because $f(e) = 1$. The set $K$ of all these forms is a bounded subset of the dual Banach space $A'$ of $A$ and is $\sigma(A', A)$-closed. By (III, 4.3) Corollary, $K$ is compact for this topology.

Every $f \in K$ is a $^*$-homomorphism: if $f \in K$ is arbitrary, then $f(f(x)e - x) = 0$ implies $f(x) \in \sigma(x)$. So if $x$ is self-adjoint, by 2.1(iv) $f(x) \in \mathbf{R}$. This implies $f(y^*) = \overline{f(y)}$ for each $y = a + ib$ where $a, b \in A_{sa}$.

Furthermore, $\|x\| = \sup\{|f(x)| : f \in K\}$, which implies $K$ separates points on $A$. The Gelfand transform $\Gamma: A \to C(K)$ defined by $\Gamma(x)(f) = f(x)$ is an isometric $^*$-isomorphism. Uniqueness of $K$ up to homeomorphism follows from the uniqueness of the maximal ideal space.
