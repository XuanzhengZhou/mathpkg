---
role: proof
locale: en
of_concept: conditional-expectation-measurable-factor
source_book: gtm046
source_chapter: "VIII"
source_section: "28.2"
---

**Proof.** The assertion holds first for indicator functions $X = I_{B'}$ where $B' \in \mathfrak{B}$, since for every $B \in \mathfrak{B}$,

$$\int_B E^\mathfrak{B}(I_{B'}Y) \, dP = \int_B I_{B'}Y \, dP = \int_{BB'} Y \, dP = \int_{BB'} E^\mathfrak{B}Y \, dP = \int_B I_{B'} E^\mathfrak{B}Y \, dP.$$

Therefore, $E^\mathfrak{B}(I_{B'}Y) = I_{B'}E^\mathfrak{B}Y$ a.s.

The assertion extends to simple $\mathfrak{B}$-measurable functions $X_n = \sum_k x_k I_{B_k}$ by linearity:

$$E^\mathfrak{B}(X_n Y) = E^\mathfrak{B}\left(\sum_k x_k I_{B_k} Y\right) = \sum_k x_k E^\mathfrak{B}(I_{B_k}Y) = \sum_k x_k I_{B_k} E^\mathfrak{B}Y = X_n E^\mathfrak{B}Y \quad \text{a.s.}$$

For nonnegative $\mathfrak{B}$-measurable $X$, take $0 \leq X_n \uparrow X$ with $X_n$ simple and $\mathfrak{B}$-measurable, and apply the conditional monotone convergence theorem:

$$E^\mathfrak{B}(XY) = \lim_n E^\mathfrak{B}(X_n Y) = \lim_n X_n E^\mathfrak{B}Y = X E^\mathfrak{B}Y \quad \text{a.s.}$$

For general $\mathfrak{B}$-measurable $X$, decompose $X = X^+ - X^-$ and apply the result to each part. This completes the proof.
