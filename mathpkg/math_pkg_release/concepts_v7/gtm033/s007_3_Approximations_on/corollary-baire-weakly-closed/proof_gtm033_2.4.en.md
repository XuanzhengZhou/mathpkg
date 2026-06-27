---
role: proof
locale: en
of_concept: corollary-baire-weakly-closed
source_book: gtm033
source_chapter: "2"
source_section: "4. Weak and Strong Topologies on Function Spaces"
---

# Proof of Corollary: Baire Property for Weakly Closed Subsets of Function Spaces

**Corollary.** If $M$ and $N$ are $C^0$ manifolds, every weakly closed subset $Q \subset C(M,N)$ is a Baire space in the strong topology.

*Proof.* Let $\{A_n\}_{n \in \mathbb{N}}$ be a sequence of dense open subsets of $Q$ (referring always to the strong topology), and let $U \subset Q$ be a nonempty open set. Then $A_0 \cap U$ is a nonempty open subset of $Q$. Therefore there exists $f_0 \in A_0 \cap U$ and $\varepsilon_0 \in C(X, \mathbb{R}_+)$ such that

$$Q \cap \bar{\mathcal{N}}(f_0, \varepsilon_0) \subset A_0 \cap U$$

where $\bar{\mathcal{N}}(f_0, \varepsilon_0) = \{g : d(f_0 x, g x) \leqslant \varepsilon_0(x)\}$. We may obviously assume $\varepsilon_0 < 1$.

By recursion there are sequences $\{f_n\}$ in $Q$ and $\{\varepsilon_n\}$ in $C(X, \mathbb{R}_+)$ such that for all $n \in \mathbb{N}$:

$$Q \cap \bar{\mathcal{N}}(f_{n+1}, \varepsilon_{n+1}) \subset A_{n+1} \cap \mathcal{N}(f_n, \varepsilon_n),$$

and $\varepsilon_{n+1} \leqslant \varepsilon_n/2$. The sequence $\{f_n\}$ satisfies

$$d(f_{n+1}x, f_n x) \leqslant 2^{-n}$$

and so is uniformly convergent. The limit $f$ is in $Q$ since $Q$ is uniformly closed. Also $f$ belongs to every $\mathcal{N}(f_n, \varepsilon_n)$, so $f \in U$ and also $f \in \bigcap A_n$.

Thus $\bigcap_n A_n$ is dense in $Q$, establishing the Baire property.

QED
