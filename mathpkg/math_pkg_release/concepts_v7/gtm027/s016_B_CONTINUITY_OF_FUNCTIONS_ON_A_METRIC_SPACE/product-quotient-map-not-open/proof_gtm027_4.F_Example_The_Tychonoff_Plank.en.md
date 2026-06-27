---
role: proof
locale: en
of_concept: product-quotient-map-not-open
source_book: gtm027
source_chapter: "4"
source_section: "F. Example (The Tychonoff Plank) on Subspaces of Normal Spaces"
---

# Proof: The Natural Map from Product to Product of Quotients Need Not Be Open

**Statement (c)**: There is a natural map $\varphi: X \times X \to (X/S) \times (X/S)$ defined by $\varphi(x, y) = (S[x], S[y])$, where $S[x]$ denotes the equivalence class of $x$ under the relation $S$. It is natural to ask whether this map is open when $X/S$ is given the quotient topology and both products are given the product topologies. (This is equivalent to asking whether the product of quotients is topologically the quotient of the product.) If $S$ is the relation defined in part (b), the map $\varphi$ is **not** open.

**Proof**:

Let $S = \Delta \cup (A \times A) \cup (B \times B)$ be the equivalence relation from part (b), on the Tychonoff Plank $X = (\Omega' \times \Omega') \setminus \{(\Omega, \Omega)\}$. Recall that $A = \Omega_0 \times \{\Omega\}$ and $B = \{(x, x) : x \in \Omega_0\}$.

Consider the point $(a, b) \in X \times X$ where $a \in A$ and $b \in B$. (Note that $A$ and $B$ are disjoint, so $a \neq b$.)

Consider the open neighborhood $W$ of $(a, b)$ in $X \times X$ defined by
$$W = (X \times X) \setminus (A \times A \cup B \times B \cup \Delta).$$

This is the complement of the union of three closed sets ($A \times A$, $B \times B$, and $\Delta$ are all closed, as argued in part (b)), so $W$ is open in $X \times X$.

We claim that its image $\varphi(W)$ is **not** open in $(X/S) \times (X/S)$.

The image of $W$ contains the point $\varphi(a, b) = ([A], [B])$, since $a \in A$ so $S[a] = [A]$, and $b \in B$ so $S[b] = [B]$. However, we can show that no basic open neighborhood of $([A], [B])$ in $(X/S) \times (X/S)$ is completely contained in $\varphi(W)$.

Any basic open neighborhood of $([A], [B])$ in the product topology has the form $U \times V$, where $U$ is an open neighborhood of $[A]$ in $X/S$ and $V$ is an open neighborhood of $[B]$ in $X/S$. Their preimages $\pi^{-1}(U)$ and $\pi^{-1}(V)$ are saturated open subsets of $X$ containing $A$ and $B$ respectively.

Now, $\pi^{-1}(U)$ being a saturated open set containing $A$ means it contains an open neighborhood of each point of $A$. Given a point $(x, \Omega) \in A$, there exist ordinals $\alpha_x < x < \beta_x \leq \Omega$ and $\gamma_x < \Omega$ such that the basic open rectangle $(\alpha_x, \beta_x) \times (\gamma_x, \Omega]$ is contained in $\pi^{-1}(U)$.

Similarly for $\pi^{-1}(V)$ containing $B$. By the same type of argument as in part (e) (using the function $f$ and the fixed-point accumulation theorem), one can find points in $\pi^{-1}(U) \times \pi^{-1}(V)$ whose preimages under $\varphi$ lie in $A \times A \cup B \times B \cup \Delta$ (the complement of $W$), specifically points of the form $((x, y), (x, y)) \in \Delta$ or pairs both in $A$ or both in $B$.

Since $W = (X \times X) \setminus (A \times A \cup B \times B \cup \Delta)$, these points do not belong to $W$, yet their $\varphi$-images lie in $U \times V$. Hence $U \times V \not\subset \varphi(W)$, and $\varphi(W)$ cannot be open.

Therefore the natural product-quotient map $\varphi$ is not open, demonstrating that the product of quotient topologies need not coincide with the quotient of the product topologies.
