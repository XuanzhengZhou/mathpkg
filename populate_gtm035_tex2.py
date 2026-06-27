#!/usr/bin/env python3
"""Supplementary populate: fill remaining 68 theorem.tex files for GTM035 concepts."""
import os

CONCEPTS_DIR = '/home/a123/文档/mathpkg/pipeline_output/concepts_v7/gtm035'

statements = {}

# Chapter 1 - Basic definitions
statements["function-algebra-on-compact-space"] = (
    r"""Let $X$ be a compact Hausdorff space. A function algebra on $X$ is a subalgebra $\mathfrak{A}$ of $C(X)$ that is closed under uniform convergence on $X$ and contains the constant functions.""",
)

statements["banach-algebra-definition"] = (
    r"""A commutative Banach algebra with unit is a commutative complex algebra $\mathfrak{A}$ equipped with a complete norm $\|\cdot\|$ satisfying $\|xy\| \leq \|x\|\|y\|$ for all $x, y \in \mathfrak{A}$ and $\|1\| = 1$.""",
)

statements["gelfand-transform-definition"] = (
    r"""For $f \in \mathfrak{A}$ and $M \in \mathcal{M}$, the Gelfand transform $\hat{f}(M)$ is the value at $f$ of the homomorphism of $\mathfrak{A}$ into $\mathbb{C}$ corresponding to the maximal ideal $M$.""",
)

statements["maximal-ideal-space-definition"] = (
    r"""$\mathcal{M}(\mathfrak{A})$ is the space of maximal ideals of $\mathfrak{A}$, identified with the set of nonzero complex homomorphisms $\mathfrak{A} \to \mathbb{C}$, equipped with the Gelfand topology (the weak-$^*$ topology).""",
)

# Chapter 11 - Maximum modulus algebras
statements["k-diameter-definition"] = (
    r"""For a finite set $S = \{z_1, \ldots, z_k\} \subset \mathbb{C}$, the $k$-diameter $d_k(S)$ is
$$d_k(S) = \left( \prod_{1 \leq i < j \leq k} |z_i - z_j| \right)^{\frac{2}{k(k-1)}}.$$""",
)

statements["restriction-of-tensor-product-algebra"] = (
    r"""$A^{(n)}$ is the restriction of $\otimes^n A$ to $X^{(n)} = \{(x_1, \ldots, x_n) \in X^n : p(x_1) = \cdots = p(x_n)\}$.""",
)

statements["tensor-restriction-maximum-modulus"] = (
    r"""$(A^{(n)}, X^{(n)}, \Omega, \pi)$ is a maximum modulus algebra, where $\pi(x_1, \ldots, x_n) = p(x_1)$.""",
)

statements["subharmonicity-of-diameter-log"] = (
    r"""For $F \in A$, the function $\lambda \mapsto \log d_n(F(p^{-1}(\lambda)))$ is subharmonic on $\Omega$.""",
)

statements["analytic-cover-corollary"] = (
    r"""If a maximum modulus algebra lies finite-sheeted over $\Omega$, then $X$ is an analytic cover of $\Omega$.""",
)

statements["hardy-extension-lemma"] = (
    r"""Under the hypothesis of the tensor product theorem, there exists $G \in H^\infty(T^n)$ such that $G(0, \ldots, 0) = F(x^0)$ and $G(\zeta) \in \overline{co}(F(\Pi^{-1}(\zeta)))$ for a.a. $\zeta \in T^n$.""",
)

statements["local-maximum-modulus-implies-maximum-modulus"] = (
    r"""If $\mathfrak{A}$ is a uniform algebra whose maximal ideal space satisfies the local maximum modulus principle, then $\mathfrak{A}$ gives rise to a maximum modulus algebra structure over suitable domains.""",
)

