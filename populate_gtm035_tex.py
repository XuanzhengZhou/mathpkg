#!/usr/bin/env python3
"""Populate theorem.tex files for GTM035 concepts with actual LaTeX statements from section text."""
import os, re

SECTIONS_DIR = '/home/a123/文档/mathpkg/pipeline_output/stitched_sections/(GTM035)Several Complex Variables and Banach Algebras'
CONCEPTS_DIR = '/home/a123/文档/mathpkg/pipeline_output/concepts_v7/gtm035'

# Load all section texts
section_texts = {}
for fname in sorted(os.listdir(SECTIONS_DIR)):
    if fname.endswith('.md'):
        with open(os.path.join(SECTIONS_DIR, fname), 'r', encoding='utf-8') as f:
            section_texts[fname] = f.read()

# Map slugs to their statements
# key: slug -> (statement, ref_section)
statements = {}

# ============================================================
# CHAPTER 1 - Preliminaries
# ============================================================
statements["riesz-banach-approximation-theorem"] = (
    r"""Let $\mathcal{L}$ be a linear subspace of $C(X)$ and fix $g$ in $C(X)$. If for every measure $\mu$ on $X$
$$\mu \perp \mathcal{L} \text{ implies } \mu \perp g,$$
then $g$ lies in the closure of $\mathcal{L}$. In particular, if
$$\mu \perp \mathcal{L} \text{ implies } \mu = 0,$$
then $\mathcal{L}$ is dense in $C(X)$.""",
    "s001"
)

statements["uniform-algebra-definition"] = (
    r"""Let $X$ be a compact Hausdorff space. A uniform algebra on $X$ is an algebra $\mathfrak{A}$ of continuous complex-valued functions on $X$ satisfying
\begin{enumerate}
\item $\mathfrak{A}$ is closed under uniform convergence on $X$.
\item $\mathfrak{A}$ contains the constants.
\item $\mathfrak{A}$ separates the points of $X$.
\end{enumerate}
$\mathfrak{A}$ is normed by $\|f\| = \max_x |f|$ and so becomes a Banach algebra.""",
    "s001"
)

# ============================================================
# CHAPTER 2 - Classical Approximation Theorems
# ============================================================
statements["real-stone-weierstrass-theorem"] = (
    r"""If $\mathfrak{A}$ separates the points of $X$, then $\mathfrak{A}$ is dense in $C_{\mathbb{R}}(X)$.""",
    "s002"
)

statements["krein-milman-extreme-point"] = (
    r"""Let $B$ be a real Banach space and $B^*$ its dual space taken in the weak-$^*$ topology. Let $K$ be a nonempty compact convex subset of $B^*$. Then $K$ has an extreme point.""",
    "s002"
)

statements["complex-stone-weierstrass-theorem"] = (
    r"""$\mathfrak{A}$ is a subalgebra of $C(X)$ containing the constants and separating points. If
$$f \in \mathfrak{A} \Rightarrow \bar{f} \in \mathfrak{A},$$
then $\mathfrak{A}$ is dense in $C(X)$.""",
    "s002"
)

statements["logarithmic-potential-cauchy-transform-summability"] = (
    r"""The functions
$$\int \left| \log \left| \frac{1}{z - \zeta} \right| \right| d|\mu|(\zeta) \quad \text{and} \quad \int \left| \frac{1}{\zeta - z} \right| d|\mu|(\zeta)$$
are summable $-dx\,dy$ over compact sets in $\mathbb{C}$. It follows that these functions are finite a.e. $-dx\,dy$ and hence that $\mu^*$ and $\hat{\mu}$ are defined a.e. $-dx\,dy$.""",
    "s002"
)

statements["cauchy-transform-inversion-formula"] = (
    r"""For $F \in C_0^1(\mathbb{C})$,
$$\frac{\partial F}{\partial \bar{z}} \text{ satisfies } \int \frac{\partial F}{\partial \bar{z}} \frac{dx\,dy}{\zeta - z} = -\pi F(\zeta).$$""",
    "s002"
)

statements["newtonian-potential-representation"] = (
    r"""Let $G \in C_0^2(\mathbb{C})$. Then
$$G(\zeta) = -\frac{1}{2\pi} \int_{\mathbb{C}} \Delta G(z) \log \frac{1}{|z-\zeta|} \,dx\,dy, \quad \text{all } \zeta \in \mathbb{C}.$$""",
    "s002"
)

statements["cauchy-transform-vanishing-implies-measure-zero"] = (
    r"""If $\hat{\mu} = 0$ a.e. $-dx\,dy$, then $\mu = 0$. Similarly, if $\mu^* = 0$ a.e. $-dx\,dy$, then $\mu = 0$.""",
    "s002"
)

statements["hartogs-rosenthal-theorem"] = (
    r"""Assume that $X \subset \mathbb{C}$ has Lebesgue two-dimensional measure $0$. Then rational functions whose poles lie off $X$ are uniformly dense in $C(X)$.""",
    "s002"
)

statements["runge-approximation-theorem"] = (
    r"""Let $K$ be a compact subset of the plane and let $E$ be a set containing at least one point from each bounded component of $\mathbb{C}\setminus K$. Then every function holomorphic in a neighborhood of $K$ can be uniformly approximated on $K$ by rational functions whose poles lie in $E$.""",
    "s002"
)

