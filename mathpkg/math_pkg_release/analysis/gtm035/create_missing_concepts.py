#!/usr/bin/env python3
"""Create all missing concept files for GTM035 sections 12,15,19-26."""
import os, json, hashlib

BASE = "/home/a123/文档/mathpkg/pipeline_output/concepts_v7/gtm035"
DATE = "2026-06-25"
AGENT = "v7-section-test"

concepts = {
    # === SECTION 12: Hulls of Curves and Arcs ===
    "s012_Section_12": [
        {
            "slug": "polynomial-hull-of-curves-is-analytic-variety",
            "title_en": "Polynomial Hull of Curves is a One-Dimensional Analytic Variety",
            "title_zh": "曲线的多项式包是一维解析簇",
            "type": "theorem",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Theorem 12.1.} Let $\gamma_1, \gamma_2, \ldots, \gamma_p$ be a finite collection of compact smooth curves in $\mathbb{C}^N$ and let $\gamma$ be their union. If $\gamma$ is not polynomially convex, then $\hat{\gamma} \setminus \gamma$ is a one-dimensional analytic subvariety of $\mathbb{C}^N \setminus \gamma$.""",
        },
        {
            "slug": "peak-point-lemma-for-uniform-algebras",
            "title_en": "Peak Point Lemma for Uniform Algebras",
            "title_zh": "一致代数的峰值点引理",
            "type": "lemma",
            "domain": "analysis",
            "subdomain": "banach-algebras",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Lemma 12.2.} Let $(A, X, \mathcal{M})$ be a uniform algebra. Fix $p \in \mathcal{M} \setminus X$, $f \in A$, and put $\lambda_0 = f(p)$. Define $K = \{ \lambda : |\lambda - \lambda_0| \leq r, \alpha \leq \arg(\lambda - \lambda_0) \leq \beta \}$ where $-\pi/2 < \alpha < \beta < 3\pi/2$. Assume that for some compact neighborhood $\mathcal{N}$ of $p$ in $\mathcal{M} \setminus X$ we have $f(\mathcal{N}) \subseteq K$. Then $p$ is not a peak-point of the algebra $A|_{f^{-1}(\lambda_0)}$ on the space $f^{-1}(\lambda_0)$.""",
        },
        {
            "slug": "smooth-arc-is-polynomially-convex",
            "title_en": "Smooth Arc is Polynomially Convex",
            "title_zh": "光滑弧是多项式凸的",
            "type": "theorem",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Theorem 12.4.} Let $\gamma$ be a smooth arc in $\mathbb{C}^N$. Then $\gamma$ is polynomially convex and $P(\gamma) = C(\gamma)$.""",
        },
        {
            "slug": "polynomial-hull-of-k-union-curve",
            "title_en": "Polynomial Hull of $K \cup \gamma$",
            "title_zh": "$K \cup \gamma$的多项式包",
            "type": "theorem",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Theorem 12.5.} Let $\gamma$ be a finite union of smooth compact curves in $\mathbb{C}^N$ and let $K$ be a compact polynomially convex set in $\mathbb{C}^N$. Then $\widehat{K \cup \gamma} \setminus (K \cup \gamma)$ is a (possibly empty) one-dimensional analytic subvariety of $\mathbb{C}^N \setminus (K \cup \gamma)$.""",
        },
    ],

    # === SECTION 15: First Cohomology Group of Maximal Ideal Space ===
    "s015_Section_15": [
        {
            "slug": "arens-royden-theorem",
            "title_en": "Arens-Royden Theorem",
            "title_zh": "Arens-Royden定理",
            "type": "theorem",
            "domain": "analysis",
            "subdomain": "banach-algebras",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Theorem 15.3 (Arens-Royden).} Let $\mathfrak{A}$ be a Banach algebra with maximal ideal space $X = \mathcal{M}(\mathfrak{A})$. Then there exists a natural isomorphism
$$\Phi : \mathfrak{A}^{-1} / \exp \mathfrak{A} \longrightarrow H^1(X, \mathbb{Z}).$$""",
        },
        {
            "slug": "natural-homomorphism-ckx-to-h1",
            "title_en": "Natural Homomorphism $C(X)^{-1} \to H^1(X, \mathbb{Z})$",
            "title_zh": "自然同态 $C(X)^{-1} \to H^1(X, \mathbb{Z})$",
            "type": "theorem",
            "domain": "topology",
            "subdomain": "cech-cohomology",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Theorem 15.4.} Let $X$ be a compact space. There exists a natural homomorphism
$$\eta : C(X)^{-1} \rightarrow H^1(X, \mathbb{Z})$$
such that $\eta$ is onto and $\ker \eta = \exp C(X)$.""",
        },
        {
            "slug": "full-subalgebra",
            "title_en": "Full Subalgebra",
            "title_zh": "完全子代数",
            "type": "definition",
            "domain": "analysis",
            "subdomain": "banach-algebras",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Definition 15.3.} Let $X$ be a compact space and $\mathcal{L}$ a subalgebra of $C(X)$. $\mathcal{L}$ is \textit{full} if
\begin{enumerate}
\item $\eta$ maps $\mathcal{L}^{-1}$ onto $H^1(X, \mathbb{Z})$,
\item $x \in \mathcal{L}^{-1}$ and $\eta(x) = 0$ imply $\exists y \in \mathcal{L}$ with $x = e^y$.
\end{enumerate}""",
        },
        {
            "slug": "holomorphic-germ-algebra",
            "title_en": "Holomorphic Germ Algebra $\mathcal{H}(X)$",
            "title_zh": "全纯芽代数 $\mathcal{H}(X)$",
            "type": "definition",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "intermediate",
            "theorem_tex": r"""\textbf{Definition 15.4.} Let $X$ be a compact polynomially convex subset of $\mathbb{C}^n$.
