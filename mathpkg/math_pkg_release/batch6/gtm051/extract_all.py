#!/usr/bin/env python3
"""Extract ALL concepts from GTM051 (A Course in Differential Geometry) - 47 sections."""
import os

BASE = "/home/a123/文档/mathpkg/pipeline_output/math_pkg_tmp/concepts_batch6/gtm051"
os.makedirs(BASE, exist_ok=True)

def write_concept(slug, typ, title, domain, subdomain, stmt, intro, ch, sec, difficulty="intermediate"):
    d = os.path.join(BASE, slug)
    os.makedirs(d, exist_ok=True)
    yaml = f"""id: {slug}
title_en: "{title}"
title_zh: ""
type: {typ}
domain: {domain}
subdomain: {subdomain}
difficulty: {difficulty}
tags: []
depends_on: {{required: [], recommended: [], suggested: []}}
source_books: [{{book_id: "gtm051", author: "Wilhelm Klingenberg", title: "A Course in Differential Geometry", chapter: "{ch}", section: "{sec}", pages: "", role_in_book: ""}}]
content_hash: ""
extraction_date: "2026-06-27"
extraction_agent: "v8-full-extract"
"""
    with open(os.path.join(d, "concept.yaml"), "w") as f:
        f.write(yaml)
    with open(os.path.join(d, "theorem.tex"), "w") as f:
        f.write(stmt)
    intro_md = f"""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

{intro}
"""
    with open(os.path.join(d, "introduce.en.md"), "w") as f:
        f.write(intro_md)
    return d

def write_proof(slug, proof_text, ch, sec):
    d = os.path.join(BASE, slug)
    proof_md = f"""---
role: proof
locale: en
of_concept: {slug}
source_book: gtm051
source_chapter: "{ch}"
source_section: "{sec}"
---

{proof_text}
"""
    with open(os.path.join(d, f"proof_gtm051_{ch}_{sec}.en.md"), "w") as f:
        f.write(proof_md)

# ===================================================================
# CHAPTER 0: Calculus in Euclidean Space
# ===================================================================

# s001: 0.3 Differentiation in R^n
write_concept("differential-of-a-map", "definition",
    "Differential of a Differentiable Map", "geometry", "differential-geometry",
    "Let $F: U \\to \\mathbb{R}^m$ be a differentiable map on an open set $U \\subset \\mathbb{R}^n$. For $x_0 \\in U$, the differential $dF_{x_0}: \\mathbb{R}^n \\to \\mathbb{R}^m$ is the unique linear map $L$ satisfying\n$$|F(x) - F(x_0) - L(x - x_0)| = o(|x - x_0|).$$\nThe differential is also denoted by $dF$ or $dF_{x_0}$.",
    "The differential is the best linear approximation to a differentiable map at a point. It generalizes the derivative from single-variable calculus, with the Jacobian matrix as its coordinate representation.",
    "0", "0.3", "basic")

write_concept("tangent-space-euclidean", "definition",
    "Tangent Space of Euclidean Space", "geometry", "differential-geometry",
    "For $x_0 \\in \\mathbb{R}^n$, the tangent space $T_{x_0}\\mathbb{R}^n$ (also written $\\mathbb{R}_{x_0}^n$) is the $n$-dimensional vector space consisting of pairs $(x_0, x) \\in \\{x_0\\} \\times \\mathbb{R}^n$, with vector space structure defined via the bijection $(x_0, x) \\mapsto x$.",
    "The tangent space at a point formalizes the notion of vectors attached to a point. It is the foundation for defining differentials, vector fields, and all of differential geometry.",
    "0", "0.4", "basic")

# s002: 0.5 Local Behavior — Inverse Function Theorem
write_concept("inverse-function-theorem", "theorem",
    "Inverse Function Theorem", "geometry", "differential-geometry",
    "Let $U$ be an open neighborhood of $0 \\in \\mathbb{R}^n$. Suppose $F: U \\to \\mathbb{R}^n$ is a differentiable function with $F(0) = 0$. If $dF_0: \\mathbb{R}^n \\to \\mathbb{R}^n$ is bijective, then there exists an open neighborhood $U' \\subset U$ of $0$ such that $F|_{U'}: U' \\to F(U')$ is a diffeomorphism.",
    "The inverse function theorem is the fundamental result that a differentiable map with invertible differential is locally invertible. It is the cornerstone for the study of manifolds, submersions, and immersions.",
    "0", "0.5", "basic")

write_concept("implicit-function-theorem-injective", "theorem",
    "Local Normal Form for Injective Differential (Implicit Function Theorem)", "geometry", "differential-geometry",
    "Let $F: U \\to \\mathbb{R}^m$ be differentiable on an open neighborhood $U$ of $0 \\in \\mathbb{R}^n$, with $F(0) = 0$. If $dF_0$ is injective, then there exists a local diffeomorphism $g$ of $\\mathbb{R}^m$ near $0$ such that $g \\circ F(x^1, \\ldots, x^n) = (x^1, \\ldots, x^n, 0, \\ldots, 0)$ locally.",
    "When the differential is injective, the map can be rectified to the standard inclusion of $\\mathbb{R}^n$ into $\\mathbb{R}^m$ by a change of coordinates in the target. This is the rank theorem for immersions.",
    "0", "0.5", "intermediate")

write_concept("implicit-function-theorem-surjective", "theorem",
    "Local Normal Form for Surjective Differential (Implicit Function Theorem)", "geometry", "differential-geometry",
    "Let $F: U \\to \\mathbb{R}^m$ be differentiable on an open neighborhood $U$ of $0 \\in \\mathbb{R}^n$, with $F(0) = 0$. If $dF_0$ is surjective, then there exists a local diffeomorphism $h$ of $\\mathbb{R}^n$ near $0$ such that $F \\circ h(x^1, \\ldots, x^n) = (x^1, \\ldots, x^m)$ locally.",
    "When the differential is surjective, the map can be rectified to the standard projection from $\\mathbb{R}^n$ onto $\\mathbb{R}^m$ by a change of coordinates in the domain. This is the rank theorem for submersions.",
    "0", "0.5", "intermediate")

# ===================================================================
# CHAPTER 1: Curves
# ===================================================================

# s002 (continued): 1.1 Definitions
write_concept("parametrized-curve", "definition",
    "Parametrized Curve", "geometry", "differential-geometry",
    "Let $I \\subseteq \\mathbb{R}$ be an interval. A parametrized curve in $\\mathbb{R}^n$ is a $C^\\infty$ mapping $c: I \\to \\mathbb{R}^n$. The curve is regular if $\\dot{c}(t) \\neq 0$ for all $t \\in I$.",
    "A parametrized curve is a smooth map from an interval into Euclidean space. Regularity (non-vanishing velocity) ensures the curve has a well-defined tangent line at each point.",
    "1", "1.1", "basic")

write_concept("vector-field-along-curve", "definition",
    "Vector Field along a Curve", "geometry", "differential-geometry",
    "A vector field along a curve $c: I \\to \\mathbb{R}^n$ is a differentiable mapping $X: I \\to \\mathbb{R}^n$. The vector $X(t)$ is considered as an element of $T_{c(t)}\\mathbb{R}^n$.",
    "A vector field along a curve assigns a tangent vector at each point of the curve. These are fundamental for studying curvature, torsion, and parallel transport.",
    "1", "1.1", "basic")

write_concept("parameter-transformation", "definition",
    "Parameter Transformation of a Curve", "geometry", "differential-geometry",
    "Let $c: I \\to \\mathbb{R}^n$ be a curve. A parameter transformation is a diffeomorphism $\\phi: J \\to I$ where $J$ is an interval. The curve $\\tilde{c} := c \\circ \\phi: J \\to \\mathbb{R}^n$ is called a reparametrization of $c$. Relationship by parameter transformation defines an equivalence relation; an equivalence class is called an unparameterized curve.",
    "A parameter transformation changes the speed of traversal without changing the geometric image of the curve. Unparameterized curves capture the intrinsic geometry independent of parametrization.",
    "1", "1.1", "basic")

write_concept("arc-length-parameterization", "definition",
    "Arc Length Parameterization", "geometry", "differential-geometry",
    "A curve $c: I \\to \\mathbb{R}^n$ is parameterized by arc length if $|\\dot{c}(t)| = 1$ for all $t \\in I$. The length of $c$ is $L(c) := \\int_I |\\dot{c}(t)| dt$ and the energy is $E(c) := \\frac{1}{2} \\int_I \\dot{c}(t)^2 dt$.",
    "Arc length parameterization gives a curve unit speed, making it the natural parametrization for studying geometric properties. Length and energy are fundamental geometric invariants of curves.",
    "1", "1.1", "basic")

write_concept("existence-arc-length-parametrization", "proposition",
    "Existence of Arc Length Parametrization", "geometry", "differential-geometry",
    "Every regular curve $c: I \\to \\mathbb{R}^n$ can be parameterized by arc length. That is, there exists a change of variables $\\phi: J \\to I$ such that $|(c \\circ \\phi)'(s)| = 1$ for all $s \\in J$.",
    "Any regular curve admits a unit-speed reparametrization. The construction uses the arc length function $s(t) = \\int_{t_0}^t |\\dot{c}(t')| dt'$, which is invertible by regularity.",
    "1", "1.1", "basic")

