---
role: proof
locale: en
of_concept: kernel-of-weak-quasifield-is-skewfield
source_book: gtm006
source_chapter: "VII"
source_section: "2"
---

**Proof.** Let $a, b$ be any two elements of $W$ and $h, k$ be any elements of $K$.

First we show $K$ is closed under subtraction. Using the left distributive law (valid in $W$) and Lemma 7.1:

\begin{align*}
(a + b)(h - k) &= (a + b)h + (a + b)(-k) \\
&= (a + b)h - (a + b)k \quad \text{(by Lemma 7.1)} \\
&= ah + bh - ak - bk \quad \text{(since $h, k$ distribute on the right)} \\
&= ah - ak + bh - bk \quad \text{(since addition is abelian)} \\
&= a(h - k) + b(h - k) \quad \text{(using left distributive law and Lemma 7.1)}.
\end{align*}

\begin{align*}
(ab)(h - k) &= (ab)h - (ab)k \quad \text{(by Lemma 7.1 and the left distributive law)} \\
&= a(bh) - a(bk) \quad \text{(since $h, k$ associate on the right)} \\
&= a(bh - bk) \quad \text{(using left distributive law)} \\
&= a(b(h - k)) \quad \text{(by Lemma 7.1 and the left distributive law)}.
\end{align*}

Hence $K$ is closed under subtraction and is non-empty ($0$ and $1$ are in $K$), so $(K, +)$ is an (abelian) subgroup of $(W, +)$.

We must now show that $(K^*, \cdot)$ is a group. Clearly, from the definition of $K$, multiplication in $K$ is associative and $1 \in K$, so we must show that $K$ is closed under multiplication and that every non-zero element of $K$ has an inverse in $K$.

For closure under multiplication: let $h, k \in K$. Then for all $x, y \in W$:
$$(x + y)(hk) = ((x + y)h)k = (xh + yh)k = (xh)k + (yh)k = x(hk) + y(hk),$$
using first the right-associativity of $k$, then right-distributivity of $h$, then right-distributivity of $k$, then right-associativity of $k$. Similarly,
$$(xy)(hk) = ((xy)h)k = (x(yh))k = x((yh)k) = x(y(hk)).$$
Thus $hk \in K$ and $K$ is closed under multiplication.

For inverses: if $k \in K^*$, the equation $kx = 1$ has a unique solution $x \in W$ (since $W^*$ is a loop). One then verifies that this $x$ satisfies the kernel axioms (i) and (ii), showing $x \in K$, so $k^{-1} \in K$.

Thus $(K, +, \cdot)$ is a skewfield. The right vector space structure of $W$ over $K$ is given by the multiplication in $W$: for $w \in W$ and $k \in K$, define $w \cdot k = wk$. The vector space axioms follow from the kernel properties and the fact that $(W, +)$ is an abelian group.