---
role: proof
locale: en
of_concept: kernel-of-weak-quasifield-is-skewfield
source_book: gtm006
source_chapter: "VII"
source_section: "2"
---

Let $a, b$ be any two elements of $W$ and $h, k$ be any elements of $K$.

First we show $K$ is closed under subtraction. Compute:
$$
(a + b)(h - k) = (a + b)h + (a + b)(-k)
$$
by the left distributive law. By Lemma 7.1 (which states $x(-y) = -(xy)$ for all $x, y \in W$), this equals
$$
(a + b)h - (a + b)k.
$$
Since $h, k \in K$, they distribute on the right, so
$$
(a + b)h - (a + b)k = ah + bh - ak - bk.
$$
Since addition in $W$ is abelian,
$$
ah + bh - ak - bk = ah - ak + bh - bk.
$$
Using the left distributive law and Lemma 7.1 again,
$$
ah - ak + bh - bk = a(h - k) + b(h - k).
$$
Thus $(a + b)(h - k) = a(h - k) + b(h - k)$, so $h - k$ satisfies condition (i).

Similarly,
$$
(ab)(h - k) = (ab)h - (ab)k \quad \text{(by Lemma 7.1 and left distributive law)}
$$
$$
= a(bh) - a(bk) \quad \text{(since $h, k$ associate on the right)}
$$
$$
= a(bh - bk) \quad \text{(using left distributive law)}
$$
$$
= a(b(h - k)) \quad \text{(by Lemma 7.1 and left distributive law)}.
$$
Thus $h - k$ satisfies condition (ii). Hence $K$ is closed under subtraction and is non-empty (0 and 1 are in $K$), so $(K, +)$ is an abelian subgroup of $(W, +)$.

Now we show $(K^*, \cdot)$ is a group, where $K^* = K \setminus \{0\}$. From the definition of $K$, multiplication in $K$ is associative and $1 \in K$. We must show $K$ is closed under multiplication and that every non-zero element of $K$ has a multiplicative inverse in $K$.

If $h, k \in K$, then for all $x, y \in W$:
$$
(x + y)(hk) = ((x + y)h)k = (xh + yh)k = (xh)k + (yh)k = x(hk) + y(hk),
$$
and
$$
(xy)(hk) = ((xy)h)k = (x(yh))k = x((yh)k) = x(y(hk)).
$$
Thus $hk \in K$, so $K$ is closed under multiplication.

To show existence of inverses, let $k \in K^*$. Since $W^*$ is a loop, the equation $xk = 1$ has a unique solution $x \in W$. We must show $x \in K$. For any $a, b \in W$, using the fact that $k \in K$:
$$
(a + b) = (a + b) \cdot 1 = (a + b)(xk) = ((a + b)x)k.
$$
Also $a + b = a \cdot 1 + b \cdot 1 = a(xk) + b(xk) = (ax)k + (bx)k$. Since right multiplication by $k$ is injective (as $W^*$ is a loop), we obtain $(a + b)x = ax + bx$, so $x$ satisfies condition (i). A similar argument using $(ab)x = a(bx)$ shows $x$ satisfies condition (ii). Hence $x \in K$ and $K^*$ is a group.

Finally, since addition in $W$ is abelian, scalar multiplication (right multiplication by elements of $K$) distributes over addition, and $K$ is a skewfield, $W$ is a right vector space over $K$ in the natural way.
