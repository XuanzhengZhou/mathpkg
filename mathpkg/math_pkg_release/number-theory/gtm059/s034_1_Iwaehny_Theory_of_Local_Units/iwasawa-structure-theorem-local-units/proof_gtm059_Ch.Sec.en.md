---
role: proof
locale: en
of_concept: iwasawa-structure-theorem-local-units
source_book: gtm059
source_chapter: "Iwasawa Theory of Local Units"
source_section: "2"
---

**Proof.** The proof proceeds in several steps, occupying the remainder of this section and culminating in the construction of an explicit $\Lambda$-basis for $U(\chi)$.

*Step 1: Reduction.* By Lemma 1 (rank of the unit $\chi$-eigenspace), we have $\operatorname{rank}_{\mathbb{Z}_p} U_n(\chi) = p^n$ for each $n$ and $\chi \neq 1$. Passing to the projective limit, one deduces that $U(\chi)$ is a finitely generated torsion-free $\Lambda$-module. By Lemma 2, $U$ has no $\mathbb{Z}_p$-torsion, so $U(\chi)$ is a torsion-free $\Lambda$-module.

*Step 2: Exact sequence.* One considers the exact sequence of $\Lambda$-modules
$$0 \to U(\chi) \to A \to B \to 0$$
where $A$ is a free $\Lambda$-module and $B$ is a finite module. Using the Iwasawa algebra structure theorem (Chapter 5), one shows that a finitely generated $\Lambda$-module whose reduction modulo $(T, p)$ is free over $\mathbb{F}_p$ of constant rank must be quasi-isomorphic to a free $\Lambda$-module. Lemma 4 reduces the problem to showing that the finite torsion submodule $B$ is actually trivial.

*Step 3: Vanishing of $B$.* Lemma 5 shows that $B = 0$ for $\chi \neq 1, \omega$, by analyzing the exact cohomology sequence and using that $U(\chi)$ has no torsion. Since $B$ is finite, its vanishing implies the exact sequence splits, so $U(\chi) \cong A$ is free over $\Lambda$. The rank calculation from the finite levels forces the rank to be exactly $1$.

*Step 4: Explicit basis.* In the subsequent section, an explicit $\Lambda$-basis element $\xi(\chi) \in U(\chi)$ is constructed using the Kummer-Takagi exponents and Lubin-Tate theory. This basis realizes the isomorphism $U(\chi) \cong \Lambda$ explicitly. $\square$
