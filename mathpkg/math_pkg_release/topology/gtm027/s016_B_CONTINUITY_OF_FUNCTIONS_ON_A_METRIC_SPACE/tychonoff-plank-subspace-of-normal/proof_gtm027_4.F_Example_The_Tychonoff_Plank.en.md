---
role: proof
locale: en
of_concept: tychonoff-plank-subspace-of-normal
source_book: gtm027
source_chapter: "4"
source_section: "F. Example (The Tychonoff Plank) on Subspaces of Normal Spaces"
---

# Proof: A Subspace of a Normal Space May Fail to be Normal (The Tychonoff Plank)

**Statement**: A subspace of a normal space may fail to be normal. The normality property is not hereditary.

**Proof by counterexample (The Tychonoff Plank)**:

Consider the ordinal spaces $\Omega_0 = [0, \Omega)$ and $\Omega' = [0, \Omega]$, both equipped with the order topology. By part (c) of the ordinal space problems (Section E), both $\Omega_0$ and $\Omega'$ are normal spaces.

Now consider the product space $X = \Omega' \times \Omega'$. Since $\Omega' = [0, \Omega]$ is a compact Hausdorff space (it is homeomorphic to the one-point compactification of $\Omega_0$), the product $X = \Omega' \times \Omega'$ is also compact Hausdorff, and therefore normal (compact Hausdorff spaces are normal).

Define the **Tychonoff Plank** as the subspace
$$T = (\Omega' \times \Omega') \setminus \{(\Omega, \Omega)\},$$
i.e., we remove the "top-right corner point" $(\Omega, \Omega)$.

The Tychonoff Plank $T$ is a subspace of the normal space $\Omega' \times \Omega'$. We claim that $T$ is **not** normal.

To prove this, consider the following two closed disjoint subsets of $T$:
$$A = \{(x, x) : x \in \Omega_0\} = \text{the diagonal of } \Omega_0 \subset T,$$
$$B = \Omega_0 \times \{\Omega\} \subset T.$$

(Note that $B$ excludes $(\Omega, \Omega)$ since that point was removed from $T$.)

Both $A$ and $B$ are closed in $T$ (as closed subsets of $\Omega' \times \Omega'$ intersected with $T$) and $A \cap B = \varnothing$.

Suppose $U$ is any open set in $T$ containing $A$. We show that the closure of $U$ in $T$ must intersect $B$, hence $A$ and $B$ cannot be separated by disjoint open sets.

The argument proceeds exactly as in part (e) of the ordinal space problems: for each $x \in \Omega_0$, define $f(x)$ as the smallest ordinal larger than $x$ such that $(x, f(x)) \notin U$. Then $f(x) \geq x$, and by part (d), there exists $\xi \in \Omega_0$ such that $(\xi, \xi)$ is an accumulation point of the graph of $f$. The contradiction that arises shows that any open neighborhood of $A$ must have its closure intersect $B$.

Therefore $T$ is not normal, even though it is a subspace of the normal (indeed compact Hausdorff) space $\Omega' \times \Omega'$. This proves that normality is not a hereditary property.