$$\mathcal{H}(X) = \{f \in C(X) \mid \exists \text{ neighborhood } U \text{ of } X \text{ and } \exists F \in H(U) \text{ with } F = f \text{ on } X\}.$$""",
        },
        {
            "slug": "holomorphic-germ-algebra-is-full",
            "title_en": "$\mathcal{H}(X)$ is Full",
            "title_zh": "$\mathcal{H}(X)$是完全的",
            "type": "lemma",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Lemma 15.5.} Let $X$ be a compact polynomially convex subset of $\mathbb{C}^n$. Then $\mathcal{H}(X)$ is full.""",
        },
        {
            "slug": "finitely-generated-uniform-algebra-is-full",
            "title_en": "Finitely Generated Uniform Algebra is Full",
            "title_zh": "有限生成一致代数是完全的",
            "type": "lemma",
            "domain": "analysis",
            "subdomain": "banach-algebras",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Lemma 15.6.} Let $\mathcal{L}$ be a finitely generated uniform algebra on a space $X$ with $X = \mathcal{M}(\mathcal{L})$. Then $\mathcal{L}$ is full as a subalgebra of $C(X)$.""",
        },
        {
            "slug": "first-cech-cohomology-definition",
            "title_en": "First Čech Cohomology Group $H^1(X, \mathbb{Z})$",
            "title_zh": "第一Čech上同调群 $H^1(X, \mathbb{Z})$",
            "type": "definition",
            "domain": "topology",
            "subdomain": "cech-cohomology",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Definition 15.2.} Let $X$ be a compact Hausdorff space. $H^1(X, \mathbb{Z})$ is the limit group of the direct system of groups $\{H^1(\mathcal{U}, \mathbb{Z}) \mid \mathcal{U}\}$, where $\mathcal{U}$ runs over all open coverings of $X$ directed by refinement.""",
        },
    ],

    # === SECTION 19: Harvey-Lawson Boundary Theorem ===
    "s019_Section_19": [
        {
            "slug": "plemelj-theorem",
            "title_en": "Plemelj's Theorem (Sokhotski-Plemelj)",
            "title_zh": "Plemelj定理",
            "type": "theorem",
            "domain": "analysis",
            "subdomain": "complex-analysis",
            "difficulty": "intermediate",
            "theorem_tex": r"""\textbf{Plemelj's Theorem.} Let $\alpha$ be a smooth oriented curve and let $g$ be a Hölder continuous function on $\alpha$. Define
$$G(z) = \frac{1}{2\pi i} \int_{\alpha} \frac{g(\zeta)}{\zeta - z} d\zeta$$
for $z \notin \alpha$, and let $G^+$, $G^-$ denote the restrictions to the two sides of $\alpha$. Then $G^+$ and $G^-$ have continuous extensions to $\alpha$, and on $\alpha$:
$$G^+(z) - G^-(z) = g(z), \quad z \in \alpha.$$""",
        },
        {
            "slug": "harvey-lawson-boundary-theorem",
            "title_en": "Harvey-Lawson Boundary Theorem for Curves in $\mathbb{C}^2$",
            "title_zh": "Harvey-Lawson边界定理（$\mathbb{C}^2$中曲线）",
            "type": "theorem",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Theorem 19.1 (Harvey-Lawson).} Let $\gamma$ be a smooth simple closed curve in $\mathbb{C}^2$. Assume that the projection $\pi : (z, w) \mapsto z$ is a local diffeomorphism on $\gamma$ and that $\gamma$ satisfies the moment condition:
$$\int_{\gamma} z^n w^m dz = 0, \quad n, m \geq 0.$$
Then there exists a one-dimensional analytic subvariety $\Sigma$ of $\mathbb{C}^2 \setminus \gamma$ such that $b\Sigma = \pm \gamma$ in the sense of Stokes' theorem.""",
        },
        {
            "slug": "holomorphic-chain",
            "title_en": "Holomorphic Chain",
            "title_zh": "全纯链",
            "type": "definition",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Definition 19.1.} Let $\Omega$ be an open set in $\mathbb{C}^n$. A \textit{holomorphic chain} of complex dimension $k$ in $\Omega$ is a formal sum $\sum n_j V_j$, where the branches $\{V_j\}$ constitute a locally finite family of irreducible analytic subvarieties of complex dimension $k$ in $\Omega$ and the $n_j$ are nonzero integers.""",
        },
        {
            "slug": "maximally-complex-manifold",
            "title_en": "Maximally Complex Manifold",
            "title_zh": "极大复流形",
            "type": "definition",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Definition 19.2.} A real manifold $M$ of dimension $2p-1$ in $\mathbb{C}^n$ is \textit{maximally complex} if, for all $z \in M$, the tangent space $T_z(M)$ contains a complex subspace of complex dimension $p-1$.""",
        },
        {
            "slug": "moment-condition",
            "title_en": "Moment Condition for Boundaries of Analytic Varieties",
            "title_zh": "解析簇边界的矩条件",
            "type": "definition",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Definition 19.3.} A real manifold $M$ of dimension $2p-1$ in $\mathbb{C}^n$ satisfies the \textit{moment condition} if $\int_M \omega = 0$ for all $(p, p-1)$-forms $\omega$ such that $\bar{\partial}\omega = 0$.""",
        },
        {
            "slug": "jump-theorem-bochner-martinelli",
            "title_en": "Jump Theorem for Bochner-Martinelli Integral",
            "title_zh": "Bochner-Martinelli积分的跳跃定理",
            "type": "theorem",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Jump Theorem.} Let $\alpha$ be a smooth oriented hypersurface in $\mathbb{C}^n$ and let $g$ be a smooth function on $\alpha$. Define
$$G^{\pm}(z) = \int_{\alpha} g(\zeta) K_{BM}(\zeta, z)$$
for $z$ on the two sides $\Omega^{\pm}$ of $\alpha$. Then $G^{+}$ and $G^{-}$ have continuous extensions to $\alpha$, and on $\alpha$:
$$G^{+}(z) - G^{-}(z) = g(z), \quad z \in \alpha.$$""",
        },
    ],

    # === SECTION 20: Polynomial Hulls of Sets Over the Circle ===
    "s020_Section_20": [
        {
            "slug": "hull-over-circle-with-convex-fibers",
            "title_en": "Polynomial Hull Over Circle with Convex Fibers",
            "title_zh": "圆上凸纤维的多项式包",
            "type": "theorem",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Theorem 20.2.} Fix a compact set $Y$ in $\mathbb{C}^2$ lying over the unit circle $\Gamma$. Assume that $Y_{\lambda}$ is convex for every $\lambda \in \Gamma$. Then $\hat{Y} \setminus Y$ equals the union of all graphs $\{(\lambda, f(\lambda)) : |\lambda| < 1\}$ with $f \in \mathcal{F}$, where $\mathcal{F}$ is the space of all $f \in H^{\infty}$ such that $f(\lambda) \in Y_{\lambda}$ a.e. on $\Gamma$.""",
        },
        {
            "slug": "fiberwise-convexity-of-hull-over-circle",
            "title_en": "Fiberwise Convexity of Hull Over Circle",
            "title_zh": "圆上包的逐纤维凸性",
            "type": "theorem",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Theorem 20.3.} Let $Y$ be a compact set in $\mathbb{C}^2$ lying over $\Gamma$. Assume that each fiber $Y_{\lambda}$, $\lambda \in \Gamma$, is convex. Then each fiber $\hat{Y}_{\lambda}$, $|\lambda| < 1$, is also convex.""",
        },
        {
            "slug": "rational-function-description-of-hull-fibers",
            "title_en": "Rational Function Description of Hull Fibers Over the Circle",
            "title_zh": "圆上包纤维的有理函数描述",
            "type": "theorem",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Theorem 20.5.} Let $P, Q$ be polynomials with $Q \neq 0$ on $\Gamma$ and $|P(\lambda)/Q(\lambda)| \leq 1$ on $\Gamma$. Define $Y = \{(\lambda, w) : \lambda \in \Gamma, |w - P(\lambda)/Q(\lambda)| \leq 1/|Q(\lambda)|\}$. Then for each $\lambda$ with $|\lambda| < 1$, $\hat{Y}_{\lambda}$ is a nondegenerate closed disk explicitly described by a Pick matrix condition: $\hat{Y}_{\lambda} = \{ \frac{P(\lambda)}{Q(\lambda)} + \frac{w}{Q_0(\lambda)} : D(\lambda, w) \geq 0 \}$.""",
        },
    ],

    # === SECTION 21: Area Theorems ===
    "s021_Section_21": [
        {
            "slug": "area-lower-bound-for-spectrum",
            "title_en": "Area Lower Bound for Spectrum in Uniform Algebras",
            "title_zh": "一致代数中谱的面积下界",
            "type": "theorem",
            "domain": "analysis",
            "subdomain": "banach-algebras",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Theorem 21.1.} Let $A$ be a uniform algebra on a compact space $X$ with maximal ideal space $M$. Let $\phi \in M$ and let $\mu$ be a representing measure supported on $X$ for $\phi$. Let $f \in A$ with $\phi(f) = 0$. Then
$$\pi \int |f|^2 d\mu \leq \operatorname{area}(f(M)).$$""",
        },
        {
            "slug": "ahlfors-beurling-estimate",
            "title_en": "Ahlfors-Beurling Estimate for Cauchy Potential",
            "title_zh": "Cauchy势的Ahlfors-Beurling估计",
            "type": "lemma",
            "domain": "analysis",
            "subdomain": "complex-analysis",
            "difficulty": "intermediate",
            "theorem_tex": r"""\textbf{Lemma 21.2 (Ahlfors-Beurling).} Let $K$ be a compact subset of the plane and set
$$F(z) = \iint_K \frac{1}{\zeta - z} du\,dv, \quad \zeta = u + iv.$$
Then $F$ is continuous on the plane and $\|F\|_K \leq (\pi \operatorname{area}(K))^{1/2}$.""",
        },
        {
            "slug": "distance-to-rk-bound",
            "title_en": "Distance from $\bar{z}$ to $R(K)$",
            "title_zh": "$\bar{z}$到$R(K)$的距离",
            "type": "lemma",
            "domain": "analysis",
            "subdomain": "complex-analysis",
            "difficulty": "intermediate",
            "theorem_tex": r"""\textbf{Lemma 21.3.} Let $K$ be a compact subset of $\mathbb{C}$. Then
$$\operatorname{dist}(\bar{z}, R(K)) \leq \left( \frac{1}{\pi} \operatorname{area}(K) \right)^{1/2}.$$""",
        },
        {
            "slug": "isoperimetric-inequality-via-rational-approximation",
            "title_en": "Isoperimetric Inequality via Rational Approximation",
            "title_zh": "通过有理逼近的等周不等式",
            "type": "proposition",
            "domain": "analysis",
            "subdomain": "complex-analysis",
            "difficulty": "intermediate",
            "theorem_tex": r"""\textbf{Proposition 21.4.} Let $\Omega$ be a closed Jordan domain in the plane with smooth boundary. Let $A = \operatorname{area}(\Omega)$ and $L = \operatorname{length}(\partial \Omega)$. Then
$$\frac{2A}{L} \leq \operatorname{dist}(\bar{z}, R(\Omega)).$$""",
        },
        {
            "slug": "area-of-analytic-variety-formula",
            "title_en": "Area Formula for One-Dimensional Analytic Varieties",
            "title_zh": "一维解析簇的面积公式",
            "type": "theorem",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Theorem 21.9.} Let $V$ be a one-dimensional analytic subvariety of a domain in $\mathbb{C}^n$. Then