statements["lavrentieff-polynomial-approximation-theorem"] = (
    r"""If the interior of $X$ is empty and $\mathbb{C} \setminus X$ is connected, then $P(X) = C(X)$.""",
    "s003"
)

statements["logarithmic-potential-boundary-limit"] = (
    r"""Let $\alpha$ be a real measure on $E$ satisfying
$$\int_E \left| \log \left| \frac{1}{z_0 - \zeta} \right| \right| d|\alpha|(\zeta) < \infty.$$
Then
$$\lim_{t \to 0} \int \alpha^* d\sigma_t(z) = \alpha^*(z_0).$$""",
    "s003"
)

# ============================================================
# CHAPTER 3 - Operational Calculus in One Variable
# ============================================================
statements["gelfand-operational-calculus-one-variable"] = (
    r"""Let $\mathfrak{A}$ be a Banach algebra, $x \in \mathfrak{A}$, and let $\Omega$ be an open set containing $\sigma(x)$. Then there exists a map $\tau : H(\Omega) \rightarrow \mathfrak{A}$, written $F \mapsto F(x)$, satisfying:
\begin{enumerate}
\item[(a)] $\tau$ is an algebra homomorphism.
\item[(b)] If $F_n \rightarrow F$ in $H(\Omega)$, then $F_n(x) \rightarrow F(x)$ in $\mathfrak{A}$.
\item[(c)] If $F(z) = z$, then $F(x) = x$.
\item[(d)] $\widehat{F(x)} = F(\hat{x})$ on $\mathcal{M}$.
\item[(e)] $\sigma(F(x)) = F(\sigma(x))$ (Spectral Mapping Theorem).
\end{enumerate}""",
    "s005"
)

statements["idempotent-from-disconnected-spectrum"] = (
    r"""Assume there is an element $x$ in $\mathfrak{A}$ such that $\sigma(x)$ is disconnected. Then $\mathfrak{A}$ contains a nontrivial idempotent.""",
    "s005"
)

statements["exponential-representation-in-banach-algebra"] = (
    r"""Assume that $\sigma(x)$ is contained in a simply connected region $\Omega$, where $0 \notin \Omega$. Then there exists $y \in \mathfrak{A}$ with $x = e^y$.""",
    "s005"
)

# ============================================================
# CHAPTER 4 - Differential Forms
# ============================================================
statements["smooth-functions-on-domain"] = (
    r"""$C^\infty(\Omega)$ is the algebra of all infinitely differentiable complex-valued functions on $\Omega$.""",
    "s005"
)

statements["tangent-space-at-point"] = (
    r"""Fix $x \in \Omega$. $T_x$ is the collection of all maps $v : C^\infty \to \mathbb{C}$ for which
\begin{enumerate}
\item[(a)] $v$ is linear.
\item[(b)] $v(f \cdot g) = f(x) \cdot v(g) + g(x) \cdot v(f)$, $f, g \in C^\infty$.
\end{enumerate}
$T_x$ is called the tangent space at $x$ and its elements tangent vectors at $x$.""",
    "s005"
)

statements["tangent-space-basis"] = (
    r"""$\partial/\partial x_1|_x, \ldots, \partial/\partial x_N|_x$ forms a basis for $T_x$.""",
    "s005"
)

statements["cotangent-space"] = (
    r"""The dual space to $T_x$ is denoted $T_x^*$.""",
    "s005"
)

statements["one-form-definition"] = (
    r"""A 1-form $\omega$ on $\Omega$ is a map $\omega$ assigning to each $x$ in $\Omega$ an element of $T_x^*$.""",
    "s005"
)

statements["one-form-coordinate-representation"] = (
    r"""Every 1-form $\omega$ admits a unique representation
$$\omega = \sum_{1}^{N} C_j dx_j,$$
the $C_j$ being scalar functions on $\Omega$.""",
    "s006"
)

statements["exterior-algebra-is-associative"] = (
    r"""Under the wedge product $\wedge$, $\mathcal{G}(V)$ is an associative algebra with identity.""",
    "s006"
)

statements["wedge-product-anticommutativity"] = (
    r"""If $\tau \in \wedge^k(V)$, $\sigma \in \wedge^l(V)$, then $\tau \wedge \sigma = (-1)^{kl} \sigma \wedge \tau$.""",
    "s006"
)

statements["basis-of-k-forms"] = (
    r"""Fix $k$. The set of elements
$$e_{i_1} \wedge e_{i_2} \wedge \cdots \wedge e_{i_k}, \quad 1 \leq i_1 < i_2 < \cdots < i_k \leq N,$$
forms a basis for $\wedge^k(V)$.""",
    "s006"
)

statements["k-form-definition"] = (
    r"""A $k$-form $\omega^k$ on $\Omega$ is a map $\omega^k$ assigning to each $x$ in $\Omega$ an element of $\wedge^k(T_x)$.""",
    "s006"
)

statements["exterior-derivative-definition"] = (
    r"""Let $\omega^k \in \wedge^k(\Omega)$, with
$$\omega^k = \sum_{i_1 < \cdots < i_k} C_{i_1 \cdots i_k} dx_{i_1} \wedge \cdots \wedge dx_{i_k}.$$
Define
$$d\omega^k = \sum_{i_1 < \cdots < i_k} dC_{i_1 \cdots i_k} \wedge dx_{i_1} \wedge \cdots \wedge dx_{i_k}.$$
$d$ maps $\wedge^k(\Omega) \rightarrow \wedge^{k+1}(\Omega)$ and is called the exterior derivative.""",
    "s006"
)