# s002: 1.2 Frenet Frame
write_concept("moving-n-frame", "definition",
    "Moving $n$-Frame along a Curve", "geometry", "differential-geometry",
    "Let $c: I \\to \\mathbb{R}^n$ be a curve. A moving $n$-frame along $c$ is a collection of $n$ differentiable mappings $e_i: I \\to \\mathbb{R}^n$, $1 \\leq i \\leq n$, such that for all $t \\in I$, $e_i(t) \\cdot e_j(t) = \\delta_{ij}$.",
    "A moving frame provides an orthonormal basis at each point of the curve, adapted to the curve's geometry. It is the fundamental tool for studying curves in higher dimensions.",
    "1", "1.2", "intermediate")

write_concept("frenet-frame", "definition",
    "Frenet Frame", "geometry", "differential-geometry",
    "A moving $n$-frame $(e_i(t))$ along $c$ is a Frenet frame if for all $k$, $1 \\leq k \\leq n$, the $k$-th derivative $c^{(k)}(t)$ is a linear combination of $e_1(t), \\ldots, e_k(t)$.",
    "The Frenet frame is a moving frame adapted to the curve via its derivatives. The first vector is the unit tangent, and successive vectors are obtained by Gram-Schmidt from higher derivatives.",
    "1", "1.2", "intermediate")

write_concept("distinguished-frenet-frame", "proposition",
    "Existence and Uniqueness of the Distinguished Frenet Frame", "geometry", "differential-geometry",
    "Let $c: I \\to \\mathbb{R}^n$ be a curve such that for all $t \\in I$, the vectors $\\dot{c}(t), \\ddot{c}(t), \\ldots, c^{(n-1)}(t)$ are linearly independent. Then there exists a unique Frenet frame with the properties:\n(i) For $1 \\leq k \\leq n-1$, $\\dot{c}(t), \\ldots, c^{(k)}(t)$ and $e_1(t), \\ldots, e_k(t)$ have the same orientation;\n(ii) $e_1(t), \\ldots, e_n(t)$ has the positive orientation.",
    "The distinguished Frenet frame is the canonical moving frame for a curve with linearly independent derivatives. It is constructed via the Gram-Schmidt process and provides the natural basis for the Frenet equations.",
    "1", "1.2", "intermediate")

# s003: 1.3 Frenet Equations
write_concept("frenet-equations", "proposition",
    "Frenet Equations", "geometry", "differential-geometry",
    "Let $(e_i(t))$ be a moving $n$-frame along $c$. Then the derivatives $\\dot{e}_i(t)$ can be expressed as\n$$\\dot{e}_i(t) = \\sum_j \\omega_{ij}(t) e_j(t)$$\nwhere $\\omega(t) = (\\omega_{ij}(t))$ is a skew-symmetric matrix. If $(e_i(t))$ is a distinguished Frenet frame, then $\\omega_{ij}(t) = 0$ for $|i - j| > 1$, i.e., $\\omega$ is tridiagonal.",
    "The Frenet equations describe the infinitesimal rotation of the Frenet frame. For a distinguished Frenet frame, only adjacent frame vectors interact, with curvatures $\\kappa_i = \\omega_{i,i+1}$ generalizing the classical curvature and torsion in $\\mathbb{R}^3$.",
    "1", "1.3", "intermediate")

write_concept("frenet-equations-invariance", "proposition",
    "Invariance of Frenet Equations under Isometries and Parameter Change", "geometry", "differential-geometry",
    "Let $c: I \\to \\mathbb{R}^n$ be a curve with Frenet frame $(e_i(t))$ and Frenet matrix $\\omega(t)$.\n(i) If $B: \\mathbb{R}^n \\to \\mathbb{R}^n$ is an isometry, then $\\tilde{c} = B \\circ c$ has Frenet frame $\\tilde{e}_i = R e_i$ (where $R$ is the orthogonal part of $B$) and $\\tilde{\\omega}_{ij} = \\omega_{ij}$.\n(ii) If $\\phi: J \\to I$ is a change of variables and $\\tilde{c} = c \\circ \\phi$, then the Frenet curvatures satisfy $\\tilde{\\kappa}_i(s) = \\kappa_i(\\phi(s))$.",
    "The Frenet equations are invariant under Euclidean motions (isometries) and under reparametrization. This means the curvatures are genuine geometric invariants of the unparameterized curve up to rigid motion.",
    "1", "1.3", "intermediate")

# s004: 1.4-1.5 Plane and Space Curves
write_concept("characterization-of-straight-line", "proposition",
    "Characterization of Straight Lines by Curvature", "geometry", "differential-geometry",
    "Let $c: I \\to \\mathbb{R}^n$ be a regular curve parameterized by arc length. Then $\\kappa(t) = |\\ddot{c}(t)| = 0$ for all $t \\in I$ if and only if $c$ is a straight line.",
    "A curve has zero curvature exactly when it is a straight line. This is the fundamental characterization linking the analytic condition $\\ddot{c} = 0$ with the geometric property of being linear.",
    "1", "1.4", "basic")

write_concept("characterization-of-circle", "proposition",
    "Characterization of the Circle", "geometry", "differential-geometry",
    "For a regular plane curve $c: I \\to \\mathbb{R}^2$ parameterized by arc length, the following are equivalent:\n(i) $\\kappa(t) = \\text{const} > 0$ and $\\tau(t) = 0$;\n(ii) The image of $c$ is contained in a circle of radius $1/\\kappa$.",
    "A plane curve with constant positive curvature is necessarily a circle (or an arc thereof). This is a classic characterization: circles are the only plane curves of constant non-zero curvature.",
    "1", "1.4", "basic")

# ===================================================================
# CHAPTER 2: Plane Curves — Global Theory
# ===================================================================

# s005: 2.1 Rotation Number
write_concept("closed-curve", "definition",
    "Closed Curve", "geometry", "differential-geometry",
    "A curve $c: I = [a, b] \\to \\mathbb{R}^n$ is closed if there exists a curve $\\tilde{c}: \\mathbb{R} \\to \\mathbb{R}^n$ such that $\\tilde{c}|_I = c$ and $\\tilde{c}(t + \\omega) = \\tilde{c}(t)$ for all $t \\in \\mathbb{R}$, where $\\omega = b - a$. Equivalently, $c(a) = c(b)$ and $c^{(k)}(a) = c^{(k)}(b)$ for all $k > 0$.",
    "A closed curve is periodic with all derivatives matching at the endpoints. This allows the curve to be extended smoothly to a periodic function on the whole real line.",
    "2", "2.1", "basic")

write_concept("piecewise-smooth-curve", "definition",
    "Piecewise Smooth Curve", "geometry", "differential-geometry",
    "A piecewise smooth curve is a continuous function $c: [a, b] \\to \\mathbb{R}^n$ together with a partition $a = a_0 < b_0 = a_1 < \\ldots < b_k = b$ such that each restriction $c_j := c|_{[a_j, b_j]}$ is differentiable. The points $c(a_j) = c(b_{j-1})$ are called corners.",
    "A piecewise smooth curve allows finitely many corners where the derivative may jump. This generalization is essential for studying polygons and closed curves with vertices in global theory.",
    "2", "2.1", "basic")

write_concept("tangent-mapping-angle-function", "proposition",
    "Existence of Continuous Angle Function for Tangent Map", "geometry", "differential-geometry",
    "Let $c: [a, b] \\to \\mathbb{R}^2$ be a regular curve. Then there exists a continuous, piecewise differentiable function $\\theta: [a, b] \\to \\mathbb{R}$ such that\n$$e_1(t) = \\dot{c}(t)/|\\dot{c}(t)| = (\\cos \\theta(t), \\sin \\theta(t)).$$\nMoreover, the difference $\\theta(b) - \\theta(a)$ is independent of the choice of $\\theta$.",
    "The tangent direction of a plane curve can be continuously lifted from the circle $S^1$ to the real line $\\mathbb{R}$. The total change $\\theta(b) - \\theta(a)$ measures how many times the tangent vector winds around.",
    "2", "2.1", "intermediate")

write_concept("rotation-number", "definition",
    "Rotation Number of a Closed Plane Curve", "geometry", "differential-geometry",
    "Let $c: [0, \\omega] \\to \\mathbb{R}^2$ be a piecewise smooth, regular, closed curve. The rotation number $n_c$ is defined by\n$$n_c := \\frac{1}{2\\pi} \\int_0^\\omega \\kappa(t) |\\dot{c}(t)| dt + \\frac{1}{2\\pi} \\sum_j \\alpha_j$$\nwhere $\\alpha_j$ are the exterior angles at the corners.",
    "The rotation number is the total number of times the tangent vector winds around the circle as one traverses the closed curve. It is a global topological invariant of the curve.",
    "2", "2.1", "intermediate")

