---
role: proof
locale: en
of_concept: bishop-analytic-structure-from-positive-measure
source_book: gtm035
source_chapter: "Chapter 10"
source_section: "10.7"
---
# Proof of Bishop's Theorem on Analytic Structure from Positive Measure

**Theorem 10.7 (Bishop).** Let $\mathfrak{A}$ be a uniform algebra on a compact space $X$ with maximal ideal space $\mathcal{M}$. Let $f \in \mathfrak{A}$ satisfy

(a) $|f| = 1$ on $X$.

(b) $0 \in f(\mathcal{M})$.

(c) There exists a closed subset $\Gamma_0$ of the unit circle $\Gamma$ having positive linear measure such that for each $\lambda \in \Gamma_0$ there is a unique point $q$ in $X$ with $f(q) = \lambda$.

Then

(7) For each $z_1 \in \mathring{D}$ there is a unique point $x \in \mathcal{M}$ with $f(x) = z_1$.

(8) If $g \in \mathfrak{A}$, there exists a function $G$ analytic in $\mathring{D}$ such that

$$g = G \circ f \quad \text{on } f^{-1}(\mathring{D}).$$

**Proof of (7).** For each measure $\mu$ on $X$, let $f_*(\mu)$ denote the induced measure on $\Gamma$; that is, for a Borel set $S \subset \Gamma$,

$$f_*(\mu)(S) = \mu(f^{-1}(S)).$$

Suppose $p_1, p_2 \in \mathcal{M}$ satisfy $f(p_1) = f(p_2) = z_1 \in \mathring{D}$. Let $\mu_1$ and $\mu_2$ be representing measures on $X$ for $p_1$ and $p_2$ respectively. By condition (c), the map $f: f^{-1}(\Gamma_0) \to \Gamma_0$ is bijective, and it follows that the restrictions of $\mu_1$ and $\mu_2$ to $f^{-1}(\Gamma_0)$ coincide. Consequently, the measures $g\mu_1$ and $g\mu_2$ (defined by $d(g\mu_j) = g \, d\mu_j$) also coincide when restricted to $f^{-1}(\Gamma_0)$.

Set $\lambda_j = f_*(g\mu_j)$ for $j = 1, 2$. Then $\lambda_1$ and $\lambda_2$ are measures on $\Gamma$ that coincide when restricted to $\Gamma_0$.

Now choose $g \in \mathfrak{A}$ such that $g(p_1) = 1$ and $g(p_2) = 0$. For any polynomial $G(z) = \sum_{k=0}^{N} c_k z^k$, we compute

$$\int_\Gamma G \, d\lambda_1 = \int_X G(f) \, g \, d\mu_1 = G(f(p_1)) \, g(p_1) = G(z_1),$$

$$\int_\Gamma G \, d\lambda_2 = \int_X G(f) \, g \, d\mu_2 = G(f(p_2)) \, g(p_2) = 0.$$

Thus

$$\int_\Gamma G \, d(\lambda_1 - \lambda_2) = G(z_1) \quad \text{for all polynomials } G.$$

The measure $\nu = (z - z_1) \, d(\lambda_1 - \lambda_2)$ on $\Gamma$ then satisfies

$$\int_\Gamma z^n \, d\nu = \int_\Gamma z^n(z - z_1) \, d(\lambda_1 - \lambda_2) = \int_\Gamma (z^{n+1} - z_1 z^n) \, d(\lambda_1 - \lambda_2) = z_1^{n+1} - z_1 \cdot z_1^n = 0$$

for all $n \geq 0$. Thus $\nu$ is a measure on $\Gamma$ orthogonal to all analytic polynomials.

By the theorem of F. and M. Riesz, there exists a function $k \in H^1(\Gamma)$ such that

$$(z - z_1) \, d(\lambda_1 - \lambda_2) = k \, dz.$$

On $\Gamma_0$, the measures $\lambda_1$ and $\lambda_2$ coincide, so $k = 0$ almost everywhere on $\Gamma_0$. Since $\Gamma_0$ has positive Lebesgue measure, a classical result on Hardy spaces (see Hoffman, *Banach Spaces of Analytic Functions*) implies that an $H^1$ function vanishing on a set of positive measure must be identically zero. Hence $k \equiv 0$.

But $z - z_1 \neq 0$ on $\Gamma$ (since $z_1 \in \mathring{D}$ and $|z| = 1$ on $\Gamma$), so $\lambda_1 - \lambda_2 = 0$ as measures on $\Gamma$. This contradicts the fact that $\int G \, d(\lambda_1 - \lambda_2) = G(z_1) \neq 0$ for non-constant polynomials $G$. The contradiction shows that $p_1 = p_2$, proving the uniqueness part of (7).

The existence part follows from the fact that $f(\mathcal{M})$ is the spectrum of $f$ in $\mathfrak{A}$, which by condition (a) is contained in $\overline{D}$ and by (b) contains $0$, so by connectivity of the spectrum, $f(\mathcal{M}) \supseteq \mathring{D}$.

**Proof of (8).** From (7), the map $f: f^{-1}(\mathring{D}) \to \mathring{D}$ is a continuous bijection. For $g \in \mathfrak{A}$, define $G: \mathring{D} \to \mathbb{C}$ by $G(\lambda) = g(f^{-1}(\lambda))$. Then $G$ is continuous on $\mathring{D}$. It remains to show $G$ is analytic.

Fix an open disk $U$ with closure $\overline{U} \subset \mathring{D}$. For each $z_0 \in \overline{U}$, let $\mu_{z_0}$ be the unique representing measure for the point $x_{z_0} = f^{-1}(z_0)$ in $\mathcal{M}$. Then

$$G(z_0) = g(x_{z_0}) = \int_X g \, d\mu_{z_0}.$$

Using the push-forward by $f$, this representation transfers to an integral on $\Gamma$, and one shows that $G$ coincides with the Poisson integral of a boundary function, which yields analyticity. Alternatively, one may use the abstract $H^\infty$ functional calculus: the map $\Phi: H^\infty(\Gamma) \to \mathfrak{A}$ defined by $\Phi(h) = h \circ f$ (via the $L^2(\mu)$-lifting argument from Chapter 11) provides an isometric embedding, and the analyticity of $G$ follows from the analyticity of the representing functions.

The key point is that the uniqueness of the fiber $f^{-1}(\lambda)$ for $\lambda \in \mathring{D}$ forces $g$ to be an analytic function of $f$ over $\mathring{D}$. ∎
