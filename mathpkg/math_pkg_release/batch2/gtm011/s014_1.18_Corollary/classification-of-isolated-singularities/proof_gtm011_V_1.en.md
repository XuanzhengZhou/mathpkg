---
role: proof
locale: en
of_concept: classification-of-isolated-singularities
source_book: gtm011
source_chapter: "V"
source_section: "§1. Classification of Singularities"
---

**(a)** If $a_n = 0$ for $n \leq -1$, then define $g(z)$ in $B(a; R)$ by $g(z) = \sum_{n=0}^{\infty} a_n(z-a)^n$. The power series converges in the full disk $B(a; R)$, so $g$ is analytic there and agrees with $f$ in the punctured disk $B(a; R) \setminus \{a\}$. Hence $f$ has a removable singularity at $z = a$. Conversely, if $z = a$ is a removable singularity, then $f$ extends analytically to $a$, and its Laurent expansion must coincide with its Taylor expansion, so all negative-index coefficients vanish.

**(b)** Suppose $a_n = 0$ for $n \leq -(m+1)$. Then $(z-a)^m f(z)$ has a Laurent Expansion

$$(z-a)^m f(z) = \sum_{n=-m}^{\infty} a_n (z-a)^{n+m} = \sum_{k=0}^{\infty} a_{k-m} (z-a)^k,$$

which contains no negative powers of $(z-a)$. By part (a), $(z-a)^m f(z)$ has a removable singularity at $z = a$. Moreover, $a_{-m} \neq 0$ ensures that the extended function does not vanish at $a$, so $f$ has a pole of order $m$ at $z = a$. The converse follows by retracing the steps: if $f$ has a pole of order $m$, then $(z-a)^m f(z)$ has a removable singularity with non-zero value at $a$, so $a_n = 0$ for $n \leq -(m+1)$ and $a_{-m} \neq 0$.

**(c)** By definition, $f$ has an essential singularity at $z = a$ precisely when it has neither a removable singularity nor a pole. Therefore $z = a$ is an essential singularity iff it is not the case that all but finitely many negative-index coefficients are zero --- that is, iff $a_n \neq 0$ for infinitely many negative integers $n$.
