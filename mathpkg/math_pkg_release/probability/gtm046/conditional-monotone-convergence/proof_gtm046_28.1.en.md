---
role: proof
locale: en
of_concept: conditional-monotone-convergence
source_book: gtm046
source_chapter: "VIII"
source_section: "28.1"
---

**Proof.** Assume $0 \leq X_n \uparrow X$ a.s. By monotonicity of conditional expectation, $0 \leq E^\mathfrak{B}X_n \uparrow$ a.s., so the limit $Y = \lim_n E^\mathfrak{B}X_n$ exists a.s. (possibly infinite). For every $B \in \mathfrak{B}$,

$$\int_B Y \, dP = \lim_n \int_B E^\mathfrak{B}X_n \, dP = \lim_n \int_B X_n \, dP = \int_B X \, dP = \int_B E^\mathfrak{B}X \, dP,$$

where the interchange of limit and integral is justified by the ordinary monotone convergence theorem applied to the sequence $X_n I_B$. Since the indefinite integrals of $Y$ and $E^\mathfrak{B}X$ coincide on $\mathfrak{B}$ and both are $\mathfrak{B}$-measurable (the limit of $\mathfrak{B}$-measurable functions is $\mathfrak{B}$-measurable), it follows that $Y = E^\mathfrak{B}X$ a.s. Hence

$$0 \leq E^\mathfrak{B}X_n \uparrow E^\mathfrak{B}X \quad \text{a.s.}$$

In particular, for any sequence of events $A_k$,

$$P^\mathfrak{B}\left(\sum_{k=1}^{\infty} A_k\right) = \sum_{k=1}^{\infty} P^\mathfrak{B}A_k \quad \text{a.s.}$$

which is the conditional $\sigma$-additivity of $P^\mathfrak{B}$.