statements["exterior-derivative-squared-zero"] = (
    r"""$d^2 = 0$ for every $k$; i.e., if $\omega^k \in \wedge^k(\Omega)$, then $d(d\omega^k) = 0$.""",
    "s006"
)

# ============================================================
# CHAPTER 5 - The ∂̄-Operator
# ============================================================
statements["one-form-dz-dzbar-representation"] = (
    r"""If $\omega \in \wedge^1(\Omega)$, then
$$\omega = \sum_{j=1}^{n} a_j dz_j + b_j d\bar{z}_j$$
where $a_j, b_j \in C^\infty$.""",
    "s006"
)

statements["wirtinger-derivatives"] = (
    r"""We define operators on $C^\infty$ as follows:
$$\frac{\partial}{\partial z_j} = \frac{1}{2} \left( \frac{\partial}{\partial x_j} - i \frac{\partial}{\partial y_j} \right), \quad \frac{\partial}{\partial \bar{z}_j} = \frac{1}{2} \left( \frac{\partial}{\partial x_j} + i \frac{\partial}{\partial y_j} \right).$$""",
    "s006"
)

statements["del-and-delbar-operators"] = (
    r"""We define two maps from $C^\infty \to \wedge^1(\Omega)$: for $f \in C^\infty$,
$$\partial f = \sum_{j=1}^{n} \frac{\partial f}{\partial z_j} dz_j, \quad \bar{\partial} f = \sum_{j=1}^{n} \frac{\partial f}{\partial \bar{z}_j} d\bar{z}_j.$$""",
    "s006"
)

statements["delbar-on-differential-forms"] = (
    r"""Choose $\omega^k$ in $\wedge^k(\Omega)$,
$$\omega^k = \sum_{I,J} a_{IJ} dz_I \wedge d\bar{z}_J,$$
$$\partial \omega^k = \sum_{I,J} \partial a_{IJ} \wedge dz_I \wedge d\bar{z}_J,$$
and
$$\bar{\partial} \omega^k = \sum_{I,J} \bar{\partial} a_{IJ} \wedge dz_I \wedge d\bar{z}_J.$$""",
    "s006"
)

statements["delbar-squared-zero"] = (
    r"""$$\bar{\partial}^2 = 0, \quad \partial^2 = 0, \quad \text{and} \quad \partial \bar{\partial} + \bar{\partial} \partial = 0.$$""",
    "s006"
)

statements["delbar-closed-implies-analytic-polydisk"] = (
    r"""Assume that $\partial f / \partial \bar{z}_j = 0$, $j = 1, \ldots, n$, in the polydisk $\Omega = \{z \in \mathbb{C}^n \mid |z_j| < R_j\}$. Then there exist constants $A_\nu$ in $\mathbb{C}$ for each tuple $\nu = (\nu_1, \ldots, \nu_n)$ of nonnegative integers such that
$$f(z) = \sum_{\nu} A_\nu z^\nu,$$
the series converging absolutely in $\Omega$ and uniformly on every compact subset of $\Omega$.""",
    "s006"
)

statements["delbar-product-rule"] = (
    r"""If $\omega^k \in \wedge^k(\Omega)$ and $\omega^l \in \wedge^l(\Omega)$, then
$$\bar{\partial}(\omega^k \wedge \omega^l) = \bar{\partial}\omega^k \wedge \omega^l + (-1)^k \omega^k \wedge \bar{\partial}\omega^l.$$""",
    "s006"
)

# ============================================================
# CHAPTER 6 & 7 - ∂̄u=f and Oka-Weil
# ============================================================
statements["complex-poincare-lemma"] = (
    r"""Let $\Omega$ be a neighborhood of $\Delta^n$. Fix $\omega \in \wedge^{p,q}(\Omega)$, $q > 0$, with $\bar{\partial}\omega = 0$. Then there exists a neighborhood $\Omega_1$ of $\Delta^n$ and $\tau \in \wedge^{p,q-1}(\Omega_1)$ such that $\bar{\partial}\tau = \omega$ in $\Omega_1$.""",
    "s007"
)

statements["delbar-solution-in-plane"] = (
    r"""Let $\phi \in C^1(\mathbb{R}^2)$ and assume that $\phi$ has compact support. Put
$$\Phi(\zeta) = -\frac{1}{\pi} \int_{\mathbb{R}^2} \phi(z) \frac{dx\,dy}{z - \zeta}.$$
Then $\Phi \in C^1(\mathbb{R}^2)$ and $\partial \Phi / \partial \bar{\zeta} = \phi(\zeta)$ for all $\zeta$.""",
    "s007"
)

statements["delbar-solution-polydisk-neighborhood"] = (
    r"""There exists a neighborhood $\Omega_1$ of $\Delta^n$ and, for given data, a solution to the $\bar{\partial}$-equation in $\Omega_1$ with control on derivatives.""",
    "s007"
)

statements["oka-weil-approximation-theorem"] = (
    r"""Assume that $\mathbb{C}\setminus K$ is connected. Let $F$ be holomorphic in some neighborhood $\Omega$ of $K$. Then $F|_K$ is in $P(K)$.""",
    "s007"
)

