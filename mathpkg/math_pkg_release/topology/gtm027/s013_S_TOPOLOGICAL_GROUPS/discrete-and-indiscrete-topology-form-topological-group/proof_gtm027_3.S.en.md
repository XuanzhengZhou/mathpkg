---
role: proof
locale: en
of_concept: discrete-and-indiscrete-topology-form-topological-group
source_book: gtm027
source_chapter: "3"
source_section: "S"
---

# Proof that Discrete and Indiscrete Topologies Form Topological Groups

**Statement.** Every group, with the discrete topology or with the indiscrete topology, is a topological group.

**Proof.** Let $(G, \cdot)$ be a group and let $\varphi: G \times G \to G$ be the map $\varphi(x, y) = x \cdot y^{-1}$.

**Case 1: Discrete topology.** In the discrete topology, every subset of $G$ is open. Then every subset of $G \times G$ is open in the product topology (since the product of discrete spaces is discrete). In particular, for any open set $W \subset G$, the preimage $\varphi^{-1}(W)$ is a subset of $G \times G$, hence open. Therefore $\varphi$ is continuous, and $(G, \cdot, \mathfrak{J}_{\text{disc}})$ is a topological group.

**Case 2: Indiscrete topology.** In the indiscrete topology, the only open sets are $\varnothing$ and $G$. Then in the product topology on $G \times G$, the only open sets are $\varnothing$ and $G \times G$. The preimage $\varphi^{-1}(\varnothing) = \varnothing$ is open, and $\varphi^{-1}(G) = G \times G$ is open. Therefore $\varphi$ is continuous, and $(G, \cdot, \mathfrak{J}_{\text{indisc}})$ is a topological group.

**Additional examples given in the text:**

1. **Real numbers under addition.** Let $G = \mathbb{R}$ with the usual topology $\mathfrak{J}$. The map $\varphi(x, y) = x - y$ is continuous (subtraction is continuous on $\mathbb{R}$), so $(\mathbb{R}, +, \mathfrak{J})$ is a topological group.

2. **Non-zero real numbers under multiplication.** Let $G = \mathbb{R} \setminus \{0\}$ with the relative usual topology. The map $\varphi(x, y) = x \cdot y^{-1}$ is continuous on $G \times G$ (multiplication and inversion are continuous on $\mathbb{R} \setminus \{0\}$), so $(G, \cdot, \mathfrak{J})$ is a topological group.

3. **$p$-adic topology on integers.** Let $G = \mathbb{Z}$ and let $p$ be a prime. Define $\mathfrak{u}$ to be the family of all subsets $U \subset \mathbb{Z}$ such that for some positive integer $k$, every integral multiple of $p^k$ belongs to $U$; i.e., $p^k \mathbb{Z} \subset U$. Then $\mathfrak{u}$ consists of sets that contain a subgroup $p^k \mathbb{Z}$. One verifies that $\mathfrak{u}$ satisfies the four axioms of the neighborhood system characterization (proved above): intersections contain $p^{\max(k_1, k_2)}\mathbb{Z}$, the sum $p^k\mathbb{Z} + p^k\mathbb{Z} = p^k\mathbb{Z}$, symmetry holds since $p^k\mathbb{Z}$ is a subgroup, and invariance under inner automorphisms is automatic in the abelian group $\mathbb{Z}$. Hence by the neighborhood system characterization theorem, there is a unique topology $\mathfrak{J}$ (the $p$-adic topology) such that $(\mathbb{Z}, +, \mathfrak{J})$ is a topological group with $\mathfrak{u}$ as the neighborhood system of $0$. ∎
