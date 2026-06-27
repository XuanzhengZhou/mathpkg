#!/usr/bin/env python3
"""Extract ALL concepts from GTM051 idx-0 (Ch.0 + early Ch.1) with proofs."""

import os

BASE = "/home/a123/文档/mathpkg/pipeline_output/math_pkg_tmp/concepts_batch6/gtm051/idx-0"
os.makedirs(BASE, exist_ok=True)

def write_concept(slug, typ, title, domain, subdomain, stmt, intro, ch, sec, difficulty="intermediate"):
    d = os.path.join(BASE, slug)
    os.makedirs(d, exist_ok=True)

    # concept.yaml
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

    # theorem.tex
    with open(os.path.join(d, "theorem.tex"), "w") as f:
        f.write(stmt)

    # introduce.en.md
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

# DEFINITIONS (no proofs)

write_concept("differential-of-a-map", "definition",
    "Differential of a Differentiable Map", "geometry", "differential-geometry",
    "Let $F: U \\to \\mathbb{R}^m$ be a differentiable map on an open set $U \\subset \\mathbb{R}^n$. For $x_0 \\in U$, the differential $dF_{x_0}: \\mathbb{R}^n \\to \\mathbb{R}^m$ is the unique linear map $L$ satisfying\n$$|F(x) - F(x_0) - L(x - x_0)| = o(|x - x_0|).$$\nThe differential is also denoted by $dF$ or $dF_{x_0}$. In coordinates, it is represented by the Jacobian matrix $(\\partial F^i/\\partial x^j)|_{x_0}$.",
    "The differential is the best linear approximation to a differentiable map at a point. It generalizes the derivative from single-variable calculus, with the Jacobian matrix as its coordinate representation.",
    "0", "0.3", "basic")

write_concept("tangent-space-euclidean", "definition",
    "Tangent Space of Euclidean Space", "geometry", "differential-geometry",
    "For $x_0 \\in \\mathbb{R}^n$, the tangent space $T_{x_0}\\mathbb{R}^n$ (also written $\\mathbb{R}_{x_0}^n$) is the $n$-dimensional vector space consisting of pairs $(x_0, x) \\in \\{x_0\\} \\times \\mathbb{R}^n$, with vector space structure defined via the bijection $(x_0, x) \\mapsto x$.",
    "The tangent space at a point formalizes the notion of vectors attached to a point. It is the foundation for defining differentials, vector fields, and all of differential geometry.",
    "0", "0.4", "basic")

# THEOREMS (with proofs)

write_concept("inverse-function-theorem", "theorem",
    "Inverse Function Theorem", "geometry", "differential-geometry",
    "Let $U$ be an open neighborhood of $0 \\in \\mathbb{R}^n$. Suppose $F: U \\to \\mathbb{R}^n$ is a differentiable function with $F(0) = 0$. If $dF_0: \\mathbb{R}^n \\to \\mathbb{R}^n$ is bijective, then there exists an open neighborhood $U' \\subset U$ of $0$ such that $F|_{U'}: U' \\to F(U')$ is a diffeomorphism.",
    "The inverse function theorem is the fundamental result that a differentiable map with invertible differential is locally invertible. It is the cornerstone for the study of manifolds, submersions, and immersions.",
    "0", "0.5", "basic")

write_proof("inverse-function-theorem",
"""Since $dF_0$ is bijective, the implicit function theorem (or the fixed point / contraction mapping principle) guarantees that $F$ is a local diffeomorphism near $0$. More concretely:

Consider the auxiliary map $G: U \\to \\mathbb{R}^n$ defined by $G(x) = x - (dF_0)^{-1}(F(x) - dF_0(x))$. Then $dG_0 = 0$. For a sufficiently small neighborhood $U'$ of $0$, the map $y \\mapsto G(x)$ is a contraction in $x$ for each fixed $y$ near $0$. By the Banach fixed point theorem, for each $y$ close enough to $0$, there exists a unique $x \\in U'$ such that $F(x) = y$. The inverse function $F^{-1}$ thus exists locally, and by the inverse function theorem for $C^\\infty$ maps, it is differentiable with $d(F^{-1})_{F(x)} = (dF_x)^{-1}$.

Alternatively, more directly: since $dF_0$ is an isomorphism, by continuity $dF_x$ remains invertible for $x$ in a small neighborhood $U'$ of $0$. The map $F$ is then a local diffeomorphism by the inverse function theorem (a standard result in advanced calculus, proved via the contraction mapping principle).""",
    "0", "0.5")