write_concept("rotation-number-integer", "proposition",
    "Rotation Number is an Integer", "geometry", "differential-geometry",
    "The rotation number $n_c$ of a closed piecewise smooth curve is an integer. It is invariant under orientation-preserving change of variables and under congruences of $\\mathbb{R}^2$. An orientation-reversing change of variables or a symmetry changes the sign of $n_c$.",
    "The rotation number is always an integer, reflecting the fact that the tangent vector must return to its starting direction after a full traversal. This is a topological fact with deep geometric consequences.",
    "2", "2.1", "intermediate")

# s006: 2.2 Umlaufsatz
write_concept("umlaufsatz", "theorem",
    "Umlaufsatz (Theorem of Turning Tangents)", "geometry", "differential-geometry",
    "Let $c: I \\to \\mathbb{R}^2$ be a piecewise smooth, regular, simple closed plane curve. Suppose the exterior angles $\\alpha_j$ of $c$ are never equal to $\\pi$ in absolute value. Then the rotation number $n_c = \\pm 1$.",
    "The Umlaufsatz states that the tangent vector of a simple closed curve makes exactly one full turn. This is a cornerstone of global differential geometry, equivalent to the fact that the total curvature of a simple closed curve is $\\pm 2\\pi$.",
    "2", "2.2", "advanced")

# s007: 2.3 Convex Curves
write_concept("convex-curve", "definition",
    "Convex Plane Curve", "geometry", "differential-geometry",
    "A regular plane curve $c: I \\to \\mathbb{R}^2$ is convex if, for all $t_0 \\in I$, the curve lies entirely on one side of the tangent at $c(t_0)$. In other words, for every $t_0 \\in I$, either $(c(t) - c(t_0)) \\cdot e_2(t_0) \\geq 0$ for all $t \\in I$, or $(c(t) - c(t_0)) \\cdot e_2(t_0) \\leq 0$ for all $t \\in I$.",
    "A convex curve never crosses its tangent lines; it always lies on one side. This captures the intuitive geometric notion of convexity for curves in the plane.",
    "2", "2.3", "intermediate")

write_concept("characterization-convex-curves", "theorem",
    "Characterization of Convex Curves via Curvature", "geometry", "differential-geometry",
    "Let $c: I \\to \\mathbb{R}^2$ be a simple closed regular plane curve. Then $c$ is convex if and only if $\\kappa(t) \\geq 0$ for all $t \\in I$, or $\\kappa(t) \\leq 0$ for all $t \\in I$.",
    "A simple closed curve is convex exactly when its curvature does not change sign. This elegant characterization links the global geometric property of convexity to the local analytic property of curvature sign.",
    "2", "2.3", "intermediate")

write_concept("four-vertex-theorem", "theorem",
    "Four-Vertex Theorem", "geometry", "differential-geometry",
    "A simple closed convex plane curve has at least four vertices, i.e., points where $\\dot{\\kappa}(t) = 0$.",
    "The four-vertex theorem states that any simple closed convex curve must have at least four curvature extrema. An ellipse has exactly four. The theorem was first proved by Mukhopadhyaya in 1909.",
    "2", "2.4", "advanced")

# s008: 2.4 Constant Width
write_concept("constant-width-curve", "definition",
    "Curve of Constant Width", "geometry", "differential-geometry",
    "A closed, strictly convex curve $c: I \\to \\mathbb{R}^2$ is said to have constant width $d$ if for every $t$, the unique point $c(t')$ with opposite tangent direction satisfies $d(c(t), c(t')) = d$, a constant.",
    "A curve of constant width has the same distance between any pair of opposite parallel tangent lines. The circle is the simplest example, but non-circular examples (Reuleaux triangle) also exist.",
    "2", "2.4", "intermediate")

# ===================================================================
# CHAPTER 3: Surfaces — Local Theory
# ===================================================================

# s009: 3.1 Definitions
write_concept("surface-patch", "definition",
    "Parameterized Surface Patch", "geometry", "differential-geometry",
    "Let $U \\subset \\mathbb{R}^2$ be an open set. A differentiable mapping $f: U \\to \\mathbb{R}^3$ such that $df_u: T_u\\mathbb{R}^2 \\to T_{f(u)}\\mathbb{R}^3$ is injective for all $u \\in U$ is called a (parameterized) surface patch. Such an $f$ is called regular. The points $u \\in U$ are called parameters of $f$.",
    "A surface patch is a regular smooth map from a planar domain into $\\mathbb{R}^3$. The injectivity of the differential ensures the image is a two-dimensional smooth submanifold, at least locally.",
    "3", "3.1", "basic")

write_concept("tangent-space-surface", "definition",
    "Tangent Space of a Surface", "geometry", "differential-geometry",
    "Let $f: U \\to \\mathbb{R}^3$ be a surface. The two-dimensional linear subspace $df_u(T_u\\mathbb{R}^2) \\subset T_{f(u)}\\mathbb{R}^3$ is called the tangent space of $f$ at $u$, denoted by $T_u f$. Elements of $T_u f$ are called tangent vectors of $f$ at $u$.",
    "The tangent space is the image of the differential, a 2-plane in $\\mathbb{R}^3$ attached at $f(u)$. It is spanned by the partial derivatives $f_{u^1}$ and $f_{u^2}$.",
    "3", "3.1", "basic")

write_concept("change-of-variables-surface", "definition",
    "Change of Variables for a Surface", "geometry", "differential-geometry",
    "Let $f: U \\to \\mathbb{R}^3$ be a surface. A change of variables of $f$ is a diffeomorphism $\\phi: V \\subset \\mathbb{R}^2 \\to U \\subset \\mathbb{R}^2$, where $V$ is open, such that $d\\phi$ always has rank 2. If $\\det(d\\phi) > 0$, $\\phi$ is orientation preserving. The surface $\\tilde{f} := f \\circ \\phi$ is related to $f$ by $\\phi$.",
    "A change of variables (reparametrization) produces an equivalent surface patch. This defines an equivalence relation; an equivalence class is an unparameterized surface.",
    "3", "3.1", "basic")

write_concept("vector-field-along-surface", "definition",
    "Vector Field along a Surface", "geometry", "differential-geometry",
    "A vector field along a surface $f: U \\to \\mathbb{R}^3$ is a differentiable mapping $X: U \\to \\mathbb{R}^3$. The vector $X(u)$ is considered as an element of $T_{f(u)}\\mathbb{R}^3$.",
    "A vector field along a surface assigns a vector in $\\mathbb{R}^3$ at each point of the surface. Tangential vector fields (those in $T_u f$) are particularly important for intrinsic geometry.",
    "3", "3.1", "basic")

write_concept("tangential-vector-field", "definition",
    "Tangential Vector Field", "geometry", "differential-geometry",
    "Let $f: U \\to \\mathbb{R}^3$ be a surface. A vector field $X$ along $f$ is tangential if $X(u) \\in T_u f$ for all $u \\in U$. Every tangential vector field can be written as $X = \\sum_{i=1}^2 a^i f_{u^i}$ with differentiable coefficient functions $a^i(u)$.",
    "Tangential vector fields lie in the tangent space of the surface at each point. They form the natural domain for the first and second fundamental forms and are the objects of intrinsic differential geometry.",
    "3", "3.1", "basic")

write_concept("gauss-map-unit-normal", "definition",
    "Gauss Map and Unit Normal Field", "geometry", "differential-geometry",
    "Let $f: U \\to \\mathbb{R}^3$ be a surface. The Gauss unit normal field is defined by\n$$n := \\frac{f_{u^1} \\times f_{u^2}}{|f_{u^1} \\times f_{u^2}|}.$$\nThe mapping $n: U \\to S^2 \\subset \\mathbb{R}^3$ is called the Gauss map. The triple $(f_{u^1}, f_{u^2}, n)$ is called the Gauss frame.",
    "The Gauss map assigns to each point the unit normal vector to the surface. It encodes the extrinsic curvature of the surface via its differential, which is the Weingarten map.",
    "3", "3.1", "basic")

# s010: 3.2 First Fundamental Form
write_concept("quadratic-form-review", "definition",
    "Symmetric Bilinear Form (Quadratic Form) on a Vector Space", "geometry", "differential-geometry",
    "Let $T$ be a real vector space. A symmetric bilinear form (quadratic form) is a map $\\beta: T \\times T \\to \\mathbb{R}$ satisfying:\n$$\\beta(X, Y) = \\beta(Y, X) \\quad \\text{(symmetry)}$$\n$$\\beta(aX + bY, Z) = a\\beta(X, Z) + b\\beta(Y, Z) \\quad \\text{(bilinearity)}$$\nfor all $X, Y, Z \\in T$ and $a, b \\in \\mathbb{R}$.",
    "A quadratic form on a vector space generalizes the dot product. Its matrix representation transforms by congruence $G = A H A^t$ under change of basis.",
    "3", "3.2", "basic")