# Chapter 12
statements["fiber-cardinality-bound-for-uniform-algebra"] = (
    r"""Let $(A, X, \mathcal{M})$ be a uniform algebra. Fix $p \in \mathcal{M} \setminus X$, $f \in A$, and put $\lambda_0 = f(p)$. Then the fiber $f^{-1}(\lambda_0) \cap X$ has cardinality bounded in terms of the behavior of $f$ on $X$.""",
)

statements["edge-fiber-cardinality-bound"] = (
    r"""For almost all points $\lambda$ on an edge arc $\alpha$, the fiber $f^{-1}(\lambda) \cap \hat{\gamma}$ contains at most $k+s$ points, where $k$ and $s$ are bounds from adjacent regions.""",
)

# Chapter 13 - Integral Kernels
statements["kernel-differential-is-closed"] = (
    r"""Fix $z \in D$, then $dK_w(\zeta, z) = 0$ for $\zeta \in D \setminus \{z\}$.""",
)

statements["kernel-residue-at-diagonal"] = (
    r"""Fix $z \in D$, and choose $\epsilon > 0$ such that the closed ball $\{|\zeta - z| \leq \epsilon\}$ is contained in $D$. Then
$$1 = a_0 \int_{\{|\zeta - z| = \epsilon\}} K_w(\zeta, z),$$
where $a_0 = (-1)^{n(n-1)/2}(n-1)!/(2\pi i)^n$.""",
)

# Chapter 14 - Perturbations
statements["perturbed-stone-weierstrass-polynomial-sequence"] = (
    r"""Given an integer $n \geq 1$, there exists a polynomial $P_n$ approximating $1/w$ on a closed semidisk $S \subset \{\text{Re } w \geq 0\}$.""",
)

statements["polynomial-approximation-with-estimates"] = (
    r"""There exists a sequence of polynomials $\{P_n\}$ such that $P_n(w) \to 1/w$ on $S \setminus \{0\}$ and $|P_n(w)| \leq C/|w|$ for $w \in S \setminus \{0\}$.""",
)

statements["delbar-representation-lemma"] = (
    r"""Let $\phi \in C_0^1(N)$. Fix $z \in N$. Then
$$\phi(z) = -\frac{(n-1)!}{(2\pi i)^n} \int_N \bar{\partial} \phi(\zeta) \wedge K(\zeta, z).$$""",
)

statements["measure-orthogonality-and-delbar"] = (
    r"""Let $\mu$ be a measure on $X$ with $\|\mu\| < \infty$ and $\mu \perp \mathfrak{A}$. Fix $z$ such that $\int_X d|\mu|(\zeta)/|\zeta - z|^{2n-1} < \infty$. Then $\int_X K_j(\zeta, z) d\mu(\zeta) = 0$ for all $j$.""",
)

# Chapter 15 - Cohomology
statements["cech-cohomology-definition"] = (
    r"""For a compact space $X$ with open cover $\mathcal{U} = \{U_\alpha\}$, the Čech cohomology group $H^p(\mathcal{U}, \mathbb{Z})$ is defined via alternating cochains $c^p(U_{\alpha_0}, \ldots, U_{\alpha_p})$ with integer values, with coboundary operator $\delta$.""",
)

statements["refinement-homomorphism"] = (
    r"""$\rho$ induces a homomorphism $K^{\mathcal{U}, \mathcal{V}} : H^p(\mathcal{U}, \mathbb{Z}) \rightarrow H^p(\mathcal{V}, \mathbb{Z})$ for any refinement $\mathcal{V}$ of $\mathcal{U}$.""",
)

statements["refinement-independence"] = (
    r"""$K^{\mathcal{U}, \mathcal{V}}$ depends only on $\mathcal{U}$ and $\mathcal{V}$, not on the choice of the refining map $\phi$.""",
)

statements["first-cohomology-limit-group"] = (
    r"""$H^1(X, \mathbb{Z})$ is the limit group of the direct system of groups $\{H^1(\mathcal{U}, \mathbb{Z}) \mid \mathcal{U}\}$ over all open covers $\mathcal{U}$ of $X$.""",
)