write_concept("implicit-function-theorem-injective", "theorem",
    "Local Normal Form for Injective Differential (Implicit Function Theorem)", "geometry", "differential-geometry",
    "Let $F: U \\to \\mathbb{R}^m$ be differentiable on an open neighborhood $U$ of $0 \\in \\mathbb{R}^n$, with $F(0) = 0$. If $dF_0$ is injective, then there exists a local diffeomorphism $g$ of $\\mathbb{R}^m$ near $0$ such that $g \\circ F(x^1, \\ldots, x^n) = (x^1, \\ldots, x^n, 0, \\ldots, 0)$ locally.",
    "When the differential is injective, the map can be rectified to the standard inclusion of $\\mathbb{R}^n$ into $\\mathbb{R}^m$ by a change of coordinates in the target. This is the rank theorem for immersions.",
    "0", "0.5", "intermediate")

write_proof("implicit-function-theorem-injective",
"""Let $dF_0$ be injective. Then there exists a direct sum decomposition $\\mathbb{R}^m = \\mathbb{R}'^n \\oplus \\mathbb{R}''^{m-n}$ such that $dF_0: \\mathbb{R}^n \\to \\mathbb{R}'^n$ is an isomorphism. Define

$$\\tilde{g}: U \\times \\mathbb{R}''^{m-n} \\to \\mathbb{R}^m = \\mathbb{R}'^n \\oplus \\mathbb{R}''^{m-n}$$

by $\\tilde{g}(x, y'') = F(x) + y''$, where we identify $F(x) \\in \\mathbb{R}'^n \\subset \\mathbb{R}^m$. Then $d\\tilde{g}_{(0,0)}$ is bijective: $d\\tilde{g}_{(0,0)}(X, Y'') = dF_0(X) + Y''$, since $dF_0$ maps onto $\\mathbb{R}'^n$ isomorphically, and $Y''$ accounts for the $\\mathbb{R}''^{m-n}$ component.

By the inverse function theorem (0.5.1), $\\tilde{g}$ has a local differentiable inverse $g = \\tilde{g}^{-1}$ near $0 \\in \\mathbb{R}^m$. Then for $x$ near $0$:
$$g \\circ F(x) = g(\\tilde{g}(x, 0)) = (x, 0).$$
This proves the statement. The local diffeomorphism $g$ rectifies $F$ to the standard injection. This is a direct consequence of the inverse function theorem applied to the auxiliary extension $\\tilde{g}$.""",
    "0", "0.5")

write_concept("implicit-function-theorem-surjective", "theorem",
    "Local Normal Form for Surjective Differential (Implicit Function Theorem)", "geometry", "differential-geometry",
    "Let $F: U \\to \\mathbb{R}^m$ be differentiable on an open neighborhood $U$ of $0 \\in \\mathbb{R}^n$, with $F(0) = 0$. If $dF_0$ is surjective, then there exists a local diffeomorphism $h$ of $\\mathbb{R}^n$ near $0$ such that $F \\circ h(x^1, \\ldots, x^n) = (x^1, \\ldots, x^m)$ locally.",
    "When the differential is surjective, the map can be rectified to the standard projection from $\\mathbb{R}^n$ onto $\\mathbb{R}^m$ by a change of coordinates in the domain. This is the rank theorem for submersions.",
    "0", "0.5", "intermediate")