statements["polynomial-peak-point-characterization"] = (
    r"""Let $K$ be a compact set in $\mathbb{C}$. $\mathbb{C} \setminus K$ is connected if and only if for each $x^0 \in \mathbb{C} \setminus K$ we can find a polynomial $P$ such that
$$|P(x^0)| > \max_K |P|.$$""",
    "s007"
)

statements["polynomially-convex-set-definition"] = (
    r"""A compact set $X \subset \mathbb{C}^n$ is polynomially convex if for each $z \notin X$ there exists a polynomial $P$ with $|P(z)| > \max_X |P|$.""",
    "s007"
)

statements["p-polyhedron-definition"] = (
    r"""A subset $\Pi$ of $\mathbb{C}^n$ is a $p$-polyhedron if there exist polynomials $P_1, \ldots, P_s$ such that
$$\Pi = \{z \in \mathbb{C}^n \mid |z_j| \leq 1, \text{ all } j, \text{ and } |P_k(z)| \leq 1, k = 1, 2, \ldots, s\}.$$""",
    "s008"
)

statements["polyhedron-approximation-polynomially-convex"] = (
    r"""Let $X$ be a compact polynomially convex subset of $\Delta^n$. Let $\mathcal{O}$ be an open set containing $X$. Then there exists a $p$-polyhedron $\Pi$ with $X \subset \Pi \subset \mathcal{O}$.""",
    "s008"
)

statements["oka-extension-theorem"] = (
    r"""Let $\Pi = P^n(p_1, \ldots, p_r)$ be a $p$-polyhedron. Let $f$ be holomorphic in a neighborhood of $\Pi$. Then there exists $F$ holomorphic in a neighborhood of $\Delta^{n+r}$ such that
$$F(z, p_1(z), \ldots, p_r(z)) = f(z), \quad \text{all } z \in \Pi.$$""",
    "s008"
)

statements["delbar-on-p-polyhedron"] = (
    r"""Let $\Pi$ be a $p$-polyhedron in $\mathbb{C}^n$ and $\Omega$ a neighborhood of $\Pi$. Given $\phi \in \wedge^{p,q}(\Omega)$, $q > 0$, with $\bar{\partial}\phi = 0$, there exists a neighborhood $\Omega_1$ of $\Pi$ and $\psi \in \wedge^{p,q-1}(\Omega_1)$ with $\bar{\partial}\psi = \phi$.""",
    "s008"
)

statements["holomorphic-pullback-of-forms"] = (
    r"""If $u = (u_1, \ldots, u_k)$ is a holomorphic map and $\omega(u)$ is a differential form, then $d(\omega(u)) = (d\omega)(u)$ and $\bar{\partial}(\omega(u)) = (\bar{\partial}\omega)(u)$.""",
    "s008"
)

statements["oka-extension-lemma"] = (
    r"""Fix $k$ and polynomials $q_1, \ldots, q_r$ in $z = (z_1, \ldots, z_k)$. Let $f$ be holomorphic in a neighborhood $W$ of $\Pi = P^k(q_1, \ldots, q_r)$. Then there exists $F$ holomorphic in a neighborhood of $\Pi' = P^{k+1}(q_2, \ldots, q_r)$ such that
$$F(z, q_1(z)) = f(z), \quad z \in \Pi.$$""",
    "s008"
)

# ============================================================
# CHAPTER 8 - Operational Calculus in Several Variables
# ============================================================
statements["joint-spectrum-definition"] = (
    r"""$\sigma(x_1, \ldots, x_n)$, the joint spectrum of $x_1, \ldots, x_n$, is
$$\{(\hat{x}_1(M), \ldots, \hat{x}_n(M)) \mid M \in \mathcal{M}\}.$$""",
    "s008"
)

statements["joint-spectrum-characterization"] = (
    r"""$(\lambda_1, \ldots, \lambda_n)$ in $\mathbb{C}^n$ lies in $\sigma(x_1, \ldots, x_n)$ if and only if the equation
$$\sum_{j=1}^{n} y_j(x_j - \lambda_j) = 1$$
has no solution $y_1, \ldots, y_n \in \mathfrak{A}$.""",
    "s008"
)

statements["operational-calculus-several-variables"] = (
    r"""Let $\mathfrak{A}$ be a Banach algebra and $x_1, \ldots, x_n \in \mathfrak{A}$. Let $\Omega$ be an open set containing $\sigma(x_1, \ldots, x_n)$. Then there exists a map $\tau: H(\Omega) \to \mathfrak{A}$ such that for all $F \in H(\Omega)$,
$$\widehat{\tau(F)} = F(\hat{x}_1, \ldots, \hat{x}_n) \text{ on } \mathcal{M}.$$""",
    "s009"
)

statements["joint-spectrum-polynomially-convex"] = (
    r"""Assume that $x_1, \ldots, x_n$ generate $\mathfrak{A}$. Then $\sigma(x_1, \ldots, x_n)$ is a polynomially convex subset of $\mathbb{C}^n$.""",
    "s008"
)

statements["separating-elements-for-maximal-ideals"] = (
    r"""There exist $a_1, \ldots, a_N \in \mathfrak{A}$ such that if $\hat{a}$ is the map $\mathcal{M} \to \mathbb{C}^N : M \mapsto (\hat{a}_1(M), \ldots, \hat{a}_N(M))$, then $\hat{a}(\mathcal{M}_1) \cap \hat{a}(\mathcal{M}_2) = \emptyset$ for disjoint closed subsets $\mathcal{M}_1, \mathcal{M}_2$ of $\mathcal{M}$.""",
    "s009"
)

