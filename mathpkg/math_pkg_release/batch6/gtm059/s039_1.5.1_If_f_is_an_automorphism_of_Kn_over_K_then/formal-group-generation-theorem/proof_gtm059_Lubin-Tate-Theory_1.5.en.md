---
role: proof
locale: en
of_concept: formal-group-generation-theorem
source_book: gtm059
source_chapter: "Lubin-Tate Theory"
source_section: "1.5"
---

*Proof.* Since $X = X \cup F = F \cup I$ and given $x \in u_i$, we can find $n_i \in u_i$ such that

$$x = [u_i]_{v_i} \equiv 0 \pmod{\mathfrak{m}^q}$$

because $[u_i]_{v_i} = u_i \bmod \mathfrak{m}^q$. We may then proceed recursively to find $n_1, \dots, n_{q-1}$, and more generally we can find $n_i \in u_i$ modulo $\mathfrak{m}^q$.

This shows that the elements $a_i$ with $i \in I$ generate $A(\mathfrak{a}_i)$ modulo $\mathfrak{m}^{q-1}[A(\mathfrak{a}_i)]$ over $I$. It remains to prove linear independence modulo $\mathfrak{m}^{q-1}$.

Assume $\sum_{i \in I} [a_i] = 0$ modulo $\mathfrak{m}^{q-1}$ in $A(\mathfrak{a}_i)$. We may normalize so that some coefficient $a_i$ is a unit, and without loss of generality $a_i = 1$.

**Case 1.** $k > 0$. For any $x \in A$, the expansion

$$[x] = x^k + \cdots + x^k$$

implies that either the term $x^k$ dominates, in which case $a_k$ is divisible by $\mathfrak{m}$, or some other term dominates, meaning

$$p \cdot \operatorname{ord} x > (p^k - 1) + \operatorname{ord} x,$$

so $\operatorname{ord} x > p^k$. This implies no nonzero coefficient can arise, because with ordinary addition and $\operatorname{ord} x > 0$, we have

$$\operatorname{ord}(x, y) = y \text{ minus } \operatorname{ord}(x, y) \operatorname{ord}(y).$$

Hence there can be no cancellation in the left-hand side, establishing the result.

**Case 2.** Proceeding as in Case 1, we may suppose each $a_i$ is divisible by $\mathfrak{m}$ for $i \in I$, from which the conclusion follows in $[a_i]$ modulo $\mathfrak{m}^{q-1}$.
