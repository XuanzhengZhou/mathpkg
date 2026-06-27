---
role: proof
locale: en
of_concept: convolution-distribution-smooth-properties
source_book: gtm012
source_chapter: "7"
source_section: "7. Convolution of distributions"
---

# Proof of Properties of Convolution of a Distribution with a Smooth Function

**Proposition 7.1.** If $F$ is a periodic distribution and $u$ is a smooth periodic function, then the function $F * u$ defined by

$$(F * u)(x) = F(T_x \tilde{u})$$

is a smooth periodic function. Moreover,

$$(aF) * u = a(F * u) = F * (au), \quad F \in \mathcal{P}', u \in \mathcal{P}, a \in \mathbb{C}; \tag{2}$$

$$(F + G) * u = F * u + G * u, \quad F, G \in \mathcal{P}', u \in \mathcal{P}; \tag{3}$$

$$F * (u + v) = F * u + F * v, \quad F \in \mathcal{P}', u, v \in \mathcal{P}. \tag{4}$$

*Proof.* First we establish the translation property

$$T_t(F * u) = (T_t F) * u = F * (T_t u). \tag{5}$$

Indeed,

$$T_t(F * u)(x) = (F * u)(x - t) = F(T_{x-t} \tilde{u}) = F(T_x(T_t u)^\sim) = (F * (T_t u))(x).$$

On the other hand,

$$T_t(F * u)(x) = F(T_{x-t} \tilde{u}) = (T_t F)(T_x \tilde{u}) = ((T_t F) * u)(x).$$

This proves (5). It follows that

$$(F * u)(x + 2\pi) = (F * (T_{2\pi} u))(x) = (F * u)(x),$$

so $F * u$ is periodic.

We know that

$$t^{-1}[T_{-t} F - F] \to DF \quad (\mathcal{P}') \text{ as } t \to 0.$$

Therefore

$$t^{-1}[(F * u)(x + t) - (F * u)(x)] = t^{-1}[T_{-t}(F * u)(x) - (F * u)(x)]$$

$$= t^{-1}[T_{-t} F - F](T_x \tilde{u}) \to DF(T_x \tilde{u}) = ((DF) * u)(x).$$

This shows that $F * u$ is differentiable at each point $x \in \mathbb{R}$, with derivative $(DF) * u(x)$. By induction, $D^k(F * u) = (D^k F) * u$. Thus $F * u \in \mathcal{P}$.

Finally, using (5) again,

$$t^{-1}[(F * u)(x + t) - (F * u)(x)] = F * [t^{-1}(T_{-t} u - u)](x)$$

$$= F(T_x [t^{-1}(T_{-t} u - u)]^\sim) \to F(T_x (Du)^\sim) = (F * (Du))(x).$$

By induction, $D^k(F * u) = F * (D^k u)$ for all $k$.

We leave the proofs of (2), (3), (4) as an exercise. $\square$
