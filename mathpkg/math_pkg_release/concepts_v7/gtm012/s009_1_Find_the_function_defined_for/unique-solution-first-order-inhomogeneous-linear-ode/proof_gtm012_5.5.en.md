---
role: proof
locale: en
of_concept: unique-solution-first-order-inhomogeneous-linear-ode
source_book: gtm012
source_chapter: "5"
source_section: "5"
---

# Proof of Unique Solution of First-Order Inhomogeneous Linear ODE

**Theorem 5.2.** For each $a, c \in \mathbb{C}$ and each continuous function $h: \mathbb{R} \to \mathbb{C}$ there is a unique continuously differentiable function $f: \mathbb{R} \to \mathbb{C}$ such that

$$f(0) = c, \quad f'(x) = a f(x) + h(x), \quad x \in \mathbb{R}. \tag{5.5}$$

**Proof.** Let

$$f_0(x) = E(ax), \quad g(x) = E(-ax).$$

As in the proof of Theorem 5.1, the product $f_0 g$ is constant:

$$(f_0 g)'(x) = a E(ax) E(-ax) + E(ax)(-a) E(-ax) = 0,$$

and $f_0(0) g(0) = 1$. Hence $f_0(x) g(x) \equiv 1$ for all $x \in \mathbb{R}$. In particular, neither $f_0$ nor $g$ ever vanishes.

Now suppose $f$ is any solution of (5.5). Write $f$ as

$$f = f_1 f_0, \quad \text{where} \quad f_1 = g f.$$

Differentiating,

$$f' = f_1' f_0 + f_1 f_0' = f_1' f_0 + f_1 (a f_0) = f_1' f_0 + a f.$$

Comparing with the differential equation $f' = a f + h$, we see that (5.5) holds if and only if

$$f_1' f_0 = h.$$

Since $f_0$ never vanishes, this is equivalent to

$$f_1'(x) = h(x) g(x) = E(-ax) h(x),$$

where we used $f_0(x) g(x) = 1$, i.e., $1/f_0(x) = g(x) = E(-ax)$. The initial condition $f(0) = c$ translates to $f_1(0) = g(0) f(0) = c$.

Therefore $f_1$ must satisfy

$$f_1(0) = c, \quad f_1'(x) = E(-ax) h(x).$$

Integrating,

$$f_1(x) = c + \int_0^x E(-a t) h(t) \, dt.$$

Substituting back, the unique solution of (5.5) is

$$f(x) = f_1(x) f_0(x) = c E(ax) + E(ax) \int_0^x E(-a t) h(t) \, dt. \tag{5.6}$$

This proves both existence and uniqueness. $\square$
