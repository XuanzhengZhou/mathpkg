#!/usr/bin/env python3
"""Batch create concept files for GTM033 unprocessed sections."""
import os, json

BASE = "/home/a123/文档/mathpkg/pipeline_output/concepts_v7/gtm033"
BOOK_SRC = {"book_id": "gtm033", "author": "Morris W. Hirsch", "title": "Differential Topology",
             "chapter": "", "section": "", "pages": "", "role_in_book": ""}

def write_concept(section_dir, slug, ctype, title_en, domain, subdomain, difficulty, tex, intro):
    d = os.path.join(section_dir, slug)
    os.makedirs(d, exist_ok=True)

    yaml = {
        "id": slug,
        "title_en": title_en,
        "title_zh": "",
        "type": ctype,
        "domain": domain,
        "subdomain": subdomain,
        "difficulty": difficulty,
        "tags": [],
        "depends_on": {"required": [], "recommended": [], "suggested": []},
        "source_books": [dict(BOOK_SRC)],
        "content_hash": "",
        "extraction_date": "2026-06-25",
        "extraction_agent": "v7-section-test"
    }
    with open(os.path.join(d, "concept.yaml"), "w") as f:
        json.dump(yaml, f, indent=2)
        f.write("\n")

    with open(os.path.join(d, "theorem.tex"), "w") as f:
        f.write(tex.strip() + "\n")

    with open(os.path.join(d, "introduce.en.md"), "w") as f:
        f.write("---\nrole: introduce\nlocale: en\ncontent_hash: \"\"\nwritten_against: \"\"\n---\n")
        f.write(intro.strip() + "\n")

# =========== s012 ===========
D12 = f"{BASE}/s012_6_Collars_and_Tubular_Neighborhoods_of_Neat_Submanifolds"
os.makedirs(D12, exist_ok=True)

write_concept(D12, "theorem-6-4-tubular-neighborhood-extension", "theorem",
    "Tubular Neighborhood Extension Theorem", "topology", "differential-topology", "advanced",
    r"""Let $M \subset V$ be a neat submanifold. Then every tubular neighborhood of $\partial M$ in $\partial V$ is the intersection with $\partial V$ of a tubular neighborhood for $M$ in $V$.""",
    "If $M$ is a neat submanifold of $V$, any tubular neighborhood of the boundary $\partial M$ in $\partial V$ extends to a tubular neighborhood of $M$ in $V$ whose restriction to the boundary recovers the given neighborhood. This extension theorem is a fundamental tool for constructing tubular neighborhoods on manifolds with boundary.")

write_concept(D12, "theorem-6-6-isotopy-of-disk-embeddings", "theorem",
    "Isotopy of Disk Embeddings by Determinant", "topology", "differential-topology", "advanced",
    r"""Let $E^n = D^n$ or $\mathbb{R}^n$ and let $f_i: (E^n, 0) \to (V, x_0)$ be an embedding, $i = 0, 1$, where $n = \dim V$. If
$$\operatorname{Det}(D(f_1^{-1}f_0)(0)) > 0$$
then $f_0$ and $f_1$ are isotopic rel $0$.""",
    "Two embeddings of an $n$-disk (or $\mathbb{R}^n$) into an $n$-manifold $V$, both sending $0$ to $x_0$, are isotopic relative to $0$ provided the derivative of the transition map at $0$ has positive determinant. This means that up to isotopy there are at most two ways to embed a disk, distinguished by orientation.")

write_concept(D12, "definition-closed-tubular-neighborhood", "definition",
    "Closed Tubular Neighborhood", "topology", "differential-topology", "intermediate",
    r"""A closed tubular neighborhood of radius $\varepsilon > 0$ of a submanifold $M \subset V$ is an embedding of the closed disk bundle $D(\nu_M, \varepsilon) \to V$ extending the inclusion $M \hookrightarrow V$, where $\nu_M$ denotes the normal bundle of $M$ in $V$.""",
    "A closed tubular neighborhood of radius $\varepsilon$ is a tubular neighborhood whose fibres are closed disks of radius $\varepsilon$ in the normal bundle. For $\partial V = \varnothing$, a closed tubular neighborhood of radius 1 at a point $x_0 \in V$ is an embedding $(D^n, 0) \to (V, x_0)$ where $n = \dim V$.")

# =========== s014 ===========
D14 = f"{BASE}/s014_1_Degrees_of_Maps"
os.makedirs(D14, exist_ok=True)

write_concept(D14, "definition-degree-of-a-map", "definition",
    "Degree of a Map", "topology", "differential-topology", "intermediate",
    r"""Let $(M, \omega)$ and $(N, \theta)$ be compact oriented $n$-manifolds without boundary, with $N$ connected, and let $f: M \to N$ be a continuous map. The degree of $f$, denoted $\deg f$, is the integer $\deg(f, y)$ for any regular value $y \in N$ of a smooth approximation to $f$, where
$$\deg(f, y) = \sum_{x \in f^{-1}(y)} \operatorname{sign} T_x f$$
with $\operatorname{sign} T_x f = +1$ if $T_x f: M_x \to N_y$ preserves orientation and $-1$ otherwise.""",
    "The degree of a map between compact oriented $n$-manifolds counts the algebraic number of preimages of a regular value, weighted by whether the derivative preserves or reverses orientation. It is a fundamental homotopy invariant in differential topology.")

write_concept(D14, "definition-mod-2-degree", "definition",
    "Mod 2 Degree of a Map", "topology", "differential-topology", "intermediate",
    r"""Let $M, N$ be compact $n$-manifolds without boundary, with $N$ connected, and let $f: M \to N$ be a continuous map. The mod 2 degree of $f$, denoted $\deg_2 f$, is the element of $\mathbb{Z}_2$ given by the parity of $|f^{-1}(y)|$ for any regular value $y$ of a smooth approximation to $f$.""",
    "The mod 2 degree is defined for not-necessarily-orientable manifolds and counts the number of preimages of a regular value modulo 2. It is independent of the choice of regular value and is a homotopy invariant.")

