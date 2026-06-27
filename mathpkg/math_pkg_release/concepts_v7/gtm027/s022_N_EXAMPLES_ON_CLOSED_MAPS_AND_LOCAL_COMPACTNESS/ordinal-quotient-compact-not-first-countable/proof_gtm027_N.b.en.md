---
role: proof
locale: en
of_concept: ordinal-quotient-compact-not-first-countable
source_book: gtm027
source_chapter: "N"
source_section: "Examples on Closed Maps and Local Compactness"
---

# Proof of Quotient of the Ordinal Space $\Omega_0$ by Collapsing a Closed Uncountable Set

Let $\Omega_0$ be the set of all ordinal numbers less than $\Omega$ (the first uncountable ordinal), equipped with the order topology. Let $A \subset \Omega_0$ be a closed uncountable set whose complement $\Omega_0 \setminus A$ is also uncountable. Let $\mathfrak{D}$ be the decomposition of $\Omega_0$ whose single non-degenerate member is $A$ and whose remaining members are the singletons $\{x\}$ for $x \in \Omega_0 \setminus A$.

Let $\pi : \Omega_0 \to \Omega_0/\mathfrak{D}$ be the projection onto the quotient space.

**Continuity** holds by definition of the quotient topology.

**Closedness of $\pi$.** $\Omega_0$ is a closed subset of the compact space $[0,\Omega]$ (the set of ordinals $\leq \Omega$ with the order topology), hence $\Omega_0$ is a normal space. The decomposition $\mathfrak{D}$ is upper semi-continuous: $A$ is closed, and the decomposition is clearly upper semi-continuous because for any open set $U$ containing $A$, the saturation of $U$ is also open (as $\Omega_0$ is well-ordered and the order topology has the property that each point is the limit of a net from below). Consequently, $\pi$ is a closed map.

**Compactness of the quotient.** Since $\Omega_0$ is closed in the compact space $[0,\Omega]$ and $\pi$ is continuous, the image $\pi[\Omega_0] = \Omega_0/\mathfrak{D}$ is compact.

**Failure of first countability.** The point $\pi(A)$ in the quotient space does not satisfy the first axiom of countability. Suppose $\{V_n\}_{n \in \omega}$ were a countable local base at $\pi(A)$. Then each $\pi^{-1}[V_n]$ is a saturated open neighborhood of $A$ in $\Omega_0$. By the interlacing lemma (4.E), there exists an ordinal $\alpha < \Omega$ such that the interval $(\alpha, \Omega)$ is contained in each $\pi^{-1}[V_n]$. One can then construct a saturated open set containing $A$ that is strictly smaller than all $\pi^{-1}[V_n]$, contradicting the local base property. Specifically, since $A$ is closed and uncountable with uncountable complement, the interlacing lemma guarantees a sequence of ordinals interlacing with $A$ that prevents the existence of a countable local base at the collapsed point.