$$\operatorname{area}(V) = \sum_{j=1}^{n} \int_V \frac{i}{2} dz_j \wedge d\bar{z}_j.$$""",
        },
        {
            "slug": "rutishauser-corollary-higher-dim",
            "title_en": "Rutishauser-Type Corollary for Polynomial Hulls",
            "title_zh": "多项式包的Rutishauser型推论",
            "type": "corollary",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Corollary 21.10.} Let $X$ be a compact subset of $\mathbb{C}^n$. Suppose that $p \in \hat{X}$ and $B(p, r) \subseteq \mathbb{C}^n \setminus X$. Then $\mathcal{H}^2(\hat{X} \cap B(p, r)) \geq \pi r^2$.""",
        },
    ],

    # === SECTION 22: Topology of Hulls ===
    "s022_Section_22": [
        {
            "slug": "andreotti-narasimhan-theorem",
            "title_en": "Andreotti-Narasimhan Theorem on Runge Domain Homology",
            "title_zh": "Runge域同调的Andreotti-Narasimhan定理",
            "type": "theorem",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Theorem 22.2 (Andreotti-Narasimhan).} If $\Omega$ is a Runge domain in $\mathbb{C}^n$, then
$$H_k(\Omega; G) = 0 \quad \text{for } k \geq n.$$""",
        },
        {
            "slug": "forstneric-theorem",
            "title_en": "Forstnerič Theorem on Complement Homology",
            "title_zh": "补空间同调的Forstnerič定理",
            "type": "theorem",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Theorem 22.3 (Forstnerič).} Let $K$ be a compact polynomially convex set in $\mathbb{C}^n$ ($n \geq 2$). Then
$$H_k(\mathbb{C}^n \setminus K; G) = 0 \quad \text{for } 1 \leq k \leq n-1$$
and
$$\pi_k(\mathbb{C}^n \setminus K) = 0 \quad \text{for } 1 \leq k \leq n-1.$$""",
        },
        {
            "slug": "plurisubharmonic-morse-function-existence",
            "title_en": "Existence of Strictly Plurisubharmonic Morse Function",
            "title_zh": "严格多重次调和Morse函数的存在性",
            "type": "lemma",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Lemma 22.4.} Let $K$ be polynomially convex in $\mathbb{C}^n$ with $K \subseteq U$, $U$ open and bounded. Then there exists a smooth strictly plurisubharmonic function $\rho : \mathbb{C}^n \to \mathbb{R}$ and $R > 0$ such that:
