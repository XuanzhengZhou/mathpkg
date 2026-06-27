---
role: proof
locale: en
of_concept: existence-of-nonfield-andre-quasifields
source_book: gtm006
source_chapter: "IX"
source_section: "3"
---

In view of Lemma 9.4, it suffices to find a mapping $\phi$ from some subfield $K$ of $F$, $K \neq F$, into $\mathbb{Z}_m$ (where $m = [F:K]$) such that some element of $K$ other than $0$ or $1$ is mapped to a non-zero element.

(a) If $p$ is odd and $n \geq 2$: Choose $K = \mathrm{GF}(p)$. The Galois group is $\mathbb{Z}_n$. Send $-1 \in K^*$ to $1 \in \mathbb{Z}_n$ (which is non-zero since $n \geq 2$). This defines a non-trivial $\phi$, yielding a non-field André quasifield.

(b) If $p = 2$ and $n$ is prime: The only proper subfield of $\mathrm{GF}(2^n)$ is $\mathrm{GF}(2)$. The trivial group forces $\phi(1) = 0$ in $\mathbb{Z}_n$, so $F_\phi$ is a field. Thus no non-trivial André quasifield exists.

If $p = 2$ and $n$ is composite: Write $n = rs$ with $r > 1, s > 1$. Then $\mathrm{GF}(2^r)$ is a proper subfield strictly between $\mathrm{GF}(2)$ and $\mathrm{GF}(2^n)$. Choose $K = \mathrm{GF}(2^r)$. Then $K^*$ contains a non-identity element which we map to $1$ in $\mathbb{Z}_{s}$. This yields a non-field André quasifield. $\square$