write_concept(D14, "lemma-1-1-orientation-arc-endpoints", "lemma",
    "Orientation of Arc Endpoints in a $\partial$-Manifold", "topology", "differential-topology", "intermediate",
    r"""Let $(W, \omega)$ be an oriented $\partial$-manifold. Suppose $K \subset W$ is an embedded arc which is transverse to $\partial W$ at its endpoints $u, v \in \partial W$. Let $\kappa$ be an orientation of $K$, and consider the quotient orientation $\omega/\kappa$ of the algebraic normal bundle of $K$. Then
$$\omega_u/\kappa_u = (\partial \omega)_u \Longleftrightarrow \omega_v/\kappa_v = -(\partial \omega)_v.$$""",
    "This lemma describes how the orientation of the normal bundle of an arc relates to the boundary orientation at the two endpoints. If the quotient orientation agrees with the boundary orientation at one endpoint, it must be opposite at the other. This is used to track signs when computing degrees.")

write_concept(D14, "lemma-1-2-degree-of-extendable-map", "lemma",
    "Degree of an Extendable Map is Zero", "topology", "differential-topology", "intermediate",
    r"""Let $W$ be a compact oriented manifold of dimension $n + 1$, $N$ a compact oriented $n$-manifold without boundary and $h: W \to N$ a $C^\infty$ map. Let $y \in N$ be a regular value for both $h$ and $h|\partial W$. Then $\deg(h|\partial W, y) = 0$.""",
    "If a map defined on the boundary of a compact oriented $(n+1)$-manifold extends to the whole manifold, then its degree is zero. This is a fundamental obstruction: nonzero degree implies the map cannot be extended.")

write_concept(D14, "lemma-1-4-degree-independence-regular-value", "lemma",
    "Independence of Degree from Regular Value", "topology", "differential-topology", "intermediate",
    r"""Let $M, N$ be compact oriented $n$-manifolds without boundaries, $n \geqslant 1$, with $N$ connected. Let $y, z \in N$ be regular values for a $C^\infty$ map $f: M \to N$. Then $\deg(f, y) = \deg(f, z)$.""",
    "The degree of a map does not depend on which regular value is used to compute it, as long as $N$ is connected. This is proved by constructing a diffeomorphism of $N$ homotopic to the identity that moves one regular value to the other.")

write_concept(D14, "lemma-1-5-smooth-approximation", "lemma",
    "Smooth Approximation of Continuous Maps", "topology", "differential-topology", "basic",
    r"""Let $M, N$ be manifolds and $f: M \to N$ a continuous map. Then $f$ can be approximated by $C^\infty$ maps homotopic to $f$.""",
    "Every continuous map between manifolds can be approximated arbitrarily closely by a smooth ($C^\infty$) map that is homotopic to the original. This allows degree theory to be developed for continuous maps by passing to smooth approximations.")

write_concept(D14, "theorem-1-6-degree-homotopy-invariance", "theorem",
    "Homotopy Invariance of Degree", "topology", "differential-topology", "intermediate",
    r"""Let $M, N$ be compact $n$-manifolds without boundary, with $N$ connected.
(a) Homotopic maps $M \to N$ have the same degree if $M, N$ are oriented, and the same mod 2 degree otherwise.
(b) Let $M = \partial W$, $W$ compact. Suppose a map $f: M \to N$ extends to $W$. Then $\deg f = 0$ if $W$ and $N$ are orientable, and $\deg_2 f = 0$ otherwise.""",
    "The degree (or mod 2 degree) is a complete homotopy invariant for maps into spheres. Part (a) states homotopic maps have the same degree. Part (b) states that if a map extends from the boundary to the whole manifold, its degree is zero.")

write_concept(D14, "lemma-1-7-extension-from-arc", "lemma",
    "Extension from an Arc via Tubular Neighborhoods", "topology", "differential-topology", "advanced",
    r"""Let $W$ be a compact oriented $\partial$-manifold of dimension $n + 1$. Let $f: \partial W \to S^n$ be a $C^\infty$ map and $K \subset W$ a neat arc whose endpoints are in $\partial W$ and which is otherwise disjoint from $\partial W$. Suppose $y \in S^n$ is a regular value for $f$ and $f^{-1}(y) = \partial K$. Suppose further that the two endpoints of $K$ are of opposite type for $f$. Then $f$ extends to a map $W \to S^n$ having $y$ as a regular value, with the preimage of $y$ being exactly $K$.""",
    "Given an arc $K$ in $W$ whose endpoints on $\partial W$ are preimages of a regular value $y$ with opposite signs, the map $f$ can be extended across a tubular neighborhood of $K$ so that $y$ remains a regular value and the preimage of $y$ is exactly $K$.")

write_concept(D14, "theorem-1-8-extension-oriented-to-sphere", "theorem",
    "Extension Theorem for Maps to $S^n$ (Oriented Case)", "topology", "differential-topology", "advanced",
    r"""Let $W$ be a connected compact oriented $\partial$-manifold of dimension $n + 1 \geqslant 2$. A map $f: \partial W \to S^n$ extends to $W$ if and only if $\deg f = 0$.""",
    "A map from the boundary of a compact oriented $(n+1)$-manifold to the $n$-sphere extends to the whole manifold exactly when its degree is zero. This is a definitive extension criterion that generalizes the earlier obstruction results.")

write_concept(D14, "theorem-1-9-extension-nonorientable-to-sphere", "theorem",
    "Extension Theorem for Maps to $S^n$ (Nonorientable Case)", "topology", "differential-topology", "advanced",
    r"""Let $W$ be a connected compact nonorientable $\partial$-manifold of dimension $n + 1 \geqslant 2$. A map $f: \partial W \to S^n$ extends to $W$ if and only if $\deg_2 f = 0$.""",
    "For nonorientable manifolds, the extension criterion uses the mod 2 degree: a map from the boundary to the sphere extends if and only if its mod 2 degree is zero. The proof requires dimension at least 3 or a special argument in dimension 2.")