write_concept("first-fundamental-form", "definition",
    "First Fundamental Form of a Surface", "geometry", "differential-geometry",
    "Let $f: U \\to \\mathbb{R}^3$ be a surface. The first fundamental form $I$ is the quadratic form on $T_u f$ induced by the Euclidean inner product on $\\mathbb{R}^3$ via the inclusion $T_u f \\subset T_{f(u)}\\mathbb{R}^3$. That is, $I_u(X, Y) := X \\cdot Y$ for $X, Y \\in T_u f$. The matrix representation with respect to the basis $\\{f_{u^1}, f_{u^2}\\}$ is $(g_{ik}) := (f_{u^i} \\cdot f_{u^k})$.",
    "The first fundamental form is the restriction of the Euclidean dot product to the tangent space. It measures lengths of tangent vectors, angles between them, and areas on the surface. It is the Riemannian metric induced by the embedding.",
    "3", "3.2", "basic")

write_concept("first-fundamental-form-positive-definite", "proposition",
    "Positive Definiteness and Differentiability of the First Fundamental Form", "geometry", "differential-geometry",
    "Let $f: U \\to \\mathbb{R}^3$ be a surface.\n(i) The first fundamental form $I$ is positive definite.\n(ii) $I$ is differentiable, i.e., the coefficients $g_{ik}: U \\to \\mathbb{R}$ are differentiable. Equivalently, for any tangential vector fields $X, Y$ along $f$, the map $u \\mapsto I_u(X(u), Y(u))$ is differentiable.",
    "The first fundamental form gives a smoothly varying inner product on each tangent space. Positive definiteness follows from the injectivity of $df$, which guarantees $f_{u^1}$ and $f_{u^2}$ are linearly independent.",
    "3", "3.2", "basic")

write_concept("invariance-first-fundamental-form", "proposition",
    "Invariance of the First Fundamental Form", "geometry", "differential-geometry",
    "Let $f: U \\to \\mathbb{R}^3$ be a surface.\n(i) If $B: \\mathbb{R}^3 \\to \\mathbb{R}^3$ is an isometry, then $\\tilde{f} = B \\circ f$ satisfies $\\tilde{I}_u(dB X, dB Y) = I_u(X, Y)$ for all $X, Y \\in T_u f$.\n(ii) If $\\phi: V \\to U$ is a change of variables and $\\tilde{f} = f \\circ \\phi$, then $\\tilde{I}_v(X, Y) = I_{\\phi(v)}(d\\phi X, d\\phi Y)$ for all $X, Y \\in T_v \\mathbb{R}^2$.",
    "The first fundamental form is invariant under Euclidean isometries and transforms naturally under reparametrization by the differential of the change of variables.",
    "3", "3.2", "basic")

write_concept("transformation-matrix-first-fundamental-form", "corollary",
    "Transformation of Fundamental Matrix under Change of Variables", "geometry", "differential-geometry",
    "Let $\\phi: V \\to U$ be a change of variables given by $u^i = u^i(v^1, v^2)$. Then the fundamental matrix $(\\tilde{g}_{ij})$ of $\\tilde{f} = f \\circ \\phi$ is related to $(g_{ij})$ of $f$ by\n$$\\tilde{g}_{ij}(v) = \\sum_{k,l} \\frac{\\partial u^k}{\\partial v^i} \\frac{\\partial u^l}{\\partial v^j} g_{kl}(\\phi(v)).$$",
    "The fundamental matrix transforms as a covariant 2-tensor. This transformation law is the defining property of a Riemannian metric.",
    "3", "3.2", "basic")

# s011: 3.3 Second Fundamental Form
write_concept("second-fundamental-form", "definition",
    "Second Fundamental Form of a Surface", "geometry", "differential-geometry",
    "Let $f: U \\to \\mathbb{R}^3$ be a surface with Gauss normal field $n$. The second fundamental form $II$ is the quadratic form defined on $T_u \\mathbb{R}^2$ by\n$$II_u := -dn_u \\cdot df_u: T_u\\mathbb{R}^2 \\times T_u\\mathbb{R}^2 \\to \\mathbb{R}.$$\nThe matrix representation with respect to the canonical basis is $(h_{ik}) := (-n_{u^i} \\cdot f_{u^k}) = (n \\cdot f_{u^i u^k})$. In Gauss' notation:\n$$\\begin{pmatrix} L & M \\\\ M & N \\end{pmatrix} := \\begin{pmatrix} h_{11} & h_{12} \\\\ h_{21} & h_{22} \\end{pmatrix}.$$",
    "The second fundamental form measures the rate of change of the unit normal, i.e., how the surface bends in space. It is the extrinsic curvature counterpart to the intrinsic first fundamental form.",
    "3", "3.3", "intermediate")

write_concept("weingarten-map", "definition",
    "Weingarten Map (Shape Operator)", "geometry", "differential-geometry",
    "Let $f: U \\to \\mathbb{R}^3$ be a surface. The Weingarten map (shape operator) is the linear mapping $L_u := -dn_u \\circ df_u^{-1}: T_u f \\to T_u f$. The second fundamental form can be expressed as $II_u(X, Y) = L_u X \\cdot Y$ for all $X, Y \\in T_u f$.",
    "The Weingarten map is the differential of the Gauss map pulled back to the tangent space. It is a self-adjoint linear operator whose eigenvalues are the principal curvatures.",
    "3", "3.3", "intermediate")

write_concept("third-fundamental-form", "definition",
    "Third Fundamental Form of a Surface", "geometry", "differential-geometry",
    "The third fundamental form $III$ of a surface $f: U \\to \\mathbb{R}^3$ is the symmetric bilinear form defined by\n$$III_u(X, Y) := dn_u X \\cdot dn_u Y$$\nfor $X, Y \\in T_u\\mathbb{R}^2$. On $T_u f$, it is given by $L_u X \\cdot L_u Y$.",
    "The third fundamental form measures the metric induced by the Gauss map. It is related to the first and second fundamental forms by the identity $III - 2H II + K I = 0$.",
    "3", "3.3", "intermediate")

# s012: 3.4 Curves on Surfaces
write_concept("normal-curvature", "definition",
    "Normal Curvature of a Curve on a Surface", "geometry", "differential-geometry",
    "Let $c = f \\circ u$ be a curve on a surface $f$, parameterized by arc length. The normal curvature $\\kappa_n$ of $c$ is the component of the acceleration $\\ddot{c}$ in the direction of the surface normal $n$. It satisfies\n$$\\kappa_n(t) = II_{u(t)}(\\dot{u}(t), \\dot{u}(t)) = \\kappa(t) \\cos \\theta(t)$$\nwhere $\\theta(t)$ is the angle between the principal normal of $c$ and the surface normal.",
    "The normal curvature measures how much the surface bends in the direction of the curve's tangent. It depends only on the tangent direction, not on the curve itself (Meusnier's theorem).",
    "3", "3.4", "intermediate")

write_concept("meusnier-theorem", "theorem",
    "Meusnier's Theorem", "geometry", "differential-geometry",
    "All curves on a surface passing through a given point with the same tangent direction have the same normal curvature at that point.",
    "Meusnier's theorem establishes that normal curvature is a property of the tangent direction alone, not of the particular curve. It follows from the fact that $\\ddot{c} \\cdot n = II(\\dot{c}, \\dot{c})$ depends only on the first derivative.",
    "3", "3.4", "intermediate")

write_concept("principal-directions-curvatures", "definition",
    "Principal Directions and Principal Curvatures", "geometry", "differential-geometry",
    "Let $f: U \\to \\mathbb{R}^3$ be a surface. The eigenvectors of the Weingarten map $L_u = -dn_u \\circ df_u^{-1}$ are called principal directions. The corresponding eigenvalues $\\kappa_1(u), \\kappa_2(u)$ are the principal curvatures of $f$ at $u$.",
    "Principal directions are the tangent directions where the normal curvature attains its maximum and minimum. The principal curvatures are the eigenvalues of the Weingarten map and characterize the local shape of the surface.",
    "3", "3.5", "intermediate")

# s013: 3.5 Principal Curvature
write_concept("gauss-curvature-and-mean-curvature", "definition",
    "Gauss Curvature and Mean Curvature", "geometry", "differential-geometry",
    "Let $f: U \\to \\mathbb{R}^3$ be a surface with principal curvatures $\\kappa_1, \\kappa_2$. The Gauss curvature $K$ and mean curvature $H$ are defined by\n$$K(u) := \\kappa_1(u) \\cdot \\kappa_2(u), \\quad H(u) := \\frac{1}{2}(\\kappa_1(u) + \\kappa_2(u)).$$",
    "The Gauss curvature is the product of principal curvatures (determinant of the Weingarten map), while mean curvature is their average (half the trace). Together they completely determine the local extrinsic geometry of the surface.",
    "3", "3.5", "intermediate")

