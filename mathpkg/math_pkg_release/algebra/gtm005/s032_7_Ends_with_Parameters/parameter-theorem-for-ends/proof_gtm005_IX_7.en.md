---
role: proof
locale: en
of_concept: parameter-theorem-for-ends
source_book: gtm005
source_chapter: "IX"
source_section: "7"
---

For each object $p \in P$, let $S_p = T(p, -, -): C^{\mathrm{op}} \times C \rightarrow X$ be the functor obtained by fixing the parameter $p$. By hypothesis, each $S_p$ has an end $\langle e_p, \omega_p \rangle$ where $e_p = \int_c T(p, c, c)$ and $\omega_p: e_p \rightarrow S_p$ is the universal wedge.

Define the object function of $U$ by $U(p) = e_p$. For the arrow function, take any morphism $h: p \rightarrow p'$ in $P$. The family of arrows
\[
T(h, c, c): T(p, c, c) \rightarrow T(p', c, c)
\]
for $c \in C$ constitutes a natural transformation $\tau_h: S_p \rightarrow S_{p'}$, because $T$ is a functor on $P \times C^{\mathrm{op}} \times C$. Explicitly, for any $f: c \rightarrow d$ in $C$, the naturality square
\[
\begin{CD}
T(p, c, c) @>{T(h, c, c)}>> T(p', c, c) \\
@V{T(p, f, 1)}VV @VV{T(p', f, 1)}V \\
T(p, d, c) @>>{T(h, d, c)}> T(p', d, c)
\end{CD}
\]
commutes, and similarly for the contravariant variable, yielding a wedge condition for $\tau_h$.

Now apply Proposition 1 to the natural transformation $\tau_h: S_p \rightarrow S_{p'}$. Both $S_p$ and $S_{p'}$ have ends, so Proposition 1 provides a unique arrow
\[
U(h) = \int_c \tau_h(c, c) = \int_c T(h, c, c): \int_c T(p, c, c) \rightarrow \int_c T(p', c, c)
\]
such that $\omega_{p', c} \circ U(h) = T(h, c, c) \circ \omega_{p, c}$ for all $c \in C$.

Functoriality of $U$ follows from the composition rule in Proposition 1. For $h: p \rightarrow p'$ and $h': p' \rightarrow p''$, the composite natural transformation $\tau_{h'} \cdot \tau_h$ corresponds to $T(h' \circ h, -, -)$, and Proposition 1 gives
\[
U(h' \circ h) = \int_c T(h' \circ h, c, c) = \int_c (\tau_{h'} \cdot \tau_h)(c, c) = \left[ \int_c \tau_{h'}(c, c) \right] \circ \left[ \int_c \tau_h(c, c) \right] = U(h') \circ U(h).
\]
Similarly, $U(1_p) = \int_c T(1_p, c, c) = 1_{U(p)}$. Thus $U: P \rightarrow X$ is a functor, uniquely determined by the requirement that the wedges $\omega_p$ be natural in $p$.
