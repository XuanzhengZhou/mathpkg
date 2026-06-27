---
role: proof
locale: en
of_concept: lemma-4874946316
source_book: gtm077
source_chapter: "VIII"
source_section: "§50"
---
# Proof of Lemma on $F(p^k)$

We prove that for each power $p^k$ of a prime $p$,

$$F(p^k) = \sum_{i=0}^{k} \left( \frac{d}{p^i} \right) = 1 + \sum_{i=1}^{k} \left( \frac{d}{p} \right)^i,$$

where $F(n)$ denotes the number of integral ideals of the quadratic field $k(\sqrt{d})$ with norm $n$, and $(\frac{d}{\cdot})$ is the Kronecker symbol.

The proof proceeds by considering the three possible values of the Legendre symbol $(\frac{d}{p})$.

---

**Case (a):** $(\frac{d}{p}) = -1$.

In this case $p$ remains inert in $k(\sqrt{d})$; that is, $p$ is itself a prime ideal (up to the principal ideal $(p)$, but since $p$ is rational, the only integral ideal with norm a power of $p$ is the principal ideal $(p^u) = p^u \mathcal{O}_k$ with $u \geq 0$). If an ideal $\mathfrak{a}$ satisfies $N(\mathfrak{a}) = p^k$, then we must have $\mathfrak{a} = p^u$ with $u$ a positive rational integer. The norm of $p^u$ is $N(p^u) = (p^u)^2 = p^{2u}$, because $N(p) = p^2$ when $p$ is inert. Hence $2u = k$, which is possible only when $k$ is even.

Therefore

$$F(p^k) = \begin{cases} 1, & \text{if $k$ is even}, \\[4pt] 0, & \text{if $k$ is odd}. \end{cases}$$

Since $(\frac{d}{p}) = -1$, we compute
$$\sum_{i=0}^{k} \left( \frac{d}{p} \right)^i = \sum_{i=0}^{k} (-1)^i = \begin{cases} 1, & k \text{ even}, \\ 0, & k \text{ odd}, \end{cases}$$
which agrees with formula (144).

---

**Case (b):** $(\frac{d}{p}) = 0$.

Here $p$ ramifies in $k(\sqrt{d})$; that is, $p$ is the square of a prime ideal: $p = \mathfrak{p}^2$ (as ideals). If $N(\mathfrak{a}) = p^k$, then $\mathfrak{a}$ must be a power of the unique prime ideal $\mathfrak{p}$ lying above $p$, say $\mathfrak{a} = \mathfrak{p}^u$. The norm of $\mathfrak{p}$ is $N(\mathfrak{p}) = p$ (because $\mathfrak{p}^2 = (p)$ and the norm is multiplicative), so
$$N(\mathfrak{a}) = N(\mathfrak{p}^u) = p^u.$$
Thus $u = k$ and there is exactly one such ideal.

Therefore $F(p^k) = 1$. Since $(\frac{d}{p}) = 0$, we have $(\frac{d}{p})^i = 0$ for all $i \geq 1$, and
$$\sum_{i=0}^{k} \left( \frac{d}{p} \right)^i = 1 + 0 + \cdots + 0 = 1,$$
which again agrees with formula (144).

---

**Case (c):** $(\frac{d}{p}) = 1$.

In this case $p$ splits completely in $k(\sqrt{d})$; that is, the principal ideal $(p)$ factors as
$$(p) = \mathfrak{p}_1 \mathfrak{p}_2,$$
where $\mathfrak{p}_1$ and $\mathfrak{p}_2$ are distinct prime ideals, each of norm $p$. Any integral ideal $\mathfrak{a}$ with norm $N(\mathfrak{a}) = p^k$ must be a product of powers of $\mathfrak{p}_1$ and $\mathfrak{p}_2$, since these are the only prime ideals dividing $p$. Write
$$\mathfrak{a} = \mathfrak{p}_1^a \mathfrak{p}_2^b, \qquad a, b \geq 0.$$
Then
$$N(\mathfrak{a}) = N(\mathfrak{p}_1)^a \, N(\mathfrak{p}_2)^b = p^a \cdot p^b = p^{a+b}.$$
The condition $N(\mathfrak{a}) = p^k$ is therefore equivalent to $a + b = k$. The number of non-negative integer solutions $(a, b)$ to $a + b = k$ is $k + 1$.

Hence $F(p^k) = k + 1$. Since $(\frac{d}{p}) = 1$, we have $(\frac{d}{p})^i = 1$ for every $i$, and
$$\sum_{i=0}^{k} \left( \frac{d}{p} \right)^i = \sum_{i=0}^{k} 1 = k + 1,$$
which again agrees with formula (144).

---

Having verified the lemma in all three cases, we conclude that for every prime $p$ and every exponent $k \geq 0$,

$$F(p^k) = 1 + \sum_{i=1}^{k} \left( \frac{d}{p} \right)^i.$$

By the multiplicativity of $F$ (equation (89): $F(ab) = F(a)F(b)$ for coprime $a, b$) and the complete multiplicativity of the Kronecker symbol, this formula extends to all positive integers $n$ via prime factorization.
