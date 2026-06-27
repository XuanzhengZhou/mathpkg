---
role: proof
locale: en
of_concept: wilders-arc-is-wild
source_book: gtm047
source_chapter: "19"
source_section: "19"
---

If $A$ is tame, then there is a homeomorphism $\phi: \mathbb{R}^3 \leftrightarrow \mathbb{R}^3$ such that $\phi(A)$ is a linear interval $I$. We shall show that this is impossible. Let $P' = \phi(P)$, and let $U = \mathbb{R}^3 - I$. If $\varepsilon > 0$ is small and

$$P_0 \in N(P', \varepsilon) - I,$$

then

$$\pi(N(P', \varepsilon) - I, P_0) \approx \mathbf{Z}.$$

It follows that for every open set $V$ containing $P'$, there is an open set $W$ with $P' \in W \subset V$ such that if $p$ and $q$ are closed paths in $W - I$ with base-point $P_0 \in W - I$, then

$$pq \cong qp$$

in $\pi(W - I, P_0)$. It follows that $pq \cong qp$ in $\pi(U \cap V, P_0)$. Thus we have verified that if $U = \mathbb{R}^3 - I$ where $I$ is a linear interval, then $\pi(U)$ is locally commutative at each point of $I$. This property is invariant under homeomorphisms $\mathbb{R}^3 \leftrightarrow \mathbb{R}^3$.

Now consider the presentation of $\pi = \pi(\text{Int } C_r - A)$. The generators $a_i, b_i, c_i$ and relations obtained from the crossing points yield

$$\pi = \pi(\text{Int } C_r - A) \approx F(G)/N(R).$$

For a fixed $s$ with $W = \text{Int } C_s$, consider the homomorphism

$$h: \pi \rightarrow \pi$$

determined by

$$a_i \mapsto a_s, \quad b_i \mapsto b_s, \quad c_i \mapsto c_s,$$

for each $i \geqslant r$, with also $a_0 \mapsto a_s$. All generators collapse onto three generators $a, b, c$, and all relations collapse onto the corresponding relations for a single trefoil knot. Thus the image $h(\pi)$ is isomorphic to the trefoil group, in which generators do not commute. Therefore the pre-images $a_s$ and $b_s$ do not commute, and it is false that $a_s b_s \cong b_s a_s$ in $\pi(\text{Int } C_r - A)$.

Hence $\pi(\mathbb{R}^3 - A)$ is not locally commutative at points of $A$, so $A$ cannot be tame. Therefore $A$ is wild.