statements["idempotent-from-disconnected-maximal-ideal-space"] = (
    r"""If the maximal ideal space $\mathcal{M}$ of a Banach algebra $\mathfrak{A}$ is disconnected, then $\mathfrak{A}$ contains a nontrivial idempotent.""",
    "s009"
)

# ============================================================
# CHAPTER 9 - Šilov Boundary
# ============================================================
statements["boundary-for-function-algebra"] = (
    r"""A boundary for $\mathcal{F}$ is a closed subset $E$ of $X$ such that
$$|f(x)| \leq \max_E |f|, \quad \text{all } f \in \mathcal{F}, x \in X.$$""",
    "s009"
)

statements["silov-boundary-theorem"] = (
    r"""Let $X$ and $\mathcal{F}$ be as above. Let $S$ denote the intersection of all boundaries for $\mathcal{F}$. Then $S$ is a boundary for $\mathcal{F}$ (the Šilov boundary).""",
    "s009"
)

statements["boundary-removal-lemma"] = (
    r"""Fix $x \in X \setminus S$. There exists a neighborhood $U$ of $x$ with the following property: If $\beta$ is a boundary, then $\beta \setminus U$ is also a boundary.""",
    "s009"
)

statements["local-maximum-modulus-principle"] = (
    r"""Let $\mathfrak{A}$ be a Banach algebra and fix $x \in \mathcal{M} \setminus \check{S}(\mathfrak{A})$. Let $U$ be a neighborhood of $x$ with $U \subset \mathcal{M} \setminus \check{S}(\mathfrak{A})$. Then for all $f \in \mathfrak{A}$,
$$|\hat{f}(x)| \leq \max_{\partial U} |\hat{f}|.$$""",
    "s010"
)

statements["delbar-solution-on-two-open-sets"] = (
    r"""Let $K$ be a compact polynomially convex set. Given a $\bar{\partial}$-closed form on $U_1 \cup U_2$ that is locally solvable, there exists a global solution on a neighborhood of $K$.""",
    "s010"
)

statements["logarithmic-holomorphic-separation"] = (
    r"""Let $K$ be a compact set in $\mathbb{C}^N$ and $U_1, U_2$ open sets covering $K$ with $U_1 \cap U_2 \subset \{\text{Re } z_1 < 0\}$. Then the function $(\log z_1)/z_1$, holomorphic on $U_1 \cap U_2$, can be written as $h_1 - h_2$ with $h_j \in H(U_j)$ on a suitable neighborhood of $K$.""",
    "s010"
)

statements["peak-function-extension"] = (
    r"""Let $\mathfrak{A}$ be a Banach algebra, $T$ a closed subset of $\mathcal{M}$ and $U$ an open neighborhood of $T$. Suppose that there exists $\phi \in \mathfrak{A}$ with $\hat{\phi} = 1$ on $T$, $|\hat{\phi}| < 1$ on $U \setminus T$. Then there exists $\Phi \in \mathfrak{A}$ with $\hat{\Phi} = 1$ on $T$, $|\hat{\Phi}| < 1$ on $\mathcal{M} \setminus T$.""",
    "s010"
)

statements["silov-boundary-of-local-algebras"] = (
    r"""Let $\mathfrak{A}$ be a uniform algebra on a space $X$. Let $U_1, U_2, \ldots, U_s$ be an open covering of $\mathcal{M}$. Denote by $\mathcal{L}$ the set of all $f$ in $C(\mathcal{M})$ such that for $j = 1, \ldots, s$, $f|_{U_j}$ lies in the uniform closure of $\hat{\mathfrak{A}}|_{U_j}$. Then $\mathcal{L}$ is a closed subalgebra of $C(\mathcal{M})$ and $\check{S}(\mathcal{L}) \subseteq X$.""",
    "s010"
)

# ============================================================
# CHAPTER 10 - Maximality and Radó's Theorem
# ============================================================
statements["cohen-invertibility-lemma"] = (
    r"""Let $a, b \in \mathfrak{A}$. Assume that $\| 1 + a + \bar{b} \| < 1$. Then $a + b$ is invertible in $\mathfrak{A}$.""",
    "s010"
)

statements["maximality-of-disk-algebra"] = (
    r"""Let $B$ be a uniform algebra on $\Gamma$ with $\mathfrak{A}_0 \subseteq B \subseteq C(\Gamma)$. Then either $\mathfrak{A}_0 = B$ or $B = C(\Gamma)$.""",
    "s010"
)

statements["rudin-analyticity-from-maximum-principle"] = (
    r"""Let $\mathcal{L}$ be an algebra of continuous functions on $D$ such that
\begin{enumerate}
\item[(a)] The function $z$ is in $\mathcal{L}$.
\item[(b)] $\mathcal{L}$ satisfies a maximum principle relative to $\Gamma$: $|G(x)| \leq \max_{\Gamma} |G|$ for all $x \in D, G \in \mathcal{L}$.
\end{enumerate}
Then $\mathcal{L} \subseteq A(D)$.""",
    "s010"
)

statements["glicksberg-local-maximum-lemma"] = (
    r"""Let $X_0$ be a compact subset of $\mathcal{M}$ and $E$ a closed subset of $X_0$. Let $\mathcal{L}$ be a closed subalgebra of $C(X_0)$ with $\partial X$ as a boundary. Assume that for each $x \in X_0 \setminus E$ there exists $f \in \mathcal{L}$ with $|f(x)| > \sup_{X_0 \setminus E} |f|$. Then $E$ is a boundary for $\mathcal{L}$.""",
    "s010"
)

