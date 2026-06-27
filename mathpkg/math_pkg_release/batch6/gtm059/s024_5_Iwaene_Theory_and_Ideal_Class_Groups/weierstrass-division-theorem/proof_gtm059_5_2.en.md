---
role: proof
locale: en
of_concept: weierstrass-division-theorem
source_book: gtm059
source_chapter: "5"
source_section: "2"
---

**Proof.** Write $f(X) = a_n X^n + \text{higher terms} + (\text{terms with coefficients in } \mathfrak{m})$. Then

$$f(X) = a_n X^n + \sum_{k \neq n} a_k X^k = a_n X^n(1 + h(X))$$

where $h(X) \in \mathfrak{m}[[X]]$. Since $a_n$ is a unit and $1+h(X)$ is a unit in $A[[X]]$ (its inverse is given by the geometric series in the $\mathfrak{m}$-adic topology, which converges because $A$ is complete), we have

$$f(X) = u(X) \cdot X^n$$

with $u(X)$ a unit in $A[[X]]$.

Now consider the $A$-linear map $\phi: A[[X]] \to A[X]/(X^n)$ defined by reducing modulo $f(X)$ and taking the remainder of degree $< n$. This map is surjective with kernel $(f)$. To show existence and uniqueness, we construct $q$ and $r$ by successive approximation using the Euclidean algorithm in the complete local ring.

Specifically, write $g = g_0$. Since $f = u X^n + \cdots$, we can subtract an appropriate multiple $q_0 f$ to reduce the degree of the leading terms. Iterating this process yields a convergent sequence in the $\mathfrak{m}$-adic topology on $A[[X]]$, giving $q = \sum q_i$ and remainder $r = g - qf$ with $\deg r < n$.

Uniqueness follows because if $g = q_1 f + r_1 = q_2 f + r_2$ with $\deg r_1, \deg r_2 < n$, then $(q_1 - q_2)f = r_2 - r_1$. The left side has degree at least $n$ (or is zero) while the right side has degree $< n$, forcing both sides to vanish.

The preservation of the subring $B$ follows from the same iterative construction, noting that all operations stay within $B$ when $a_n$ is a unit in $B$.
