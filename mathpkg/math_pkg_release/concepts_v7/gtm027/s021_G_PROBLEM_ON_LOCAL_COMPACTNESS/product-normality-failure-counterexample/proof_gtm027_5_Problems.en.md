---
role: proof
locale: en
of_concept: product-normality-failure-counterexample
source_book: gtm027
source_chapter: "5"
source_section: "Problems"
---

# Proof that Product of Normal and Compact Hausdorff May Not Be Normal

**Proposition.** The product of a locally compact, normal Hausdorff space and a compact Hausdorff space may fail to be normal.

**Proof.** We present Kelley's counterexample using ordinal spaces.

Let $\Omega$ be the first uncountable ordinal. Define:
- $\Omega_0 = \{\alpha : \alpha < \Omega\}$, the set of all countable ordinals, with the order topology.
- $\Omega' = \{\alpha : \alpha \leq \Omega\}$, the set of all ordinals up to and including $\Omega$, with the order topology.

**Properties of $\Omega_0$:** As established in Problem 5.E, $\Omega_0$ is locally compact, Hausdorff, and satisfies the first axiom of countability. Moreover, $\Omega_0$ is normal (in fact, every order topology on a well-ordered set is normal).

**Properties of $\Omega'$:** $\Omega'$ is compact Hausdorff. It is the one-point compactification of $\Omega_0$, adding the point $\Omega$ at infinity. Being a closed interval in a well-ordered set, $\Omega'$ is compact in the order topology.

Now consider the product space $\Omega_0 \times \Omega'$. We claim this product is not normal.

The non-normality argument (the difficult part referenced in the problem statement, established in Problem 4.E) proceeds by exhibiting two disjoint closed sets that cannot be separated by disjoint open sets:

Consider the "anti-diagonal" sets:
\[
A = \{(\alpha, \alpha) : \alpha < \Omega\} \subset \Omega_0 \times \Omega',
\]
\[
B = \{(\alpha, \Omega) : \alpha < \Omega\} \subset \Omega_0 \times \Omega'.
\]

Both $A$ and $B$ are closed in the product. However, any open sets $U \supset A$ and $V \supset B$ must intersect. This follows from a pressing-down lemma argument: for each $\alpha < \Omega$, there exists a basic open neighborhood $I_\alpha \times J_\alpha$ of $(\alpha, \Omega)$ contained in $V$, where $I_\alpha$ is an open interval around $\alpha$ in $\Omega_0$. By the pressing-down lemma (Fodor's lemma), there is a stationary set on which the $I_\alpha$ are constant, forcing an intersection with $U$.

Thus $\Omega_0 \times \Omega'$ is not normal, providing the required counterexample.
