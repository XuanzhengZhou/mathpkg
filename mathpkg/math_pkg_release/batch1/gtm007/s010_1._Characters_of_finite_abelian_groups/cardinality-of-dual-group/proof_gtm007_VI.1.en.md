---
role: proof
locale: en
of_concept: cardinality-of-dual-group
source_book: gtm007
source_chapter: "VI"
source_section: "1"
---

We use induction on the order $n$ of $G$. The case $n = 1$ is trivial, since the trivial group has exactly one character (the trivial homomorphism).

Suppose $n \geq 2$ and choose a nontrivial cyclic subgroup $H$ of $G$. By the remark following Proposition 1, the restriction homomorphism $\rho \colon \widehat{G} \to \widehat{H}$ is surjective and its kernel is isomorphic to $\widehat{G/H}$. Hence
$$|\widehat{G}| = |\widehat{G/H}| \cdot |\widehat{H}|.$$

By the example for cyclic groups, $|\widehat{H}| = |H|$ since $H$ is cyclic. By the induction hypothesis, $|\widehat{G/H}| = |G/H|$ since $|G/H| < n$. Therefore
$$|\widehat{G}| = |G/H| \cdot |H| = |G|,$$
which completes the induction.
