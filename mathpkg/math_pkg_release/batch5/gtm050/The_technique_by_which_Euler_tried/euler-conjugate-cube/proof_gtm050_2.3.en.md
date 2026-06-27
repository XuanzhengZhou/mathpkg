---
role: proof
locale: en
of_concept: euler-conjugate-cube
source_book: gtm050
source_chapter: "2"
source_section: "2.3"
---

Define conjugation $\sigma: \mathbb{Z}[\sqrt{-3}] \to \mathbb{Z}[\sqrt{-3}]$ by $\sigma(a + b\sqrt{-3}) = a - b\sqrt{-3}$.

First, $\sigma$ is a ring homomorphism: for any $\alpha = a + b\sqrt{-3}$ and $\beta = c + d\sqrt{-3}$,

$$
\begin{aligned}
\sigma(\alpha + \beta) &= \sigma((a+c) + (b+d)\sqrt{-3}) = (a+c) - (b+d)\sqrt{-3} \\
&= (a - b\sqrt{-3}) + (c - d\sqrt{-3}) = \sigma(\alpha) + \sigma(\beta).
\end{aligned}
$$

For multiplication:
$$
\begin{aligned}
\alpha\beta &= (ac - 3bd) + (ad + bc)\sqrt{-3}, \\
\sigma(\alpha\beta) &= (ac - 3bd) - (ad + bc)\sqrt{-3}.
\end{aligned}
$$

On the other hand:
$$
\sigma(\alpha)\sigma(\beta) = (a - b\sqrt{-3})(c - d\sqrt{-3}) = (ac - 3bd) - (ad + bc)\sqrt{-3}.
$$

Thus $\sigma(\alpha\beta) = \sigma(\alpha)\sigma(\beta)$. By induction, $\sigma(\alpha^n) = \sigma(\alpha)^n$ for all $n \in \mathbb{N}$. In particular, for $n = 3$:

If $p + q\sqrt{-3} = \alpha^3$, then applying $\sigma$ to both sides gives $p - q\sqrt{-3} = \sigma(\alpha^3) = \sigma(\alpha)^3 = (a - b\sqrt{-3})^3$.
