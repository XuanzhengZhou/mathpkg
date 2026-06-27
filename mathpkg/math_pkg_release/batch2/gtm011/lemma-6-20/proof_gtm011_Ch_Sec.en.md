---
role: proof
locale: en
of_concept: lemma-6-20
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. Fix $[g]_a$ in $\mathcal{F}$ (so $(a, [g]_a) \in \mathcal{R}$); then, by hypothesis, $g(a) = \mathcal{F}(a, [g]_a) \in G$. If $b = f(g(a))$ then there is a disk $B$ about $b$ and an analytic function $h: B \to \mathbb{C}$ such that $h(b) = g(a)$ and $f(h(z)) = z$ for all $z$ in $B$. From Proposition 6.18, $[h]_b \in \mathcal{F}$. Also $a = \rho(a, [g]_a) \in \rho(\mathcal{R}) = f(G)$. According to Theorem 5.11 there is a path $\gamma$ in $f(G)$ from $a$ to $b$ such that $[h]_b$ is the continuation along $\gamma$ of $[g]_a$. Let $\{(g_t, D_t)\}$ be a continuation along $\gamma$ with each $D_t$ a disk such that $[g_0]_a = [g]_a$ and $[g_1]_b = [

$f(\zeta)): \zeta \in \Delta$ and define $\varphi: U \to \mathbb{C}$ by $\varphi(\zeta, f(\zeta)) = f(\zeta)$; so $(U, \varphi)$ is a coordinate patch on graph $(f)$ (Proposition 6.6). Also $N(f, D) = \{(z, [g]_z): z \in D\}$ gives that $(N(g, D), \rho)$ is a coordinate patch on $\mathcal{R}$ (Theorem 6.7) containing $(a, [g]_a)$, and satisfying $\tau(N(g, D)) \subset U$. Hence to complete the proof it must be shown that $\varphi \circ \tau \circ \rho^{-1}$ is an analytic function on $D$. This is trivial. In fact, if $z \in D$ then

$$\varphi \circ \tau \circ \rho^{-1}(z) = \varphi \circ \tau(z, [g]_z)$$

$$= \varphi(g(z), z)$$

$$= z;$$

that is, $\varphi \circ \tau \circ \rho^{-1}$ is the identity function on $D$.

If $G$ is the punctured plane and $f(z) = z^n$ for some $n$ or if $G = \mathbb{C}$ and $f(z) = e^z$ then the hypothesis of Proposition 6.19 is satisfied. Let us examine this a little more closely for the case where $f(z) = z^2$, $z \in G = \mathbb{C} - \{0\}$. So $\mathcal{R}$ is isomorphic to the graph of $z^2$; let $\Gamma = \{(z, z^2): z \neq 0\}$. Now $\tau: \mathcal{R} \to \Gamma$ is defined by $\tau(a, [g]_a) = (g(a), a)$. Recall that $\mathcal{F}: \mathcal{R} \to \mathbb{C}$ is defined by $\mathcal{F}(a, [g]_a) = g(a)$. For this case $\mathcal{F}$ acts like the square root function. In other words, we

Therefore, we would like to have a more geometric picture of the Riemann surface. Consider two copies of the plane that have been slit along the negative real axis. So imagine the planes as having two negative real axes and label them $*$ and $\sim$ as shown in the figure. The space $X$ we will describe will be the union of the two planes but where the two $*-axes$ are identified and the two $\sim$-axes are identified. So if a curve in Plane 1 approaches the $*-axis$ and hits it at $-x$ then it exits in Plane 2 at $-x$ on the $*-axis$. For the point $-1$ on the $*-axis$ a typical neighborhood would consist of a half disk about $-1$ above the $*-axis$ in Plane 1 and half a disk about $-1$ below the $*-axis$ in Plane 2. This is a representation of the Riemann surface of local inverses for $z^2$ (the Riemann surface of $\sqrt{z}$ for short). To see this define a map $k: X \to \mathbb{R}$ as follows. If $z$ is in Plane 1, $z$ not on the negative real axis, let $h(z) = (z, [g]_z)$ where $g$ is the principal branch of the square root. If $z$ is in Plane 2 but not on the negative real axis let $h(z) = (z, [g]_z)$ where $-g$ is the principal branch of the square root. It remains to define $h(z)$ for $z$ on the $*-axis$ and the $\sim$-axis. This we leave to the reader along with the proof that the resulting function $h$ is an isomorphism (the space $X$ has a natural analytic structure).

