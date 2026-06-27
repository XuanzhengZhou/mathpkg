---
role: proof
locale: en
of_concept: permutation-parity
source_book: gtm030
source_chapter: "I"
source_section: "12"
---

First, note the following identities for multiplying by a transposition $(ab)$:

If $a$ and $b$ occur in the same cycle $(a c_1 \cdots c_h b d_1 \cdots d_k)$ of $\alpha$, then
$$(a c_1 \cdots c_h b d_1 \cdots d_k)(ab) = (a c_1 \cdots c_h)(b d_1 \cdots d_k).$$

If $a$ and $b$ occur in different cycles $(a c_1 \cdots c_h)$ and $(b d_1 \cdots d_k)$ of $\alpha$, then
$$(a c_1 \cdots c_h)(b d_1 \cdots d_k)(ab) = (a c_1 \cdots c_h b d_1 \cdots d_k).$$

In the first case, $N(\alpha(ab)) = N(\alpha) - 1$; in the second case, $N(\alpha(ab)) = N(\alpha) + 1$. Thus in all cases,

$$N(\alpha(ab)) = N(\alpha) \pm 1.$$

Now suppose $\alpha$ can be written as a product of $m$ transpositions: $\alpha = (ab)(cd) \cdots (pq)$. Then $\alpha(pq) \cdots (cd)(ab) = 1$. Since $N(1) = 0$, iterating the formula $N(\cdot (ab)) = N(\cdot) \pm 1$ gives

$$0 = N(\alpha) \pm 1 \pm 1 \cdots \pm 1 \quad (m \text{ terms}).$$

Hence $N(\alpha)$ and $m$ have the same parity. Therefore, if $N(\alpha)$ is even, any factorization into transpositions has an even number of factors; if $N(\alpha)$ is odd, any such factorization has an odd number of factors.
