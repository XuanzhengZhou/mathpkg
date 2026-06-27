---
role: proof
locale: en
of_concept: proposition-6-6
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. Since $\Gamma$ is homeomorphic to $G$ it must be connected. Fix $\alpha = (a, f(a))$ in $\Gamma$; it is left to the reader to show that $\varphi_\alpha$ is a homeomorphism of $U_\alpha$ onto $f(D_a)$. Suppose that $\beta = (b, f(b)) \in \Gamma$ with $U_\alpha \cap U_\beta \neq \emptyset$ and compute $\varphi_\alpha \circ \varphi_\beta^{-1}$. Since $f: D_b \to \mathbb{C}$ is one-one there is an analytic function $g: \Omega \to D_b$, where $\Omega = f(D_b)$, such that $f(g(\omega)) = \omega$ for all $\omega$ in $\Omega$. Since $\varphi_\beta(U_\beta) = \Omega$

The function is analytic on $X$ if it is analytic at each point of $X$.

The condition that $(U, \varphi)$ can be found such that $a \in U$ and $f(U) \subset \Lambda$ is a consequence of the continuity of $f$ (Proposition 4.9(c)). The heart of the definition is the requirement that $\psi \circ f \circ \varphi^{-1}$ be an analytic function from $\varphi(U) \subset \mathbb{C}$ into $\mathbb{C}$.

For two given analytic surfaces there may be many analytic functions from one to the other or there may be very few. Clearly every constant function is analytic; but there may be no other analytic functions. For example, if $X = \mathbb{C}$ and $\Omega$ is a bounded region in the plane then Liouville’s Theorem implies there are no non-constant analytic functions from $X$ into $\Omega$. Also, suppose that $f: \mathbb{C}_{\infty} \to \mathbb{C}$ is an analytic function; then $f(\mathbb{C}_{\infty})$ is compact so that the restriction of $f$ to $\mathbb{C}$ is a bounded analytic function on $\mathbb{C}$. Again, Liouville’s Theorem says that each such $f$ is a constant function. On the other hand, if $p$ is a polynomial and $a \in \mathbb{C}$ then both $p(z)$ and $p\left(\frac{1}{z-a}\right)$ are analytic functions from $\mathbb{C}_{\infty}$ to $\mathbb{C}_{\infty}$. In fact, these are practically the only analytic functions from $\mathbb{C}_{\infty}$ to $\mathbb{C}_{\infty}$ (Exercise 7).

If $(X, \Phi)$ is an analytic surface then there are many analytic functions defined on open subsets of $X$. For example, if $(U, \varphi) \in \Phi$ then $\varphi: U \to \mathbb{C}$ is analytic. It follows (Proposition 6.10 below) that $f \circ \varphi: U \to \mathbb{C}$ is analytic for any analytic function $f: \varphi(U)

analytic functions from $X$ into $\Omega$. If $\{x \in X : f(x) = g(x)\}$ has a limit point in $X$ then $f = g$.

Proof. Define the subset $A$ of $X$ by

$$A = \{x : f \text{ and } g \text{ agree on a neighborhood of } x\}.$$

This set $A$ will be shown to be non-empty and the reader will be required to prove that $A$ is both open and closed in $X$. By hypothesis there is a point $a$ in $X$ such that for every neighborhood $U$ of $a$ there is a point $x$ in $U$ with $x \neq a$ and $f(x) = g(x)$. It is easy to conclude that $f(a) = g(a) = \alpha$. If $(\Lambda, \psi) \in \Psi$ and $\alpha \in \Lambda$ then there is a patch $(U, \varphi)$ in $\Phi$ such that $f(U)$ and $g(U)$ are contained in $\Lambda$ with both $\psi \circ f \circ \varphi^{-1}$ and $\psi \circ g \circ \varphi^{-1}$ analytic in a disk $D$ about $z_0 = \varphi(\alpha)$. But the hypothesis gives that $z_0$ is a limit point of $\{z \in D : \psi \circ f \circ \varphi^{-1}(z) = \psi \circ g \circ \varphi^{-1}(z)\} = F$. In fact, if $f(x) = g(x)$ then $\varphi(x) \in F$. Thus $\psi \circ f \circ \varphi^{-1}(z) = \psi \circ g \circ \varphi^{-1}(z)$ for all $z$ in $D$; or $f(x) = g(x)$ for all $x$ in $U \cap \varphi^{-1}(D)$. Hence $a \in A$ and $A \neq \square$.

