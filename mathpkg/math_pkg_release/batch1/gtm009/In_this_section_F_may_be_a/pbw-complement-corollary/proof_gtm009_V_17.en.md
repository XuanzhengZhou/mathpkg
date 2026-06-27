---
role: proof
locale: en
of_concept: pbw-complement-corollary
source_book: gtm009
source_chapter: "V"
source_section: "17"
---

Consider the following commutative diagram (all maps canonical):
\[
\begin{array}{ccccc}
U_m & \twoheadrightarrow & G^m \\
\uparrow & & \uparrow \\
T^m & \twoheadrightarrow & S^m \\
\cup & & \uparrow \\
W & \stackrel{\sim}{\longrightarrow} & S^m
\end{array}
\]

The PBW Theorem asserts that $\omega: \mathfrak{S} \to \mathfrak{G}$ is an isomorphism; in particular, the map $S^m \to G^m$ is an isomorphism for each $m$. By hypothesis, the canonical map $T^m \to S^m$ restricts to an isomorphism on $W \subset T^m$. Hence the composition $W \hookrightarrow T^m \twoheadrightarrow S^m \stackrel{\cong}{\to} G^m$ is an isomorphism.

The top row of the diagram gives the map $U_m \twoheadrightarrow G^m = U_m / U_{m-1}$. Since $W \to T^m \to U_m \to G^m$ is an isomorphism, the image $\pi(W)$ in $U_m$ maps isomorphically onto $G^m$. Therefore $\pi(W)$ is a vector space complement to $U_{m-1}$ in $U_m$, i.e., $U_m = U_{m-1} \oplus \pi(W)$.
