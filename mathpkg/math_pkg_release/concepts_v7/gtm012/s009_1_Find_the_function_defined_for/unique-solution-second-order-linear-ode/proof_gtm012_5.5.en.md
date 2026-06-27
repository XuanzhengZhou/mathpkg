---
role: proof
locale: en
of_concept: unique-solution-second-order-linear-ode
source_book: gtm012
source_chapter: "5"
source_section: "5"
---

# Proof of Unique Solution of Second-Order Linear ODE via Operator Factorization

**Theorem 5.3.** For any $b, c, d_0, d_1 \in \mathbb{C}$ and any continuous function $h: \mathbb{R} \to \mathbb{C}$ there is a unique function $f: \mathbb{R} \to \mathbb{C}$ of class $C^2$ satisfying

$$f(0) = d_0, \quad f'(0) = d_1, \tag{5.7}$$

$$f'' + b f' + c f = h. \tag{5.8}$$

**Proof.** Consider the characteristic polynomial $z^2 + b z + c$. Let $a_1, a_2 \in \mathbb{C}$ be its roots, so that

$$z^2 + b z + c = (z - a_1)(z - a_2),$$

which implies

$$b = -(a_1 + a_2), \quad c = a_1 a_2.$$

Introduce the differentiation operator $D$ and the identity operator $I$:

$$(D f)(x) = f'(x), \quad (I f)(x) = f(x).$$

From the properties of differentiation,

$$(D - a_1 I)[(D - a_2 I) f] = D^2 f - (a_1 + a_2) D f + a_1 a_2 f = f'' + b f' + c f.$$

Define the auxiliary function

$$g = f' - a_2 f = (D - a_2 I) f.$$

Then $f$ satisfies (5.8) if and only if

$$(D - a_1 I) g = g' - a_1 g = h.$$

If (5.7) also holds, then

$$g(0) = f'(0) - a_2 f(0) = d_1 - a_2 d_0.$$

Thus $f$ is a solution of the second-order problem (5.7)--(5.8) if and only if

$$f(0) = d_0, \quad f' - a_2 f = g, \tag{5.9}$$

where $g$ satisfies the first-order problem

$$g(0) = d_1 - a_2 d_0, \quad g' - a_1 g = h. \tag{5.10}$$

By Theorem 5.2 (with $a = a_1$, $c = d_1 - a_2 d_0$, and inhomogeneous term $h$), problem (5.10) has a unique solution $g$. Once $g$ is determined, problem (5.9) is again a first-order linear equation (with $a = a_2$, $c = d_0$, and inhomogeneous term $g$). By Theorem 5.2, (5.9) also has a unique solution $f$.

Therefore the original second-order problem (5.7)--(5.8) has a unique solution. $\square$
