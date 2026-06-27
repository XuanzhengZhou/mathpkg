---
role: proof
locale: en
of_concept: heine-borel-lebesgue-theorem
source_book: gtm027
source_chapter: "5"
source_section: "Products of Compact Spaces"
---

# Proof of Heine-Borel-Lebesgue Theorem

**Theorem.** A subset of Euclidean $n$-space $E^n$ is compact if and only if it is closed and bounded.

*Proof.* ($\Rightarrow$) Let $A$ be a compact subset of $E^n$. Then $A$ is closed because $E^n$ is a Hausdorff space. By compactness, $A$ can be covered by a finite family of open spheres of radius one; since each of these spheres is bounded, their finite union is bounded, and hence $A$ is bounded.

($\Leftarrow$) Suppose $A$ is a closed and bounded subset of $E^n$. We first prove that every closed bounded interval $[a, b]$ in the real line $\mathbb{R}$ is compact. Let $\mathcal{C}$ be an open cover of $[a, b]$. Define

$$c = \sup \{ x \in [a, b] : \text{some finite subfamily of } \mathcal{C} \text{ covers } [a, x] \}.$$

The set is non-void since $a$ is a member (the interval $[a, a] = \{a\}$ is trivially covered). Choose $U \in \mathcal{C}$ such that $c \in U$, and choose a member $d$ of the open interval $(a, c)$ such that $[d, c] \subset U$. By definition of $c$, there exists a finite subfamily of $\mathcal{C}$ which covers $[a, d]$, and this family together with $U$ covers $[a, c]$. Unless $c = b$, the same finite subfamily would also cover an interval extending to the right of $c$ (since $U$ is open), which contradicts the definition of $c$ as a supremum. Hence $c = b$ and $[a, b]$ is covered by a finite subfamily of $\mathcal{C}$. Therefore $[a, b]$ is compact.

Since $A$ is bounded, it is contained in some closed cube $[-M, M]^n$. Each factor $[-M, M]$ is compact as shown above, and by Tychonoff's theorem their product $[-M, M]^n$ is compact. The set $A$ is closed in $E^n$, hence closed in the subspace topology of $[-M, M]^n$. A closed subset of a compact space is compact, so $A$ is compact. $\square$
