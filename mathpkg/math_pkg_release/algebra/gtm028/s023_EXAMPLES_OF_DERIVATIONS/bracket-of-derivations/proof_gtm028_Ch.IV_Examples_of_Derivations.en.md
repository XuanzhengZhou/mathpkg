---
role: proof
locale: en
of_concept: bracket-of-derivations
source_book: gtm028
source_chapter: "IV"
source_section: "Examples of Derivations"
---

Let $D$ and $D'$ be derivations of $K$ with values in $L$. Set $[D, D'] = D'D - DD'$.

The additive property is obvious since both $D$ and $D'$ are additive:
$$[D, D'](x + y) = D'(D(x+y)) - D(D'(x+y)) = D'(D(x) + D(y)) - D(D'(x) + D'(y))$$
$$= D'(D(x)) + D'(D(y)) - D(D'(x)) - D(D'(y)) = [D, D'](x) + [D, D'](y).$$

For the Leibniz rule, we compute:
$$\begin{aligned}
(D'D - DD')(xy) &= D'(D(xy)) - D(D'(xy)) \\
&= D'(x D(y) + y D(x)) - D(x D'(y) + y D'(x)) \\
&= D'(x D(y)) + D'(y D(x)) - D(x D'(y)) - D(y D'(x)).
\end{aligned}$$

Applying the Leibniz rule for each term:
$$\begin{aligned}
D'(x D(y)) &= x D'(D(y)) + D'(x) D(y), \\
D'(y D(x)) &= y D'(D(x)) + D'(y) D(x), \\
D(x D'(y)) &= x D(D'(y)) + D(x) D'(y), \\
D(y D'(x)) &= y D(D'(x)) + D(y) D'(x).
\end{aligned}$$

Substituting back, the cross terms cancel:
$$D'(x)D(y) + D'(y)D(x) - D(x)D'(y) - D(y)D'(x) = 0$$
since the sum is symmetric in $D$ and $D'$ with opposite signs. Thus
$$\begin{aligned}
(D'D - DD')(xy) &= x D'(D(y)) + y D'(D(x)) - x D(D'(y)) - y D(D'(x)) \\
&= x (D'D - DD')(y) + y (D'D - DD')(x),
\end{aligned}$$
which is exactly the Leibniz rule for $[D, D']$. Hence $[D, D']$ is a derivation of $K$.
