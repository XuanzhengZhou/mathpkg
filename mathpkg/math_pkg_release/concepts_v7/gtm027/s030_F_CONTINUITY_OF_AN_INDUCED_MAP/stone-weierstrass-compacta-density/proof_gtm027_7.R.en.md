---
role: proof
locale: en
of_concept: stone-weierstrass-compacta-density
source_book: gtm027
source_chapter: "7"
source_section: "R"
---

# Proof of Stone-Weierstrass Theorem: Density Under Uniform Convergence on Compacta

Let $X$ be a topological space and let $C(X)$ be the family of all continuous real-valued functions on $X$, endowed with the topology of uniform convergence on compacta. We prove that every subalgebra of $C(X)$ which has the **two-point property** (separates points and contains a nonzero constant function) is dense in $C(X)$.

**Proof.** The theorem follows from three steps:

**(i)** If $L$ is a linear subspace of $C(X)$ closed under the lattice operations $\wedge$ and $\vee$ (i.e., a vector sublattice) that has the two-set property, then $L$ is dense in $C(X)$ relative to uniform convergence. This is proved in part (d) (the Density Lemma, section P).

**(ii)** The closure of a subalgebra of $C(X)$ under uniform convergence on compacta is a closed subalgebra, hence closed under uniform convergence. By the Stone-Weierstrass theorem for compact spaces (applied to each compact subset), this closure contains sufficiently many functions to separate points and to approximate any continuous function on compact sets.

**(iii)** More concretely: given any $f \in C(X)$, any compact $K \subseteq X$, and $\varepsilon > 0$, apply the classical Stone-Weierstrass theorem to the subalgebra restricted to $K$. The restricted subalgebra is dense in $C(K)$ under uniform convergence on $K$. Thus there exists $g$ in the subalgebra such that $|f(x) - g(x)| < \varepsilon$ for all $x \in K$.

Taking the maximum of a properly chosen finite family of functions completes the proof: one constructs a function in the algebra whose values on finitely many compact sets are controlled, and uses the directedness of the family of compacta.

Alternatively (the standard modern proof): the uniform closure $\overline{A}$ of the subalgebra $A$ is a closed subalgebra, hence a vector lattice (by the lattice-closure property of closed subalgebras), and satisfies the two-point property. Then by the lemma from section P, $\overline{A} = C(X)$.
