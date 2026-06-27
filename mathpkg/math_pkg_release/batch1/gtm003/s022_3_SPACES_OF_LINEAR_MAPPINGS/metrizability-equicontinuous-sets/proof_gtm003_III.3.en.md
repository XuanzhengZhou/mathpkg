---
role: proof
locale: en
of_concept: metrizability-equicontinuous-sets
source_book: gtm003
source_chapter: "III"
source_section: "3"
---

By Proposition 4.5, the topology of simple convergence on \(H\) coincides with the topology of simple convergence on any total subset of \(E\). Since \(E\) is separable, there exists an at most countable set \(A = \{x_n\}\) which is linearly independent and total in \(E\).

Let \(\{V_m\}\) be a countable \(0\)-neighborhood base in \(F\). The sets
\[
M(x_n, V_m) \cap H = \{u \in H : u(x_n) \in V_m\}
\]
form a countable subbase for the topology of simple convergence on \(H\) (restricted to \(A\)). Since a countable subbase generates a second-countable (hence metrizable, as the topology is uniform) topology, \(H\) is metrizable.

If \(F\) is also separable, then for each \(x_n\), the image \(\{u(x_n) : u \in H\}\) is a subset of a metrizable separable space, hence separable. The product of countably many separable metrizable spaces is separable, so \(H\) with the topology induced by evaluation on \(\{x_n\}\) is separable.
