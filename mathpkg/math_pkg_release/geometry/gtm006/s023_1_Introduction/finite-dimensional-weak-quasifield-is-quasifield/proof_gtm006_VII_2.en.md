---
role: proof
locale: en
of_concept: finite-dimensional-weak-quasifield-is-quasifield
source_book: gtm006
source_chapter: "VII"
source_section: "2"
---

**Proof.** We must show that given any $a, b, c \in W$, $a \neq b$, the equation $ax = bx + c$ has a unique solution for $x$.

For any $a \in W$ define a mapping $L_a$ of $W$ onto itself by $xL_a = ax$; i.e., $L_a$ is left multiplication by $a$. Since $W$ satisfies the left distributive law,
$$(x + y)L_a = ax + ay = xL_a + yL_a.$$
Furthermore, for any $h \in H$,
$$(xh)L_a = a(xh) = (ax)h = (xL_a)h,$$
using the fact that $H \subseteq K$ and elements of $K$ associate on the right. Thus $L_a$ is a linear transformation of $W$ over $H$ and, since $W^*$ is a multiplicative loop, $L_a$ is non-singular unless $a = 0$.

We must show that $xL_a = xL_b + c$ has a unique solution for $x$ given any $a, b, c$ with $a \neq b$; this is equivalent to showing
$$x(L_a - L_b) = c$$
has a unique solution for $x$. Clearly, since $W$ has finite dimension over $H$, $x(L_a - L_b) = c$ has a unique solution if and only if $L_a - L_b$ is non-singular.

If $L_a - L_b$ is singular then there exists $w \neq 0$ such that $w(L_a - L_b) = 0$. But this implies $aw - bw = 0$ or $aw = bw$, and thus, since $W^*$ is a loop and left cancellation holds (Theorem 6.4), we obtain $a = b$; a contradiction. Hence $L_a - L_b$ is non-singular, and the unique solution exists. Therefore $W$ satisfies axiom (5) of a quasifield and is a quasifield.