write_concept(D14, "theorem-1-10-classification-maps-into-sphere", "theorem",
    "Classification of Maps into $S^n$ by Degree", "topology", "differential-topology", "advanced",
    r"""Let $M$ be a compact connected $n$-manifold, $n \geqslant 1$. Let $f, g: M \to S^n$ be continuous maps.
(a) If $M$ is oriented and $\partial M = \varnothing$, then $f \simeq g$ if and only if $\deg f = \deg g$; and there are maps of every degree $m \in \mathbb{Z}$.
(b) If $M$ is nonorientable and $\partial M = \varnothing$, then $f \simeq g$ if and only if $\deg_2 f = \deg_2 g$.
(c) If $\partial M \neq \varnothing$, then every map $M \to S^n$ is nullhomotopic.""",
    "For a compact connected $n$-manifold $M$ without boundary, homotopy classes of maps $M \to S^n$ are completely classified by the degree (if $M$ is oriented) or the mod 2 degree (if $M$ is nonorientable). When $\partial M \neq \varnothing$, every map to $S^n$ is nullhomotopic.")

# =========== s016 ===========
D16 = f"{BASE}/s016_1_Morse_Functions"
os.makedirs(D16, exist_ok=True)

write_concept(D16, "definition-cotangent-bundle", "definition",
    "Cotangent Bundle", "topology", "differential-topology", "intermediate",
    r"""Let $M$ be a manifold of dimension $n$. The cotangent bundle $T^*M$ is defined like the tangent bundle $TM$ using the dual vector space $(\mathbb{R}^n)^* = L(\mathbb{R}^n, \mathbb{R})$ instead of $\mathbb{R}^n$. As a set, $T^*M = \bigcup_{x \in M} M_x^*$ where $M_x^* = L(M_x, \mathbb{R})$. If $(\varphi, U)$ is a chart on $M$, a natural chart on $T^*M$ is the map
$$T^*U \to \varphi(U) \times (\mathbb{R}^n)^*$$
which sends $\lambda \in M_x^*$ to $(\varphi(x), \lambda \circ \varphi_x^{-1})$. The projection map $p: T^*M \to M$ sends $M_x^*$ to $x$.""",
    "The cotangent bundle is the dual vector bundle to the tangent bundle. Its fibre at $x \in M$ is the dual space $M_x^*$ of linear maps $M_x \to \mathbb{R}$. The differential $Df$ of a real-valued function $f: M \to \mathbb{R}$ is a section of the cotangent bundle.")

write_concept(D16, "definition-critical-point-function", "definition",
    "Critical Point of a Real-Valued Function", "topology", "differential-topology", "basic",
    r"""Let $f: M \to \mathbb{R}$ be a $C^1$ map. A point $x \in M$ is a critical point of $f$ if the linear map $T_x f: M_x \to \mathbb{R}$ is zero. Equivalently, $Df(x)$ is the zero element of $M_x^*$. The set of critical points of $f$ is the preimage of the zero section under $Df: M \to T^*M$.""",
    "A critical point of a real-valued function on a manifold is a point where the differential vanishes. Geometrically, the level sets of $f$ fail to be smooth submanifolds at critical points. Morse theory studies the topology of a manifold via the critical points of a generic smooth function.")

write_concept(D16, "definition-hessian-form", "definition",
    "Hessian Quadratic Form at a Critical Point", "topology", "differential-topology", "intermediate",
    r"""Let $f: M \to \mathbb{R}$ be a $C^2$ map and $x \in M$ a critical point of $f$. The Hessian quadratic form $H_x f: M_x \to \mathbb{R}$ is defined as the composition
$$H_x f: M_x \xrightarrow{D\varphi_x} \mathbb{R}^n \xrightarrow{H_{\varphi(x)}(f\varphi^{-1})} \mathbb{R}$$
where $\varphi$ is any chart at $x$ and $H_p g(y) = D^2 g(p)(y, y)$ is the usual Hessian of a function on $\mathbb{R}^n$. This definition is independent of the choice of chart.""",
    "The Hessian at a critical point is a well-defined quadratic form on the tangent space, obtained by computing the second derivatives in any coordinate chart. Its nondegeneracy characterizes whether the critical point is nondegenerate, and its signature gives the index of the critical point.")

write_concept(D16, "definition-nondegenerate-critical-point", "definition",
    "Nondegenerate Critical Point", "topology", "differential-topology", "intermediate",
    r"""A critical point $x$ of a $C^2$ map $f: M \to \mathbb{R}$ is nondegenerate if the associated Hessian quadratic form $H_x f$ is a nondegenerate quadratic form, i.e., the associated symmetric bilinear form has maximal rank.""",
    "A critical point is nondegenerate if the Hessian matrix (in any coordinate system) is invertible. Nondegenerate critical points are isolated and are the ones studied in Morse theory. A Morse function is defined as a function all of whose critical points are nondegenerate.")

write_concept(D16, "definition-index-of-critical-point", "definition",
    "Index of a Nondegenerate Critical Point", "topology", "differential-topology", "intermediate",
    r"""Let $x$ be a nondegenerate critical point of $f: M \to \mathbb{R}$. The index of $f$ at $x$, denoted $\operatorname{Ind}_x f$, is the maximal dimension of a subspace of $M_x$ on which the Hessian $H_x f$ is negative definite. Equivalently, it is the number of negative eigenvalues of the Hessian matrix in any coordinate system.""",
    "The index measures how many independent directions at the critical point are 'downward curving.' For a Morse function on an $n$-manifold, the index ranges from $0$ (local minimum) to $n$ (local maximum). The index determines how the topology of sublevel sets changes when passing the critical value.")

write_concept(D16, "theorem-1-1-morse-lemma", "theorem",
    "Morse Lemma", "topology", "differential-topology", "advanced",
    r"""Let $p \in M$ be a nondegenerate critical point of index $k$ of a $C^{r+2}$ map $f: M \to \mathbb{R}$, $1 \leqslant r \leqslant \omega$. Then there is a $C^r$ chart $(\varphi, U)$ at $p$ such that
$$f\varphi^{-1}(u_1, \ldots, u_n) = f(p) - \sum_{i=1}^{k} u_i^2 + \sum_{i=k+1}^{n} u_i^2.$$""",
    "The Morse Lemma provides a canonical local coordinate representation of a function near a nondegenerate critical point. In suitable coordinates, the function equals its value at the critical point plus a standard quadratic form with $k$ negative squares and $n-k$ positive squares. This is the fundamental local result of Morse theory.")