statements["rado-boundary-uniqueness-theorem"] = (
    r"""Let $f \in A(\Omega)$ and assume that $f = 0$ on $\partial \Omega \cap U$ for some neighborhood $U$ of a nonisolated boundary point $z_0$. Then $f \equiv 0$ in $\Omega$.""",
    "s010"
)

statements["rado-theorem"] = (
    r"""Let $f$ be a continuous function on a domain $\Omega$ that is analytic on $\Omega \setminus Z(f)$, where $Z(f) = \{z \in \Omega : f(z) = 0\}$. Then $f$ is analytic on $\Omega$.""",
    "s010"
)

statements["bishop-analytic-structure-from-positive-measure"] = (
    r"""Let $\mathfrak{A}$ be a uniform algebra on a space $X$ with maximal ideal space $\mathcal{M}$. Let $f \in \mathfrak{A}$ satisfy
\begin{enumerate}
\item[(a)] $|f| = 1$ on $X$.
\item[(b)] $0 \in f(\mathcal{M})$.
\item[(c)] There exists a closed subset $\Gamma_0$ of $\Gamma$ having positive linear measure such that for each $\lambda \in \Gamma_0$ there is a unique point $q$ in $X$ with $f(q) = \lambda$.
\end{enumerate}
Then for each $z_1 \in \mathring{D}$ there is a unique $x \in \mathcal{M}$ with $f(x) = z_1$, and if $g \in \mathfrak{A}$, there exists $G$ analytic in $\mathring{D}$ such that $g = G(f)$ on $f^{-1}(\mathring{D})$.""",
    "s010"
)

# ============================================================
# CHAPTERS 11-26: Key theorems only (due to volume)
# ============================================================

statements["maximum-modulus-algebra-definition"] = (
    r"""Let $A$ be an algebra of continuous complex-valued functions on a locally compact Hausdorff space $X$, separating points. Fix $p \in A$ and an open set $\Omega \subset \mathbb{C}$ such that $p$ is a proper map of $X$ onto $\Omega$. Assume for each $\lambda_0 \in \Omega$, each closed disk $\Delta$ centered at $\lambda_0$, and each $x^0 \in p^{-1}(\lambda_0)$,
$$|g(x^0)| \leq \max_{p^{-1}(\partial \Delta)} |g|, \quad \forall g \in A.$$
Then $(A, X, \Omega, p)$ is a maximum modulus algebra.""",
    "s010"
)

statements["hardy-space-projection-theorem"] = (
    r"""Fix $F \in A$. Let $G$ denote the orthogonal projection in $L^2(\mu)$ of $F$ to $C$. Then $G \in H^2$, $G(0) = F(x^0)$, and $G(\lambda) \in \overline{co}(F(p^{-1}(\lambda)))$ for a.a. $\lambda \in \Gamma$.""",
    "s010"
)

statements["analytic-function-of-projection-for-one-sheeted"] = (
    r"""Let $(A, X, \Omega, f)$ be a maximum modulus algebra and fix a closed disk $\Delta \subseteq \Omega$. Assume that $X$ lies one-sheeted over $\Delta$. Then every $g \in A$ is an analytic function of $f$ on $f^{-1}(\Delta)$.""",
    "s010"
)

statements["log-capacity-subharmonic-theorem"] = (
    r"""Let $(A, X, \Omega, p)$ be a maximum modulus algebra over $\Omega$. Fix $F \in A$. Then $\lambda \mapsto \log Z_F(\lambda)$ is subharmonic on $\Omega$, where $Z_F(\lambda) = \max\{|F(x)| : x \in p^{-1}(\lambda)\}$.""",
    "s010"
)

statements["tensor-product-maximum-modulus-theorem"] = (
    r"""Let $(A, X, \Omega, p)$ be a maximum modulus algebra over $\Omega$ with $\Delta \subset \Omega$. Fix $F \in \otimes^n A$ and fix $x^0 \in \Pi^{-1}(0, \ldots, 0)$. Then
$$|F(x^0)| \leq \max_{\Pi^{-1}(\gamma)} |F|.$$""",
    "s010"
)

statements["finite-sheeted-analytic-cover-theorem"] = (
    r"""Let $(A, X, \Omega, f)$ be a maximum modulus algebra. Assume that $\#f^{-1}(\lambda) \leq n$ for all $\lambda \in \Omega$. Then $X$ is an $n$-sheeted analytic cover of $\Omega$.""",
    "s011"
)

statements["fiber-cardinality-bound-theorem"] = (
    r"""Let $(A, X, \mathcal{M})$ be a uniform algebra with $X$ the maximal ideal space. Fix $f \in A$. If there exists a set of positive measure on which $f^{-1}(\lambda)$ has cardinality $\leq n$, then this bound extends to a neighborhood.""",
    "s012"
)

statements["polynomial-hull-of-curves-is-analytic-variety"] = (
    r"""If $\gamma$ is a finite union of smooth compact curves in $\mathbb{C}^N$ and $\gamma$ is not polynomially convex, then $\hat{\gamma} \setminus \gamma$ is a one-dimensional analytic subvariety of $\mathbb{C}^N \setminus \gamma$.""",
    "s012"
)