statements["full-subalgebra-definition"] = (
    r"""A subalgebra $\mathcal{L}$ of $C(X)$ is full if for every $f \in \mathcal{L}^{-1}$, the cohomology class $\eta(f) \in H^1(X, \mathbb{Z})$ vanishes whenever $f$ can be written locally as an exponential of elements of $\mathcal{L}$.""",
)

statements["algebra-of-locally-holomorphic-functions"] = (
    r"""$\mathcal{H}(X) = \{f \in C(X) \mid \exists \text{ neighborhood } U \text{ of } X \text{ and } \exists F \in H(U) \text{ with } F = f \text{ on } X\}$.""",
)

statements["hx-is-full"] = (
    r"""$\mathcal{H}(X)$ is a full subalgebra of $C(X)$.""",
)

statements["higher-cohomology-of-maximal-ideal-space"] = (
    r"""Let $\mathfrak{A}$ be a Banach algebra with $n$ generators. Then $H^p(\mathcal{M}, \mathbb{Z}) = 0$ for $p \geq n$.""",
)

# Chapter 16 - ∂̄ in smoothly bounded domains
statements["distributional-delbar-derivative"] = (
    r"""Let $u \in L^2(\Omega)$. Fix $k \in L^2(\Omega)$ and fix $j$. We say $\partial u / \partial \bar{z}_j = k$ in the distributional sense if $\int_\Omega u \cdot \partial \phi / \partial z_j = -\int_\Omega k \phi$ for all test functions $\phi \in C_0^\infty(\Omega)$.""",
)

statements["l2-delbar-closed-operator"] = (
    r"""The operator $T$ is the closure of $\bar{\partial}$ acting on smooth forms, considered as a densely-defined operator on $L^2$ spaces of differential forms.""",
)

statements["l2-adjoint-operator"] = (
    r"""$S$ is the Hilbert space adjoint of the $\bar{\partial}$-operator $T$, defined on an appropriate dense domain in the $L^2$ space of $(0,1)$-forms.""",
)

statements["closed-densely-defined-operator"] = (
    r"""$A$ is closed if for each sequence $g_n \in \mathcal{D}_A$ with $g_n \to g$ and $Ag_n \to h$, we have $g \in \mathcal{D}_A$ and $Ag = h$.""",
)

statements["integration-by-parts-for-delbar"] = (
    r"""For $f \in \mathcal{D}_S \cap C_{0,1}^1(\bar{\Omega})$, an integration by parts formula relates $\|Sf\|^2$ to $\|\bar{\partial}f\|^2$ plus boundary terms.""",
)

statements["elliptic-regularity-for-delbar"] = (
    r"""Let $B = \{z \in \mathbb{C}^n \mid |z| < 1\}$. Let $u \in L^2(B)$. Assume that for each $j$, $\partial u / \partial \bar{z}_j$, defined as distribution on $B$, is continuous. Then $u$ is continuous.""",
)

statements["l2-extension-for-delbar"] = (
    r"""Let $\Omega$ be a bounded domain in $\mathbb{C}^n$ and $u \in L^2(\Omega)$. If all distributional $\bar{\partial}$-derivatives of $u$ lie in $L^2$, then $u$ can be extended as an $L^2$ solution of the $\bar{\partial}$-equation.""",
)

# Chapter 17 - Manifolds without complex tangents
statements["complex-tangent-definition"] = (
    r"""A complex tangent to a real submanifold $\Sigma$ at $x$ is a complex line, i.e., a complex-linear subspace of $\mathbb{C}^n$ of complex dimension 1, contained in the real tangent space $T_x(\Sigma)$.""",
)