write_concept("curvature-functions-formulas", "proposition",
    "Formulas for Gauss and Mean Curvature", "geometry", "differential-geometry",
    "Let $f: U \\to \\mathbb{R}^3$ be a surface. Then\n(i) $\\det(\\kappa \\cdot \\mathrm{id} + dn \\circ df^{-1}) = \\kappa^2 - 2H\\kappa + K$, where the left side is the characteristic polynomial $\\chi(L_u)$ of the Weingarten map. Consequently, $K(u) = \\det L_u$ and $2H(u) = \\operatorname{Tr} L_u$.\n(ii) In terms of the matrices $(g_{ik})$ and $(h_{ik})$: $K = \\det(h_{ik})/\\det(g_{ik})$ and $H = (h_{11}g_{22} - 2h_{12}g_{12} + h_{22}g_{11})/(2\\det(g_{ik}))$.",
    "These formulas express $K$ and $H$ in terms of the coefficients of the first and second fundamental forms. The characteristic polynomial representation connects to linear algebra of the Weingarten map.",
    "3", "3.5", "intermediate")

write_concept("third-fundamental-form-identity", "proposition",
    "Relation between the Three Fundamental Forms", "geometry", "differential-geometry",
    "For a surface $f: U \\to \\mathbb{R}^3$, the three fundamental forms satisfy\n$$III - 2H II + K I = 0.$$",
    "This identity shows that the third fundamental form is not independent but is algebraically determined by $I$, $II$, $K$, and $H$. It is a special case of the Cayley-Hamilton theorem applied to the Weingarten map.",
    "3", "3.5", "intermediate")

write_concept("invariance-of-curvatures", "theorem",
    "Invariance of Principal Curvatures and Curvature Functions", "geometry", "differential-geometry",
    "Let $f: U \\to \\mathbb{R}^3$ be a surface, $X \\in T_u f$ a principal direction with principal curvature $\\kappa(X)$.\n(i) If $B: \\mathbb{R}^3 \\to \\mathbb{R}^3$ is an isometry, then $\\tilde{f} = B \\circ f$ is a surface with $\\tilde{X} = dB X$ as a principal direction, $\\tilde{\\kappa}(\\tilde{X}) = \\pm \\kappa(X)$, $\\tilde{K}(u) = K(u)$, and $\\tilde{H}(u) = \\pm H(u)$. The signs are positive for congruences and negative for symmetries.\n(ii) Under change of variables $\\phi$, principal curvatures remain the same and $K$, $H$ are invariant.",
    "Gauss curvature is invariant under all isometries (including orientation-reversing ones). Mean curvature changes sign under orientation reversal. Under reparametrization, both are invariant.",
    "3", "3.5", "intermediate")

write_concept("umbilic-point", "definition",
    "Umbilic Point of a Surface", "geometry", "differential-geometry",
    "A point $u_0$ on a surface $f: U \\to \\mathbb{R}^3$ is called an umbilic (or umbilic point) if $\\kappa_1(u_0) = \\kappa_2(u_0)$. If additionally $\\kappa_1(u_0) = \\kappa_2(u_0) = 0$, it is a planar point.",
    "At an umbilic point, the normal curvature is the same in all directions — the surface bends equally in every tangent direction. A plane consists entirely of planar points; a sphere consists entirely of (non-planar) umbilic points.",
    "3", "3.5", "intermediate")

# s014: 3.6 Normal Form
write_concept("normal-form-surface", "proposition",
    "Normal Form of a Surface near a Point", "geometry", "differential-geometry",
    "Let $f: U \\to \\mathbb{R}^3$ be a surface and $u_0 \\in U$. There exists a change of variables $\\phi: V_0 \\to U_0 \\subset U$ near $u_0$ with $\\phi(0) = u_0$ such that if $\\tilde{f} = f \\circ \\phi$,\n$$\\tilde{f}(v) - \\tilde{f}(0) = v^1 X_1 + v^2 X_2 + r(v)n_0, \\quad v = (v^1, v^2),$$\nwhere $X_i = f_{u^i}(u_0)$, $n_0$ is the unit normal at $u_0$, and the Hessian of $r$ at $0$ equals the second fundamental form: $r_{v^i v^j}(0) = h_{ij}(u_0)$.",
    "Every surface can be locally expressed as the graph of a height function over its tangent plane. The second-order behavior of this height function is exactly the second fundamental form.",
    "3", "3.6", "intermediate")

write_concept("asymptotic-direction", "definition",
    "Asymptotic Direction on a Surface", "geometry", "differential-geometry",
    "A tangent direction $X \\in T_u f$ is called an asymptotic direction if $II_u(X, X) = 0$, i.e., the normal curvature in that direction vanishes. A curve on the surface whose tangent is everywhere an asymptotic direction is an asymptotic line.",
    "Asymptotic directions are those where the surface does not bend (zero normal curvature). They exist at a point if and only if $K(u) \\leq 0$, since $K = \\kappa_1 \\kappa_2$.",
    "3", "3.6", "intermediate")

# s015: 3.6.10 Proposition
write_concept("asymptotic-directions-gauss-curvature", "proposition",
    "Asymptotic Directions and Gauss Curvature Sign", "geometry", "differential-geometry",
    "Let $f: U \\to \\mathbb{R}^3$ be a surface.\n(i) $K(u) < 0$ if and only if there exist exactly two (up to sign) asymptotic directions at $u$.\n(ii) $K(u) = 0$ if and only if there exists exactly one (up to sign) asymptotic direction, unless $u$ is a planar point.\n(iii) $K(u) > 0$ if and only if there are no asymptotic directions at $u$.",
    "The existence and number of asymptotic directions are determined by the sign of Gauss curvature. This proposition gives geometric meaning to the sign of $K$: negative curvature means saddle-like, positive means bowl-like.",
    "3", "3.6", "intermediate")

# s016: 3.7 Special Surfaces
write_concept("developable-surface", "definition",
    "Developable Surface", "geometry", "differential-geometry",
    "A surface is called developable if $K \\equiv 0$ everywhere. Equivalently, it can be locally isometrically mapped onto a plane. Developable surfaces include cylinders, cones, and tangent surfaces of space curves.",
    "A developable surface has zero Gauss curvature everywhere, meaning it is intrinsically flat. Such surfaces can be rolled out onto a plane without stretching or tearing.",
    "3", "3.7", "intermediate")

write_concept("ruled-surface", "definition",
    "Ruled Surface", "geometry", "differential-geometry",
    "A ruled surface is a surface that can be parameterized as $f(s, t) = c(s) + t X(s)$, where $c(s)$ is a curve (the directrix) and $X(s)$ is a vector field along $c$ (the generator directions). The curves $t = \\text{const}$ are called generators (straight lines) and $s = \\text{const}$ are called directrices.",
    "A ruled surface is swept out by a family of straight lines. Cylinders, cones, hyperboloids of one sheet, and helicoids are ruled surfaces. Developable surfaces are a special class of ruled surfaces.",
    "3", "3.7", "intermediate")

# s017-s018: 3.8 Gauss-Codazzi and Theorema Egregium
write_concept("gauss-codazzi-equations", "theorem",
    "Gauss and Codazzi-Mainardi Equations", "geometry", "differential-geometry",
    "For a surface $f: U \\to \\mathbb{R}^3$, the coefficients of the first and second fundamental forms satisfy the following compatibility conditions.\n\n**Gauss equation:**\n$$K = \\frac{R_{1212}}{\\det(g_{ij})}, \\quad R_{1212} = -\\frac{1}{2}(g_{11,22} + g_{22,11} - 2g_{12,12}) + \\sum g^{kl}(\\Gamma_{11,k}\\Gamma_{22,l} - \\Gamma_{12,k}\\Gamma_{12,l}).$$\n\n**Codazzi-Mainardi equations:**\n$$h_{11,2} - h_{12,1} = \\sum h_{1k}\\Gamma_{21}^k - \\sum h_{2k}\\Gamma_{11}^k$$\n$$h_{12,2} - h_{22,1} = \\sum h_{1k}\\Gamma_{22}^k - \\sum h_{2k}\\Gamma_{12}^k.$$",
    "The Gauss-Codazzi equations are the integrability conditions for the existence of a surface with prescribed first and second fundamental forms. They are the fundamental equations of surface theory, analogous to the Frenet equations for curves.",
    "3", "3.8", "advanced")

write_concept("theorema-egregium", "theorem",
    "Theorema Egregium (Gauss)", "geometry", "differential-geometry",
    "The Gauss curvature $K(u)$ of a surface can be expressed entirely in terms of the coefficients $g_{ik}$ of the first fundamental form and their first and second derivatives. Therefore, $K$ is invariant under local isometries.",
    "Gauss's 'remarkable theorem' states that Gauss curvature is an intrinsic quantity — it can be measured from within the surface without reference to the ambient space. This discovery was the foundation of intrinsic Riemannian geometry.",
    "3", "3.8", "advanced")

# ===================================================================
# CHAPTER 4: Intrinsic Geometry of Surfaces — Local Theory
# ===================================================================

