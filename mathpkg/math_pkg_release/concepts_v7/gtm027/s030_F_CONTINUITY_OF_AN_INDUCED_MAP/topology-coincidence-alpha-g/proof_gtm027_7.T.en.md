---
role: proof
locale: en
of_concept: topology-coincidence-alpha-g
source_book: gtm027
source_chapter: "7"
source_section: "T"
---

# Proof of Coincidence of Topologies on the Compactification Group

Let $\alpha[G]$ be the almost periodic compactification. If $A$ is given the topology of pointwise convergence on $G$, and $\alpha[G] \subseteq A^A$ has the resulting product topology, then this topology coincides with the topology of pointwise convergence of operators. Explicitly:

$$R_n \to R \text{ in } \alpha[G] \iff R_n(f)(x) \to R(f)(x) \text{ for all } f \in A \text{ and all } x \in G.$$

**Proof.** The topology on $A$ as pointwise convergence on $G$ means: $f_n \to f$ in $A$ iff $f_n(x) \to f(x)$ for each $x \in G$. The topology on $\alpha[G] \subseteq A^A$ is the product topology induced by this topology on $A$, i.e., the topology of pointwise convergence of maps $A \to A$ when $A$ is given the pointwise convergence topology.

Thus $R_n \to R$ in $\alpha[G]$ iff for each $f \in A$, $R_n(f) \to R(f)$ in the pointwise topology on $A$, which means $R_n(f)(x) \to R(f)(x)$ for all $x \in G$. This is exactly the condition stated.

Since $\alpha[G]$ is the closure of $\{L_x : x \in G\}$ in this topology (by definition), the product topology makes $\alpha[G]$ a compact Hausdorff space (as a closed subset of the product of compact spaces, once one verifies that the left translations lie in a compact subset of $A^A$).