\begin{enumerate}
\item $\rho < 0$ on $K$ and $\rho > 0$ on $\mathbb{C}^n \setminus U$;
\item $\rho(z) = |z|^2$ for $|z| > R$;
\item $\rho$ is a Morse function on $\mathbb{C}^n$.
\end{enumerate}""",
        },
        {
            "slug": "runge-domain-neighborhood-lemma",
            "title_en": "Runge Domain Neighborhood Lemma",
            "title_zh": "Runge域邻域引理",
            "type": "lemma",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "intermediate",
            "theorem_tex": r"""\textbf{Lemma 22.5.} Let $K$ be a compact polynomially convex set in $\mathbb{C}^n$ and let $U$ be an open neighborhood of $K$. Then there exists a Runge domain $\Omega$ such that $K \subseteq \Omega \subseteq U$.""",
        },
        {
            "slug": "morse-lemma",
            "title_en": "Morse's Lemma",
            "title_zh": "Morse引理",
            "type": "lemma",
            "domain": "topology",
            "subdomain": "morse-theory",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Morse's Lemma.} Let $f : M \to \mathbb{R}$ be a smooth function on a manifold $M$, let $K$ be compact and $U$ open relatively compact with $K \subseteq U \subseteq M$, and let $s > 0$ be an integer. Then there exists a smooth function $g : M \to \mathbb{R}$ such that $g$ has nondegenerate critical points on $K$, the derivatives of $g$ uniformly approximate those of $f$ up to order $s$ on $U$, and $g = f$ off $U$.""",
        },
        {
            "slug": "morse-theorem",
            "title_en": "Morse's Theorem on Handle Attachment",
            "title_zh": "Morse手柄附加定理",
            "type": "theorem",
            "domain": "topology",
            "subdomain": "morse-theory",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Morse's Theorem.} Let $\rho$ be a Morse function on $M$.
\begin{enumerate}
\item[(a)] If $\rho$ has no critical points in $\{x \in M : a \leq \rho(x) \leq b\}$, then $M^b$ is diffeomorphic to $M^a$.
\item[(b)] If $\rho$ has exactly one critical point in $\{x : a \leq \rho(x) \leq b\}$ and this critical point is nondegenerate of index $\lambda$, then $M^b$ has the homotopy type of $M^a$ with a $\lambda$-cell attached.
\end{enumerate}""",
        },
        {
            "slug": "morse-homology-corollary",
            "title_en": "Morse Homology Vanishing Corollary",
            "title_zh": "Morse同调消失推论",
            "type": "corollary",
            "domain": "topology",
            "subdomain": "morse-theory",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Corollary.} Let $\rho$ be a Morse function and $a < b$.
\begin{enumerate}
\item[(i)] If $\rho$ has no critical points in $\{a \leq \rho \leq b\}$, then $H_k(M^b, M^a; G) = 0$ for all $k$.
\item[(ii)] If $\rho$ has exactly one critical point of index $\lambda$, then $H_{\lambda}(M^b, M^a; G) = G$ and $H_k(M^b, M^a; G) = 0$ for $k \neq \lambda$.
\item[(iii)] If all critical points have index $\leq \sigma$, then $H_k(M^b, M^a; G) = 0$ for $k \geq \sigma + 1$.
\end{enumerate}""",
        },
    ],

    # === SECTION 23: Pseudoconvexity ===
    "s023_Section_23": [
        {
            "slug": "levi-pseudoconvexity",
            "title_en": "Levi Pseudoconvexity",
            "title_zh": "Levi伪凸性",
            "type": "definition",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "intermediate",
            "theorem_tex": r"""\textbf{Definition 23.1.} Let $\Omega = \{\rho < 0\}$ be a smoothly bounded domain in $\mathbb{C}^n$. $\partial \Omega$ is \textit{pseudoconvex in the sense of Levi} at $z^0 \in \partial \Omega$ if
$$\sum_{j,k=1}^{n} \left( \frac{\partial^2 \rho}{\partial z_j \partial \bar{z}_k} \right)_0 \zeta_j \bar{\zeta}_k \geq 0$$
for every complex tangent vector $\zeta$ to $\partial \Omega$ at $z^0$, i.e., $\sum_{j=1}^{n} (\partial \rho / \partial z_j)_0 \zeta_j = 0$.""",
        },
        {
            "slug": "pseudoconvex-domain",
            "title_en": "Pseudoconvex Domain",
            "title_zh": "伪凸域",
            "type": "definition",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "intermediate",
            "theorem_tex": r"""\textbf{Definition 23.2.} Let $\Omega$ be a domain in $\mathbb{C}^n$. $\Omega$ is \textit{pseudoconvex} if there exists a continuous plurisubharmonic exhaustion function on $\Omega$.""",
        },
        {
            "slug": "components-of-ball-minus-hull-are-pseudoconvex",
            "title_en": "Components of $B \setminus \hat{Y}$ are Pseudoconvex",
            "title_zh": "$B \setminus \hat{Y}$的分支是伪凸的",
            "type": "theorem",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Theorem 23.1.} Fix a compact set $Y$ in $\mathbb{C}^2$ and a point $p^0 \in \hat{Y} \setminus Y$. Let $B$ be an open ball in $\mathbb{C}^2$, centered at $p^0$, such that $\bar{B}$ does not meet $Y$. Then each connected component of $B \setminus \hat{Y}$ is pseudoconvex.""",
        },
        {
            "slug": "analytic-disk-in-boundary-implies-levi-flat",
            "title_en": "Analytic Disk in Boundary Implies Levi-Flat",
            "title_zh": "边界中的解析圆盘蕴含Levi平坦",
            "type": "theorem",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Theorem 23.5.} Let $\Omega$ be a region in $\mathbb{C}^2$ and fix $z^0 \in \partial \Omega$ with $\partial \Omega$ smooth near $z^0$. Assume there exists an analytic disk $z = f(\lambda)$, $|\lambda| < 1$, with $f(0) = z^0$, which is contained in $\partial \Omega$, and $df/d\lambda(0) \neq 0$. Then $\partial \Omega$ is Levi-flat at $z^0$.""",
        },
        {
            "slug": "levi-flat-boundary-of-hull-over-circle",
            "title_en": "Levi-Flat Boundary of Hull Over the Circle",
            "title_zh": "圆上包的Levi平坦边界",
            "type": "theorem",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Theorem 23.6.} Let $Y$ be a compact set in $\mathbb{C}^2$ lying over the circle $\{|z_1| = 1\}$. Let $\Omega$ be the interior of $\hat{Y}$. Then $\partial \Omega$ is Levi-flat at each point $z^0 = (z_1^0, z_2^0)$ with $|z_1^0| < 1$ at which $\partial \Omega$ is smooth.""",
        },
    ],

    # === SECTION 24: Examples ===
    "s024_Section_24": [
        {
            "slug": "rational-function-algebra-r0x",
            "title_en": "Rational Function Algebra $R_0(X)$",
            "title_zh": "有理函数代数 $R_0(X)$",
            "type": "definition",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "intermediate",
            "theorem_tex": r"""\textbf{Definition 24.1.} Let $X$ be a compact subset of $\mathbb{C}^n$. $R_0(X)$ denotes the algebra of continuous functions $f$ on $X$ of the form $f = A/B$, where $A$ and $B$ are polynomials and $B$ has no zero on $X$. $R(X)$ denotes the uniform closure of $R_0(X)$ on $X$.""",
        },
        {
            "slug": "rationally-convex-hull",
            "title_en": "Rationally Convex Hull",
            "title_zh": "有理凸包",
            "type": "definition",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "intermediate",
            "theorem_tex": r"""\textbf{Definition 24.2.} Let $X$ be a compact subset of $\mathbb{C}^n$. The \textit{rationally convex hull} of $X$, denoted $h_r(X)$, is the set
$$\{z \in \mathbb{C}^n : |f(z)| \leq \max_X |f| \text{ for all } f \in R_0(X)\}.$$""",
        },
        {
            "slug": "hull-without-analytic-disk",
            "title_en": "Existence of Hull Without Analytic Disks (Stolzenberg)",
            "title_zh": "无解析圆盘的包的存在性（Stolzenberg）",
            "type": "theorem",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Theorem 24.1.} There exists a compact set $X \subseteq \partial \Delta^2$ (the boundary of the bidisk in $\mathbb{C}^2$) such that $h_r(X) \neq X$ and $h_r(X)$ contains no analytic disk.""",
        },
        {
            "slug": "non-polynomially-convex-arc-c3",
            "title_en": "Non-Polynomially Convex Arc in $\mathbb{C}^3$",
            "title_zh": "$\mathbb{C}^3$中非多项式凸的弧",
            "type": "theorem",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Theorem 24.15.} Let $\gamma$ be an arc in the plane having positive planar measure, and let $F, F_2, F_3 \in \mathfrak{A}_{\gamma}$ be separating functions. Define $J_0 \subseteq \mathbb{C}^3$ as the image of $\gamma$ under $\zeta \mapsto (F(\zeta), F_2(\zeta), F_3(\zeta))$. Then $J_0$ is not polynomially convex in $\mathbb{C}^3$, and $P(J_0) \neq C(J_0)$.""",
        },
    ],

    # === SECTION 25: Pseudoconcave Sets ===
    "s025_Section_25": [
        {
            "slug": "pseudoconcave-set",
            "title_en": "Pseudoconcave Set",
            "title_zh": "伪凹集",
            "type": "definition",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "intermediate",
            "theorem_tex": r"""\textbf{Definition 25.1.} Let $\Omega$ be a domain in $\mathbb{C}^n$ and let $E$ be a relatively closed subset of $\Omega$. $E$ is called \textit{pseudoconcave} in $\Omega$ if the open set $\Omega \setminus E$ is pseudoconvex.""",
        },
        {
            "slug": "hartogs-theorem-pseudoconcave",
            "title_en": "Hartogs' Theorem on Pseudoconcave Sets",
            "title_zh": "伪凹集的Hartogs定理",
            "type": "theorem",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Theorem 25.1 (Hartogs).} Let $E$ be a pseudoconcave set in $\{|z| < 1\} \times \mathbb{C} \subseteq \mathbb{C}^2$ such that $E$ lies one-sheeted over $\{|z| < 1\}$, i.e., every vertical line $\{z = z_0\}$ with $|z_0| < 1$ meets $E$ exactly once. Then $E$ is the graph of an analytic function on $\{|z| < 1\}$.""",
        },
        {
            "slug": "pseudoconcave-implies-maximum-modulus-algebra",
            "title_en": "Pseudoconcave Sets Yield Maximum Modulus Algebras",
            "title_zh": "伪凹集产生极大模代数",
            "type": "theorem",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Theorem 25.2.} Let $X$ be a pseudoconcave set contained in the open bidisk $\{|z| < 1, |w| < 1\} \subseteq \mathbb{C}^2$. Denote by $A$ the algebra of polynomials in $z$ and $w$ restricted to $X$. Putting $D = \{|z| < 1\}$ and $\pi : (z, w) \mapsto z$, then $(A, X, D, \pi)$ is a maximum modulus algebra.""",
        },
    ],

    # === SECTION 26: Appendix / Historical ===
    "s026_Section_26": [
        {
            "slug": "plurisubharmonic-function-definition",
            "title_en": "Plurisubharmonic Function",
            "title_zh": "多重次调和函数",
            "type": "definition",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "intermediate",
            "theorem_tex": r"""\textbf{Definition (Appendix A6).} A real-valued function $\psi$ defined on an open set $\Omega$ in $\mathbb{C}^n$ is called \textit{plurisubharmonic} on $\Omega$ if it is upper semicontinuous and its restriction to each complex line $L$ is subharmonic on $L \cap \Omega$. If $\psi \in C^2$, then $\psi$ is plurisubharmonic on $\Omega$ if and only if