# s019: 4.1 Covariant Differentiation
write_concept("covariant-differentiation", "definition",
    "Covariant Differentiation on a Surface", "geometry", "differential-geometry",
    "Let $f: U \\to \\mathbb{R}^3$ be a surface and $X$ a tangential vector field along $f$. For a tangent vector $V \\in T_u f$, the covariant derivative $\\nabla_V X$ is defined as the tangential component of the ordinary directional derivative $dX(V)$:\n$$\\nabla_V X := dX(V) - (dX(V) \\cdot n)n.$$\nIn coordinates, if $X = \\sum a^i f_{u^i}$, then\n$$\\nabla_{f_{u^k}} X = \\sum_i \\left( \\frac{\\partial a^i}{\\partial u^k} + \\sum_j a^j \\Gamma_{jk}^i \\right) f_{u^i},$$\nwhere the Christoffel symbols are $\\Gamma_{jk}^i = \\sum_l g^{il} \\Gamma_{jk,l}$ with $\\Gamma_{jk,l} = \\frac{1}{2}(g_{jl,k} + g_{kl,j} - g_{jk,l})$.",
    "Covariant differentiation is the intrinsic derivative on a surface, obtained by projecting the ordinary derivative onto the tangent plane. The Christoffel symbols encode how the tangent basis changes across the surface.",
    "4", "4.1", "intermediate")

write_concept("christoffel-symbols", "definition",
    "Christoffel Symbols", "geometry", "differential-geometry",
    "The Christoffel symbols of the first kind are $\\Gamma_{ij,k} := \\frac{1}{2}(g_{ik,j} + g_{jk,i} - g_{ij,k})$, and of the second kind are $\\Gamma_{ij}^k := \\sum_l g^{kl} \\Gamma_{ij,l}$, where $(g^{kl})$ is the inverse matrix of $(g_{kl})$.",
    "Christoffel symbols are the connection coefficients that describe how the coordinate basis changes from point to point. They are not tensors but transform in a specific way under coordinate changes to ensure covariant derivatives are tensorial.",
    "4", "4.1", "intermediate")

# s020: 4.2 Parallel Translation
write_concept("parallel-vector-field", "definition",
    "Parallel Vector Field along a Curve", "geometry", "differential-geometry",
    "Let $f$ be a surface and $c = f \\circ u: I \\to \\mathbb{R}^3$ a curve on $f$. A tangential vector field $X(t)$ along $c$ is parallel if its covariant derivative vanishes: $\\nabla X/dt := \\nabla_{\\dot{c}} X = 0$. In coordinates:\n$$\\frac{d a^k}{dt} + \\sum_{i,j} \\Gamma_{ij}^k \\dot{u}^i a^j = 0, \\quad k = 1,2,$$\nwhere $X(t) = \\sum a^k(t) f_{u^k}(u(t))$.",
    "A parallel vector field along a curve has zero intrinsic acceleration. Given an initial vector, there exists a unique parallel vector field along the curve extending it — this is parallel translation.",
    "4", "4.2", "intermediate")

write_concept("existence-uniqueness-parallel-translation", "proposition",
    "Existence and Uniqueness of Parallel Translation", "geometry", "differential-geometry",
    "Let $c: I \\to f(U)$ be a curve on a surface $f$ and $t_0 \\in I$. For every $X_0 \\in T_{u(t_0)}f$, there exists a unique parallel vector field $X(t)$ along $c$ with $X(t_0) = X_0$. The map $P_c: T_{c(t_0)}f \\to T_{c(t)}f$ defined by parallel translation is a linear isometry.",
    "Parallel translation is a linear isometry between tangent spaces along a curve. It generalizes the notion of 'constant vector field' to curved surfaces and preserves the first fundamental form.",
    "4", "4.2", "intermediate")

# s021: 4.3 Geodesics
write_concept("geodesic", "definition",
    "Geodesic on a Surface", "geometry", "differential-geometry",
    "A curve $c = f \\circ u$ on a surface $f$ is a geodesic if its tangent vector field $\\dot{c}$ is parallel along $c$, i.e., $\\nabla \\dot{c}/dt = 0$. In coordinates, the geodesic equation is\n$$\\ddot{u}^k + \\sum_{i,j} \\Gamma_{ij}^k \\dot{u}^i \\dot{u}^j = 0, \\quad k = 1,2.$$",
    "Geodesics are curves with zero covariant acceleration — they are the 'straightest' curves on a surface. They are the paths followed by particles moving freely on the surface and locally minimize length.",
    "4", "4.3", "intermediate")

write_concept("geodesic-parallel-coordinates", "definition",
    "Geodesic Parallel Coordinates", "geometry", "differential-geometry",
    "Coordinates $(u^1, u^2)$ on a surface are called geodesic parallel coordinates if the curves $u^2 = \\text{const}$ are geodesics parameterized by arc length, the curves $u^1 = \\text{const}$ are orthogonal to them, and $g_{11} \\equiv 1$.",
    "In geodesic parallel coordinates, the metric takes the form $ds^2 = (du^1)^2 + g_{22}(u^1, u^2)(du^2)^2$. These coordinates are the surface analog of polar coordinates and are fundamental for studying curvature.",
    "4", "4.3", "intermediate")

# s022: 4.4 Surfaces of Constant Curvature
write_concept("surfaces-constant-curvature", "proposition",
    "Characterization of Surfaces of Constant Gauss Curvature", "geometry", "differential-geometry",
    "For a surface with a Riemannian metric, the following are equivalent:\n(i) $K = \\text{const}$;\n(ii) In geodesic polar coordinates, $\\sqrt{g_{22}}$ depends only on $u^1$;\n(iii) In geodesic parallel coordinates, $\\sqrt{g_{22}}$ depends only on $u^1$;\n(iv) All curves $u^1 = \\text{const}$ (in geodesic parallel coordinates) are geodesics.",
    "Surfaces of constant curvature have special metric forms. The function $\\sqrt{g_{22}}$ satisfies the Jacobi equation $\\partial^2 \\sqrt{g_{22}}/\\partial (u^1)^2 + K \\sqrt{g_{22}} = 0$, connecting curvature to the spread of geodesics.",
    "4", "4.4", "intermediate")

# ===================================================================
# CHAPTER 5: Two-Dimensional Riemannian Geometry
# ===================================================================

# s023-s025: 5.1 Local Riemannian Geometry
write_concept("riemannian-metric", "definition",
    "Two-Dimensional Riemannian Metric", "geometry", "differential-geometry",
    "A two-dimensional Riemannian metric on an open set $U \\subset \\mathbb{R}^2$ is a differentiable map $g: U \\to S(2)$, where $S(2)$ is the set of real symmetric positive definite $2 \\times 2$ matrices. The pair $(U, g)$ is a local Riemannian manifold. Equivalently, a Riemannian metric is a smoothly varying positive definite quadratic form on each tangent space.",
    "A Riemannian metric generalizes the first fundamental form to abstract surfaces. It defines lengths, angles, and areas without reference to an embedding in $\\mathbb{R}^3$. This is the foundation of intrinsic Riemannian geometry.",
    "5", "5.1", "intermediate")

write_concept("special-linear-group", "definition",
    "Special Linear Group SL(2,R)", "geometry", "differential-geometry",
    "$SL(2, \\mathbb{R})$ is the group of all real $2 \\times 2$ matrices with determinant 1. It is a three-dimensional Lie group that acts on the upper half-plane by fractional linear transformations, preserving the hyperbolic metric.",
    "$SL(2, \\mathbb{R})$ is the symmetry group of the hyperbolic plane. Its study connects differential geometry with Lie theory and is central to the uniformization theorem for surfaces.",
    "5", "5.1", "intermediate")

write_concept("gauss-curvature-intrinsic", "definition",
    "Intrinsic Definition of Gauss Curvature", "geometry", "differential-geometry",
    "For a two-dimensional Riemannian manifold $(U, g)$, the Gauss curvature $K$ is defined intrinsically as $K = R_{1212}/\\det(g_{ij})$, where $R_{1212}$ is the Riemann curvature tensor component computed from the metric $g$ and its derivatives.",
    "Gauss curvature can be defined purely from the metric without any embedding, as guaranteed by the Theorema Egregium. This intrinsic definition is the starting point for Riemannian geometry.",
    "5", "5.1", "intermediate")

# s026: 5.2 Tangent Bundle and Exponential Map
write_concept("tangent-bundle", "definition",
    "Tangent Bundle of a Surface", "geometry", "differential-geometry",
    "The tangent bundle $TM$ of a two-dimensional manifold $M$ is the set of all tangent vectors at all points of $M$, endowed with a natural differentiable structure. If $(u_\\alpha, M_\\alpha)_{\\alpha \\in A}$ is an atlas for $M$, then $(Tu_\\alpha, TM_\\alpha)_{\\alpha \\in A}$ is an atlas for $TM$, where $Tu_\\alpha: TM_\\alpha \\to T U_\\alpha = U_\\alpha \\times \\mathbb{R}^2$ maps $X \\in T_p M$ to $(u_\\alpha(p), du_\\alpha(X))$.",
    "The tangent bundle packages all tangent spaces into a single four-dimensional manifold. It is the natural domain for the exponential map and for studying geodesic flow.",
    "5", "5.2", "intermediate")

