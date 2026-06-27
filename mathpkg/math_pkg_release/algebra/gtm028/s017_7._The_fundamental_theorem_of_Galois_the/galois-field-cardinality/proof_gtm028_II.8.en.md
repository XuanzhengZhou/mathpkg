---
role: proof
locale: en
of_concept: galois-field-cardinality
source_book: gtm028
source_chapter: "II"
source_section: "§8. Galois fields"
---

Let $K$ be a Galois field of characteristic $p$. The prime subfield of $K$ is $\mathcal{F}_p$, the field of $p$ elements. Let $n = [K:\mathcal{F}_p]$ and let $x_1, x_2, \cdots, x_n$ be a basis of $K$ over $\mathcal{F}_p$. Then every element of $K$ has a unique expression of the form
\[
a_1 x_1 + a_2 x_2 + \cdots + a_n x_n, \quad a_i \in \mathcal{F}_p.
\]
Since each coefficient $a_i$ can take independently $p$ values (as $\mathcal{F}_p$ contains exactly $p$ elements), the number of elements in $K$ is $p^n$.

If $k$ is a Galois field consisting of $m$ elements and $K$ is a finite extension of $k$ of degree $n$, then a similar argument shows that $K$ consists of $m^n$ elements.

The elements of $K$, other than $0$, form a multiplicative group of order $h = p^n - 1$. Hence $x^h = 1$ for all elements $x$ of this group, and consequently $x^{p^n} - x = 0$ for all elements $x$ of $K$ (including $0$). Since the degree of the polynomial $X^{p^n} - X$ is the same as the number of elements of $K$, we conclude that this polynomial factors completely into linear factors in $K[X]$:
\[
X^{p^n} - X = \prod_{i=1}^{p^n} (X - \alpha_i),
\]
where $\alpha_1, \alpha_2, \cdots, \alpha_{p^n}$ are all the elements of $K$. It follows that $K$ is a splitting field over $\mathcal{F}_p$ of the polynomial $X^{p^n} - X$, and is therefore a normal extension of $\mathcal{F}_p$.