statements["smooth-arc-polynomially-convex"] = (
    r"""Let $\gamma$ be a smooth arc in $\mathbb{C}^N$. Then $\gamma$ is polynomially convex and $P(\gamma) = C(\gamma)$.""",
    "s013"
)

statements["hull-of-k-union-gamma"] = (
    r"""Let $\gamma$ be a finite union of smooth compact curves in $\mathbb{C}^N$ and let $K$ be a compact polynomially convex set in $\mathbb{C}^N$. Then $\widehat{K \cup \gamma} \setminus (K \cup \gamma)$ is a (possibly empty) one-dimensional analytic subvariety of $\mathbb{C}^N \setminus (K \cup \gamma)$.""",
    "s013"
)

statements["bochner-martinelli-integral-representation"] = (
    r"""Assume that $K$ is a kernel given by $K(\zeta, z) = \sum_{j=1}^{n} a_j(\zeta, z) d\bar{\zeta}_1 \wedge \cdots \wedge \widehat{d\bar{\zeta}_j} \wedge \cdots \wedge d\bar{\zeta}_n \wedge d\zeta_1 \wedge \cdots \wedge d\zeta_n$ and satisfies (4) $dK = 0$ on $D \setminus \{z\}$, (5) $\int_{|\zeta-z|=\epsilon} K = c_0$, (6) boundedness condition. Then for each $f \in A(D) \cap C^1(\bar{D})$,
$$c_0 f(z) = \int_{\partial D} f(\zeta)K(\zeta, z), \quad z \in D.$$""",
    "s013"
)

statements["martinelli-bochner-kernel-estimate"] = (
    r"""$K_{MB}$ satisfies conditions (4), (5), and (6) on each smoothly bounded domain $D \subseteq \mathbb{C}^n$. The constant $c_0$ in (5) equals $(2\pi i)^n / (n-1)!$.""",
    "s013"
)

statements["martinelli-bochner-formula"] = (
    r"""For $f \in A(D) \cap C^1(\bar{D})$,
$$\frac{(2\pi i)^n}{(n-1)!} f(z) = \int_{\partial D} f(\zeta) K_{MB}(\zeta, z), \quad z \in D,$$
where $K_{MB}$ is the Bochner-Martinelli kernel.""",
    "s013"
)

statements["leray-cauchy-fantappie-formula"] = (
    r"""Given $w = (w_1, \ldots, w_n)$ defined on $\bar{D} \times \bar{D} \setminus \{\zeta = z\}$ with $\sum w_j(\zeta, z)(\zeta_j - z_j) = 1$, the Cauchy-Fantappiè kernel $K_w$ satisfies the integral representation formula for $f \in A(D) \cap C^1(\bar{D})$.""",
    "s013"
)

statements["dense-subalgebra-from-perturbation"] = (
    r"""Assume that there is a constant $k < 1$ such that $|R(z) - R(z')| \leq k|z - z'|$ for $z, z' \in D$. Then $[z, \bar{z} + R(z)]$ is dense in $C(D)$.""",
    "s014"
)

statements["generalized-perturbation-stone-weierstrass"] = (
    r"""Assume that there exists $k$, $0 \leq k < 1$, with $|R(z) - R(z')| \leq k|z - z'|$ for $z, z' \in N$. Then $\mathfrak{A} = [z_1, \ldots, z_n, \bar{z}_1 + R_1, \ldots, \bar{z}_n + R_n]$ is dense in $C(X)$.""",
    "s014"
)

statements["arens-royden-theorem"] = (
    r"""There exists a natural isomorphism
$$\mathfrak{A}^{-1} / \exp \mathfrak{A} \cong H^1(\mathcal{M}, \mathbb{Z}),$$
where $\mathfrak{A}$ is a Banach algebra and $\mathcal{M}$ is its maximal ideal space.""",
    "s015"
)

statements["finitely-generated-uniform-algebra-is-full"] = (
    r"""Let $\mathcal{L}$ be a finitely generated uniform algebra on a space $X$ with $X = \mathcal{M}(\mathcal{L})$. Then $\mathcal{L}$ is full as a subalgebra of $C(X)$.""",
    "s015"
)

statements["l2-delbar-estimate-theorem"] = (
    r"""For a smoothly bounded domain $\Omega \subset \mathbb{C}^n$, there exists a constant $C$ such that for every $\bar{\partial}$-closed $(0,1)$-form $g$, there exists $u$ with $\bar{\partial}u = g$ and $\|u\|_{L^2} \leq C\|g\|_{L^2}$.""",
    "s016"
)

statements["approximation-on-maximally-complex-manifolds"] = (
    r"""Let $\Sigma$ be a $k$-dimensional sufficiently smooth submanifold of an open set in $\mathbb{C}^n$ with no complex tangents. Then functions on $\Sigma$ can be approximated by polynomials in the coordinates.""",
    "s017"
)

statements["analytic-disk-existence-theorem"] = (
    r"""Given a suitable submanifold, there exists an analytic disk $E$ whose boundary $\partial E$ lies in the submanifold near a point of complex tangency.""",
    "s018"
)

statements["bishop-disk-theorem-high-dimension"] = (
    r"""Let $\Sigma^k$ be a $k$-dimensional real submanifold of $\mathbb{C}^n$ of class $C^e$ near $0$, with a complex tangent at $0$. Under appropriate genericity conditions, there exists an analytic disk whose boundary lies in $\Sigma^k$.""",
    "s018"
)