$$\sum_{j,k=1}^{n} \frac{\partial^2 \psi}{\partial z_j \partial \bar{z}_k}(p) \xi_j \bar{\xi}_k \geq 0$$
for every $p \in \Omega$ and every $\xi = (\xi_1, \ldots, \xi_n) \in \mathbb{C}^n$.""",
        },
        {
            "slug": "cartan-subharmonic-capacity-result",
            "title_en": "Cartan's Result on Subharmonic Functions and Capacity",
            "title_zh": "Cartan关于次调和函数与容量的结果",
            "type": "theorem",
            "domain": "analysis",
            "subdomain": "potential-theory",
            "difficulty": "advanced",
            "theorem_tex": r"""\textbf{Theorem (Cartan, Appendix A2).} A function subharmonic in a plane region and equal to $-\infty$ on a Borel set of positive logarithmic capacity is identically $-\infty$ in the region.""",
        },
        {
            "slug": "runge-domain-interior-of-polynomially-convex-set",
            "title_en": "Interior of Polynomially Convex Set is Runge",
            "title_zh": "多项式凸集的内部是Runge域",
            "type": "lemma",
            "domain": "analysis",
            "subdomain": "several-complex-variables",
            "difficulty": "intermediate",
            "theorem_tex": r"""\textbf{Lemma (Appendix A9).} Let $L$ be polynomially convex in $\mathbb{C}^n$ and let $\Omega$ be the interior of $L$. Then $\Omega$ is a Runge domain.""",
        },
    ],
}

# English introductions for each concept
introductions = {
    "polynomial-hull-of-curves-is-analytic-variety": "This fundamental result of Stolzenberg and Alexander characterizes the polynomial hull of a finite union of smooth compact curves in $\\mathbb{C}^N$. When the union is not polynomially convex, the added points form a one-dimensional analytic variety. This theorem provides a bridge between polynomial approximation theory and complex analytic geometry in higher dimensions.",
    "peak-point-lemma-for-uniform-algebras": "This lemma is a key technical tool in the study of uniform algebras and their maximal ideal spaces. It gives a sufficient condition (in terms of the image of a neighborhood under an algebra element lying in a sector) for a point in $\\mathcal{M} \\setminus X$ to fail to be a peak point for the restricted algebra. It is used in the geometric analysis of polynomial hulls of curves.",
    "smooth-arc-is-polynomially-convex": "This theorem shows that any smooth arc in $\\mathbb{C}^N$ is polynomially convex, meaning that every continuous function on the arc can be uniformly approximated by polynomials. The proof uses the argument principle and the fact that a smooth arc admits an analytic logarithm in a neighborhood. This contrasts with the case of arcs of positive planar measure in $\\mathbb{C}^3$, which may fail to be polynomially convex.",
    "polynomial-hull-of-k-union-curve": "This generalization of Theorem 12.1 allows an additional compact polynomially convex set $K$ to be adjoined to the curve $\\gamma$. The added part of the hull $\\widehat{K \\cup \\gamma} \\setminus (K \\cup \\gamma)$ remains a one-dimensional analytic variety. This is useful in iterative constructions where polynomially convex sets are built up step by step.",
    "arens-royden-theorem": "The Arens-Royden theorem establishes a profound connection between the algebraic structure of a commutative Banach algebra and the topology of its maximal ideal space. Specifically, the group of invertible elements modulo exponentials is naturally isomorphic to the first \\v{C}ech cohomology group $H^1(\\mathcal{M}, \\mathbb{Z})$. This generalizes the classical fact that on a compact space $X$, the quotient $C(X)^{-1}/\\exp C(X)$ is isomorphic to $H^1(X, \\mathbb{Z})$.",
    "natural-homomorphism-ckx-to-h1": "This theorem constructs an explicit surjective homomorphism $\\eta$ from the group of invertible continuous functions $C(X)^{-1}$ to $H^1(X, \\mathbb{Z})$ whose kernel is exactly $\\exp C(X)$. The construction uses local logarithms and \\v{C}ech cochains. This gives a cohomological interpretation of the obstruction to taking a global logarithm of a nonvanishing continuous function.",
    "full-subalgebra": "A subalgebra $\\mathcal{L}$ of $C(X)$ is called 'full' if the restriction of the natural homomorphism $\\eta$ to $\\mathcal{L}^{-1}$ is surjective onto $H^1(X, \\mathbb{Z})$ and its kernel within $\\mathcal{L}^{-1}$ is exactly $\\exp \\mathcal{L}$. This property captures when the algebra is 'cohomologically complete' and plays a key role in the proof of the Arens-Royden theorem for general Banach algebras.",
    "holomorphic-germ-algebra": "For a compact polynomially convex set $X \\subseteq \\mathbb{C}^n$, $\\mathcal{H}(X)$ consists of continuous functions on $X$ that admit a holomorphic extension to some neighborhood of $X$. This algebra interpolates between the polynomial algebra $P(X)$ and the full algebra $C(X)$, and is an important tool in approximation theory.",
    "holomorphic-germ-algebra-is-full": "This lemma establishes that the holomorphic germ algebra $\\mathcal{H}(X)$ over a compact polynomially convex set is full. The proof uses the Oka-Weil theorem and the fact that $\\bar{\\partial}$-equations can be solved on $p$-polyhedra. This lemma is a crucial step in proving that finitely generated uniform algebras (and hence arbitrary Banach algebras via the Arens-Royden theorem) are full.",
    "finitely-generated-uniform-algebra-is-full": "This lemma states that any finitely generated uniform algebra on its maximal ideal space is full as a subalgebra of $C(X)$. The proof reduces to the case $\\mathcal{L} = P(X)$ where $X$ is polynomially convex, and then uses the fact that $\\mathcal{H}(X)$ is full together with approximation arguments. This is a key ingredient in the proof of the Arens-Royden theorem.",
    "first-cech-cohomology-definition": "The first \\v{C}ech cohomology group $H^1(X, \\mathbb{Z})$ with integer coefficients is defined as the direct limit of the cohomology groups $H^1(\\mathcal{U}, \\mathbb{Z})$ of finite open coverings $\\mathcal{U}$ of $X$, under the refinement homomorphisms. For decent spaces, \\v{C}ech cohomology coincides with singular cohomology.",
    "plemelj-theorem": "The Plemelj (or Sokhotski-Plemelj) theorem describes the boundary behavior of the Cauchy-type integral. It states that the limiting values from the two sides of an oriented curve differ precisely by the density function. This is a fundamental result in the theory of singular integral equations and boundary value problems.",
    "harvey-lawson-boundary-theorem": "The Harvey-Lawson theorem characterizes which smooth closed curves in $\\mathbb{C}^2$ bound analytic varieties. The necessary and sufficient condition is the moment condition $\\int_{\\gamma} z^n w^m dz = 0$ for all $n, m \\geq 0$, together with the projection being a local diffeomorphism. This is a higher-dimensional analogue of the fact that every closed curve in $\\mathbb{C}$ bounds a Riemann surface.",
    "holomorphic-chain": "A holomorphic chain is a formal integer linear combination of irreducible analytic subvarieties. Chains provide a natural framework for stating boundary theorems in complex analysis, generalizing the notion of analytic varieties to allow multiplicities and orientations. They appear in the Harvey-Lawson theory of boundaries of analytic varieties.",
    "maximally-complex-manifold": "A real $(2p-1)$-dimensional manifold $M$ in $\\mathbb{C}^n$ is maximally complex if its tangent space at each point contains a complex subspace of the maximal possible dimension $p-1$. This is a necessary condition for $M$ to be the boundary of a $p$-dimensional analytic variety, and is a key geometric condition in the Harvey-Lawson boundary theorem.",
    "moment-condition": "The moment condition requires that the integral of any $\\bar{\\partial}$-closed $(p, p-1)$-form over $M$ vanish. It is a necessary condition (by Stokes' theorem) for $M$ to bound a $p$-dimensional analytic variety. For curves in $\\mathbb{C}^2$, this reduces to $\\int_{\\gamma} z^n w^m dz = 0$ for all $n, m$.",
    "jump-theorem-bochner-martinelli": "The Jump Theorem is the higher-dimensional generalization of the Plemelj formula, using the Bochner-Martinelli kernel instead of the Cauchy kernel. It describes how the Bochner-Martinelli integral jumps when crossing a hypersurface, with the jump equal to the density function.",
    "hull-over-circle-with-convex-fibers": "This theorem gives a complete description of the polynomial hull of a compact set lying over the unit circle in $\\mathbb{C}^2$ when each fiber is convex. The added points are exactly the graphs of bounded analytic functions whose boundary values lie in the fibers. This connects polynomial hulls to Hardy space theory.",
    "fiberwise-convexity-of-hull-over-circle": "This theorem shows that if the fibers over the unit circle of a compact set $Y$ are convex, then the fibers of the polynomial hull $\\hat{Y}$ over the open disk are also convex. This 'preservation of convexity' result is fundamental in the study of polynomial hulls.",
    "rational-function-description-of-hull-fibers": "For a special class of sets over the circle defined by rational functions, the fibers of the polynomial hull are explicitly described as closed disks whose radii are computed via Pick interpolation theory. This connects polynomial hulls to classical Nevanlinna-Pick interpolation.",
    "area-lower-bound-for-spectrum": "This theorem of Alexander provides a lower bound for the area of the image $f(M)$ of the maximal ideal space of a uniform algebra in terms of the $L^2$-norm of $f$ with respect to a representing measure. It generalizes the classical area formula for disk algebra functions.",
    "ahlfors-beurling-estimate": "This lemma bounds the supremum of the Cauchy potential $F(z) = \\iint_K (\\zeta - z)^{-1} du dv$ on a compact set $K$ by $\\sqrt{\\pi \\operatorname{area}(K)}$. The elegant proof uses complex geometry and an integral estimate over level sets.",
    "distance-to-rk-bound": "This lemma gives a quantitative bound on how well the conjugate function $\\bar{z}$ can be approximated by rational functions with poles off a compact set $K$, in terms of the area of $K$. It is a quantitative refinement of the Hartogs-Rosenthal theorem.",
    "isoperimetric-inequality-via-rational-approximation": "This proposition connects the classical isoperimetric inequality $4\\pi A \\leq L^2$ to rational approximation theory by showing $2A/L \\leq \\operatorname{dist}(\\bar{z}, R(\\Omega))$. Combined with Lemma 21.3, this yields a proof of the isoperimetric inequality via function theory.",
    "area-of-analytic-variety-formula": "This theorem expresses the area of a one-dimensional analytic variety in $\\mathbb{C}^n$ as the integral of the K\\\"ahler form $\\frac{i}{2} \\sum dz_j \\wedge d\\bar{z}_j$. This generalizes the classical formula $\\operatorname{area}(f(D)) = \\int_D |f'|^2 dx dy$ to higher codimension.",
    "rutishauser-corollary-higher-dim": "This corollary of Rutishauser type states that if a point $p$ is in the polynomial hull of $X$ and a ball around $p$ avoids $X$, then the part of the hull inside that ball has two-dimensional Hausdorff measure at least $\\pi r^2$. This gives a lower bound on the size of the added hull.",
    "andreotti-narasimhan-theorem": "This theorem states that a Runge domain in $\\mathbb{C}^n$ has vanishing homology in dimensions $k \\geq n$. The proof uses Morse theory with a strictly plurisubharmonic exhaustion function, whose critical points have index at most $n$. This is a fundamental topological property of domains of holomorphy.",
    "forstneric-theorem": "Forstneri\\v{c}'s theorem states that the complement of a compact polynomially convex set in $\\mathbb{C}^n$ ($n \\geq 2$) has vanishing homology and homotopy groups in dimensions 1 through $n-1$. This is a far-reaching generalization of the fact that polynomially convex sets in $\\mathbb{C}$ have connected complement.",
    "plurisubharmonic-morse-function-existence": "This lemma constructs a strictly plurisubharmonic Morse function that is negative on a given polynomially convex set $K$ and positive outside a neighborhood $U$. This is a crucial technical tool for applying Morse theory to study the topology of polynomial hulls and Runge domains.",
    "runge-domain-neighborhood-lemma": "This lemma shows that every polynomially convex compact set admits a neighborhood basis of Runge domains. The construction uses polynomial polyhedra, which are defined by finitely many polynomial inequalities. This bridges the gap between compact polynomially convex sets and Runge domains.",
    "morse-lemma": "Morse's Lemma is a fundamental approximation result in differential topology. It states that any smooth function can be approximated by a Morse function (one with only nondegenerate critical points), with agreement outside a compact set. This allows Morse theory techniques to be applied to arbitrary smooth functions.",
    "morse-theorem": "Morse's Theorem describes how the topology of sublevel sets of a Morse function changes when crossing a critical point. The fundamental result is that passing a nondegenerate critical point of index $\\lambda$ attaches a $\\lambda$-cell to the sublevel set. This is the cornerstone of Morse theory.",
    "morse-homology-corollary": "This corollary summarizes the homological consequences of Morse's Theorem. It gives vanishing and non-vanishing results for relative homology groups $H_k(M^b, M^a; G)$ based on the indices of critical points of a Morse function between levels $a$ and $b$.",
    "levi-pseudoconvexity": "Levi pseudoconvexity is the complex analog of convexity for domains in $\\mathbb{C}^n$. A smoothly bounded domain is Levi pseudoconvex if the complex Hessian (Levi form) of a defining function is positive semidefinite on the complex tangent space at each boundary point. This condition, discovered by E. E. Levi in 1910, characterizes domains of holomorphy.",
    "pseudoconvex-domain": "A pseudoconvex domain is one that admits a continuous plurisubharmonic exhaustion function. This is the natural generalization of a domain of holomorphy to domains that may have non-smooth boundaries. The equivalence between this definition and Levi pseudoconvexity for smoothly bounded domains is a fundamental theorem of Oka.",
    "components-of-ball-minus-hull-are-pseudoconvex": "This theorem reveals a deep relationship between polynomial hulls and pseudoconvexity: near a point of the added hull, the complement of the hull in a small ball has pseudoconvex components. This provides a link between the theory of polynomial hulls and the \\bar{\\partial}-Neumann problem.",
    "analytic-disk-in-boundary-implies-levi-flat": "This theorem states that if the boundary of a domain contains an analytic disk (a nonconstant holomorphic image of the unit disk), then the Levi form must vanish identically at the central point. Thus the boundary is Levi-flat at that point. This is a geometric manifestation of the maximum principle for plurisubharmonic functions.",
    "levi-flat-boundary-of-hull-over-circle": "This theorem shows that for a polynomial hull over the unit circle in $\\mathbb{C}^2$, the boundary of the interior of the hull is Levi-flat at interior points (where $|z_1| < 1$). The proof uses both the pseudoconvexity of the hull's complement and the polynomial convexity of the hull itself to force the Levi form to vanish.",
    "rational-function-algebra-r0x": "$R_0(X)$ is the algebra of rational functions on a compact set $X \\subseteq \\mathbb{C}^n$ that are holomorphic on $X$ (denominator has no zeros on $X$). Its uniform closure $R(X)$ is the natural algebra associated to rational convexity, just as $P(X)$ is associated to polynomial convexity.",
    "rationally-convex-hull": "The rationally convex hull $h_r(X)$ is the set of points in $\\mathbb{C}^n$ that cannot be separated from $X$ by rational functions holomorphic on $X$. It is generally smaller than the polynomial hull $\\hat{X}$ and is the natural maximal ideal space of $R(X)$.",
    "hull-without-analytic-disk": "This theorem, due to Stolzenberg, gives a counterexample to the conjecture that polynomial hulls always contain analytic varieties of positive dimension. The construction produces a compact subset of the boundary of the bidisk in $\\mathbb{C}^2$ whose rationally convex hull is strictly larger yet contains no analytic disk.",
    "non-polynomially-convex-arc-c3": "This theorem shows that in $\\mathbb{C}^3$, an arc that is the image of a plane arc of positive measure under a separating map fails to be polynomially convex. This contrasts with the result (Theorem 12.4) that smooth arcs are polynomially convex in any $\\mathbb{C}^N$.",
    "pseudoconcave-set": "A relatively closed subset $E$ of a domain $\\Omega$ is pseudoconcave if its complement $\\Omega \\setminus E$ is pseudoconvex. This notion, introduced by Nishino, is dual to pseudoconvexity and plays a role in the theory of analytic multifunctions and maximum modulus algebras.",
    "hartogs-theorem-pseudoconcave": "Hartogs' theorem on pseudoconcave sets generalizes the classical Hartogs extension phenomenon: a one-sheeted pseudoconcave set over the unit disk must be the graph of an analytic function. This is a 'removable singularities' type result for sets with pseudoconcave structure.",
    "pseudoconcave-implies-maximum-modulus-algebra": "This theorem connects pseudoconcavity to the theory of maximum modulus algebras: a pseudoconcave set in the bidisk gives rise to a maximum modulus algebra when one takes the polynomial algebra restricted to the set, with projection to the first coordinate. This unifies Oka-Nishino theory with the theory of maximum modulus algebras.",
    "plurisubharmonic-function-definition": "A plurisubharmonic function is the several-complex-variables analog of a subharmonic function. It is upper semicontinuous and subharmonic on every complex line. For $C^2$ functions, plurisubharmonicity is equivalent to the complex Hessian (Levi matrix) being positive semidefinite.",
    "cartan-subharmonic-capacity-result": "This result of H. Cartan states that a subharmonic function in a plane region that equals $-\\infty$ on a set of positive logarithmic capacity must be identically $-\\infty$. It is a crucial tool in the proof of Theorem 11.8 on the finite-sheeted nature of maximum modulus algebras.",
    "runge-domain-interior-of-polynomially-convex-set": "This lemma states that the interior of any polynomially convex set is a Runge domain, i.e., polynomials are dense in the holomorphic functions on it. It follows from the basic property that the polynomial hull of a compact subset of the interior stays within the interior.",
}

def write_concept(section_dir, c):
    slug = c["slug"]
    concept_dir = os.path.join(BASE, section_dir, slug)
    os.makedirs(concept_dir, exist_ok=True)

    tex = c["theorem_tex"]
    content_hash = hashlib.md5(tex.encode()).hexdigest()[:12]

    # concept.yaml
    yaml = f"""id: {slug}