6.12 Maximum Modulus Theorem. Let $(X, \Phi)$ be an analytic manifold and let $f: X \to \mathbb{C}$ be an analytic function.

Recall that the Riemann Mapping Theorem states that if $G$ is a simply connected region in the plane and $G \neq \mathbb{C}$, then $G$ is isomorphic to the open unit disk if both are considered as analytic surfaces. Also recall that Proposition 6.3(b) states that if $(X, \Phi)$ is an analytic manifold and $h: X \to \Omega$ is a homeomorphism of $X$ onto the topological space $\Omega$, then $h$ induces an analytic structure on $\Omega$; denote this structure by $\Phi \circ h^{-1}$. Suppose $\Omega$ already has an analytic structure $\Psi$. It is easy to see that $\Phi \circ h^{-1} = \Psi$ iff $h$ is analytic; that is, iff $h$ is an isomorphism from $(X, \Phi)$ onto $(\Omega, \Psi)$.

As an example let $X = \mathbb{C}$ and $\Omega = \{z: |z| < 1\}$, and define $h: X \to \Omega$ by

$$h(z) = \frac{z}{1 + |z|}.$$

Then $h$ is a homeomorphism of $\mathbb{C}$ onto $\Omega$, but it is clearly not analytic. So using $h$ and the analytic structure on $\mathbb{C}$, a structure can be induced on $\Omega$ which is completely unrelated to its natural structure. For example, with this induced structure $\Omega$ will have no bounded non-constant analytic functions.

Consider the following situation: let $G$ be a region in the plane and let $f: G \to \mathbb{C}$ be an analytic function with non-vanishing derivative. Let $(g, D)$ be a function element such that $g(D) \subset G$ and $f(g(z)) = z$ for all $z$ in $D$. (That is, $g$ is a "local" inverse of $f$.) If $\mathcal{F}$ is the complete analytic function obtained from $(g, D)$ and $(\mathcal{R}, \rho)$ is its Riemann surface, let us examine whether $\mathcal{R

about $\alpha$ and $\beta$ respectively such that there are analytic functions $g_0: \Delta_0 \to \mathbb{C}$ and $g_1: \Delta_1 \to \mathbb{C}$ with $g_0(\alpha) = a, g_1(\beta) = b, f(g_0(\zeta)) = \zeta$ for all $\zeta$ in $\Delta_0$, $f(g_1(\zeta)) = \zeta$ for all $\zeta$ in $\Delta_1$. Then there is a path $\sigma$ in $f(G)$ from $\alpha$ to $\beta$ such that $(g_1, \Delta_1)$ is the continuation of $(g_0, \Delta_0)$ along $\sigma$.

Proof. Since $G$ is connected there is a path $\gamma$ in $G$ from $a$ to $b$. For $0 \leq t \leq 1$ let $D_t$ be a disk about $\gamma(t)$ such that $D_t \subset G$ and on which $f$ is one-one. Let $\sigma = f \circ \gamma$ and let $\Delta_t$ be a disk about $\sigma(t)$ such that $\Delta_t \subset f(D_t)$. Finally, let $g_t: \Delta_t \to \mathbb{C}$ be an analytic function such that

$$f(g_t(\zeta)) = \zeta \text{ for } \zeta \text{ in } \Delta_t$$

$$g_t(\sigma(t)) = \gamma(t)$$

Claim. $\{(g_t, \Delta_t)\}$ is an analytic continuation along $\sigma$. To show this fix $t$ and let $\delta$ be chosen so that $\gamma(s) \in f^{-1}(\Delta_t) \cap D_t$ whenever $|s-t| < \delta$. Now fix $s$ with $|s-t| < \delta$ and let $B$ be a disk about $\gamma(s)$ such that $B \subset f^{-1}(\Delta_t) \cap D_s \cap D_t$. So $f(B)$ is an open set containing $\sigma(s) = f(\gamma(s))$ and $f(B) \subset f(D_t)$. By definition $g_s(f(z

of $f$, and let $(\mathcal{R}, \rho)$ be the Riemann surface of $\mathcal{F}$. If $\mathcal{F}(\mathcal{R}) = G$ and $\rho(\mathcal{R}) = f(G)$ then

$$\tau(z, [g]_z) = (g(z), z)$$

defines an isomorphism between the analytic manifold $\mathcal{R}$ and graph $(f)$.

Before proving this proposition we must show that under the same hypothesis each member of $\mathcal{F}$ is a local inverse of $f$. This provides a partial converse to Proposition 6.18.
