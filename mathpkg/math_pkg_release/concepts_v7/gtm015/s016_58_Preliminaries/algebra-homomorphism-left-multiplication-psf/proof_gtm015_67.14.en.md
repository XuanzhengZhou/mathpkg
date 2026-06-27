---
role: proof
locale: en
of_concept: algebra-homomorphism-left-multiplication-psf
source_book: gtm015
source_chapter: "67"
source_section: "States and representations"
---

# Proof of Left multiplication defines an algebra homomorphism

Proof. If $a, b \in A$ then

$$T_{ab} x_\varphi = ((ab)x)_\varphi = (a(bx))_\varphi = T_a(bx)_\varphi = T_a(T_b x_\varphi) = (T_a T_b) x_\varphi$$

for all $x \in A$, therefore $T_{ab} = T_a T_b$. Similarly $T_{a+b} = T_a + T_b$ and $T_{\lambda a} = \lambda T_a$ for all $\lambda \in \mathbb{C}$.

The ‘adjoint relation’ (*) is the relation $\varphi(ax, y) = \varphi(x, a^*y)$ in disguise.

If $A$ has a unit element 1, it is obvious that $T_1 = I$. Also, $T_x 1_\varphi = (x1)_\varphi = x_\varphi$, thus

$$\left(T_x 1_\varphi | T_y 1_\varphi\right) = \left(x_\varphi | y_\varphi\right) = \varphi(x, y)$$

for all $x, y \in A$.

Suppose $\varphi$ is an adjunctive PSF on a $\ast$-algebra $A$.

for all $x \in A$, that is,

$$\varphi(ax, ax) \leq K_a \varphi(x, x)$$

for all $x \in A$. This prompts the following definition:
