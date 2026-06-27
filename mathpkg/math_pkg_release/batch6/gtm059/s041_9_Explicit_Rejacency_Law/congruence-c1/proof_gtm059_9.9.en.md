---
role: proof
locale: en
of_concept: congruence-c1
source_book: gtm059
source_chapter: "9"
source_section: "9"
---

Suppose first that $m = 1$, then the worst case of (0). We have to verify that

$$T_k^* \left( \frac{1}{2} T_k^* u_n \right) = n^{k+1} u_n.$$

Recall that $\operatorname{ord}_n = n \in \{0, \dots, n-1\}$.

By Chapter 5, Lemma 1, $i \in A_n$ is a power series whose terms are either integral, or at worst with factor $\frac{i}{n^2}$ and $i \geq 1$.

Suppose $x \in d(A_n)$. Then the exponent satisfies

$$\operatorname{ord} \, k(s) = \operatorname{ord} \, x \geq \frac{2}{x-1}.$$

From the definition of the different $T_k^* = n^{-k} T_k^* u_k$, this is equivalent to: $n^{k+1} T_k^* (T_k^*) u_k$ is integral. It will even be shown that if $n \in \{0, \dots, n-1\}$, $n^{k+1} T_k^* (T_k^*) u_k$ is integral.