title_en: "{c['title_en']}"
title_zh: "{c.get('title_zh', '')}"
type: {c['type']}
domain: {c['domain']}
subdomain: {c['subdomain']}
difficulty: {c['difficulty']}
tags: []
depends_on:
  required: []
  recommended: []
  suggested: []
source_books:
- book_id: "gtm035"
  author: "Alexander-Wermer"
  title: "Several Complex Variables and Banach Algebras"
  chapter: ""
  section: ""
  pages: ""
  role_in_book: ""
content_hash: "{content_hash}"
extraction_date: "{DATE}"
extraction_agent: "{AGENT}"
"""
    with open(os.path.join(concept_dir, "concept.yaml"), "w") as f:
        f.write(yaml)

    # theorem.tex
    with open(os.path.join(concept_dir, "theorem.tex"), "w") as f:
        f.write(tex + "\n")

    # introduce.en.md
    intro = introductions.get(slug, f"This is the {c['type']} '{c['title_en']}' from the book 'Several Complex Variables and Banach Algebras' (GTM035).")
    md = f"""---
role: introduce
locale: en
content_hash: "{content_hash}"
written_against: ""
---

{intro}
"""
    with open(os.path.join(concept_dir, "introduce.en.md"), "w") as f:
        f.write(md)

for section, clist in concepts.items():
    print(f"Processing {section} ({len(clist)} concepts)...")
    for c in clist:
        try:
            write_concept(section, c)
            print(f"  OK: {c['slug']}")
        except Exception as e:
            print(f"  FAIL: {c['slug']}: {e}")
    # Write .done
    done_path = os.path.join(BASE, section, ".done")
    with open(done_path, "w") as f:
        f.write("DONE\n")
    print(f"  -> {section} marked DONE")

print("\nAll done!")