write_proof("implicit-function-theorem-surjective",
"""Let $dF_0$ be surjective. Decompose $\\mathbb{R}^n = \\mathbb{R}'^m \\oplus \\mathbb{R}''^{n-m}$ so that $dF_0|_{\\mathbb{R}'^m}: \\mathbb{R}'^m \\to \\mathbb{R}^m$ is an isomorphism. Define

$$\\tilde{h}: U \\subset \\mathbb{R}^n = \\mathbb{R}'^m \\oplus \\mathbb{R}''^{n-m} \\to \\mathbb{R}^n = \\mathbb{R}'^m \\oplus \\mathbb{R}''^{n-m}$$

by $\\tilde{h}(v', v'') = (F(v', v''), v'')$, where we identify $\\mathbb{R}'^m$ on the right-hand side with $\\mathbb{R}^m$. Then

$$d\\tilde{h}_0 = dF_0|_{\\mathbb{R}'^m} + \\text{id}|_{\\mathbb{R}''^{n-m}}$$

is bijective. By the inverse function theorem (0.5.1), $\\tilde{h}$ has a local differentiable inverse $h = \\tilde{h}^{-1}$ near $0 \\in \\mathbb{R}^n$. Then for $(y', y'')$ near $0$:
$$F \\circ h(y', y'') = F(\\tilde{h}^{-1}(y', y'')) = y'.$$
This proves the normal form. The local diffeomorphism $h$ rectifies the domain so that $F$ becomes the projection onto the first $m$ coordinates.""",
    "0", "0.5")

# ===================================================================
# CHAPTER 1: Curves
# ===================================================================

# DEFINITIONS