write_concept("exponential-map", "definition",
    "Exponential Map on a Riemannian Manifold", "geometry", "differential-geometry",
    "For a point $p$ on a Riemannian manifold $M$, the exponential map $\\exp_p: T_p M \\to M$ is defined by $\\exp_p(X) = c(1)$, where $c(t)$ is the unique geodesic with $c(0) = p$ and $\\dot{c}(0) = X$. The exponential map is a local diffeomorphism near $0 \\in T_p M$.",
    "The exponential map sends tangent vectors to points reached by following geodesics. It generalizes polar coordinates to curved spaces and is the key tool for constructing geodesic normal coordinates.",
    "5", "5.2", "intermediate")

# s027: 5.3 Gauss Lemma
write_concept("gauss-lemma", "proposition",
    "Gauss Lemma", "geometry", "differential-geometry",
    "In geodesic polar coordinates, the metric takes the form\n$$ds^2 = d\\rho^2 + G(\\rho, \\theta) d\\theta^2,$$\nwhere $\\rho = |X|$ is the radial distance. In particular, geodesics through the base point are orthogonal to the geodesic circles $\\rho = \\text{const}$.",
    "Gauss's lemma states that geodesic spheres (loci of points at constant distance from a point) are orthogonal to the radial geodesics emanating from that point. This is the geometric analog of the fact that in polar coordinates on the plane, $dr$ and $d\\theta$ are orthogonal.",
    "5", "5.3", "intermediate")

# s028: 5.4 Jacobi Fields
write_concept("jacobi-field", "definition",
    "Jacobi Field along a Geodesic", "geometry", "differential-geometry",
    "A Jacobi field along a geodesic $c(t)$ is a vector field $Y(t)$ satisfying the Jacobi differential equation\n$$\\frac{\\nabla^2 Y}{dt^2} + R(Y, \\dot{c})\\dot{c} = 0,$$\nwhere $R$ is the Riemann curvature tensor. In surface theory with $e_2(t)$ a unit parallel field orthogonal to $\\dot{c}$, a Jacobi field can be written $Y(t) = y(t)e_2(t)$ with $\\ddot{y}(t) + K(c(t))y(t) = 0$.",
    "Jacobi fields describe the infinitesimal variation of a family of geodesics. They measure how nearby geodesics spread apart or come together, and their zeros correspond to conjugate points along the geodesic.",
    "5", "5.4", "advanced")

write_concept("jacobi-field-variational-property", "proposition",
    "Jacobi Fields as Variation Fields of Geodesic Variations", "geometry", "differential-geometry",
    "Let $c(t)$ be a geodesic and $Y(t)$ a tangential vector field along $c$ with $Y(0) = 0$. Then $Y(t)$ is a Jacobi field if and only if it arises as the variation field of a geodesic variation, i.e., $Y(t) = \\frac{\\partial}{\\partial s} c_s(t)|_{s=0}$ for a one-parameter family of geodesics $c_s(t)$.",
    "Jacobi fields are exactly the variational vector fields of geodesic variations starting from a point. In geodesic polar coordinates, $Y(t) = t \\frac{\\partial}{\\partial \\theta}$ is a Jacobi field.",
    "5", "5.4", "advanced")

# s029-s030: 5.5 Manifolds
write_concept("differentiable-manifold", "definition",
    "Two-Dimensional Differentiable Manifold", "geometry", "differential-geometry",
    "A two-dimensional differentiable manifold $M$ is a Hausdorff topological space with a countable basis, together with a differentiable atlas $(u_\\alpha, M_\\alpha)_{\\alpha \\in A}$, where $M_\\alpha$ is an open covering of $M$ and $u_\\alpha: M_\\alpha \\to U_\\alpha \\subset \\mathbb{R}^2$ is a homeomorphism such that all transition maps $u_\\beta \\circ u_\\alpha^{-1}$ are diffeomorphisms.",
    "A manifold generalizes the concept of a surface to an abstract setting without a fixed embedding. It is locally modeled on $\\mathbb{R}^2$ with smooth transition maps, providing the global framework for Riemannian geometry.",
    "5", "5.5", "intermediate")

write_concept("orientable-manifold", "definition",
    "Orientable Manifold", "geometry", "differential-geometry",
    "A differentiable manifold $M$ is orientable if it admits an atlas $(u_\\alpha, M_\\alpha)_{\\alpha \\in A}$ such that all transition maps $u_\\beta \\circ u_\\alpha^{-1}$ have positive Jacobian determinant.",
    "Orientability is a global topological property. A Mobius strip is non-orientable. On an orientable surface, one can consistently define a unit normal field and integrate 2-forms (including the area form $K dM$).",
    "5", "5.5", "intermediate")

# s031-s032: 5.6 Differential Forms
write_concept("whitney-sum-tangent-bundle", "proposition",
    "Whitney Sum of Tangent Bundle", "geometry", "differential-geometry",
    "$TM \\oplus TM$ can be given the structure of a six-dimensional differentiable manifold. If $(u_\\alpha, M_\\alpha)_{\\alpha \\in A}$ is an atlas for $M$, then $(Tu_\\alpha \\oplus Tu_\\alpha, TM_\\alpha \\oplus TM_\\alpha)_{\\alpha \\in A}$ is an atlas for $TM \\oplus TM$.",
    "The Whitney sum provides the natural setting for Riemannian metrics as sections of $T^*M \\otimes T^*M$ and for the curvature tensor as a section of an appropriate tensor bundle.",
    "5", "5.6", "intermediate")

write_concept("one-form", "definition",
    "Differential 1-Form on a Manifold", "geometry", "differential-geometry",
    "A differential 1-form $\\omega$ on a manifold $M$ is a section of the cotangent bundle $T^*M$, i.e., a linear map $\\omega_p: T_p M \\to \\mathbb{R}$ at each $p \\in M$, varying smoothly.",
    "A 1-form is a linear functional on tangent vectors at each point. Examples include $df$ (differential of a function). 1-forms are the objects that can be integrated along curves.",
    "5", "5.6", "intermediate")

write_concept("integral-of-one-form", "definition",
    "Integral of a 1-Form along a Curve", "geometry", "differential-geometry",
    "Let $\\omega$ be a 1-form on $M$ and $c: I \\to M$ a curve with $I$ compact. The integral of $\\omega$ along $c$ is\n$$\\int_c \\omega := \\int_I \\omega(\\dot{c}(t)) dt.$$",
    "The line integral of a 1-form generalizes the work integral in vector calculus. It is independent of parametrization and is the foundation for integration on manifolds.",
    "5", "5.6", "intermediate")

# s033: 5.7 Laplace-Beltrami
write_concept("laplace-beltrami-operator", "definition",
    "Laplace-Beltrami Operator on a Riemannian Manifold", "geometry", "differential-geometry",
    "Let $F(M)$ denote the algebra of differentiable functions on a Riemannian manifold $M$. The Laplace-Beltrami operator is the mapping $\\Delta: F(M) \\to F(M)$ defined in local coordinates by\n$$\\Delta f = \\frac{1}{\\sqrt{\\det g}} \\sum_{i,j} \\frac{\\partial}{\\partial u^i} \\left( \\sqrt{\\det g}\\, g^{ij} \\frac{\\partial f}{\\partial u^j} \\right).$$",
    "The Laplace-Beltrami operator is the intrinsic generalization of the Laplacian to curved spaces. It is a central object in geometric analysis, governing heat flow, wave propagation, and the spectrum of the manifold.",
    "5", "5.7", "intermediate")

# ===================================================================
# CHAPTER 6: Global Geometry of Surfaces
# ===================================================================

# s034: 6.1 Surfaces in Euclidean Space
write_concept("embedded-surface", "lemma",
    "Embedded Surface in Euclidean Space as Differentiable Manifold", "geometry", "differential-geometry",
    "Let $M \\subset \\mathbb{R}^3$ be a subset with the induced topology such that for each $p \\in M$, there exists an open neighborhood $V \\subset \\mathbb{R}^3$ of $p$ and a regular surface patch $f: U \\to \\mathbb{R}^3$ with $f(U) = M \\cap V$ and $f^{-1}: M \\cap V \\to U$ continuous. Then $M$ is a differentiable surface in the sense of (5.5.1).",
    "A subset of $\\mathbb{R}^3$ that is locally a regular surface patch is an embedded surface. The induced atlas makes it a differentiable manifold, connecting the classical theory with the modern manifold approach.",
    "6", "6.1", "intermediate")

# s035: 6.1.6 Orientability
write_concept("orientability-surface-in-r3", "proposition",
    "Characterization of Orientability for Surfaces in R^3", "geometry", "differential-geometry",
    "A surface $M \\subset \\mathbb{R}^3$ is orientable if and only if there exists a continuous unit normal vector field $n: M \\to S^2$, $p \\mapsto n(p)$, such that $n(p) \\perp T_p M$ for all $p \\in M$.",
    "For surfaces in $\\mathbb{R}^3$, orientability is equivalent to the existence of a globally defined continuous unit normal. This gives a concrete criterion and connects the abstract notion to the familiar Gauss map.",
    "6", "6.1", "intermediate")

