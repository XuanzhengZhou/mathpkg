---
role: proof
locale: en
of_concept: thom-homomorphism
source_book: gtm033
source_chapter: "7"
source_section: "2"
---

# Proof of the Thom Homomorphism

Let $\xi = (p, E, B)$ be a vector bundle over a compact manifold $B$ without boundary. The one-point compactification of $E$ is denoted by $E^* = E \cup \{\infty\}$. Fix $s > n+k$ and let $E = E_{s,k}$, $G = G_{s,k}$ be the Grassmann $k$-plane bundle over $\mathbb{R}^s$, with $E^* = E^*_{s,k}$ its one-point compactification.

**Theorem (Thom Homomorphism).** Define $\tau: \pi_{n+k}(E^*) \to \mathfrak{N}^n$ as follows: given a homotopy class $\alpha \in \pi_{n+k}(E^*)$, represent $\alpha$ by a map $f: S^{n+k} \to E^*$ which is transverse to $G$ (always possible by a small homotopy). Set

$$\tau(\alpha) = [f^{-1}(G)],$$

the cobordism class of the inverse image of the Grassmann manifold. Then:
(a) $\tau$ is well-defined, independent of the choice of representative.
(b) $\tau$ is a group homomorphism.
(c) $\tau$ is surjective if $k > n$ and $s \geqslant k+n$.
(d) $\tau$ is bijective if $k > n+1$ and $s \geqslant k+n+1$.

There is an analogous oriented Thom homomorphism $\tilde{\tau}: \pi_{n+k}(\tilde{E}^*) \to \Omega^n$.

---

*Proof.* **Well-definedness.** Suppose $f, g: S^{n+k} \to E^*$ are homotopic maps, both transverse to $G$. There is a homotopy $H: S^{n+k} \times I \to E^*$ from $f$ to $g$, which we can choose transverse to $G$. Then $H^{-1}(G)$ is a compact manifold with boundary

$$\partial(H^{-1}(G)) = f^{-1}(G) \times 0 \;\cup\; g^{-1}(G) \times 1,$$

so $H^{-1}(G)$ is a cobordism from $f^{-1}(G)$ to $g^{-1}(G)$. Hence $[f^{-1}(G)] = [g^{-1}(G)]$, showing that $\tau$ is well-defined.

**Homomorphism property.** Let $\alpha, \beta \in \pi_{n+k}(E^*)$ be represented by maps $f, g: S^{n+k} \to E^*$ transverse to $G$. The sum $\alpha + \beta$ in the homotopy group is represented by the map $h: S^{n+k} \to E^*$ which equals $f$ on the upper hemisphere and $g$ on the lower hemisphere, after a homotopy making both basepoint-preserving. We may assume that $f$, $g$, and $h$ are transverse to $G$. It is clear that $h^{-1}(G)$ is the disjoint union of $f^{-1}(G)$ and $g^{-1}(G)$, since these lie in disjoint open hemispheres. Therefore

$$\tau(\alpha + \beta) = [h^{-1}(G)] = [f^{-1}(G) \cup g^{-1}(G)] = [f^{-1}(G)] + [g^{-1}(G)] = \tau(\alpha) + \tau(\beta).$$

Thus $\tau$ is a group homomorphism.

**Surjectivity (a).** Assume $k > n$ and $s \geqslant k+n$. Let $[M^n] \in \mathfrak{N}^n$ be any cobordism class. Since $k > n$, we can embed the compact $n$-manifold $M$ in the sphere $S^{n+k}$. The normal bundle of $M$ in $S^{n+k}$ is a $k$-plane bundle, which by the classification theorem (Section 4.3) is induced from the universal bundle $\gamma_{s,k} \to G_{s,k}$ via a map $g_0: M \to G$; the tubular neighborhood $U \subset S^{n+k}$ of $M$ then admits a vector bundle map $\Phi: U \to E$ covering $g_0$. Define a map $f: S^{n+k} \to E^*$ by

$$f(x) = \begin{cases} \Phi(x) & \text{for } x \in U \\ \infty & \text{for } x \notin U \end{cases}$$

Then $f^{-1}(G) = M$ and $f$ is transverse to $G$. Hence $\tau([f]) = [M]$, proving surjectivity.

**Injectivity (b).** Now assume $k > n+1$ and $s \geqslant k+n+1$. Suppose $g: S^{n+k} \to E^*$ is such that $\tau([g]) = 0 \in \mathfrak{N}^n$. By Lemma 2.2 we may assume $g$ is in standard form; put $g^{-1}(G) = M^n$. Then $\tau([g]) = [M^n] = 0$, so $M$ bounds a compact manifold $W^{n+1}$.

The assumption $k > n+1$ implies that the inclusion $M^n \hookrightarrow S^{n+k}$ extends to a neat embedding $W^{n+1} \hookrightarrow D^{n+k+1}$. The tubular neighborhood $U \subset S^{n+k}$ of $M^n$ (used for the standard form of $g$) extends to a tubular neighborhood $V \subset D^{n+k+1}$ of $W^{n+1}$ (Theorem 4.6.4). By Theorem 4.3.4 the bundle map $g|_U: U \to E$ extends to a bundle map $h: V \to E$, since $s \geqslant k + (n+1)$. Extend $h$ to all of $D^{n+k+1}$ by mapping $D^{n+k+1} \setminus V$ to $\infty$. Since $h|_{S^{n+k}} = g$, it follows that $[g] = 0$ in $\pi_{n+k}(E^*)$. Hence $\tau$ is injective.

Combining (c) and (d), $\tau$ is an isomorphism when $k > n+1$ and $s \geqslant k+n+1$.

**Oriented version.** For oriented cobordism, one replaces $(E_{s,k}, G_{s,k})$ by the oriented Grassmann bundle $(\tilde{E}_{s,k}, \tilde{G}_{s,k})$. Here $\tilde{G}_{s,k}$ is the manifold of oriented $k$-planes in $\mathbb{R}^s$ (a double cover of $G_{s,k}$), and $\tilde{E}_{s,k}$ is the pullback of the universal bundle. The same transversality argument yields a homomorphism $\tilde{\tau}: \pi_{n+k}(\tilde{E}^*) \to \Omega^n$ with analogous properties.

$\square$
