---
role: proof
locale: en
of_concept: algebraic-integer-criterion-quadratic-field
source_book: gtm028
source_chapter: "V"
source_section: "12"
---

Let $K = \mathbb{Q}(\sqrt{m})$ with $m$ a square-free integer. For $x = a + b\sqrt{m} \in K$ ($a, b \in \mathbb{Q}$), the conjugates are $x$ and $a - b\sqrt{m}$, so $T(x) = 2a$ and $N(x) = a^2 - mb^2$.

For $x$ to be an algebraic integer, $T(x)$ and $N(x)$ must be in $\mathbb{Z}$. Thus $2a \in \mathbb{Z}$, so $a = a'/2$ with $a' \in \mathbb{Z}$. Also $a^2 - mb^2 = (a'^2 - m(2b)^2)/4 \in \mathbb{Z}$, whence $m(2b)^2 \in \mathbb{Z}$. Since $m$ is square-free, $2b \in \mathbb{Z}$, so $b = b'/2$ with $b' \in \mathbb{Z}$.

The condition becomes $a'^2 - mb'^2 \equiv 0 \pmod{4}$. If $m \equiv 1 \pmod{4}$, this admits solutions with $a', b'$ both odd (e.g., $1^2 - m \cdot 1^2 \equiv 0 \pmod{4}$). If $m \equiv 2, 3 \pmod{4}$, we must have $a', b'$ both even, giving $a, b \in \mathbb{Z}$.

Thus the ring of integers is $\mathbb{Z}[\sqrt{m}]$ for $m \equiv 2,3 \pmod{4}$, and $\mathbb{Z}[(1+\sqrt{m})/2]$ for $m \equiv 1 \pmod{4}$.
