---
role: proof
locale: en
of_concept: duality-commutes-with-restriction-contraction
source_book: gtm054
source_chapter: "X"
source_section: "D"
---

(a) We show that the two matroids $(\Lambda_{[U]})^\perp$ and $(\Lambda^\perp)_{[U]}$ have the same circuits. The circuits of $\Lambda_{[U]}$ are $\mathcal{M}(\pi_U[\mathcal{M}])$. By the characterization of orthogonal matroids, the circuits of $(\Lambda_{[U]})^\perp$ are the minimal sets meeting no circuit of $\Lambda_{[U]}$ in a 1-set. On the other hand, the circuits of $(\Lambda^\perp)_{[U]}$ are obtained by projecting the circuits of $\Lambda^\perp$ onto $U$ and taking minimal members. Using the description of $\mathcal{M}^\perp$ from D5 in terms of sets avoiding 1-intersections with $\mathcal{M}$, one verifies these two collections coincide.

(b) The rank function of $(\Lambda_U)^\perp$ evaluated at $S \subseteq U$ is $|S| + r_U(U \setminus S) - r_U(U)$. Using $r_U = r|_{\mathcal{P}(U)}$ from D12c, this equals $|S| + r(U \setminus S) - r(U)$. For $(\Lambda^\perp)_{[U]}$, the rank function by D12d is $r^\perp(V \setminus U \cup S) - r^\perp(V \setminus U)$. Using D4e ($r^\perp(S) = |S| + r(V \setminus S) - r(V)$), this simplifies to the same expression. Since $\Lambda_{[U]}$ and $\Lambda_U$ have the same rank function when $U$ is a flat, and the two matroids share the same rank function on $\mathcal{P}(U)$, they are equal.
