---
role: proof
locale: en
of_concept: parity-of-permutation
source_book: gtm030
source_chapter: "1"
source_section: "12"
---

First, using the cycle-to-transpositions formula, $\alpha$ is a product of $(r-1)+(s-1)+\cdots+(u-1) = N(\alpha)$ transpositions.

The key formulas for multiplying by a transposition $(ab)$ are:
$$(a c_1 c_2 \cdots c_h b d_1 \cdots d_k)(ab) = (a c_1 \cdots c_h)(b d_1 \cdots d_k)$$
$$(a c_1 \cdots c_h)(b d_1 \cdots d_k)(ab) = (a c_1 \cdots c_h b d_1 \cdots d_k).$$

According to these:
- If $a$ and $b$ occur in the same cycle, $N(\alpha(ab)) = N(\alpha) - 1$.
- If $a$ and $b$ occur in different cycles, $N(\alpha(ab)) = N(\alpha) + 1$.

In any case, $N(\alpha(ab)) = N(\alpha) \pm 1$.

Now suppose $\alpha$ is a product of $m$ transpositions: $\alpha = (ab)(cd) \cdots (pq)$. Since $(ab)^{-1} = (ab)$, this implies
$$\alpha(pq) \cdots (cd)(ab) = 1.$$
Since $N(1) = 0$, iterating $N(\alpha(ab)) = N(\alpha) \pm 1$ gives
$$0 = N(\alpha) \pm 1 \pm \cdots \pm 1 \quad (\text{$m$ terms of $\pm 1$}).$$
Thus $N(\alpha)$ and $m$ have the same parity. Therefore any two factorizations of $\alpha$ into transpositions have the same parity.
