---
role: proof
locale: en
of_concept: plh-approximation-of-homeomorphism-on-1-complex
source_book: gtm047
source_chapter: "6"
source_section: "6"
---

For each edge $e$ of $K^1$, let $\varepsilon_e$ be the greatest lower bound $\inf (\phi|e)$ of $\phi|e$. Then $\varepsilon_e > 0$ for each $e$. For each $e \in K^1$, $h|e$ is uniformly continuous. It follows that there is a subdivision $L$ of $K^1$, sufficiently fine so that for each edge $v_i v_j$ of $L$,

$$\delta h(v_i v_j) < \frac{\varepsilon_e}{3},$$

where $e$ is the edge of $K^1$ that contains $v_i v_j$. Let the vertices of $L$ be

$$v_0, v_1, \dots;$$

for each $i$, let

$$w_i = h(v_i);$$

and for each $i, j$, let

$$A_{ij} = h(v_i v_j),$$

$$\varepsilon_{ij} = \frac{\varepsilon_e}{3}.$$

Thus we have

$$\delta A_{ij} \leqslant \varepsilon_{ij},$$

so that

(1) For each $P, Q \in N(A_{ij}, \varepsilon_{ij})$, $d(P, Q) < 3\varepsilon_{ij} = \varepsilon_e$.

For each $i$, let

$$N_i = N(w_i, \varepsilon_i), \quad C_i = \text{Fr}\, N_i,$$

where the numbers $\varepsilon_i$ are positive and sufficiently small so that

(2) The sets $\overline{N}_i$ are disjoint,

(3) $\varepsilon_i < \varepsilon_{ij}$ whenever $v_i v_j \in L$, and

(4) $\overline{N}_i$ intersects $A_{jk}$ only if $i = j$ or $i = k$.

Now each set $A_{ij} = h(v_i v_j)$ is a homeomorphic image of a 1-simplex. By Theorem 6.1, for each edge $v_i v_j$, there is a broken line $B_{ij}$ from $w_i$ to $w_j$ lying in $N(A_{ij}, \varepsilon_{ij})$. These broken lines can be chosen so that they intersect the circles $C_i$ transversely and only at points near the endpoints. By adjusting the broken lines near the $C_i$, we can piece them together to form a PLH $f$ on $|K^1|$ that satisfies $f(v_i) = h(v_i) = w_i$ at all vertices, and such that $f$ is a $\phi$-approximation of $h$.