write_concept(D16, "definition-morse-function", "definition",
    "Morse Function", "topology", "differential-topology", "intermediate",
    r"""A $C^2$ map $f: M \to \mathbb{R}$ is a Morse function if all of its critical points are nondegenerate. Equivalently, the section $Df: M \to T^*M$ is transverse to the zero section.""",
    "A Morse function is a smooth real-valued function all of whose critical points are nondegenerate. Morse functions are generic (dense in the strong topology) and provide a powerful tool for analyzing the topology of manifolds through the study of critical points and their indices.")

# =========== s017 ===========
D17 = f"{BASE}/s017_2_Differential_Equations_and_Regular_Level_Surfaces"
os.makedirs(D17, exist_ok=True)

write_concept(D17, "theorem-2-1-collaring-theorem", "theorem",
    "Collaring Theorem via Vector Fields", "topology", "differential-topology", "advanced",
    r"""Let $M$ be a $\partial$-manifold. Then there exists a $C^\infty$ embedding
$$F: \partial M \times [0, \infty) \to M$$
such that $F(x, 0) = x$ for all $x \in \partial M$.""",
    "Every manifold with boundary admits a collar: an embedding of $\partial M \times [0, \infty)$ into $M$ that is the identity on the boundary. This theorem is proved using a vector field near the boundary that points inward, whose flow generates the collar.")

write_concept(D17, "definition-gradient-vector-field", "definition",
    "Gradient Vector Field", "topology", "differential-topology", "basic",
    r"""Let $M$ be a Riemannian manifold with inner product $\langle \cdot, \cdot \rangle$ on each tangent space. For a $C^1$ function $f: M \to \mathbb{R}$, the gradient of $f$, denoted $\operatorname{grad} f$, is the unique vector field on $M$ such that for all $x \in M$ and all $Y \in M_x$,
$$\langle \operatorname{grad} f(x), Y \rangle = T_x f(Y).$$
In local coordinates, $\operatorname{grad} f$ is the vector field dual to the differential $Df$ via the Riemannian metric.""",
    "The gradient vector field of a real-valued function on a Riemannian manifold points in the direction of steepest ascent. Its zeros are exactly the critical points of the function. The negative gradient flow can be used to deform sublevel sets and construct diffeomorphisms between regular level surfaces.")

write_concept(D17, "theorem-2-2-regular-interval-theorem", "theorem",
    "Regular Interval Theorem", "topology", "differential-topology", "advanced",
    r"""Let $f: M \to [a, b]$ be a $C^{r+1}$ map on a compact $\partial$-manifold, $1 \leqslant r \leqslant \omega$. Suppose $f$ has no critical points and $f(\partial M) = \{a, b\}$. Then there is a $C^r$ diffeomorphism $F: f^{-1}(a) \times [a, b] \to M$ such that the diagram commutes. In particular all level surfaces of $f$ are diffeomorphic.""",
    "If a function on a compact manifold with boundary has no critical points and maps the boundary to the endpoints of the interval, then the manifold is diffeomorphic to the product of a level surface with the interval. This generalizes the fact that a regular level surface evolves by diffeomorphism as the value changes.")

write_concept(D17, "corollary-2-3-diffeomorphism-from-split-boundary", "corollary",
    "Diffeomorphism from Split Boundary", "topology", "differential-topology", "intermediate",
    r"""Let $M$ be a compact manifold and assume $\partial M = A \cup B$ where $A$ and $B$ are disjoint closed sets. Suppose there exists a $C^2$ map $f: M \to \mathbb{R}$ without critical points such that $f(A) = 0$, $f(B) = 1$. Then $M$ is diffeomorphic to both $A \times I$ and $B \times I$.""",
    "If a compact manifold has its boundary split into two disjoint closed subsets and admits a function without critical points taking distinct constant values on each subset, then the manifold is a product of either boundary component with the interval.")

write_concept(D17, "theorem-2-4-reeb-sphere-theorem", "theorem",
    "Reeb Sphere Theorem", "topology", "differential-topology", "advanced",
    r"""Let $M$ be a compact $n$-dimensional manifold without boundary, admitting a Morse function $f: M \to \mathbb{R}$ with only 2 critical points. Then $M$ is homeomorphic to the $n$-sphere $S^n$.""",
    "A compact manifold without boundary that admits a Morse function with exactly two critical points (a minimum and a maximum) is homeomorphic to the sphere. This is a classical application of Morse theory. Milnor later showed such a manifold need not be diffeomorphic to the standard sphere, leading to the discovery of exotic spheres.")

# =========== s018 ===========
D18 = f"{BASE}/s018_3_Critical_Levels_and_CW"
os.makedirs(D18, exist_ok=True)

write_concept(D18, "definition-admissible-morse-function", "definition",
    "Admissible Morse Function", "topology", "differential-topology", "intermediate",
    r"""Let $M$ be a compact $\partial$-manifold. A Morse function $f: M \to [a, b]$ is admissible if $\partial M = f^{-1}(a) \cup f^{-1}(b)$ and the critical points of $f$ lie in $f^{-1}(a, b)$, i.e., the boundary consists entirely of regular level surfaces.""",
    "An admissible Morse function on a compact manifold with boundary maps the boundary to the two endpoints of the interval, with all critical points in the interior. This setup is standard for analyzing how the topology of the manifold builds up as the value increases from $a$ to $b$.")

write_concept(D18, "theorem-3-1-passing-critical-level-k-cell", "theorem",
    "Passing a Critical Level Attaches a Cell", "topology", "differential-topology", "advanced",
    r"""Let $M$ be compact and $f: M \to [a, b]$ an admissible Morse function. Suppose $f$ has a unique critical point $z$, of index $k$. Then there exists a $k$-cell $e^k \subset M - f^{-1}(b)$ such that $e^k \cap f^{-1}(a) = \partial e^k$, and there is a deformation retraction of $M$ onto $f^{-1}(a) \cup e^k$.""",
    "When a Morse function has a single critical point of index $k$, passing that critical level attaches a $k$-cell to the sublevel set. This is the fundamental theorem linking Morse theory to CW-complex structure: the manifold is built up from the minimum level set by successively attaching cells of dimensions equal to the indices of critical points.")