statements["submanifold-definition"] = (
    r"""Let $\Omega$ be an open set in $\mathbb{C}^n$. A closed subset $\Sigma \subset \Omega$ is a $k$-dimensional submanifold of $\Omega$ of class $C^e$ if for each $x_0 \in \Sigma$ there exist a neighborhood $U$ of $x_0$ and real-valued functions $\rho_1, \ldots, \rho_{2n-k}$ in $C^e(U)$ with linearly independent gradients such that $\Sigma \cap U = \{x \in U : \rho_1(x) = \cdots = \rho_{2n-k}(x) = 0\}$.""",
)

statements["no-complex-tangents-lemma"] = (
    r"""Under the hypotheses of the approximation theorem, the submanifold $\Sigma$ has no complex tangents.""",
)

statements["function-extension-from-submanifold"] = (
    r"""Fix a compact set $K$ on $\Sigma$. Let $u$ be a function of class $C^e$ defined on $\Sigma$. Then there exists a function $U$ of class $C^1$ in $\mathbb{C}^n$ extending $u$ with controlled derivatives.""",
)

statements["weinstock-approximation-theorem"] = (
    r"""An alternative elementary proof of the approximation theorem on maximally complex submanifolds, based on an integral transform, was given by Weinstock.""",
)

# Chapter 18 - Submanifolds of high dimension
statements["n-sphere-hull-property"] = (
    r"""Let $S$ be a set in $\mathbb{C}^n$ homeomorphic to the $n$-sphere. Then the polynomial hull $h(S) \neq S$.""",
)

statements["harmonic-conjugate-operator"] = (
    r"""$H_1$ is the operator that takes a real-valued function on the unit circle to its harmonic conjugate, yielding the boundary values of the analytic function in the disk (the Hilbert transform on the circle).""",
)

statements["boundary-functions-definition"] = (
    r"""Let $w_2, \ldots, w_n$ be smooth boundary functions on $\Gamma$. Then $w = (w_2, \ldots, w_n)$ is a map of $\Gamma$ into $\mathbb{C}^{n-1}$. For $x \in H_1$, these provide the boundary data for the Bishop disk construction.""",
)

statements["schlicht-function-lemma"] = (
    r"""Let $w_2, \ldots, w_n$ be smooth boundary functions with small sup-norm such that $w_2$ is schlicht (one-to-one). Then the corresponding Bishop disk is embedded.""",
)

statements["parametric-representation-of-submanifold"] = (
    r"""Under appropriate nondegeneracy conditions, the submanifold $\Sigma^k$ can be described parametrically near $0$ by equations after a complex-linear change of coordinates.""",
)

# Chapter 19 - Boundaries of analytic varieties
statements["jump-across-boundary-arc-lemma"] = (
    r"""Let $U_i, U_j$ be regions with a common smooth boundary arc $\alpha$, with $\alpha$ positively oriented for $U_j$. Functions constructed via Cauchy integrals on each side have a jump across $\alpha$ equal to the original data.""",
)

statements["analytic-extension-from-boundary-lemma"] = (
    r"""Let $G$ be a function continuous on $(\Omega \cup \alpha) \times \{|w| > R\}$ and analytic on $\Omega \times \{|w| > R\}$. Under polynomial growth conditions, $G$ extends analytically across the boundary.""",
)

statements["holomorphic-chain-definition"] = (
    r"""A holomorphic chain of complex dimension $k$ in an open set $\Omega \subset \mathbb{C}^n$ is a formal sum $\sum n_j V_j$, where the branches $\{V_j\}$ constitute a locally finite family of irreducible analytic subvarieties of complex dimension $k$ in $\Omega$ and the $n_j$ are nonzero integers (possibly negative).""",
)

statements["maximally-complex-manifold-definition"] = (
    r"""$M$ (of real dimension $2p - 1$) is maximally complex if, for all $z \in M$, the real tangent space $T_z(M)$ contains a complex subspace of complex dimension $p - 1$.""",
)

statements["moment-condition-definition"] = (
    r"""$M$ satisfies the moment condition if $\int_M \omega = 0$ for all $(p, p-1)$-forms $\omega$ such that $\bar{\partial}\omega = 0$.""",
)

