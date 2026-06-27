---
role: proof
locale: en
of_concept: initial-topology-for-linear-mapping-is-tvs
source_book: gtm015
source_chapter: "Chapter 2 – Topological Vector Spaces"
source_section: "17. Balanced sets, absorbent sets"
---

# Proof that Initial Topology for a Linear Mapping is a TVS Topology

**Corollary (17.13).** If $f: E \to F$ is a linear mapping, where $E$ is a vector space over $\mathbb{K}$ and $F$ is a TVS over $\mathbb{K}$, then the initial topology for $f$ is compatible with the vector space structure of $E$.

*Proof.* Equip $E$ with the initial topology for $f$, i.e., the coarsest topology on $E$ for which $f$ is continuous; the open sets of $E$ are the sets $f^{-1}(U)$, where $U$ is open in $F$.

Let $\mathcal{V}$ be the class of all balanced neighborhoods of $\theta$ in $F$. By (17.8), $\mathcal{V}$ is a neighborhood base at $\theta$; therefore, for each $y \in F$, the class $\{y + V : V \in \mathcal{V}\}$ is a neighborhood base at $y$. In particular, for each $x \in E$, the class $\{f(x) + V : V \in \mathcal{V}\}$ is a neighborhood base at $f(x)$; it follows from the definition of the initial topology that the class

$$\mathcal{B}_x = \{f^{-1}(f(x) + V) : V \in \mathcal{V}\}$$

is a neighborhood base at $x$. Since $f^{-1}(f(x) + V) = x + f^{-1}(V)$ by the linearity of $f$, we have

$$(*) \quad \mathcal{B}_x = \{x + f^{-1}(V) : V \in \mathcal{V}\}.$$

In particular, the class

$$\mathcal{B}_\theta = \{f^{-1}(V) : V \in \mathcal{V}\}$$

is a fundamental system of neighborhoods of $\theta$ in $E$. It is easy to see from the properties of $\mathcal{V}$, and the linearity of $f$, that $\mathcal{B}_\theta$ satisfies the conditions (i)-(iii) of (17.12), therefore there is a unique topology $\tau$ on $E$ such that $\mathcal{B}_\theta$ is a fundamental system of $\tau$-neighborhoods of $\theta$, and $\tau$ is compatible with the vector space structure of $E$. Since $\tau$ is determined by its neighborhoods of $\theta$ via translation, and $\mathcal{B}_\theta$ generates the initial topology, the initial topology coincides with $\tau$ and is therefore a TVS topology. $\square$