write_concept(D18, "theorem-3-2-dual-cell-theorem", "theorem",
    "Dual Cell Theorem", "topology", "differential-topology", "advanced",
    r"""Let $f: M \to [a, b]$ be an admissible Morse function having a unique critical point $z$, of index $k$. Then there exists an $(n-k)$-cell $e_*^{n-k} \subset M - f^{-1}(a)$ such that $e_*^{n-k} \cap f^{-1}(b) = \partial e_*^{n-k}$, and there is a deformation retraction of $M$ onto $f^{-1}(b) \cup e_*^{n-k}$. Moreover $e_*^{n-k}$ can be chosen so that $e^k$ meets $e_*^{n-k}$ only at $z$, and transversely.""",
    "By considering $-f$ instead of $f$, passing a critical level downward attaches an $(n-k)$-cell. The two cells $e^k$ and $e_*^{n-k}$ are dual to each other and intersect transversely at the critical point. This duality is a key feature of Morse theory.")

write_concept(D18, "theorem-3-3-multiple-critical-points", "theorem",
    "Multiple Critical Points at One Level", "topology", "differential-topology", "advanced",
    r"""Let $f: M \to [a, b]$ be an admissible Morse function of type $(v_0, \ldots, v_n)$ on a compact manifold. Suppose $f$ has just one critical value $c$, $a < c < b$. Then there are disjoint $k$-cells $e_i^k \subset M - f^{-1}(b)$, $1 \leqslant i \leqslant v_k$, $k = 0, \ldots, n$, such that $e_i^k \cap f^{-1}(a) = \partial e_i^k$; and there is a deformation retraction of $M$ onto $f^{-1}(a) \cup \bigcup_{i,k} e_i^k$.""",
    "If several critical points share the same critical value, disjoint cells can be attached simultaneously, one for each critical point, with dimensions equal to the corresponding indices. The sublevel set below the critical value deformation retracts onto the union of the previous sublevel set with these cells.")

write_concept(D18, "theorem-3-4-morse-inequalities", "theorem",
    "Morse Inequalities", "topology", "differential-topology", "advanced",
    r"""Let $f: M \to [a, b]$ be an admissible Morse function on a compact manifold, of type $(v_0, \ldots, v_n)$. Let $F$ be a field and denote by $\beta_k$ the dimension of the relative homology group $H_k(M, f^{-1}(a); F)$. Then:
(a) $\sum_{k=0}^{m} (-1)^{k+m} v_k \geqslant \sum_{k=0}^{m} (-1)^{k+m} \beta_k$ for $0 \leqslant m \leqslant n$;
(b) $\sum_{k=0}^{n} (-1)^k v_k = \sum_{k=0}^{n} (-1)^k \beta_k = \chi(M, f^{-1}(a))$.""",
    "The Morse inequalities relate the number $v_k$ of critical points of index $k$ to the Betti numbers $\beta_k$. The alternating sum of the $v_k$ equals the Euler characteristic. Moreover, each partial alternating sum of the $v_k$ is at least the corresponding sum of the $\beta_k$, meaning there must be at least as many critical points of each index as there are independent homology classes.")

write_concept(D18, "theorem-3-7-critical-points-exceed-betti-numbers", "theorem",
    "Critical Points Exceed Betti Numbers", "topology", "differential-topology", "intermediate",
    r"""In the Morse inequalities (Theorems 3.4 and 3.5), $v_k \geqslant \beta_k$ for $k = 0, \ldots, n$.""",
    "A direct consequence of the Morse inequalities: the number of critical points of index $k$ is at least the $k$-th Betti number. This provides a lower bound on the number of critical points a Morse function must have, based on the homology of the manifold.")

write_concept(D18, "theorem-3-8-hopf-euler-characteristic", "theorem",
    "Hopf's Theorem: Equality of Euler Characteristics", "topology", "differential-topology", "advanced",
    r"""The homological Euler characteristic equals the Euler characteristic (defined via vector field indices) for a compact manifold without boundary:
$$\sum_{k=0}^{n} (-1)^k \beta_k = \sum_{p} \operatorname{Ind}_p X$$
where $\beta_k$ are the Betti numbers and $X$ is a vector field with isolated zeros.""",
    "Hopf's theorem equates two definitions of the Euler characteristic: the alternating sum of Betti numbers (homological) and the sum of indices of zeros of a vector field (differential-topological). The proof uses a Morse function and its gradient vector field, showing the index at a critical point of index $k$ is $(-1)^k$.")

write_concept(D18, "theorem-4-1-finite-cw-complex-from-morse", "theorem",
    "Compact Manifold has Homotopy Type of Finite CW-Complex", "topology", "differential-topology", "advanced",
    r"""Let $M$ be a compact $n$-manifold and $f: M \to [a, b]$ an admissible Morse function of type $(v_0, \ldots, v_n)$. Then $M$ has the homotopy type of a finite CW-complex having exactly $v_k$ cells of dimension $k$ for each $k = 0, \ldots, n$, and no other cells.""",
    "Every compact manifold admits a Morse function, and via this function the manifold has the homotopy type of a finite CW-complex with cells corresponding to the critical points. This establishes a fundamental bridge between differential topology and homotopy theory.")

write_concept(D18, "definition-cw-complex", "definition",
    "CW-Complex", "topology", "algebraic-topology", "intermediate",
    r"""A CW-complex is a space $X$ which can be expressed as $X = \bigcup_{n=0}^{\infty} X_n$ where $X_0 \subset X_1 \subset \cdots$, $X_0$ is a discrete subset and $X_{n+1}$ is obtained from $X_n$ by attaching $n$-cells via continuous maps of their boundaries into $X_{n-1}$. It is required that a subset of $X$ is closed provided its intersection with each closed cell is closed. If $X = X_n$, $X$ is an $n$-dimensional CW-complex. If the number of cells is finite, $X$ is a finite CW-complex.""",
    "A CW-complex is a topological space built by inductively attaching cells of increasing dimension. The 'CW' stands for 'closure-finite' and 'weak topology.' Morse theory shows that every compact manifold has the homotopy type of a finite CW-complex.")

# =========== s019 ===========
D19 = f"{BASE}/s019_1_Cobordism"
os.makedirs(D19, exist_ok=True)