statements["kernel-identity-lemma"] = (
    r"""$-\bar{\partial}_{\zeta} K_1(\zeta, z) = \bar{\partial}_z K(\zeta, z)$, where $K$ is the Martinelli-Bochner kernel and $K_1$ is a related kernel used in the Harvey-Lawson theory.""",
)

statements["type-three-zero-restriction"] = (
    r"""Let $\alpha$ be a form of type $(3,0)$ defined on a neighborhood of a maximally complex real $3$-manifold $M$ in $\mathbb{C}^3$. Then the restriction of $\alpha$ to $M$ is identically zero.""",
)

statements["analytic-disk-from-3-manifold-boundary"] = (
    r"""Let $\psi(\zeta, \eta)$ be a function analytic on a neighborhood of $M$ in $\mathbb{C}^3$, where $\zeta = (\zeta_1, \zeta_2)$. The associated kernel construction produces an analytic disk from the boundary data on $M$.""",
)

# Chapter 20 - Polynomial hulls over the circle
statements["fiber-hull-characterization"] = (
    r"""Let $Y$ be a compact set in $\mathbb{C}^2$ lying over the unit circle $\Gamma$. Assume each fiber $Y_\lambda$ ($\lambda \in \Gamma$) is convex. Then each fiber $\hat{Y}_\lambda$ ($|\lambda| < 1$) is also convex and can be characterized by function theory.""",
)

statements["function-representation-for-hulls-over-circle"] = (
    r"""The algebra $\mathcal{F}$ consists of all functions $f$ on $\{|\lambda| < 1\}$ that can be written in the form $f(\lambda) = \int_{Y_\lambda} g(\lambda, \cdot) d\mu_\lambda$ for suitable choices of representing measures.""",
)

statements["explicit-hull-over-circle"] = (
    r"""For each $\lambda$ in the open unit disk, the fiber $\hat{Y}_\lambda$ of the polynomial hull can be described explicitly in terms of the original fibers $Y_\lambda$ on the circle via an analytic selection process.""",
)

# Chapter 21 - Areas
statements["distance-to-rational-algebra"] = (
    r"""Let $K$ be a compact subset of the plane. The distance from a function $g \in C(K)$ to the rational algebra $R(K)$ can be estimated via the Cauchy transform and analytic capacity.""",
)

statements["dist-zbar-rk-bound"] = (
    r"""$\text{dist}(\bar{z}, R(K)) \leq \left( \frac{1}{\pi} \text{ area}(K) \right)^{1/2}$.""",
)

# Chapter 22 - Topology of hulls
statements["plurisubharmonic-exhaustion-for-polynomially-convex"] = (
    r"""Let $K$ be polynomially convex in $\mathbb{C}^n$ with $K \subseteq U$, $U$ open and bounded. Then there exists a smooth strictly plurisubharmonic function $\rho : \mathbb{C}^n \to \mathbb{R}$ and $R > 0$ such that $K \subseteq \{\rho < 0\} \subseteq \{\rho \leq R\} \subseteq U$.""",
)

statements["linking-number-theorem"] = (
    r"""For $K$ polynomially convex in $\mathbb{C}^n$, the linking number of $\hat{X} \setminus X$ with $X$ gives topological obstructions to the structure of the polynomial hull.""",
)

# Chapter 23 - Pseudoconvex sets
statements["levi-pseudoconvex-boundary-definition"] = (
    r"""$\partial \Omega$ is pseudoconvex in the sense of Levi at $z^0$ if the defining function $\rho$ satisfies
$$\sum_{j,k=1}^{n} \frac{\partial^2 \rho}{\partial z_j \partial \bar{z}_k}(z^0) w_j \bar{w}_k \geq 0$$
for all $w \in \mathbb{C}^n$ with $\sum_{j=1}^{n} \frac{\partial \rho}{\partial z_j}(z^0) w_j = 0$.""",
)