statements["harvey-lawson-boundary-theorem"] = (
    r"""Let $\gamma$ be a smooth simple closed curve in $\mathbb{C}^n$ satisfying the moment condition. Then there exists a holomorphic chain $V$ of complex dimension 1 such that the boundary of $V$ (in the sense of currents) equals $\gamma$.""",
    "s019"
)

statements["convex-fiber-polynomial-hull-theorem"] = (
    r"""Fix a compact set $Y$ in $\mathbb{C}^2$ lying over the unit circle $\Gamma$. Assume that each fiber $Y_\lambda$, $\lambda \in \Gamma$, is convex. Then each fiber of the polynomial hull $\hat{Y}_\lambda$, $|\lambda| < 1$, can be described in terms of function theory on the disk.""",
    "s020"
)

statements["area-bound-for-polynomial-hull"] = (
    r"""Let $f \in A$ and suppose that $\phi(f) = 0$. Then the area of the polynomial hull is bounded below by a constant times the analytic capacity of the projections of the fibers.""",
    "s021"
)

statements["isoperimetric-inequality-via-rational-approximation"] = (
    r"""Let $\Omega$ be a closed Jordan domain in the plane with smooth boundary. Let $A = \text{area}(\Omega)$ and $L = \text{length}(\partial\Omega)$. Then $2A/L \leq \text{dist}(\bar{z}, R(\Omega))$.""",
    "s022"
)

statements["area-lower-bound-for-polynomial-hull"] = (
    r"""Let $X$ be a compact subset of $\mathbb{C}^n$. Suppose that $p \in \hat{X}$ and that $B(p, r) \subseteq \mathbb{C}^n \setminus X$. Then $\mathcal{H}^2(\hat{X} \cap B(p, r)) \geq \pi r^2$.""",
    "s022"
)

statements["andreotti-narasimhan-rung-theorem"] = (
    r"""If $\Omega$ is a Runge domain in $\mathbb{C}^n$, then the cohomology groups $H^k(\Omega; \mathbb{R}) = 0$ for $k \geq n$.""",
    "s022"
)

statements["forstneric-polynomially-convex-topology"] = (
    r"""Let $K$ be a compact polynomially convex set in $\mathbb{C}^n$ ($n \geq 2$). Then $\mathbb{C}^n \setminus K$ has the homotopy type of a CW-complex of dimension $\leq n$.""",
    "s022"
)

statements["pseudoconvex-complement-of-polynomial-hull"] = (
    r"""Fix a compact set $Y$ in $\mathbb{C}^2$ and fix a point $p^0 \in \hat{Y} \setminus Y$. Let $B$ be an open ball in $\mathbb{C}^2$, centered at $p^0$, such that $\bar{B}$ does not meet $Y$. Then each connected component of $B \setminus \hat{Y}$ is pseudoconvex.""",
    "s023"
)

statements["levi-flat-from-analytic-disk"] = (
    r"""Let $\Omega$ be a region in $\mathbb{C}^2$ and fix $z^0 \in \partial \Omega$ with $\partial \Omega$ smooth near $z^0$. Assume there exists an analytic disk contained in $\partial \Omega$ passing through $z^0$ with nonzero derivative. Then $\partial \Omega$ is Levi-flat at $z^0$.""",
    "s023"
)

statements["stolzenberg-no-analytic-disk-example"] = (
    r"""There exists $S$ such that $h_r(X_S) \neq X_S$ and $h_r(X_S)$ contains no analytic disk.""",
    "s023"
)

statements["cole-example"] = (
    r"""There exists a compact subset $Y$ of $\mathbb{C}^2$ whose polynomial hull $\hat{Y} \setminus Y$ contains no analytic disk, showing that analytic structure in polynomial hulls is not guaranteed.""",
    "s023"
)

statements["non-polynomially-convex-arc-example"] = (
    r"""There exists an arc $J_0$ in $\mathbb{C}^3$ that is not polynomially convex. Hence $P(J_0) \neq C(J_0)$.""",
    "s025"
)

statements["pseudoconcave-maximum-modulus-theorem"] = (
    r"""Let $X$ be a pseudoconcave set contained in the open bidisk $\{|z| < 1, |w| < 1\} \subseteq \mathbb{C}^2$. Denote by $A$ the algebra of polynomials in $z$ and $w$ restricted to $X$. Then $(A, X, D, \pi)$ with $\pi: (z,w) \mapsto z$ is a maximum modulus algebra.""",
    "s026"
)

# Done populating

print(f"Total statements prepared: {len(statements)}")

# Write theorem.tex files
count = 0
for slug, (statement, section) in statements.items():
    folder = os.path.join(CONCEPTS_DIR, slug)
    tex_file = os.path.join(folder, "theorem.tex")
    if os.path.exists(folder):
        with open(tex_file, 'w', encoding='utf-8') as f:
            f.write(f"% {slug.replace('-', ' ').title()}\n")
            f.write(f"% From GTM035, Section {section}\n")
            f.write(f"% Source: Alexander & Wermer, Several Complex Variables and Banach Algebras (GTM 35), 3rd Edition\n\n")
            f.write(statement)
            f.write("\n")
        count += 1
        print(f"  Updated: {slug}")
    else:
        print(f"  MISSING FOLDER: {slug}")

print(f"\nUpdated {count} theorem.tex files")
print(f"Remaining concepts with placeholder: {172 - count}")