write_concept(D19, "definition-cobordism", "definition",
    "Cobordism", "topology", "differential-topology", "intermediate",
    r"""Two compact $n$-manifolds $M_0, M_1$ without boundary are cobordant, denoted $M_0 \sim M_1$, if there is a compact $(n+1)$-manifold $W$ such that $\partial W \approx M_0 \times 0 \cup M_1 \times 1$. The set of cobordism classes is denoted $\mathfrak{N}^n$; the cobordism class of $M$ is $[M]$.""",
    "Cobordism is an equivalence relation on compact manifolds without boundary: two manifolds are cobordant if together they form the boundary of a compact manifold of one dimension higher. The cobordism groups $\mathfrak{N}^n$ are central objects in differential topology.")

write_concept(D19, "definition-oriented-cobordism", "definition",
    "Oriented Cobordism", "topology", "differential-topology", "intermediate",
    r"""Let $(M_i, \omega_i)$ be oriented compact $n$-manifolds. Then $(M_0, \omega_0)$ and $(M_1, \omega_1)$ are oriented cobordant if there is a compact oriented $(n+1)$-manifold $(W, \theta)$ and an orientation-preserving diffeomorphism
$$(\partial W, \partial \theta) \approx (M_0 \times 0, -\omega_0) \cup (M_1 \times 1, \omega_1).$$
The set of these equivalence classes is denoted $\Omega^n$.""",
    "Oriented cobordism is the analogue of cobordism for oriented manifolds. The boundary orientation convention involves reversing the orientation of $M_0$ and preserving that of $M_1$. The oriented cobordism groups $\Omega^n$ form a graded ring under Cartesian product.")

write_concept(D19, "theorem-1-1-cobordism-groups", "theorem",
    "Cobordism Groups", "topology", "differential-topology", "intermediate",
    r"""The operation of disjoint union makes $\mathfrak{N}^n$ and $\Omega^n$ into abelian groups. The zero element is the class of any manifold which is a boundary. The inverse of $[M]$ is $[M]$ itself (in $\mathfrak{N}^n$), and the inverse of $[M, \omega]$ is $[M, -\omega]$ (in $\Omega^n$).""",
    "Under disjoint union, cobordism classes form abelian groups. Every element in the unoriented cobordism group has order 2 (since $M \cup M$ bounds $M \times I$). In the oriented case, the inverse of a class is obtained by reversing the orientation.")

write_concept(D19, "definition-thom-homomorphism", "definition",
    "Thom Homomorphism", "topology", "differential-topology", "advanced",
    r"""Let $E_{s,k} \to G_{s,k}$ be the universal Grassmann bundle and $E^*_{s,k}$ its one-point compactification. The Thom homomorphism
$$\tau: \pi_{n+k}(E^*_{s,k}) \to \mathfrak{N}^n$$
is defined for $s$ sufficiently large by $\tau([f]) = [f^{-1}(G_{s,k})]$, where $f: S^{n+k} \to E^*_{s,k}$ is a smooth map transverse to $G_{s,k}$.""",
    "The Thom homomorphism maps homotopy classes of maps from a sphere into the Thom space to cobordism classes. The preimage of the base space (Grassmannian) under a transverse map is an $n$-manifold whose cobordism class is the image.")

write_concept(D19, "theorem-2-3-thom-isomorphism", "theorem",
    "Thom Isomorphism Theorem", "topology", "differential-topology", "advanced",
    r"""For $s \geqslant k + n + 1$ and $k > n$, the Thom homomorphism $\tau: \pi_{n+k}(E^*_{s,k}) \to \mathfrak{N}^n$ is an isomorphism. For $k > n + 1$, the same holds for the oriented Thom homomorphism $\tilde{\tau}: \pi_{n+k}(\tilde{E}^*_{s,k}) \to \Omega^n$.""",
    "The Thom isomorphism identifies cobordism groups with certain homotopy groups of Thom spaces. This is the foundational result of cobordism theory, reducing the geometric problem of classifying manifolds up to cobordism to a homotopy-theoretic computation.")

write_concept(D19, "lemma-2-2-standard-form-map", "lemma",
    "Standard Form for Maps to Thom Space", "topology", "differential-topology", "advanced",
    r"""Let $Q$ be a compact manifold and $B$ a compact manifold without boundary. Then every map $f: Q \to E^*$ (where $E^*$ is the one-point compactification of a vector bundle over $B$) is homotopic to a map $h$ in standard form: there is a submanifold $M \subset Q$ and a tubular neighborhood $U \subset Q$ of $M$ such that $U = h^{-1}(E)$, $M = h^{-1}(B)$, and $h|U$ is a vector bundle map, with $h(Q - U) = \infty$.""",
    "Every map into the Thom space of a vector bundle can be homotoped to a 'standard form' where the preimage of the base space is a submanifold, the preimage of the total space is a tubular neighborhood, and the rest of the domain maps to the point at infinity.")

# =========== s020 ===========
D20 = f"{BASE}/s020_1_Isotopy"
os.makedirs(D20, exist_ok=True)

write_concept(D20, "definition-isotopy", "definition",
    "Isotopy", "topology", "differential-topology", "intermediate",
    r"""Let $V$ and $M$ be $C^r$ manifolds. An isotopy of $V$ in $M$ is a $C^r$ map $F: V \times I \to M$ such that for each $t \in I$, the map $F_t: V \to M$, $F_t(x) = F(x, t)$, is an embedding. Two embeddings $f, g: V \hookrightarrow M$ are isotopic if there is an isotopy $F$ with $F_0 = f$ and $F_1 = g$.""",
    "An isotopy is a smooth one-parameter family of embeddings. It represents a deformation of one embedding to another through embeddings. The track of an isotopy is the level-preserving embedding $\hat{F}: V \times I \to M \times I$, $(x, t) \mapsto (F(x, t), t)$.")

write_concept(D20, "definition-diffeotopy", "definition",
    "Diffeotopy (Ambient Isotopy)", "topology", "differential-topology", "intermediate",
    r"""Let $M$ be a $C^r$ manifold. A diffeotopy (or ambient isotopy) of $M$ is an isotopy $F: M \times I \to M$ such that each $F_t: M \to M$ is a $C^r$ diffeomorphism and $F_0 = 1_M$.""",
    "A diffeotopy is an isotopy of the whole manifold that starts at the identity. It realizes an isotopy of submanifolds by a one-parameter family of diffeomorphisms of the ambient manifold. The isotopy extension theorem guarantees that isotopies of compact submanifolds extend to diffeotopies.")

