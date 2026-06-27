---
role: proof
locale: en
of_concept: triviality-of-principal-bundle-over-union
source_book: gtm020
source_chapter: "4. General Fibre Bundles"
source_section: "9.4"
---

The argument proceeds as in Section 4 of Chapter 3, where the trick is to use the interval structure to patch together local trivializations. Since $\xi|B_1$ and $\xi|B_2$ are trivial, and $B_1 \cap B_2 = A \times \{c\}$ is a deformation retract of both pieces, the transition function over the intersection can be extended to a global trivialization over $B = B_1 \cup B_2$. The compactness of $I = [a, b]$ ensures that a finite number of such patching steps suffice. For each $(x, t) \in B \times I$, there exists a neighborhood contained in one set $U_i$ intersecting only finitely many $U_j$, and since $I$ is compact, there are for each $x \in B$ a neighborhood $N$ and a natural number $r$ such that:

(1) $N \times [(q - 1)/r, q/r] \subset U_{k(q)}$ for some $k(q)$ and each $1 \leq q \leq r$.

(2) $N \times I$ intersects only finitely many $V_j = v_j^{-1}(0, 1]$ for $j$ in the index set.

By property (1), $\{v_k^{-1}(0, 1]\}$ is a covering of $B$, and by property (2), for a given $r$, the family of $\{v_k\}$ is locally finite. One then augments the maps $v_k$ to obtain a locally finite partition of unity. Let $w_r(x)$ denote the sum of all functions $v_k(x)$ with $k = (k(1), \ldots, k(s))$ and $s < r$, and define

$$u_k(x) = \max(0, v_k(x) - r w_r(x)).$$

For $x \in B$, there exists $k = (k(1), \ldots, k(r))$ with $r$ minimal such that $v_k(x) > 0$. Then $w_r(x) = 0$ and $u_k(x) = v_k(x)$. Consequently, the sets $u_k^{-1}(0, 1]$ form an open covering of $B$. Moreover, for $m > r$ with $v_k(x) > 1/m$, we have $w_m(x) > 1/m$ and $m w_m(y) > 1$ for all $y$ in a neighborhood of $x$. In this neighborhood all $u_k$ with $k = (k(1), \ldots, k(s))$ and $s \geq m$ vanish, and consequently the system $\{u_k\}$ is a locally finite partition of unity. This completes the patching argument that yields a global trivialization of $\xi$ over $B$.
