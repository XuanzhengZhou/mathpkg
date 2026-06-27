---
role: proof
locale: en
of_concept: generators-of-link-complement-fundamental-group
source_book: gtm047
source_chapter: "15"
source_section: "15"
---

Let $p$ be a closed path in $\mathbf{R}^3 - L$. By Theorem 14.6, we may suppose that $p$ is PL. And we may suppose that $p$ is in general position relative to $L$, in the sense that (1) no vertex of $|p|$ projects into the diagram of $L$, (2) no segment of the image $|p|$ is vertical, and (3) no point of $|p|$ projects onto a crossing point in the diagram.

We get a diagram of $p$ by projecting into the $xy$-plane; and this intersects the diagram of $L$ only in simple crossing points. Take the short directed segments $b$ of the diagram of the path in the neighborhoods of the crossing points. For each such $b$, take a triangular path $t$ which goes from $P_0$ to the initial point of $b$, then along $b$, and then from the terminal point of $b$ back to $P_0$. Taking these in the order of the segments $b$ on the path $p$, we get a path

$$p' = t_1 t_2 \ldots t_m.$$

Now $p' \cong p$, because all of $|p|$ except the segments of the type $b$ can be dragged continuously back to the base point, giving

$$p \cong e_1 t_1 e_2 t_2 \ldots e_m t_m e_{m+1},$$

where each $e_i$ is a constant mapping $[0, 1] \to P_0$.

If $t_i$ crosses under $a_j$, then we assert $t_i \cong g_j^{\pm 1}$. This follows because $a_j$ is an arc of the diagram of $L$ whose endpoints lie under crossing points where $a_r$ and $a_s$ are the arcs of $L$ that cross under $a_j$. (No arc of the diagram of $L$ crosses over $a_j$, because if so it would cut $a_j$ into smaller arcs in the diagram.) Preserving the $\cong$-class, we move $t_i$ so that its middle interval is very short and very close to $a_j$. Now slide it until its middle interval has the same projection as a subinterval of the middle interval of $g_j$. Then adjust it again, linearly, until it coincides with $g_j$, except perhaps for direction.

In a finite number of such steps, we get

$$p \cong \prod_{i=1}^{m} g_{j_i}^{\alpha_i} \quad (\alpha_i = \pm 1).$$

Thus every closed path in $\mathbf{R}^3 - L$ is homotopic to a product of the generators $\{g_i\}$, which proves the theorem.