write_concept(D20, "theorem-1-1-diffeotopy-from-vector-field", "theorem",
    "Diffeotopy Generated by Time-Dependent Vector Field", "topology", "differential-topology", "advanced",
    r"""Let $G$ be a time-dependent vector field on $M$ having bounded velocity. Then $G$ generates a diffeotopy of $M$. That is, there is a unique diffeotopy $F: M \times I \to M$ such that
$$\frac{\partial F}{\partial t}(x, t) = G(F(x, t), t).$$""",
    "A time-dependent vector field with bounded velocity on a manifold generates a unique diffeotopy whose velocity at each point equals the vector field. This is the fundamental existence theorem linking vector fields to diffeotopies, generalizing the flow of an autonomous vector field.")

write_concept(D20, "theorem-1-2-compact-support-vector-field-isotopy", "theorem",
    "Compact Support Vector Field Generates Isotopy", "topology", "differential-topology", "intermediate",
    r"""A time-dependent vector field which has compact support generates an isotopy. In particular, every time-dependent vector field on a compact manifold generates an isotopy.""",
    "If the time-dependent vector field vanishes outside a compact set, then it automatically has bounded velocity and thus generates an isotopy. On a compact manifold, every time-dependent vector field generates an isotopy.")

write_concept(D20, "theorem-1-3-isotopy-extension", "theorem",
    "Isotopy Extension Theorem", "topology", "differential-topology", "advanced",
    r"""Let $V \subset M$ be a compact submanifold and $F: V \times I \to M$ an isotopy of $V$. If either $F(V \times I) \subset \partial M$ or $F(V \times I) \subset M - \partial M$, then $F$ extends to a diffeotopy of $M$ having compact support.""",
    "Any isotopy of a compact submanifold that stays either entirely in the interior or entirely in the boundary can be extended to a diffeotopy of the whole ambient manifold with compact support. This is one of the most useful technical tools in differential topology.")

write_concept(D20, "theorem-1-9-smoothing-homeomorphism", "theorem",
    "Smoothing Homeomorphisms Along a Common Boundary", "topology", "differential-topology", "advanced",
    r"""For $i = 0, 1$ let $W_i$ be an $n$-manifold without boundary which is the union of two closed $n$-dimensional submanifolds $M_i, N_i$ such that $M_i \cap N_i = \partial M_i = \partial N_i = V_i$. Let $h: W_0 \to W_1$ be a homeomorphism which maps $M_0$ and $N_0$ diffeomorphically onto $M_1$ and $N_1$ respectively. Then there is a diffeomorphism $f: W_0 \approx W_1$ such that $f(M_0) = M_1$, $f(N_0) = N_1$ and $f|V_0 = h|V_0$.""",
    "A homeomorphism between manifolds that is already a diffeomorphism on each piece of a decomposition along a common boundary can be smoothed to a global diffeomorphism, using isotopies of tubular neighborhoods to adjust the gluing along the interface.")

# =========== s021 ===========
D21 = f"{BASE}/s021_3_Isotopies_of_Disks"
os.makedirs(D21, exist_ok=True)

write_concept(D21, "theorem-2-1-uniqueness-of-gluing", "theorem",
    "Uniqueness of Differential Structure on Glued Manifolds", "topology", "differential-topology", "advanced",
    r"""Let $P$ and $Q$ be $n$-dimensional $\partial$-manifolds and $f: \partial Q \approx \partial P$ a diffeomorphism. The adjunction space $W = P \cup_f Q$ admits a differential structure extending those on $P$ and $Q$, and all such differential structures are diffeomorphic.""",
    "When two manifolds with boundary are glued along their boundaries via a diffeomorphism, the resulting topological manifold admits a differential structure, and this structure is unique up to diffeomorphism. This justifies the common practice of constructing manifolds by gluing.")

write_concept(D21, "theorem-2-3-isotopic-gluing", "theorem",
    "Isotopic Gluing Diffeomorphisms Yield Diffeomorphic Manifolds", "topology", "differential-topology", "intermediate",
    r"""Let $f, g: \partial Q \approx \partial P$ be isotopic diffeomorphisms. Then $P \cup_f Q \approx P \cup_g Q$.""",
    "If two gluing diffeomorphisms are isotopic, the resulting glued manifolds are diffeomorphic. This means the diffeomorphism type of the glued manifold depends only on the isotopy class of the gluing map.")

write_concept(D21, "theorem-3-1-isotopy-of-disks", "theorem",
    "Isotopy Classification of Disk Embeddings", "topology", "differential-topology", "advanced",
    r"""Let $M$ be a connected $n$-manifold and $f, g: D^k \hookrightarrow M$ embeddings of the $k$-disk, $0 \leqslant k \leqslant n$. If $k = n$ and $M$ is orientable, assume that $f$ and $g$ both preserve, or both reverse, orientation. Then $f$ and $g$ are isotopic. If $f(D^k) \cup g(D^k) \subset M - \partial M$, an isotopy between them can be realized by a diffeotopy of $M$ having compact support.""",
    "In a connected manifold, any two embeddings of a $k$-disk are isotopic, provided orientation conditions are satisfied when $k = n$. This means there is essentially a unique way to embed a disk, up to isotopy and orientation. The result is fundamental for the classification of surfaces and for handle theory.")

write_concept(D21, "theorem-3-2-isotopy-of-disjoint-disks", "theorem",
    "Isotopy of Disjoint Disks", "topology", "differential-topology", "intermediate",
    r"""Let $M$ be a connected $n$-manifold without boundary. Suppose that $f_i, g_i: D^n \hookrightarrow M$ ($i = 1, 2$) are embeddings such that $f_1(D^n) \cap f_2(D^n) = \varnothing = g_1(D^n) \cap g_2(D^n)$. If $M$ is orientable suppose further that $f_i$ and $g_i$ both preserve, or both reverse, orientation. Then there is a diffeotopy of $M$ carrying $f_i$ to $g_i$ for $i = 1, 2$.""",
    "Two pairs of disjoint embedded $n$-disks in a connected $n$-manifold are simultaneously isotopic, provided the orientation conditions match. This generalizes the isotopy uniqueness to multiple disks and is used in constructing connected sums and analyzing handle decompositions.")

