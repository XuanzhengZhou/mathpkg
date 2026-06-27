---
role: proof
locale: en
of_concept: existence-and-uniqueness-of-sine-and-cosine
source_book: gtm012
source_chapter: "6"
source_section: "6. Trigonometric functions and the logarithm"
---

# Proof of Existence and Uniqueness of Sine and Cosine Functions

**Theorem 6.1.** There exist unique functions $S, C: \mathbb{R} \to \mathbb{C}$ of class $C^2$ such that

$$S(0) = 0, \quad S'(0) = 1, \quad S'' + S = 0,$$

$$C(0) = 1, \quad C'(0) = 0, \quad C'' + C = 0.$$

*Proof.* Existence and uniqueness of such functions is a consequence of Theorem 5.3.

Let us obtain expressions for $S$ and $C$ using the method of Theorem 5.3. The roots of $z^2 + 1$ are $z = \pm i$. Therefore

$$S(x) = \int_0^x e^{-i(x-t)} g(t) \, dt$$

where

$$g(x) = e^{ix}.$$

Thus

$$S(x) = \int_0^x e^{-i(x-t)} e^{it} \, dt = e^{-ix} \int_0^x e^{2it} \, dt$$

$$= e^{-ix} (2i)^{-1} \big[ e^{2it} \big]_{t=0}^{t=x} = e^{-ix} (2i)^{-1} (e^{2ix} - 1)$$

$$= (2i)^{-1} (e^{ix} - e^{-ix}) = \sin x.$$

Similarly, for $C$ we use the second root $-i$ and the appropriate initial conditions to obtain

$$C(x) = \frac{1}{2} (e^{ix} + e^{-ix}) = \cos x.$$

These integral representations show that $S$ and $C$ are well-defined $C^2$ (in fact $C^\infty$) functions satisfying the required differential equations and initial conditions. Uniqueness follows from the general theory of linear differential equations (Theorem 5.3), which guarantees that a solution to $f'' + f = 0$ is uniquely determined by the values $f(0)$ and $f'(0)$. $\square$
