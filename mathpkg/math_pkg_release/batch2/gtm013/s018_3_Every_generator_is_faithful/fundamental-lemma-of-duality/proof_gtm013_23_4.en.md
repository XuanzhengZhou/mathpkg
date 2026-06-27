---
role: proof
locale: en
of_concept: fundamental-lemma-of-duality
source_book: gtm013
source_chapter: "23"
source_section: "23.4"
---
The proof is dual to that of (21.1), the Fundamental Lemma for equivalences. For each $M \in {}_R \mathcal{C}$ and $N \in \mathcal{D}_S$, define
$$\mu_{MN}: \operatorname{Hom}_S(N, H'(M)) \to \operatorname{Hom}_R(M, H''(N))$$
by composing: given $\gamma: N \to H'(M)$, apply $H''$ to get $H''(\gamma): H''H'(M) \to H''(N)$, then precompose with $\eta_M^{-1}: M \to H''H'(M)$:
$$\mu_{MN}(\gamma) = H''(\gamma) \circ \eta_M^{-1}.$$
Similarly, define $v_{MN}: \operatorname{Hom}_R(M, H''(N)) \to \operatorname{Hom}_S(N, H'(M))$ by
$$v_{MN}(\delta) = H'(\delta) \circ \zeta_N^{-1}$$
for $\delta: M \to H''(N)$. Naturality of $\eta$ and $\zeta$ ensures that $\mu$ and $v$ are natural in both variables and mutually inverse. The explicit formulas (1)-(4) follow from the naturality conditions and the definitions of $\mu$ and $v$:

For (1): given $h: M_2 \to M_1$, $k: N_1 \to N_2$, and $\gamma: N_1 \to H'(M_1)$,
\begin{align*}
\mu(H'(h)\gamma k) &= H''(H'(h)\gamma k) \circ \eta_{M_2}^{-1} \\
&= H''(k) \circ H''(\gamma) \circ H''H'(h) \circ \eta_{M_2}^{-1} \\
&= h \circ \mu(\gamma) \circ H''(k)
\end{align*}
by naturality of $\eta$. The remaining relations (2)-(4) are proved similarly.
