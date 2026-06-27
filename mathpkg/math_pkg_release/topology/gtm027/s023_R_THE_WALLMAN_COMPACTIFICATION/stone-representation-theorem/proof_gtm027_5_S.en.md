---
role: proof
locale: en
of_concept: stone-representation-theorem
source_book: gtm027
source_chapter: "5"
source_section: "The Wallman Compactification"
---

# Proof of the Stone Representation Theorem

Let $(R, +, \cdot)$ be a Boolean ring (see Section 2.K). Let $S'$ be the set of all ring homomorphisms from $R$ into $I_2 = \mathbb{Z}/2\mathbb{Z}$ (the integers modulo 2), and let $S = S' \setminus \{0\}$, where $0$ denotes the homomorphism which is identically zero. Then $S'$ is a subset of the product space $I_2^R$. The **Stone space** of the ring $R$ is the set $S$ endowed with the relative product topology (where $I_2$ carries the discrete topology).

The **characteristic ring** of a Boolean space $X$ is the ring $\mathfrak{F}(X)$ of all continuous functions $f : X \to I_2$ such that $f^{-1}[1]$ is compact (equivalently, all continuous $I_2$-valued functions with compact support).

**Theorem (Stone Representation).** The evaluation map $e : R \to \mathfrak{F}(S)$ defined by

$$e(r)(s) = s(r) \qquad (r \in R,\; s \in S)$$

is a ring isomorphism from the Boolean ring $R$ onto the characteristic ring $\mathfrak{F}(S)$ of its Stone space $S$.

**Proof.** The proof proceeds in several steps.

**Step 1: $e(r)$ is continuous.** For each $r \in R$, the function $e(r) : S \to I_2$ is the restriction to $S$ of the projection map $\pi_r : I_2^R \to I_2$ onto the $r$-th coordinate. Since $I_2$ carries the discrete topology and $S$ has the relative product topology, each projection is continuous. Hence $e(r) \in C(S, I_2)$.

**Step 2: $e(r)^{-1}[1]$ is compact and open.** A subbasic open set in $S$ has the form $U(r, \varepsilon) = \{s \in S : s(r) = \varepsilon\}$ for $r \in R$ and $\varepsilon \in I_2$. The set $e(r)^{-1}[1] = \{s \in S : s(r) = 1\}$ is exactly such a subbasic open set, hence clopen. Moreover, since $S$ is a closed subspace of the compact Hausdorff space $I_2^R$ (the product of compact spaces is compact by Tychonoff's theorem), $S$ itself is compact, and therefore every closed subset of $S$—in particular every clopen set—is compact. Hence $e(r)^{-1}[1]$ is compact.

Thus $e(r) \in \mathfrak{F}(S)$ for every $r \in R$, so $e$ maps $R$ into $\mathfrak{F}(S)$.

**Step 3: $e$ is a ring homomorphism.** For $r_1, r_2 \in R$ and $s \in S$, since $s : R \to I_2$ is a ring homomorphism:

$$e(r_1 + r_2)(s) = s(r_1 + r_2) = s(r_1) + s(r_2) = e(r_1)(s) + e(r_2)(s),$$
$$e(r_1 \cdot r_2)(s) = s(r_1 \cdot r_2) = s(r_1) \cdot s(r_2) = e(r_1)(s) \cdot e(r_2)(s).$$

The operations on the right are in $I_2$. This shows $e$ is a ring homomorphism.

**Step 4: $e$ is injective.** Suppose $e(r) = 0$ (the zero function on $S$). Then $s(r) = 0$ for every $s \in S$. By the theorem on the existence of sufficiently many homomorphisms (Section 2.K), for every non-zero element $r \in R$, there exists a homomorphism $s \in S$ such that $s(r) \neq 0$. Hence $r = 0$, proving injectivity.

**Step 5: $e$ is surjective onto $\mathfrak{F}(S)$.** This step uses Proposition (b), which characterizes the clopen subsets of the Stone space $S$. By part (b), every clopen subset of $S$ has the form $e(r)^{-1}[1]$ for some $r \in R$. Since every $f \in \mathfrak{F}(S)$ is an $I_2$-valued continuous function with compact (hence clopen) support, it is the characteristic function of a clopen set, so $f = e(r)$ for some $r \in R$.

**Conclusion.** The map $e : R \to \mathfrak{F}(S)$ is a ring isomorphism, establishing that every Boolean ring is isomorphic to the characteristic ring of its Stone space (a field of clopen sets). $\square$

**Reference:** M. H. Stone [3].