statements["pseudoconvex-domain-definition"] = (
    r"""Let $\Omega$ be a domain in $\mathbb{C}^n$. $\Omega$ is pseudoconvex if there exists a continuous plurisubharmonic exhaustion function on $\Omega$.""",
)

statements["levi-flat-boundary-of-polynomial-hull"] = (
    r"""Let $Y$ be a compact set in $\mathbb{C}^2$ lying over the circle $\{|z_1| = 1\}$. Let $\Omega$ be the interior of $\hat{Y}$. Then $\partial \Omega$ is Levi-flat at each smooth point $z^0 = (z_1^0, z_2^0)$ with $|z_1^0| < 1$.""",
)

# Chapter 24 - Examples
statements["rational-algebra-on-compact-set"] = (
    r"""Let $X$ be a compact subset of $\mathbb{C}^n$. Then $R_0(X)$ denotes the algebra of continuous functions $f$ on $X$ of the form $f = A/B$, where $A$ and $B$ are polynomials and $B$ has no zero on $X$. $R(X)$ denotes the closure of $R_0(X)$ in the uniform norm over $X$.""",
)

statements["rationally-convex-hull-definition"] = (
    r"""Let $X$ be a compact subset of $\mathbb{C}^n$. The rationally convex hull of $X$, denoted $h_r(X)$, is the set $\{z \in \mathbb{C}^n : |f(z)| \leq \max_X |f| \text{ for all rational functions } f \text{ holomorphic on } X\}$.""",
)

statements["polynomial-sequence-construction-lemma"] = (
    r"""There exist two sequences of positive constants $c_j$ and $\epsilon_j$ with $c_1 = 1/10$, $c_{j+1} \leq (1/10)c_j$, and a sequence of polynomials $P_n$ in $z$ and $w$ with controlled growth on specified sets.""",
)

statements["polynomial-set-definition"] = (
    r"""With $P_n, \epsilon_n$ chosen as in the construction lemma, specific compact sets are defined via conditions on the polynomial values, used in the Stolzenberg and Cole examples.""",
)

statements["branch-functions-definition"] = (
    r"""$\mathcal{K}$ is the collection of all $2^n$ functions of the form $\sum_{j=1}^{n} c_j \rho_j \beta_j$ on $\gamma_1$, where each $\rho_j$ is a constant $= 1$ or $= -1$. These are the algebraic branch functions of the constructed example.""",
)

statements["harmonic-measure-estimate"] = (
    r"""Let $\Omega$ be a bounded domain in $\mathbb{C}$ such that $0 \in \partial \Omega$ and $\Omega$ is disjoint from the negative real axis. Then the harmonic measure of $\alpha_r$ with respect to $\Omega_r$ is $O(\sqrt{r})$ as $r \to 0$.""",
)

# Chapter 25 - Historical comments
statements["pseudoconcave-set-definition"] = (
    r"""Let $\Omega$ be a domain in $\mathbb{C}^n$ and let $E$ be a relatively closed subset of $\Omega$. $E$ is called pseudoconcave in $\Omega$ if the open set $\Omega \setminus E$ is pseudoconvex.""",
)

# Write them all
count = 0
for slug, (statement,) in statements.items():
    folder = os.path.join(CONCEPTS_DIR, slug)
    tex_file = os.path.join(folder, "theorem.tex")
    if os.path.exists(folder):
        with open(tex_file, 'w', encoding='utf-8') as f:
            f.write(f"% {slug.replace('-', ' ').title()}\n")
            f.write(f"% From GTM035\n")
            f.write(f"% Source: Alexander & Wermer, Several Complex Variables and Banach Algebras (GTM 35), 3rd Edition\n\n")
            f.write(statement)
            f.write("\n")
        count += 1
        print(f"  Updated: {slug}")
    else:
        print(f"  MISSING FOLDER: {slug}")

print(f"\nUpdated {count} additional theorem.tex files")
