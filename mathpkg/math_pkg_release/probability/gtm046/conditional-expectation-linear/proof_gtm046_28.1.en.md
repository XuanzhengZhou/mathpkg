---
role: proof
locale: en
of_concept: conditional-expectation-linear
source_book: gtm046
source_chapter: "VIII"
source_section: "28.1"
---

**Proof.** The conditional expectation $E^\mathfrak{B}$ is defined via the Radon-Nikodym theorem as a linear operation on integrable random variables. For any $c, c' \in \mathbb{R}$ and integrable $X, X'$, by the definition of conditional expectation, for every $B \in \mathfrak{B}$,

$$\int_B E^\mathfrak{B}(cX + c'X') \, dP = \int_B (cX + c'X') \, dP = c \int_B X \, dP + c' \int_B X' \, dP$$

$$= c \int_B E^\mathfrak{B}X \, dP + c' \int_B E^\mathfrak{B}X' \, dP = \int_B (cE^\mathfrak{B}X + c'E^\mathfrak{B}X') \, dP.$$

Since the indefinite integrals of both $E^\mathfrak{B}(cX + c'X')$ and $cE^\mathfrak{B}X + c'E^\mathfrak{B}X'$ coincide on all $B \in \mathfrak{B}$, these two $\mathfrak{B}$-measurable functions are $P_\mathfrak{B}$-equivalent. Hence

$$E^\mathfrak{B}(cX + c'X') = cE^\mathfrak{B}X + c'E^\mathfrak{B}X' \quad \text{a.s.}$$

In particular, $P^\mathfrak{B}\Omega = 1$ a.s., $P^\mathfrak{B}\emptyset = 0$ a.s., $P^\mathfrak{B}A \geq 0$ a.s., and for simple functions,

$$E^\mathfrak{B}\left(\sum_{k=1}^{n} x_k I_{A_k}\right) = \sum_{k=1}^{n} x_k P^\mathfrak{B}A_k \quad \text{a.s.}$$

These properties follow directly from the definition of conditional expectations and the properties of integrals.
