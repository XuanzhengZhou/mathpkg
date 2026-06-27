---
role: proof
locale: en
of_concept: theorem-2-2-regular-interval-theorem
source_book: gtm033
source_chapter: "6"
source_section: "2"
---

# Proof of Regular Interval Theorem

Give $M$ a Riemannian metric. Consider the $C^r$ vector field on $M$:

$$X(x) = \frac{\operatorname{grad} f(x)}{\|\operatorname{grad} f(x)\|^2}.$$

Notice that $X(x)$ has the same trajectories as $\operatorname{grad} f$ but with a different parametrization.

Let $\eta: [t_0, t_1] \rightarrow M$ be a solution curve of $X$. A computation shows that the derivative of the map

$$[t_0, t_1] \rightarrow \mathbb{R}, \quad t \mapsto f(\eta(t))$$

is identically $1$. Indeed,

$$\frac{d}{dt} f(\eta(t)) = \langle \operatorname{grad} f(\eta(t)), \eta'(t) \rangle = \langle \operatorname{grad} f(\eta(t)), X(\eta(t)) \rangle = \frac{\langle \operatorname{grad} f, \operatorname{grad} f \rangle}{\|\operatorname{grad} f\|^2} = 1.$$

This means that

$$f(\eta(t_1)) - f(\eta(t_0)) = t_1 - t_0. \tag{1}$$

Let $x \in f^{-1}(s)$. Since $M$ is compact, the set $J(x)$ (the maximal interval of definition of the integral curve through $x$) is closed. From (1) it follows that

$$J(x) = [a - s, b - s]. \tag{2}$$

The assumptions on $f$ imply that $f^{-1}(a)$ is a union of boundary components of $M$. (Since $f$ maps $\partial M$ to $\{a, b\}$ and has no critical points, the gradient flow lines starting at $f^{-1}(a)$ run across the manifold to $f^{-1}(b)$.)

Define a map

$$F: f^{-1}(a) \times [a, b] \rightarrow M,$$

$$F(x, t) = \eta(t - a, x).$$

By (2), for each $x \in f^{-1}(a)$, the integral curve through $x$ is defined on $[a - a, b - a] = [0, b - a]$, so $F$ is well-defined. The map $F$ is $C^r$ since the flow $\eta$ is $C^r$.

The map $F$ is a diffeomorphism because:
- It is injective: if $\eta(t-a, x) = \eta(s-a, y)$, then applying $f$ to both sides gives $t = s$ by (1), and then injectivity of the flow gives $x = y$.
- It is surjective: for any $y \in M$, let $s = f(y)$. By (2), the integral curve through $y$ extends back to $f^{-1}(a)$; let $x = \eta(a - s, y) \in f^{-1}(a)$. Then $F(x, s) = \eta(s - a, x) = \eta(s - a, \eta(a - s, y)) = \eta_0(y) = y$.
- The inverse, given by $y \mapsto (\eta(a - f(y), y), f(y))$, is also $C^r$.

The diagram

$$\begin{array}{ccc}
f^{-1}(a) \times [a, b] & \xrightarrow{F} & M \\
& \searrow{\pi_2} & \downarrow{\scriptstyle f} \\
& & [a, b]
\end{array}$$

commutes because $f(F(x, t)) = f(\eta(t-a, x)) = f(x) + (t-a) = a + (t-a) = t$ by (1).

In particular, for any $s \in [a, b]$, the restriction $F|_{f^{-1}(a) \times \{s\}}$ is a diffeomorphism onto $f^{-1}(s)$, so all level surfaces of $f$ are diffeomorphic.
