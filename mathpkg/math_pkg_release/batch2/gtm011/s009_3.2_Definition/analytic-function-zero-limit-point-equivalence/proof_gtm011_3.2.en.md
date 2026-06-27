---
role: proof
locale: en
of_concept: analytic-function-zero-limit-point-equivalence
source_book: gtm011
source_chapter: "3"
source_section: "3.2"
---

Clearly (a) implies both (b) and (c).

**(b) ⇒ (a).** Let $A = \{ z \in G : f^{(n)}(z) = 0 \text{ for all } n \geq 0 \}$. By hypothesis, $a \in A$ so $A \neq \varnothing$. We show $A$ is both open and closed in $G$; by the connectedness of $G$ it will follow that $A = G$ and so $f \equiv 0$.

To see that $A$ is closed, let $z \in A^{-}$ (the closure of $A$ in $G$) and let $z_k$ be a sequence in $A$ such that $z = \lim z_k$. Since each $f^{(n)}$ is continuous, it follows that $f^{(n)}(z) = \lim f^{(n)}(z_k) = 0$. So $z \in A$ and $A$ is closed.

To see that $A$ is open, let $a \in A$ and let $R > 0$ be such that $B(a; R) \subset G$. Then

$$f(z) = \sum_{n=0}^{\infty} a_n (z-a)^n \quad \text{for } |z-a| < R,$$

where $a_n = \frac{1}{n!} f^{(n)}(a) = 0$ for each $n \geq 0$. Hence $f(z) = 0$ for all $z$ in $B(a; R)$ and, consequently, $f^{(n)}(z) = 0$ for all $n$ and all $z \in B(a; R)$. Thus $B(a; R) \subset A$ and $A$ is open.

**(c) ⇒ (a).** Let $a \in G$ be a limit point of $\{ z \in G : f(z) = 0 \}$. By continuity, $f(a) = 0$. Suppose, for contradiction, that $f$ is not identically zero. Then not all derivatives of $f$ vanish at $a$, for otherwise $a \in A$ and by the argument above $f \equiv 0$. Let $m \geq 1$ be the smallest integer such that $f^{(m)}(a) \neq 0$. By the power series expansion of $f$ about $a$,

$$f(z) = \sum_{n=m}^{\infty} \frac{f^{(n)}(a)}{n!} (z-a)^n = (z-a)^m \, g(z),$$

where

$$g(z) = \sum_{k=0}^{\infty} \frac{f^{(m+k)}(a)}{(m+k)!} (z-a)^k$$

is analytic on $B(a; R)$ for some $R > 0$ and satisfies $g(a) = f^{(m)}(a)/m! \neq 0$. By continuity of $g$, there exists $\delta > 0$ such that $g(z) \neq 0$ for $|z-a| < \delta$. Then $f(z) = (z-a)^m g(z) \neq 0$ for $0 < |z-a| < \delta$, which contradicts the assumption that $a$ is a limit point of the zero set of $f$. Hence $f \equiv 0$.

This completes the proof of the theorem.
