---
role: proof
locale: en
of_concept: zero-finite-multiplicity
source_book: gtm011
source_chapter: "3"
source_section: "3.2"
---

Since $f$ is not identically zero, Theorem 3.7 implies that not all derivatives of $f$ vanish at $a$. Let $n$ be the smallest integer $\geq 1$ such that $f^{(n)}(a) \neq 0$. (Note that $f(a) = 0$ so $f^{(0)}(a) = 0$.) By the power series expansion of $f$ about $a$, for $z$ in a disk $B(a; R) \subset G$,

$$f(z) = \sum_{k=n}^{\infty} \frac{f^{(k)}(a)}{k!} (z-a)^k = (z-a)^n \sum_{k=0}^{\infty} \frac{f^{(n+k)}(a)}{(n+k)!} (z-a)^k.$$

Define

$$h(z) = \sum_{k=0}^{\infty} \frac{f^{(n+k)}(a)}{(n+k)!} (z-a)^k$$

for $z \in B(a; R)$. Then $h$ is analytic on $B(a; R)$ and $h(a) = f^{(n)}(a)/n! \neq 0$. For $z \neq a$ in $G$, define

$$g(z) = \frac{f(z)}{(z-a)^n},$$

and set $g(a) = h(a) = f^{(n)}(a)/n!$. Then $g$ is analytic on all of $G$ (it agrees with $h$ on $B(a; R)$ and is clearly analytic for $z \neq a$). Moreover, $g(a) \neq 0$ and $f(z) = (z-a)^n g(z)$ for all $z \in G$.
