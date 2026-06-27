---
role: proof
locale: en
of_concept: local-pairing-independence-lemma
source_book: gtm059
source_chapter: "9"
source_section: "9"
---

We have:
\begin{align*}
[x_n, x_n] &\equiv [x_n, N x_n] \pmod{n^{1+k}} \\
&= \frac{1}{2} T_k(x_n)(x_n(N x_n)) \pmod{n^{1+k}} \\
&= \frac{1}{2} T_k(x_n)(x_n(N x_n)) \pmod{n} \\
&= \frac{1}{2} T_k(x_n)(x_n(N x_n)).
\end{align*}

By the definition of the trace map $T$ and the orthogonality relations, the value is independent of the choice of $m$ within the specified ranges. The two cases (i) and (ii) correspond to different bounds on $m$ required for the integrality estimates to hold via congruences C.1 and C.3.

We remark that in the range where the symbol is well defined, it is $x_n$-linear in $n$ and multiplicative in $n$. In any case, within the ranges of Lemma 1, we view the symbol as having values in

$$K \bmod n^{1+k} x_n.$$

The lemma shows that the value $[x, x_n]$ is independent of $m$ when $x_n$ is the component of an infinite vector

$$x = (x_0, \dots, x_{n-1}) \cdot (T/K) x$$

and $m$ is sufficiently large. We define $[x]$ to be this value.