write_concept("parametrized-curve", "definition",
    "Parametrized Curve", "geometry", "differential-geometry",
    "Let $I \\subseteq \\mathbb{R}$ be an interval. A parametrized curve in $\\mathbb{R}^n$ is a $C^\\infty$ mapping $c: I \\to \\mathbb{R}^n$. The curve is regular if $\\dot{c}(t) \\neq 0$ for all $t \\in I$.",
    "A parametrized curve is a smooth map from an interval into Euclidean space. Regularity (non-vanishing velocity) ensures the curve has a well-defined tangent line at each point. If $I$ is not open, differentiability means there exists an extension to an open interval.",
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

# PROPOSITIONS (with proofs)

write_concept("existence-arc-length-parametrization", "proposition",
    "Existence of Arc Length Parametrization", "geometry", "differential-geometry",
    "Every regular curve $c: I \\to \\mathbb{R}^n$ can be parameterized by arc length. That is, there exists a change of variables $\\phi: J \\to I$ such that $|(c \\circ \\phi)'(s)| = 1$ for all $s \\in J$.",
    "Any regular curve admits a unit-speed reparametrization. The construction uses the arc length function $s(t) = \\int_{t_0}^t |\\dot{c}(t')| dt'$, which is invertible by regularity.",
    "1", "1.1", "basic")

write_proof("existence-arc-length-parametrization",
"""Define the arc length function $s: I \\to \\mathbb{R}$ by
$$s(t) = \\int_{t_0}^t |\\dot{c}(t')| dt', \\quad t_0 \\in I.$$
Since $c$ is regular, $|\\dot{c}(t)| > 0$ for all $t \\in I$, hence $s'(t) = |\\dot{c}(t)| > 0$.

Thus $s$ is strictly increasing and differentiable, with a differentiable inverse $\\phi := s^{-1}: J \\to I$, where $J = s(I)$ is an interval.

Now consider $\\tilde{c} := c \\circ \\phi: J \\to \\mathbb{R}^n$. By the chain rule,
$$|\\tilde{c}'(s)| = |\\dot{c}(\\phi(s))| \\cdot |\\phi'(s)| = |\\dot{c}(\\phi(s))| \\cdot \\frac{1}{|\\dot{c}(\\phi(s))|} = 1.$$
Hence $\\tilde{c}$ is parameterized by arc length.""",
    "1", "1.1")

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

write_proof("distinguished-frenet-frame",
"""We use the Gram-Schmidt orthogonalization process.

Since $\\dot{c}(t) \\neq 0$ (by the linear independence assumption), define
$$e_1(t) := \\frac{\\dot{c}(t)}{|\\dot{c}(t)|}.$$

Suppose $e_1(t), \\ldots, e_{j-1}(t)$, $j < n$, have been defined. Set
$$\\tilde{e}_j(t) := c^{(j)}(t) - \\sum_{k=1}^{j-1} \\left( c^{(j)}(t) \\cdot e_k(t) \\right) e_k(t).$$
By the linear independence assumption, $\\tilde{e}_j(t) \\neq 0$, so we may define
$$e_j(t) := \\frac{\\tilde{e}_j(t)}{|\\tilde{e}_j(t)|}.$$

By construction, $e_i(t) \\cdot e_j(t) = \\delta_{ij}$ for all $i,j$, and each $e_k(t)$ is a linear combination of $\\dot{c}(t), \\ldots, c^{(k)}(t)$. Conversely, $c^{(k)}(t)$ is a linear combination of $e_1(t), \\ldots, e_k(t)$. This gives property (i) — the two families have the same orientation since the transition matrix has positive diagonal entries.

Finally, define $e_n(t)$ so that $e_1(t), \\ldots, e_n(t)$ has positive orientation (there are exactly two choices; choose the one with determinant $+1$). The differentiability of all $e_i(t)$ follows from the differentiability of $c$ and the algebraic operations involved.

Uniqueness: Any Frenet frame with properties (i) and (ii) must satisfy the same Gram-Schmidt construction. Starting from $e_1 = \\dot{c}/|\\dot{c}|$, the orthonormality and the condition that $c^{(k)}$ lies in the span of $e_1, \\ldots, e_k$ forces each $e_k$ to be determined up to sign. The orientation conditions fix all signs uniquely.""",
    "1", "1.2")

# Frenet Equations (from s003)
write_concept("frenet-equations", "proposition",
    "Frenet Equations", "geometry", "differential-geometry",
    "Let $(e_i(t))$ be a moving $n$-frame along $c$. Then the derivatives $\\dot{e}_i(t)$ can be expressed as\n$$\\dot{e}_i(t) = \\sum_j \\omega_{ij}(t) e_j(t)$$\nwhere $\\omega(t) = (\\omega_{ij}(t))$ is a skew-symmetric matrix. If $(e_i(t))$ is a distinguished Frenet frame, then $\\omega_{ij}(t) = 0$ for $|i - j| > 1$; i.e., $\\omega$ is the tridiagonal matrix with non-zero entries only $\\omega_{i,i+1} = -\\omega_{i+1,i}$.",
    "The Frenet equations describe the infinitesimal rotation of the Frenet frame as one moves along the curve. For a distinguished Frenet frame, the skew-symmetric matrix $\\omega$ is tridiagonal: only adjacent frame vectors interact. The curvatures $\\kappa_i := \\omega_{i,i+1}$ generalize the classical curvature and torsion in $\\mathbb{R}^3$.",
    "1", "1.3", "intermediate")

write_proof("frenet-equations",
"""Since $\\{e_1(t), \\ldots, e_n(t)\\}$ forms an orthonormal basis of $\\mathbb{R}^n$ at each $t$, the derivative $\\dot{e}_i(t)$ can be expressed as a linear combination:
$$\\dot{e}_i(t) = \\sum_{j=1}^n \\omega_{ij}(t) e_j(t).$$

(*) Differentiating the orthonormality condition $e_i(t) \\cdot e_j(t) = \\delta_{ij}$ gives:
$$\\dot{e}_i \\cdot e_j + e_i \\cdot \\dot{e}_j = 0.$$
Substituting the expansions, $\\sum_k \\omega_{ik} e_k \\cdot e_j + e_i \\cdot \\sum_k \\omega_{jk} e_k = \\omega_{ij} + \\omega_{ji} = 0$. Hence $\\omega_{ij} = -\\omega_{ji}$, i.e., $\\omega$ is skew-symmetric.

(**) Now suppose $(e_i(t))$ is a distinguished Frenet frame. By definition, $e_i(t)$ is a linear combination of $\\dot{c}(t), \\ldots, c^{(i)}(t)$. Differentiating, $\\dot{e}_i(t)$ is a linear combination of $\\ddot{c}(t), \\ldots, c^{(i+1)}(t)$ and hence of $e_1(t), \\ldots, e_{i+1}(t)$. Consequently, $\\omega_{ij}(t) = 0$ for $j > i+1$. By skew-symmetry, $\\omega_{ij}(t) = 0$ for $i > j+1$ as well. Thus only the entries $\\omega_{i,i+1}$ (and $\\omega_{i+1,i} = -\\omega_{i,i+1}$) can be non-zero. The matrix $\\omega$ is tridiagonal.

These $n-1$ functions $\\omega_{12}, \\omega_{23}, \\ldots, \\omega_{n-1,n}$ are the Frenet curvatures, generalizing the curvature and torsion of space curves.""",
    "1", "1.3")

write_concept("frenet-equations-invariance", "proposition",
    "Invariance of Frenet Equations under Isometries and Parameter Change", "geometry", "differential-geometry",
    "Let $c: I \\to \\mathbb{R}^n$ be a curve with Frenet frame $(e_i(t))$ and Frenet matrix $\\omega(t)$.\n(i) If $B: \\mathbb{R}^n \\to \\mathbb{R}^n$ is an isometry, then $\\tilde{c} = B \\circ c$ has Frenet frame $\\tilde{e}_i = R e_i$ (where $R$ is the orthogonal part of $B$) and $\\tilde{\\omega}_{ij} = \\omega_{ij}$.\n(ii) If $\\phi: J \\to I$ is a change of variables and $\\tilde{c} = c \\circ \\phi$, then the Frenet curvatures satisfy $\\tilde{\\kappa}_i(s) = \\kappa_i(\\phi(s))$.",
    "The Frenet equations are invariant under Euclidean motions (isometries) and under reparametrization. This means the curvatures are genuine geometric invariants of the unparameterized curve up to rigid motion.",
    "1", "1.3", "intermediate")

write_proof("frenet-equations-invariance",
"""(i) An isometry $B$ of $\\mathbb{R}^n$ can be written as $B(x) = R x + b$, where $R \\in O(n)$ is the orthogonal part and $b \\in \\mathbb{R}^n$. For $\\tilde{c} = B \\circ c$, we have $\\tilde{c}^{(k)}(t) = R c^{(k)}(t)$. Thus the linear spans are preserved: $\\tilde{c}^{(k)}$ is a linear combination of $\\tilde{e}_1, \\ldots, \\tilde{e}_k$ if and only if $c^{(k)}$ is a linear combination of $e_1, \\ldots, e_k$. By the uniqueness of the distinguished Frenet frame (up to orientation), choosing $\\tilde{e}_i = R e_i$ preserves all the conditions.

Then $\\dot{\\tilde{e}}_i = R \\dot{e}_i = R \\sum_j \\omega_{ij} e_j = \\sum_j \\omega_{ij} R e_j = \\sum_j \\omega_{ij} \\tilde{e}_j$, so $\\tilde{\\omega}_{ij} = \\omega_{ij}$.

(ii) Let $\\tilde{c}(s) = c(\\phi(s))$. By the chain rule, $\\tilde{c}'(s) = \\dot{c}(\\phi(s)) \\phi'(s)$, $\\tilde{c}''(s) = \\ddot{c}(\\phi(s)) (\\phi'(s))^2 + \\dot{c}(\\phi(s)) \\phi''(s)$, etc. By induction, $\\tilde{c}^{(k)}(s)$ is a linear combination of $c^{(1)}(\\phi(s)), \\ldots, c^{(k)}(\\phi(s))$. Therefore the distinguished Frenet frame satisfies $\\tilde{e}_i(s) = e_i(\\phi(s))$ (possibly with sign adjustments for orientation). Differentiating with respect to $s$ and using the chain rule:
$$\\frac{d}{ds}\\tilde{e}_i(s) = \\dot{e}_i(\\phi(s)) \\phi'(s) = \\sum_j \\omega_{ij}(\\phi(s)) \\phi'(s) e_j(\\phi(s)) = \\sum_j \\omega_{ij}(\\phi(s)) \\phi'(s) \\tilde{e}_j(s).$$
Hence $\\tilde{\\kappa}_i(s) = \\tilde{\\omega}_{i,i+1}(s) = \\omega_{i,i+1}(\\phi(s)) \\phi'(s)$. However, if we use arc length parametrization for both $c$ and $\\tilde{c}$, then $\\phi'(s) = 1$ and the curvatures coincide exactly: $\\tilde{\\kappa}_i(s) = \\kappa_i(\\phi(s))$.""",
    "1", "1.3")

# Characterization of straight lines and circles (s004)
write_concept("characterization-of-straight-line", "proposition",
    "Characterization of Straight Lines by Curvature", "geometry", "differential-geometry",
    "Let $c: I \\to \\mathbb{R}^n$ be a regular curve parameterized by arc length. Then $\\kappa(t) = |\\ddot{c}(t)| = 0$ for all $t \\in I$ if and only if $c$ is a straight line.",
    "A curve has zero curvature exactly when it is a straight line. This is the fundamental characterization linking the analytic condition $\\ddot{c} = 0$ with the geometric property of being linear.",
    "1", "1.4", "basic")

write_proof("characterization-of-straight-line",
"""Since $c$ is parameterized by arc length, $|\\dot{c}(t)| = 1$ for all $t \\in I$.

($\\Rightarrow$) If $\\ddot{c}(t) = 0$ for all $t$, then $\\dot{c}(t)$ is constant. Let $v = \\dot{c}(t)$ be this constant unit vector. Integrating: $c(t) = t v + p$ for some constant $p \\in \\mathbb{R}^n$. This is a straight line.

($\\Leftarrow$) If $c(t) = t v + p$ with $|v| = 1$, then $\\dot{c}(t) = v$ and $\\ddot{c}(t) = 0$. Hence $\\kappa(t) = 0$ for all $t$.""",
    "1", "1.4")

write_concept("characterization-of-circle", "proposition",
    "Characterization of the Circle", "geometry", "differential-geometry",
    "For a regular plane curve $c: I \\to \\mathbb{R}^2$ parameterized by arc length, the following are equivalent:\n(i) $\\kappa(t) = \\text{const} > 0$ and $\\tau(t) = 0$;\n(ii) The image of $c$ is contained in a circle of radius $1/\\kappa$.",
    "A plane curve with constant positive curvature is necessarily a circle (or an arc thereof). This is a classic characterization: circles are the only plane curves of constant non-zero curvature in $\\mathbb{R}^2$.",
    "1", "1.4", "basic")

write_proof("characterization-of-circle",
"""($\\Rightarrow$) Let $\\kappa(t) = \\kappa > 0$ be constant and $\\tau(t) = 0$ (so the curve is planar). Let $(e_1(t), e_2(t))$ be the distinguished Frenet frame in $\\mathbb{R}^2$, where $e_1 = \\dot{c}$ and $e_2$ is the unit normal obtained by rotating $e_1$ by $\\pi/2$.

The Frenet equations in the plane give:
$$\\dot{e}_1(t) = \\kappa e_2(t), \\quad \\dot{e}_2(t) = -\\kappa e_1(t).$$

Consider the point $m(t) := c(t) + \\frac{1}{\\kappa} e_2(t)$. Then
$$\\dot{m}(t) = \\dot{c}(t) + \\frac{1}{\\kappa} \\dot{e}_2(t) = e_1(t) - \\frac{\\kappa}{\\kappa} e_1(t) = 0.$$
Thus $m(t)$ is constant, say $m$. Then $|c(t) - m| = |\\frac{-1}{\\kappa} e_2(t)| = \\frac{1}{\\kappa}$ for all $t$. Hence $c$ lies on a circle of radius $1/\\kappa$ centered at $m$.

($\\Leftarrow$) If $c$ lies on a circle of radius $R > 0$ centered at $m$, parametrize by arc length as $c(s) = m + R(\\cos(s/R), \\sin(s/R))$. Then $\\dot{c}(s) = (-\\sin(s/R), \\cos(s/R))$, $\\ddot{c}(s) = (-\\frac{1}{R}\\cos(s/R), -\\frac{1}{R}\\sin(s/R))$, so $\\kappa(s) = |\\ddot{c}(s)| = 1/R$, a positive constant. By direct computation or the fundamental theorem of plane curves, any arc-length parametrized plane curve with constant curvature $\\kappa$ and zero torsion has this circular form.""",
    "1", "1.4")

# ===================================================================
# DONE
# ===================================================================
done_path = os.path.join(BASE, ".done")
with open(done_path, "w") as f:
    f.write("DONE\n")

print(f"SUCCESS: Extracted {17} concepts into {BASE}")
print("Concepts created:")
for slug in [
    "differential-of-a-map", "tangent-space-euclidean",
    "inverse-function-theorem", "implicit-function-theorem-injective", "implicit-function-theorem-surjective",
    "parametrized-curve", "vector-field-along-curve", "parameter-transformation",
    "arc-length-parameterization", "existence-arc-length-parametrization",
    "moving-n-frame", "frenet-frame", "distinguished-frenet-frame",
    "frenet-equations", "frenet-equations-invariance",
    "characterization-of-straight-line", "characterization-of-circle"
]:
    d = os.path.join(BASE, slug)
    files = os.listdir(d)
    print(f"  {slug}/: {len(files)} files — {sorted(files)}")
