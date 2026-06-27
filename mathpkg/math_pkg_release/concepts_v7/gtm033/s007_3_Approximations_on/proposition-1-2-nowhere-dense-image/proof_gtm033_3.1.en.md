---
role: proof
locale: en
of_concept: proposition-1-2-nowhere-dense-image
source_book: gtm033
source_chapter: "3"
source_section: "1. The Morse-Sard Theorem"
---

# Proof of Proposition 1.2: $C^1$ Image from Lower-Dimensional Domain is Nowhere Dense

**Proposition 1.2.** Let $M, N$ be manifolds with $\dim M < \dim N$. If $f: M \to N$ is a $C^1$ map then $f(M)$ is nowhere dense.

*Proof.* It suffices to show that $f(M)$ has measure zero (a set of measure zero in a manifold is nowhere dense; more precisely, its complement is residual by the Baire category theorem). This reduces to the local statement: $g(U) \subset \mathbb{R}^n$ has measure zero if $U \subset \mathbb{R}^m$ is open and $g: U \to \mathbb{R}^n$ is $C^1$, with $m < n$.

To prove this assertion, write $g$ as a composition of $C^1$ maps

$$U = U \times 0 \subset U \times \mathbb{R}^{n-m} \xrightarrow{\pi} U \xrightarrow{g} \mathbb{R}^n.$$

Here $U \times 0$ is the embedding of $U$ as the zero section in $U \times \mathbb{R}^{n-m}$. Clearly $U \times 0$ has $n$-measure zero in

$$U \times \mathbb{R}^{n-m} \subset \mathbb{R}^m \times \mathbb{R}^{n-m} = \mathbb{R}^n;$$

this is because an $m$-dimensional set ($U \times 0$) is contained in a countable union of degenerate $n$-cubes (with $n-m$ sides of length zero), each of which has zero $n$-measure.

Now the composition $\pi g$ is a $C^1$ map from an open subset of $\mathbb{R}^n$ (namely $U \times \mathbb{R}^{n-m}$) to $\mathbb{R}^n$. Applying Lemma 1.1 to $\pi g$, since $U \times 0$ has measure zero in the domain, its image $(\pi g)(U \times 0) = g(U)$ has measure zero in $\mathbb{R}^n$.

Finally, a set of measure zero in a manifold is nowhere dense: it is $\sigma$-compact (union of countably many compact sets), and each compact set of measure zero has empty interior, hence is nowhere dense. By the Baire category theorem, a countable union of nowhere dense sets is nowhere dense. Therefore $f(M)$ is nowhere dense.

QED
