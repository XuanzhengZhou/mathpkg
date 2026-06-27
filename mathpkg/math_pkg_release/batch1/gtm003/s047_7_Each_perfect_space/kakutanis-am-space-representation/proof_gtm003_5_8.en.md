---
role: proof
locale: en
of_concept: kakutanis-am-space-representation
source_book: gtm003
source_chapter: "V: Order Structures"
source_section: "8. Stone-Weierstrass and Representation Theorems"
---

Let $u$ be the unit of $E$. The positive face $H_0$ of $[-u, u]^\circ$ is convex and $\sigma(E', E)$-compact. By the Krein-Milman theorem, $H_0$ has extreme points; let $X$ be the set of extreme points of $H_0$. Then $X$ is non-empty, and in fact $H_0$ is the $\sigma(E', E)$-closed convex hull of $X$.

Since $H_0$ is $\sigma(E', E)$-compact, $X$ is $\sigma(E', E)$-compact as well (being the set of extreme points of a compact convex set in a locally convex space). The evaluation map $\Phi: E \to \mathcal{C}_{\mathbb{R}}(X)$ defined by $(\Phi(x))(t) = \langle x, t \rangle$ is a vector lattice homomorphism because each $t \in X$ is a positive linear functional.

To show $\Phi$ is an isometry, observe that for any $x \in E$, $\|x\| = p_u(x) = \inf\{\lambda > 0 : -\lambda u \leq x \leq \lambda u\}$. Since each $t \in H_0$ satisfies $\langle u, t \rangle = 1$ and is positive, we have $|\langle x, t \rangle| \leq \|x\|$ for all $t \in H_0$, hence for all $t \in X$. Conversely, for $x \geq 0$, there exists (by the Hahn-Banach theorem) $t \in H_0$ with $\langle x, t \rangle = \|x\|$, and by the Krein-Milman theorem such $t$ can be taken in $X$. Thus $\|\Phi(x)\|_{\infty} = \sup_{t \in X} |\langle x, t \rangle| = \|x\|$.

Surjectivity follows from the order-theoretic form of the Stone-Weierstrass theorem (8.1): the image $\Phi(E)$ is a vector sublattice of $\mathcal{C}_{\mathbb{R}}(X)$ containing the constant function $e$ and separating points in $X$ (by the definition of $X$ as extreme points). Hence $\Phi(E)$ is dense in $\mathcal{C}_{\mathbb{R}}(X)$, and since $E$ is a Banach space, $\Phi(E)$ is closed, so $\Phi(E) = \mathcal{C}_{\mathbb{R}}(X)$. Thus $\Phi$ is an isometric isomorphism of Banach lattices.
