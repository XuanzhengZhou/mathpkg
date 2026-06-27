---
role: proof
locale: en
of_concept: direct-sum-homomorphism
source_book: gtm028
source_chapter: "III"
source_section: "§12"
---

If $x \in M$, then we can write $x = x_1 + \cdots + x_r$, $x_i \in M_i$. Hence if the required $T$ exists at all we must have $xT = x_1T_1 + \cdots + x_rT_r$, and so $T$ is unique. To prove $T$ exists we define it by this formula; since the representation is unique (because the sum is direct), $xT$ is uniquely determined. It is easily checked that $T$ is an $R$-homomorphism. If each $T_i$ is onto, so is $T$, since $MT \supset M_iT = M_iT_i = N_i$ and hence $MT = N$. Now suppose each $T_i$ is an isomorphism and the sum for $N$ is direct. If then $xT = 0$, it follows that $\sum x_iT_i = 0$. Since $N$ is direct, $x_iT_i = 0$, hence each $x_i = 0$, so $x = 0$. Thus $T$ is an isomorphism.