write_concept(D21, "theorem-3-3-classification-of-circle-diffeomorphisms", "theorem",
    "Classification of Circle Diffeomorphisms up to Isotopy", "topology", "differential-topology", "intermediate",
    r"""Every diffeomorphism of $S^1$ is isotopic to either the identity (if degree $+1$) or complex conjugation (if degree $-1$). In particular, $\pi_0(\operatorname{Diff}(S^1)) \cong \mathbb{Z}_2$.""",
    "Diffeomorphisms of the circle are classified up to isotopy by their degree: degree $+1$ diffeomorphisms are isotopic to the identity, while degree $-1$ diffeomorphisms are isotopic to complex conjugation. This is a key ingredient in the classification of surfaces.")

write_concept(D21, "corollary-3-4-sphere-from-two-critical-points", "corollary",
    "Morse Function with Two Critical Points Yields Sphere", "topology", "differential-topology", "advanced",
    r"""Let $M$ be a compact 2-manifold without boundary admitting a Morse function having only 2 critical points. Then $M \approx S^2$.""",
    "In dimension 2, Reeb's theorem can be strengthened: a compact surface admitting a Morse function with exactly two critical points is diffeomorphic (not just homeomorphic) to the 2-sphere. The proof uses the classification of circle diffeomorphisms and uniqueness of gluing.")

write_concept(D21, "definition-handle-attachment", "definition",
    "Handle Attachment on a Surface", "topology", "geometric-topology", "intermediate",
    r"""Let $M$ be a surface and $f: S^0 \times D^2 \hookrightarrow M - \partial M$ an embedding whose image is a pair of disjoint disks. The surface obtained by attaching a handle is
$$M[f] = [M - \operatorname{Int} f(S^0 \times D^2)] \bigcup_f D^1 \times S^1$$
where the gluing is along $f|S^0 \times S^1$. This adds a cylinder (handle) connecting the two disks.""",
    "Handle attachment is the fundamental surgical operation for constructing surfaces. Removing two disks and gluing in a cylinder increases the genus by 1 for orientable surfaces. Repeating this process builds surfaces of arbitrary genus starting from the sphere.")

write_concept(D21, "definition-genus-of-surface", "definition",
    "Genus of a Surface", "topology", "geometric-topology", "basic",
    r"""An orientable surface $M$ has genus $p \geqslant 0$ if $M$ can be obtained from $S^2$ by successively attaching handles $p$ times. A nonorientable surface has genus $p \geqslant 1$ if it can be obtained from $S^2$ by attaching $p$ crosscaps (i.e., taking connected sum with $p$ copies of the real projective plane).""",
    "The genus is a fundamental invariant of compact surfaces. An orientable surface of genus $p$ has Euler characteristic $2 - 2p$. A nonorientable surface of genus $p$ has Euler characteristic $2 - p$. Two connected compact surfaces without boundary are diffeomorphic if and only if they have the same genus and orientability type.")

write_concept(D21, "theorem-1-7-handle-equals-two-crosscaps", "theorem",
    "Handle Equals Two Crosscaps on Nonorientable Surface", "topology", "geometric-topology", "intermediate",
    r"""Attaching a handle to a connected nonorientable surface is the same as attaching two crosscaps. Therefore attaching a handle to a nonorientable surface of genus $p$ produces a nonorientable surface of genus $p + 2$.""",
    "On a nonorientable surface, the operations of attaching a handle and attaching two crosscaps yield diffeomorphic surfaces. This is a key relation in the classification: it explains why orientable genus $p$ surfaces become nonorientable genus $2p+1$ surfaces after attaching a crosscap.")

write_concept(D21, "theorem-1-8-crosscap-on-orientable-surface", "theorem",
    "Crosscap on an Orientable Surface", "topology", "geometric-topology", "intermediate",
    r"""Let $M$ be an orientable surface of genus $p$. Attaching a crosscap to $M$ yields a nonorientable surface of genus $2p + 1$.""",
    "Adding a crosscap (taking connected sum with the real projective plane) to an orientable surface of genus $p$ produces a nonorientable surface of genus $2p+1$. This relation together with the handle-equals-two-crosscaps theorem forms the basis for the complete classification of surfaces.")

write_concept(D21, "theorem-1-9-model-surface-classification", "theorem",
    "Classification of Model Surfaces", "topology", "geometric-topology", "intermediate",
    r"""Two model surfaces are diffeomorphic if and only if (a) they have the same genus and the same number of boundary circles, and (b) both are orientable or both are nonorientable. Equivalently, two model surfaces are diffeomorphic if and only if they have the same genus, the same Euler characteristic, and the same orientability type.""",
    "Model surfaces (orientable or nonorientable surfaces of a given genus, possibly with boundary circles) are classified by genus, number of boundary components, and orientability. This is the prelude to the full classification theorem for all compact connected surfaces.")

write_concept(D21, "theorem-2-1-disk-characterization-morse", "theorem",
    "Disk Characterization via Morse Function", "topology", "differential-topology", "advanced",
    r"""Let $f: M \to \mathbb{R}$ be an admissible Morse function on a compact connected surface $M$. Suppose $f$ has exactly 3 critical points, and these are of type 0, 0, 1. Then $M \approx D^2$.""",
    "A compact connected surface admitting an admissible Morse function with exactly three critical points (two minima and one saddle) is diffeomorphic to the 2-disk. This is the key technical lemma in the Morse-theoretic proof of the classification of surfaces, and the proof given generalizes to higher dimensions.")

write_concept(D21, "definition-connected-sum", "definition",
    "Connected Sum of Manifolds", "topology", "differential-topology", "basic",
    r"""Let $M, N$ be connected $n$-manifolds without boundary. Their connected sum $M \# N$ is obtained by removing the interior of a smoothly embedded $n$-disk from each and gluing the resulting boundary spheres together via a diffeomorphism. The result is a connected $n$-manifold without boundary, well-defined up to diffeomorphism.""",
    "The connected sum is a binary operation on manifolds that 'adds' them together. It is well-defined (independent of the choices of disks and gluing map) and associative. The sphere $S^n$ acts as the identity: $M \# S^n \approx M$. Connected sums are fundamental for constructing and classifying manifolds.")

print("All concepts created successfully!")
print(f"Total: s012=3, s014=11, s016=7, s017=5, s018=9, s019=6, s020=6, s021=14")
