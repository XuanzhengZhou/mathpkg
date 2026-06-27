---
role: proof
locale: en
of_concept: boolean-valued-quantifier-formulas
source_book: gtm008
source_chapter: "23"
source_section: "Boolean Algebras That Are Not Sets"
---

The proof is analogous to the set-sized case (Theorem 13.13). For the existential quantifier, one verifies that the meet-semilattice of values $u(x) \cdot \llbracket \varphi(x) \rrbracket$ for $x \in \mathcal{D}(u)$ has the same supremum as the collection of values $\llbracket \psi \rrbracket$ for witnesses $\psi$ of $(\exists x \in u)\varphi(x)$. The universal quantifier case follows by duality: $\forall$ is the De Morgan dual of $\exists$ via negation and the Boolean implication $a \Rightarrow b = -a + b$.

For $V^{(B)}$, the existence of the supremum over the possibly class-sized index set $\mathcal{D}(u)$ is justified by Theorem 23.3 (or similar bounding results), which shows that the supremum can be reduced to a set-sized supremum. For $V^{(\tilde{B})}$, the completeness of $\tilde{B}$ directly guarantees the existence of all required suprema and infima.
