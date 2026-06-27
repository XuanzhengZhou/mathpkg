---
role: proof
locale: en
of_concept: corollary-6-10
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. Fix a point $a$ in $G$ and let $\gamma_1, \gamma_2$ be any two rect

g: $G \to \mathbb{C}$ such that $f(z) = \exp g(z)$. If $z_0 \in G$ and $e^{w_0} = f(z_0)$, we may choose $g$ such that $g(z_0) = w_0$.

Proof. Since $f$ never vanishes, $\frac{f'}{f}$ is analytic on $G$; so, by the preceding corollary, it must have a primitive $g_1$. If $h(z) = \exp g_1(z)$ then $h$ is analytic and never vanishes. So, $\frac{f}{h}$ is analytic and its derivative is

$$\frac{h(z)f'(z) - h'(z)f(z)}{h(z)^2}$$

But $h' = g_1'h$ so that $hf' - fh' = 0$. Hence $f/h$ is a constant $c$ for all $z$ in $G$. That is $f(z) = c \exp g_1(z) = \exp [g_1(z) + c']$ for some $c'$. By letting $g(z) = g_1(z) + c' + 2\pi ik$ for an appropriate $k$, $g(z_0) = w_0$ and the theorem is proved.

Let us emphasize that the hypothesis of simple connectedness is a topological one and this was used to obtain some basic results of analysis. Not only are these last three theorems (6.15, 6.16, and 6.17) consequences of simple connectivity, but they are equivalent to it. It will be shown in Chapter VIII that if a region $G$ has the conclusion of each of these theorems satisfied for every function analytic on $G$, then $G$ must be simply connected.

We close this section with a definition.
