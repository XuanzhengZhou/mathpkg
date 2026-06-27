---
role: proof
locale: en
of_concept: approximation-on-maximally-complex-manifolds
source_book: gtm035
source_chapter: "Chapter 17"
source_section: "17.1"
---
# Proof of Approximation Theorem on Maximally Complex Manifolds

**Theorem 17.1.** Let $\Sigma$ be a $k$-dimensional sufficiently smooth submanifold of an open set in $\mathbb{C}^n$. Assume that $\Sigma$ has no complex tangents. Let $X$ be a compact polynomially convex subset of $\Sigma$. Then

$$P(X) = C(X).$$

*Note.* "Sufficiently smooth" means that $\Sigma$ is of class $C^e$ with $e > k/2 + 1$.

*Proof.* To show that $P(X) = C(X)$ we need only show that $P(X)$ contains the restriction to $X$ of every $u \in C^\infty(\mathbb{C}^n)$, since such functions are dense in $C(X)$.

Fix $u \in C^\infty(\mathbb{C}^n)$. By the Oka–Weil theorem it suffices to approximate $u$ uniformly on $X$ by functions defined and holomorphic in some neighborhood of $X$ in $\mathbb{C}^n$.

**Step 1. Construction of a neighborhood $\omega_\varepsilon$.** Using Lemma 17.2, the squared distance function $d^2(z) = \operatorname{dist}(z, \Sigma)^2$ is strongly plurisubharmonic in a neighborhood of $\Sigma$. Choose a neighborhood $\omega$ of $\Sigma$ such that $d^2$ is strongly plurisubharmonic in $\omega$.

Choose $\beta \in C_0^\infty(\omega)$ with $\beta = 1$ in a neighborhood of $X$ and $0 \leq \beta \leq 1$. Let $\Omega$ be an open set with compact closure such that $\operatorname{supp} \beta \subset \Omega \subset \overline{\Omega} \subset \omega$. Since $d^2$ is strongly plurisubharmonic in $\omega$, choose $\varepsilon > 0$ such that

$$\phi = d^2 - \varepsilon^2 \beta$$

is plurisubharmonic in $\Omega$. Choose $\varepsilon$ small enough that $\beta(z) = 1$ for all $z$ with $\operatorname{dist}(z, X) < \varepsilon$.

Choose an open set $\Omega_1$ with $\operatorname{supp} \beta \subset \Omega_1 \subset \overline{\Omega}_1 \subset \Omega$.

**Lemma 17.3.** There exists a function $u \in C^\infty(\mathbb{C}^n)$ such that $u$ is plurisubharmonic in $\Omega_1$ and $|u - \phi| < \varepsilon^2/4$ on $\Omega_1$.

Choose $\chi \in C^\infty(\mathbb{C}^n)$ with compact support for regularization. Since $u \in C^\infty(\mathbb{C}^n)$, Sard's theorem implies that the set of critical values of $u$ has measure zero in $\mathbb{R}$. Hence every interval contains a regular value $t$ of $u$. Choose such a $t$ with

$$-\frac{1}{2}\varepsilon^2 < t < -\frac{1}{4}\varepsilon^2.$$

Define

$$\omega_\varepsilon = \{ z \in \Omega_1 \mid u(z) < t \}, \qquad u_\varepsilon = u - t.$$

Then $\omega_\varepsilon = \{ u_\varepsilon < 0 \}$, and:
- $u_\varepsilon$ is plurisubharmonic in a neighborhood of $\overline{\omega_\varepsilon}$,
- $u_\varepsilon = 0$ on $\partial \omega_\varepsilon$,
- $\operatorname{grad} u_\varepsilon \neq 0$ on $\partial \omega_\varepsilon$ (since $t$ is a regular value),
- $\omega_\varepsilon \subset \operatorname{supp} \beta$,
- $X \subset \omega_\varepsilon$, and $\operatorname{dist}(X, \partial \omega_\varepsilon) \approx \varepsilon$.

Thus $\omega_\varepsilon$ is a strictly pseudoconvex neighborhood of $X$ to which Theorem 16.1 (the $L^2$ solvability of $\bar{\partial}$) applies. This completes Step 1.

**Step 2. Extension of $u$ with small $\bar{\partial}$.** By Lemma 17.4, there exists a function $U_\varepsilon \in C^1(\mathbb{C}^n)$ such that $U_\varepsilon = u$ on $X$ and

$$\left| \frac{\partial U_\varepsilon}{\partial \bar{z}_j}(z) \right| \leq C \cdot d(z, \Sigma)^{e-1} \leq C' \varepsilon^{e-1}, \quad z \in \omega_\varepsilon, \; j = 1, \ldots, n.$$

Moreover, the volume of $\omega_\varepsilon$ satisfies $\operatorname{Vol}(\omega_\varepsilon) \leq C'' \varepsilon^{2n-k}$.

**Step 3. Solving $\bar{\partial}$ and completing the proof.** Put $g = \bar{\partial} U_\varepsilon$. Then $\bar{\partial} g = 0$ in $\omega_\varepsilon$. By Theorem 16.1, there exists $V_\varepsilon \in L^2(\omega_\varepsilon)$ such that, as distributions,

$$\frac{\partial V_\varepsilon}{\partial \bar{z}_j} = \frac{\partial U_\varepsilon}{\partial \bar{z}_j}, \quad j = 1, \ldots, n,$$

and

$$\int_{\omega_\varepsilon} |V_\varepsilon|^2 \, dV \leq C' \int_{\omega_\varepsilon} \left( \sum_{j=1}^{n} \left| \frac{\partial U_\varepsilon}{\partial \bar{z}_j} \right|^2 \right) dV.$$

Using the estimates from Steps 1 and 2,

$$\int_{\omega_\varepsilon} |V_\varepsilon|^2 \, dV \leq C''' \varepsilon^{2e-2+2n-k}.$$

By Lemma 16.8, $V_\varepsilon$ is continuous in $\omega_\varepsilon$. Fix $x \in X$ and let $B_x$ be the ball centered at $x$ with radius $\varepsilon/2$. Then

$$|V_\varepsilon(x)| \leq K \left\{ \varepsilon^{-n} \|V_\varepsilon\|_{L^2(B_x)} + \varepsilon \sup_{B_x} \left( \max_j \left| \frac{\partial V_\varepsilon}{\partial \bar{z}_j} \right| \right) \right\}.$$

Since $B_x \subset \omega_\varepsilon$ and using the estimates above,

$$|V_\varepsilon(x)| \leq K \left\{ \varepsilon^{e-1-k/2} + \varepsilon^e \right\}.$$

Because $e > k/2 + 1$, the exponent $e-1-k/2 > 0$, and therefore $\sup_X |V_\varepsilon| \to 0$ as $\varepsilon \to 0$.

Now $U_\varepsilon - V_\varepsilon$ is holomorphic in $\omega_\varepsilon$ (since $\bar{\partial}(U_\varepsilon - V_\varepsilon) = 0$), and on $X$,

$$U_\varepsilon - V_\varepsilon = u - V_\varepsilon \to u$$

uniformly as $\varepsilon \to 0$. Thus $u$ can be uniformly approximated on $X$ by functions holomorphic in neighborhoods of $X$, so $u \in P(X)$ by the Oka–Weil theorem.

Since $C^\infty(\mathbb{C}^n)$ functions are dense in $C(X)$, we conclude $P(X) = C(X)$. $\square$
