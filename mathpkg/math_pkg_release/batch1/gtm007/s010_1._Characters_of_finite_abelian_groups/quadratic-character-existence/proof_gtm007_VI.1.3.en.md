---
role: proof
locale: en
of_concept: quadratic-character-existence
source_book: gtm007
source_chapter: "VI"
source_section: "§1.3"
---

To prove the existence of $\chi_a$, assume first that $a = l_1 \cdots l_k$ where the $l_i$ are distinct prime numbers, different from $2$. Define the character
$$\chi_a(x) = (-1)^{\varepsilon(x) \varepsilon(a)} \left( \frac{x}{l_1} \right) \cdots \left( \frac{x}{l_k} \right),$$
where $\varepsilon(x) = (x-1)/2 \pmod{2}$ and $\left( \frac{x}{l_i} \right)$ is the Legendre symbol.

If $p$ is a prime number distinct from $2$ and the $l_i$, the quadratic reciprocity law shows that
$$\chi_a(p) = \left( \frac{l_1}{p} \right) \cdots \left( \frac{l_k}{p} \right) = \left( \frac{a}{p} \right),$$
so $\chi_a$ has the required property.

We have $\chi_a \neq 1$ if $a \neq 1$: choose $x$ such that $\left( \frac{x}{l_1} \right) = -1$ and $x \equiv 1 \pmod{4l_2 \cdots l_k}$; then $\chi_a(x) = -1$.

When $a$ is of the form $-b$ (or $2b$ or $-2b$) with $b = l_1 \cdots l_k$ as above, take for $\chi_a$ the product of $\chi_b$ with the character $(-1)^{\varepsilon(x)}$ (or $(-1)^{\omega(x)}$ or $(-1)^{\varepsilon(x) + \omega(x)}$, where $\omega(x) = (x^2-1)/8 \pmod{2}$). A similar argument shows $\chi_a \neq 1$.

One can also express $\chi_a$ via Hilbert symbols:
$$\chi_a(x) = \prod_{l \mid m} (a, x)_l = \prod_{(l,m)=1} (a, x)_l,$$
where $(a, x)_l$ denotes the Hilbert symbol of $a$ and $x$ in the field $\mathbb{Q}_l$.
