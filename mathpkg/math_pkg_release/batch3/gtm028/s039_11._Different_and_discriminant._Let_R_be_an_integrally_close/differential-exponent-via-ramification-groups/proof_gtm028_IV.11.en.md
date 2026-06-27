---
role: proof
locale: en
of_concept: differential-exponent-via-ramification-groups
source_book: gtm028
source_chapter: "IV"
source_section: "11. Different and discriminant"
---

We assume the existence of an element $u \in R'$ such that $\{1, u, \ldots, u^{n-1}\}$ is a basis of $K'$ over $K_i$ and also of $R'$ over $R_{K_i}'$, where $n = [K' : K_i]$.

The existence of such a $u$ is justified as follows: Let $\mathfrak{P}$ be the prime ideal of $K'$ we are considering, and let $\mathfrak{P}_i = \mathfrak{P} \cap K_i$. Let $v$ be the normalized $\mathfrak{P}$-adic valuation. Choose $u \in \mathfrak{P}$ such that $u \notin \mathfrak{P}^2$ and such that the $\mathfrak{P}_i$-residue of $u$ generates the residue field extension $R'/\mathfrak{P}$ over $R_{K_i}'/\mathfrak{P}_i$ (this is possible since the residue field extension is separable). Then for any $a_j \in K_i$ with $\sum_{j=0}^{n-1} a_j u^j = 0$, the integers $v(a_j u^j) = j + v(a_j)$ are all distinct (since $v(a_j)$ are multiples of $n$ by ramification theory). Hence if $v(a_q u^q) = r$ is the smallest, the sum of the other terms is in $\mathfrak{P}^{r+1}$, contradicting the equality to $-a_q u^q$ unless all $a_j = 0$. Therefore $\{1, u, \ldots, u^{n-1}\}$ is a basis of $K'$ over $K_i$.

For any $x \in R'$, write $x = \sum_{j=0}^{n-1} b_j u^j$ with $b_j \in K_i$. Again the integers $v(b_j u^j)$ are all distinct. If $r = \min_j v(b_j u^j)$, the sum is in $\mathfrak{P}^r$ but not in $\mathfrak{P}^{r+1}$. Since $x \in R'$ implies $r \geq 0$, we get $j + v(b_j) \geq 0$ for all $j$. As $v(b_j)$ are multiples of $n$, this forces $v(b_j) \geq 0$, hence $b_j \in R_{K_i}'$. Thus $\{1, u, \ldots, u^{n-1}\}$ is also an $R_{K_i}'$-basis of $R'$.

We may now apply Theorem 29 to compute the different of $R'$ over $R_{K_i}'$: it is the ideal $R' F'(u)$. Since $K'$ is a Galois extension of $K_i$ with $G_{V_i}$ as Galois group, the minimal polynomial of $u$ over $K_i$ is

$$F(X) = \prod_{s \in G_{V_i}} (X - s(u)).$$

Therefore

$$F'(u) = \prod_{s \in G_{V_i}, s \neq 1} (u - s(u)).$$

Thus the differential exponent is

$$m(K', K_i) = v_{\mathfrak{P}}(F'(u)) = \sum_{s \in G_{V_i}, s \neq 1} v_{\mathfrak{P}}(u - s(u)).$$
