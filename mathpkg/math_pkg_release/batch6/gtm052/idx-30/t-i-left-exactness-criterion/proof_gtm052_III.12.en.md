---
role: proof
locale: en
of_concept: t-i-left-exactness-criterion
source_book: gtm052
source_chapter: "III"
source_section: "12"
---

Since tensor product is right exact, we have

$$W^i(L^\bullet \otimes M) = W^i(L^\bullet) \otimes M,$$

for any $A$-module $M$. We will write simply $W^i$ for $W^i(L^\bullet)$. Hence

$$T^i(M) = \ker(W^i \otimes M \to L^{i+1} \otimes M).$$

Let $0 \to M' \to M$ be an inclusion. Then we obtain an exact, commutative diagram

$$\begin{CD}
0 \\
@VVV \\
T^i(M') \\
@VVV \\
W^i \otimes M' @>>> L^{i+1} \otimes M' \\
@V{\alpha}VV @V{\beta}VV \\
0 \\
@VVV \\
T^i(M) \\
@VVV \\
W^i \otimes M @>>> L^{i+1} \otimes M.
\end{CD}$$

The third vertical arrow $\beta$ is injective, since $L^{i+1}$ is free. A simple diagram chase shows that $\alpha$ is injective if and only if $\beta$ is. Since this is true for any choice of $0 \to M' \to M$, we see that $T^i$ is left exact if and only if $W^i$ is flat. (Recall that in any case $T^i$ is exact in the middle by Proposition 12.1.) But since $W^i$ is finitely generated, this is equivalent to $W^i$ being projective (by the fact that a finitely generated module over a noetherian ring is flat if and only if it is projective). This shows (i) $\Leftrightarrow$ (ii).

(iii) $\Rightarrow$ (i) is obvious, since any functor of the form $\operatorname{Hom}(Q, \cdot)$ is left exact.

To prove (ii) $\Rightarrow$ (iii), let $\check{L}^{i+1}$ and $\check{W}^i$ be the dual projective modules. Define

$$Q = \operatorname{coker}(\check{L}^{i+1} \to \check{W}^i).$$

Then for every $A$-module $M$, we have the exact sequence

$$0 \to \operatorname{Hom}(Q, M) \to \operatorname{Hom}(\check{W}^i, M) \to \operatorname{Hom}(\check{L}^{i+1}, M).$$

But $\operatorname{Hom}(\check{W}^i, M) \cong W^i \otimes M$ and $\operatorname{Hom}(\check{L}^{i+1}, M) \cong L^{i+1} \otimes M$ (since $W^i$ and $L^{i+1}$ are projective, hence reflexive), and the map between them is exactly the differential. Therefore the kernel is precisely $T^i(M)$. Moreover, $Q$ is finitely generated because $\check{W}^i$ and $\check{L}^{i+1}$ are finitely generated projective modules.
