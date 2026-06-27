---
role: proof
locale: en
of_concept: maillet-determinant-theorem
source_book: gtm059
source_chapter: "3"
source_section: "7"
---

Let $C$ be a primitive $(p-1)$-th root of unity. The group $G = (\mathbb{Z}/p\mathbb{Z})^\times$ is cyclic of order $p-1$, and its elements can be represented as powers $C^i$ for $1 \leq i \leq p-1$.

The determinant under consideration has dimension $\frac{p-1}{2}$. The indices of the determinant correspond to the even powers (or odd powers, depending on convention) in the character table, since the product of all $C^i$ factors to $1$ in each term of the determinant expansion. This observation simplifies the determinant to the same as that obtained by restricting to a suitable set of representatives.

The entries $R_{ij}^+$ and $R_{ij}^-$ are related by $R_{ij}^+ + R_{ij}^- = p$ for $p \nmid ij$, and $R_{ij}^+ = R_{ij}^- = p$ when $p \mid ij$ (using the convention that the residue is $p$ rather than $0$). Hence $R_{ij}^+ - R_{ij}^- \in \{p, -p, 0\}$.

Each entry in the determinant $D_p$ is therefore an integer of absolute value at most $p$. The absolute value of the determinant equals the volume of the fundamental parallelotope spanned by the row vectors (Hadamard's inequality).

Carlitz [Ca] observed that applying Hadamard's inequality to this determinant immediately gives a bound on $|D_p|$, and consequently on the class number $h_A = h^-$. Specifically, since each row has Euclidean length at most $\sqrt{\frac{p-1}{2}} \cdot p$, Hadamard gives

$$|D_p| \leq \left(\sqrt{\frac{p-1}{2}} \cdot p\right)^{(p-1)/2}.$$

This bound, after accounting for the factor of $p^{(p-3)/2}$, yields an upper bound on the class number of the form $h^- \leq \text{const} \cdot p^{(p+1)/4}$.

The sharpness of this bound and further refinements by Montgomery-Mozgovoy [M-M] show that for primes $p \geq 200$, the class number $h^-$ is bracketed between $(2k)^p$ and $(2k)^p$ plus a lower-order term, where $k$ is a related quantity (essentially $p^{(p-3)/2}$ times a constant). For certain specific values, sharper results are known: Ankeny, Artin, and Chowla proved that $h^- = 1$ for precisely 29 distinct values of $m$ (with $m \not\equiv 1 \bmod 4$), and the largest such value is $m = 8$.