In the case $f(z) = z^n$ we can carry out the same construction, but here $n$ copies of the plane are required. If $f(z) = e^z$ the same ideas are again employed but now it is necessary to use an infinite number of planes indexed by all the integers. In the case of the surface for $z^{1/n}$, a curve which passes through the negative real axis of one plane exits through the negative real axis

2. Which of the following are analytic manifolds? What is its analytic structure if it is a manifold? (a) A cone in $\mathbb{R}^3$. (b) $\{(x_1, x_2, x_3) \in \mathbb{R}^3 : x_1^2 + x_2^2 + x_3^2 = 1$ or $x_1^2 + x_2^2 > 1$ and $x_3 = 0$}

3. The following is a generalization of Proposition 6.3(b). Let $(X, \Phi)$ be an analytic manifold, let $\Omega$ be a topological space, and suppose there is a continuous function $h$ of $X$ onto $\Omega$ that is locally one-one (that is, if $x \in X$ there is an open set $U$ such that $x \in U$ and $h$ is one-one on $U$). If $(U, \varphi) \in \Phi$ and $h$ is one-one on $U$ let $\Delta = h(U)$ and let $\psi : \Delta \to \mathbb{C}$ be defined by $\psi(\omega) = \varphi \circ (h/U)^{-1}(\omega)$. Let $\Psi$ be the collection of all such pairs $(\Delta, \psi)$. Prove that $(\Omega, \Psi)$ is an analytic manifold and $h$ is an analytic function from $X$ to $\Omega$.

4. Let $T = \{z : |z| = 1\} \times \{z : |z| = 1\}$; then $T$ is a torus. (This torus is homeomorphic to the usual hollow doughnut in $\mathbb{R}^3$.) If $\omega$ and $\omega'$ are complex numbers such that $\operatorname{Im}(\omega/\omega') \neq 0$ then $\omega$ and $\omega'$, considered as elements of the vector space $\mathbb{C}$ over $\mathbb{R}$, are linearly independent. So each $z$ in $\mathbb{C}$ can be uniquely represented as $z = t\omega + t'\omega'$; $t, t'$ in $\mathbb

(c) If $f$ is one-one, show that either $f(z) = az + b$ (some $a, b$ in $\mathbb{C}$) or $f(z) = \frac{a}{z - c} + b$ (some $a, b, c$ in $\mathbb{C}$).

8. Furnish the details of the discussion of the surface for $\sqrt{z}$ at the end of this section.

9. Let $G = \left\{ z : -\frac{\pi}{2} < \operatorname{Re} z < \frac{\pi}{2} \right\}$ and define $f: G \to \mathbb{C}$ by $f(z) = \sin z$. Give a discussion for $f$ similar to the discussion of $\sqrt{z}$ at the end of this section.

§7. Covering spaces

In this section the concept of a covering space will be introduced and some of its elementary properties will be deduced. One byproduct of this study is the fact that two closed curves in the punctured plane are homotopic iff they have the same winding number about the origin.

Intuitively, a topological space $X$ is a covering space for the topological space $\Omega$ if $X$ can be wrapped around $\Omega$ in such a way that it can be easily unwrapped. What is meant by “wrapping” one space around another? This seems to indicate that we want a function from $X$ onto $\Omega$. To say that it must be easily unwrapped must mean that we can find an inverse for the function.
