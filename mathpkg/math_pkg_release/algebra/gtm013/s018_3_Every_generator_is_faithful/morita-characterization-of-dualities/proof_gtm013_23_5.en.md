---
role: proof
locale: en
of_concept: morita-characterization-of-dualities
source_book: gtm013
source_chapter: "23"
source_section: "23.5"
---
Set $U = H''(S_S)$ and $V = H'({}_R R)$. By the Fundamental Lemma (dual to (21.1)), there is an adjunction isomorphism
$$\mu_{MN}: \operatorname{Hom}_S(N, H'(M)) \to \operatorname{Hom}_R(M, H''(N))$$
natural in $M \in {}_R \mathcal{C}$ and $N \in \mathcal{D}_S$. In particular,
$$\mu_{RS}: \operatorname{Hom}_S(S, H'(R)) \to \operatorname{Hom}_R(R, H''(S))$$
is an $(R, S)$-isomorphism. Whence by (4.5), as $(R, S)$-bimodules,
$$U \cong \operatorname{Hom}_S(S, H'(R)) \cong \operatorname{Hom}_R(R, H''(S)) \cong V.$$

Now since $\mu_{MS}$ is natural in $M$, it induces a natural $S$-isomorphism
$$\operatorname{Hom}_S(S, H'(-)) \cong \operatorname{Hom}_R(-, H''(S)).$$
Similarly $\mu_{RN}$ induces a natural $R$-isomorphism
$$\operatorname{Hom}_R(R, H''(-)) \cong \operatorname{Hom}_S(-, H'(R)).$$

So by (20.1.1) and (20.5.2), there are natural isomorphisms:
$$H' \cong \operatorname{Hom}_S(S, H'(-)) \cong \operatorname{Hom}_R(-, H''(S)) \cong \operatorname{Hom}_R(-, U),$$
and
$$H'' \cong \operatorname{Hom}_R(R, H''(-)) \cong \operatorname{Hom}_S(-, H'(R)) \cong \operatorname{Hom}_S(-, U).$$
This gives both (1) and (2).

Now to prove (3) we may assume that there is a bimodule ${}_R U_S$ and that
$$H' = \operatorname{Hom}_R(-, U) \quad \text{and} \quad H'' = \operatorname{Hom}_S(-, U)$$
gives a duality between ${}_R \mathcal{C}$ and $\mathcal{D}_S$. Let $N \in \mathcal{D}_S$. In order to prove that $N$ is $U$-reflexive we first show that the natural $S$-isomorphism
$$\zeta_N: H'H''(N) \to N$$
determines an $R$-automorphism $\alpha: H''(N) \to H''(N)$. Indeed, define $\alpha$ via
$$(\alpha(g))(n) = (\zeta_N^{-1}(n))(g)$$
for $g \in H''(N) = \operatorname{Hom}_S(N, U)$ and $n \in N$.

Now we show $\alpha$ is a composite of three isomorphisms. Define $\psi: H''(N) \to \operatorname{Hom}_S(H'(U), H''H'(N))$ via
$$\psi: g \mapsto \operatorname{Hom}_S(H'(U), g).$$
This is a $\mathbb{Z}$-isomorphism (see Exercise (20.5)). Also since ${}_R U_S$ is a bimodule, $H''H'(U)$ is a left $R$-right $S$-bimodule. Let $\gamma_N = \zeta_N^{-1}: N \to H'H''(N)$. Then
$$\operatorname{Hom}_S(\gamma_N, H''H'(U)): \operatorname{Hom}_S(H'(U), H''H'(N)) \to \operatorname{Hom}_S(N, H''H'(U))$$
is also a $\mathbb{Z}$-isomorphism. Since $\eta$ is natural, $\eta_U: H''H'(U) \to U$ is an $S$-isomorphism and
$$\operatorname{Hom}_S(N, \eta_U): \operatorname{Hom}_S(N, H''H'(U)) \to \operatorname{Hom}_S(N, U)$$
is a $\mathbb{Z}$-isomorphism. Composing these, for each $g \in \operatorname{Hom}_S(N, U)$ and each $n \in N$,
\begin{align*}
&((\operatorname{Hom}_S(N, \eta_U) \circ \operatorname{Hom}_S(\gamma_N, H''H'(U)) \circ \psi)(g))(n) \\
&= (\eta_U \circ \operatorname{Hom}_S(H'(U), g) \circ \gamma_N)(n) \\
&= \eta_U(g \circ \gamma_N(n)) = \eta_U(\operatorname{Hom}_S(\gamma_N(n), U)(g)) \\
&= (\eta_U \circ H''(\gamma_N(n)))(g) = (v_{UN}(\gamma_N(n)))(g) \\
&= (\zeta_N^{-1}(n))(g) = (\alpha(g))(n).
\end{align*}
Thus $\alpha$ is just the composite of the three isomorphisms; hence $\alpha$ is an $R$-automorphism of $H''(N)$ as claimed.

Now given $N \in \mathcal{D}_S$, we know that $N \cong H'H''(N)$ via $\zeta_N$, and the $R$-automorphism $\alpha$ of $H''(N)$ yields that $H''(N)$ is $U$-reflexive. Therefore $N \cong H'H''(N)$ is $U$-reflexive as well, since $U$-reflexivity is preserved under isomorphism. Thus $\mathcal{D}_S \subseteq \mathcal{R}_S[U]$, and by symmetry ${}_R \mathcal{C} \subseteq {}_R \mathcal{R}[U]$. This completes the proof.
