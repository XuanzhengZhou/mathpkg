---
role: proof
locale: en
of_concept: theorem-9-5-existence-andre-quasifield
source_book: gtm006
source_chapter: "IX"
source_section: "3"
---

By Lemma 9.4, $F_{\phi}$ is a field if and only if $k^{\phi} = \varepsilon$ for all $k \in N$. Thus to construct a non-field André quasifield, we need a mapping $\phi$ from some subfield $K$ of $F$, $K \neq F$, into the integers modulo $m$ (where $m = [F : K]$ is the dimension of $F$ over $K$) such that some element of $K$ other than $0$ or $1$ is mapped to something other than $0$.

**Case (a): $p$ odd and $n \geq 2$.** Choose $K = GF(p)$. Then $[F : K] = n$. Define $\phi$ by sending $-1 \in K^*$ to $1 \in \mathbb{Z}_n$. Since $-1 \neq 1$ in $GF(p)$ when $p$ is odd, this gives a non-trivial map, producing a proper André quasifield.

**Case (b): $p = 2$ and $n$ composite.** If $n$ is prime, then $GF(2)$ is the only proper subfield of $F$, and $\phi$ is completely determined on $GF(2)^* = \{1\}$ by $1^{\phi} = 0$, forcing $F_{\phi}$ to be a field. If $n$ is not prime, there exists a proper intermediate field $GF(2^m)$ with $1 < m < n$ dividing $n$. Let $K = GF(2^m)$; then $K^*$ contains a non-identity element which we can map to $1$ in $\mathbb{Z}_{n/m}$, yielding a non-field André quasifield.

**Case: $p$ odd and $n = 1$.** Then $F = GF(p)$ and the only subfield is $F$ itself. By Lemma 9.4, any André quasifield is isomorphic to $F$, hence a field. Similarly, if $p = 2$ and $n = 1$ or $n$ is an odd prime, no proper non-trivial André quasifields exist.

Thus the stated conditions are both necessary and sufficient.