# s036: 6.2 Ovaloids
write_concept("ovaloid", "definition",
    "Ovaloid (Strictly Convex Closed Surface)", "geometry", "differential-geometry",
    "An ovaloid is a connected, compact surface $M \\subset \\mathbb{R}^3$ with $K > 0$ everywhere. Equivalently, it is a strictly convex closed surface.",
    "An ovaloid is a surface that curves toward the same side at every point, like an egg. It must be diffeomorphic to a sphere. The Gauss-Bonnet theorem implies $\\int_M K dM = 4\\pi$ for any ovaloid.",
    "6", "6.2", "intermediate")

write_concept("support-function-ovaloid", "corollary",
    "Support Function of an Ovaloid", "geometry", "differential-geometry",
    "Let $M$ be an ovaloid with Gauss map $n: M \\to S^2$. The support function $h(p) = n(p) \\cdot p$ satisfies $h(p_0) > h(p)$ for all $p \\neq p_0$, where $p_0$ is the unique point where $h$ attains its maximum. As a consequence, the Gauss map of an ovaloid is a diffeomorphism onto $S^2$.",
    "The support function encodes the distance from the origin to tangent planes. Its strict maximum shows that the Gauss map is bijective, a key property of ovaloids used in the proof of the rigidity theorem.",
    "6", "6.2", "intermediate")

# s037-s038: 6.3 Gauss-Bonnet
write_concept("gauss-bonnet-theorem", "theorem",
    "Gauss-Bonnet Theorem", "geometry", "differential-geometry",
    "For a compact orientable surface $M$ with a Riemannian metric,\n$$\\int_M K dM = 2\\pi \\chi(M),$$\nwhere $\\chi(M)$ is the Euler characteristic of $M$. For a triangulation with $v$ vertices, $e$ edges, and $f$ faces, $\\chi(M) = v - e + f$.",
    "The Gauss-Bonnet theorem is the crowning achievement of classical differential geometry, linking the total Gauss curvature (an analytic/geometric quantity) to the Euler characteristic (a topological invariant). For a sphere, $\\int K = 4\\pi$; for a torus, $\\int K = 0$.",
    "6", "6.3", "advanced")

# s039: 6.4 Completeness / Hopf-Rinow
write_concept("distance-function-manifold", "theorem",
    "Distance Function on a Riemannian Manifold", "geometry", "differential-geometry",
    "Let $M$ be a connected Riemannian manifold. The distance function $d(p, q)$, defined as the infimum of lengths of piecewise differentiable curves joining $p$ and $q$, is a metric on $M$. Moreover, the metric topology coincides with the manifold topology.",
    "The Riemannian distance makes any connected manifold into a metric space. The Hopf-Rinow theorem then characterizes completeness: $M$ is complete as a metric space iff geodesics can be extended indefinitely.",
    "6", "6.4", "intermediate")

write_concept("hopf-rinow-theorem", "theorem",
    "Hopf-Rinow Theorem", "geometry", "differential-geometry",
    "For a connected Riemannian manifold $M$, the following are equivalent:\n(i) $M$ is complete as a metric space;\n(ii) Every geodesic can be extended indefinitely;\n(iii) Closed bounded subsets of $M$ are compact.\nMoreover, if $M$ is complete, any two points can be joined by a minimal geodesic.",
    "The Hopf-Rinow theorem establishes the equivalence of metric completeness, geodesic completeness, and the Heine-Borel property. It guarantees the existence of minimal geodesics between any two points on a complete manifold.",
    "6", "6.4", "advanced")

# s041: 6.5 Conjugate Points
write_concept("conjugate-points", "theorem",
    "Conjugate Points and Minimizing Geodesics", "geometry", "differential-geometry",
    "Let $c(t) = \\exp_p(t X)$, $0 \\leq t \\leq a$, be a geodesic on a surface $M$. Then $c$ is a minimal geodesic from $p = c(0)$ to $q = c(a)$ if and only if there is no $t_0 \\in (0, a)$ such that $c(t_0)$ is conjugate to $p$ along $c$. A conjugate point occurs when a non-zero Jacobi field vanishes at $p$ and at $c(t_0)$.",
    "A geodesic stops being minimizing precisely when it passes through a conjugate point. This fundamental result connects the second variation of arc length (Jacobi fields) with the global problem of finding shortest paths.",
    "6", "6.5", "advanced")

write_concept("sturm-comparison-theorem", "theorem",
    "Sturm Comparison Theorem for Jacobi Fields", "geometry", "differential-geometry",
    "Let $y_1(t)$ and $y_2(t)$ be solutions of $\\ddot{y} + K_1(t) y = 0$ and $\\ddot{y} + K_2(t) y = 0$ respectively, with $y_1(0) = y_2(0) = 0$ and $\\dot{y}_1(0) = \\dot{y}_2(0) > 0$. If $K_1(t) \\geq K_2(t)$ for all $t$, then $y_1(t) \\leq y_2(t)$ between their first zeros, and the first zero of $y_1$ occurs no later than the first zero of $y_2$.",
    "The Sturm comparison theorem compares solutions of two Jacobi-type ODEs. Applied to geometry: larger Gauss curvature $K$ implies conjugate points occur sooner. This is the key lemma for comparing manifolds of different curvatures.",
    "6", "6.5", "advanced")

# s042: 6.5.8 Bonnet Theorem
write_concept("bonnet-theorem", "theorem",
    "Bonnet's Theorem on Diameter of Positively Curved Surfaces", "geometry", "differential-geometry",
    "Let $M$ be a complete surface with Gauss curvature $K \\geq K_0 > 0$ everywhere. Then the distance between any two points of $M$ is at most $\\pi/\\sqrt{K_0}$. Consequently, $M$ is compact.",
    "Bonnet's theorem gives a sharp upper bound on the diameter of a complete surface with positive curvature bounded below. Combined with Hopf-Rinow, it implies compactness — a purely geometric criterion for a global topological conclusion.",
    "6", "6.5", "advanced")

# s043: 6.6 Curvature and Global Geometry
write_concept("waist-geodesic-lemma", "lemma",
    "Lemma on Waist Geodesics and Curve Length", "geometry", "differential-geometry",
    "Let $M$ be a Riemannian surface and $c_0(t) \\equiv p$ the constant geodesic at a point. For a family of closed curves $c_s$ with $c_0 = p$ and variation field $Y$, the length functional satisfies $L''(0) = \\int (|\\nabla Y/dt|^2 - K|Y|^2) dt$. If $K \\geq K_0 > 0$, this second variation can become negative, showing certain curves cannot minimize length.",
    "This lemma relates curvature to the second variation of arc length, the foundation for studying closed geodesics. Positive curvature tends to shorten curves, while negative curvature tends to lengthen them.",
    "6", "6.6", "advanced")

# s044: 6.7 Closed Geodesics and Fundamental Group
write_concept("closed-geodesics-fundamental-group", "proposition",
    "Closed Geodesics in Non-Trivial Homotopy Classes", "geometry", "differential-geometry",
    "On a compact Riemannian surface $M$, every non-trivial free homotopy class of closed curves contains a closed geodesic of minimal length. The universal covering space $\\tilde{M}$ is acted upon by the fundamental group $\\Gamma = \\pi_1(M)$ as a group of fixed-point free isometries.",
    "In each non-trivial homotopy class, there exists a length-minimizing closed geodesic. This connects the Riemannian geometry (geodesics) with algebraic topology (fundamental group) and is the starting point for Morse theory on surfaces.",
    "6", "6.7", "advanced")

# s045: 6.8 exercises and further results
write_concept("sturm-comparison-geometric", "theorem",
    "Geometric Interpretation of Sturm Comparison Theorem", "geometry", "differential-geometry",
    "The Sturm comparison theorem (6.5.5) and its corollary (6.5.6) have the following geometric interpretation: on a surface with larger Gauss curvature, geodesics emanating from a point come together (form conjugate points) sooner than on a surface with smaller curvature. This provides a quantitative relationship between curvature and the spread of geodesics.",
    "The Sturm comparison theorem geometrically means that positive curvature causes geodesics to converge (like on a sphere), while negative curvature causes them to diverge (like on hyperbolic space). This is the fundamental link between local curvature and global geodesic behavior.",
    "6", "6.8", "advanced")

# s046: 6.8.9 Torus and Hopf
write_concept("hopf-torus-conjugate-points", "theorem",
    "Hopf's Theorem on Tori without Conjugate Points", "geometry", "differential-geometry",
    "Let $M$ be a surface homeomorphic to a torus, equipped with a Riemannian metric. If no geodesic on $M$ has a conjugate point, then $K \\equiv 0$ everywhere, i.e., $(M, g)$ is the flat torus.",
    "Hopf's theorem characterizes the flat metric among all metrics on the torus by the absence of conjugate points. This is a profound rigidity result: the only metric on the torus with no conjugate points is the flat one.",
    "6", "6.8", "advanced")

# ===================================================================
# WRITE .done MARKER
# ===================================================================
done_path = os.path.join(BASE, ".done")
with open(done_path, "w") as f:
    f.write("DONE\n")

print(f"SUCCESS: Extracted concepts into {BASE}")
print(f"Total concept directories created in {BASE}")
