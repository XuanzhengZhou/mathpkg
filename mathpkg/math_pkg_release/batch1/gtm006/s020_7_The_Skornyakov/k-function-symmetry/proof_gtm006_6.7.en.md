---
role: proof
locale: en
of_concept: k-function-alternating-under-permutation
source_book: gtm006
source_chapter: "6"
source_section: "7. The Skornyakov-San Soucie Theorem"
---

Consider the cyclic permutation $\beta$ with $w^\beta = x$, $x^\beta = y$, $y^\beta = z$, $z^\beta = w$. Then
$$\begin{aligned}
&k(w, x, y, z) - k(x, y, z, w) + k(y, z, w, x) \\
&= [wx, y, z] - [x, y, z]w - x[w, y, z] \\
&\quad - [xy, z, w] + [y, z, w]x + y[x, z, w] \\
&\quad + [yz, w, x] - [z, w, x]y - z[y, w, x].
\end{aligned}$$

By (3) the function $f$ is identically zero in any non-associative ring. Incorporating the first, fourth, and seventh terms into $f(w, x, y, z)$ and rearranging by (18) where necessary, the expression vanishes. This shows $k(w, x, y, z) = k(x, y, z, w) = k(y, z, w, x)$, i.e., invariance under the 3-cycle $\beta$ with sign $+1$.

Also by (18),
$$\begin{aligned}
k(w, x, y, z) &= [wx, y, z] - [x, y, z]w - x[w, y, z] \\
&= -[wx, z, y] + [x, z, y]w + x[w, z, y] \\
&= -k(w, x, z, y).
\end{aligned}$$

Thus for the transposition $\gamma = (y\;z)$ (with $\operatorname{sgn} \gamma = -1$), we have $k(w, x, y, z) = (\operatorname{sgn} \gamma) k(w, x, z, y)$. Since $\langle \beta, \gamma \rangle = S_4$, the full symmetric group on $\{w, x, y, z\}$, the alternating property holds for all permutations. $\square$
