#!/usr/bin/env python3
"""Extract ALL concepts from GTM051 idx-31 (s031-s033: Sections 5.6.3-5.7.4)"""
import os

BASE = "/home/a123/文档/mathpkg/pipeline_output/math_pkg_tmp/concepts_batch6/gtm051/idx-31"
os.makedirs(BASE, exist_ok=True)

def write_concept(slug, typ, title, domain, subdomain, stmt, intro, ch, sec, difficulty="intermediate"):
    d = os.path.join(BASE, slug)
    os.makedirs(d, exist_ok=True)
    yaml = f'''id: {slug}
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
'''
    with open(os.path.join(d, "concept.yaml"), "w") as f:
        f.write(yaml)
    with open(os.path.join(d, "theorem.tex"), "w") as f:
        f.write(stmt)
    intro_md = f'''---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

{intro}
'''
    with open(os.path.join(d, "introduce.en.md"), "w") as f:
        f.write(intro_md)
    return d

def write_proof(slug, proof_text, ch, sec):
    d = os.path.join(BASE, slug)
    proof_md = f'''---
role: proof
locale: en
of_concept: {slug}
source_book: gtm051
source_chapter: "{ch}"
source_section: "{sec}"
---

{proof_text}
'''
    with open(os.path.join(d, f"proof_gtm051_{ch}_{sec}.en.md"), "w") as f:
        f.write(proof_md)

def write_exercise(slug, ex_num, ch, sec, stmt):
    d = os.path.join(BASE, slug)
    ex_md = f'''---
role: exercise
locale: en
chapter: "{ch}"
section: "{sec}"
exercise_number: {ex_num}
---

{stmt}
'''
    with open(os.path.join(d, f"exercise_gtm051_{ch}_{sec}_{ex_num}.en.md"), "w") as f:
        f.write(ex_md)

# ===================================================================
# CONCEPT 1: Differential of Function as 1-Form (Definition 5.6.6, Example 1)
# ===================================================================
write_concept("differential-of-function-as-one-form", "definition",
    "Differential of a Function as a 1-Form",
    "geometry", "differential-geometry",
    "Let $f: M \\to \\mathbb{R}$ be a differentiable function on a manifold $M$. The **differential** of $f$ is the 1-form\n$$df: TM \\to \\mathbb{R}, \\quad X \\mapsto d(f \\circ u_\\alpha^{-1}) X_\\alpha,$$\nwhere $X_\\alpha$ is the representative of $X$ in $TU_\\alpha$ with respect to the chart $(u_\\alpha, M_\\alpha)$. In particular, the coordinate 1-forms $du_\\alpha^1, du_\\alpha^2$ are the differentials of the coordinate functions $u_\\alpha^k: M_\\alpha \\to \\mathbb{R}$.",
    "The differential of a function extends the classical notion to manifolds: at each point, it is the linear map approximating the change of $f$. In coordinates, $df = \\sum \\frac{\\partial f}{\\partial u^i} du^i$. The coordinate 1-forms $du^i$ form the dual basis to the coordinate vector fields $\\partial/\\partial u^i$.",
    "5", "5.6", "intermediate")

# ===================================================================
# CONCEPT 2: Metric Isomorphism TM to T*M (Proposition/Remark 5.6.6, Example 2)
# ===================================================================
write_concept("metric-isomorphism-tangent-cotangent", "proposition",
    "Metric-Induced Isomorphism between Tangent and Cotangent Bundles",
    "geometry", "differential-geometry",
    "Let $M$ be a Riemannian manifold with metric $g$. For each $p \\in M$, the map\n$$Lg_p: X \\in T_pM \\mapsto g_p(X, \\cdot) \\in T_p^*M$$\nis a linear isomorphism. Thus a vector field $X$ defines a 1-form and conversely: if $X = \\sum_i \\xi^i(u) e_i(u)$ in local coordinates, the corresponding 1-form is\n$$\\omega = \\sum_{i,j} g_{ij}(u) \\xi^i(u) \\, du^j.$$",
    "The Riemannian metric provides a canonical isomorphism between vectors and covectors ('raising and lowering indices'). This is used to define the gradient (as the vector field corresponding to $df$) and the divergence (via the area form).",
    "5", "5.6", "intermediate")

write_proof("metric-isomorphism-tangent-cotangent",
    "For each $p \\in M$, the map $Lg_p: X \\mapsto g_p(X, \\cdot)$ is linear by bilinearity of $g$. Since $g_p$ is positive definite, $Lg_p(X) = 0$ implies $g_p(X, X) = 0$, hence $X = 0$; thus $Lg_p$ is injective. As $\\dim T_pM = \\dim T_p^*M = 2$, injectivity implies surjectivity. Hence $Lg_p$ is an isomorphism.\n\nIn coordinates, $g_p$ is represented by the matrix $(g_{ij}(u))$ with respect to the basis $\\{e_i = \\partial/\\partial u^i\\}$. The dual basis is $\\{du^j\\}$ with $du^j(e_i) = \\delta_i^j$. Then $Lg_p(e_i) = g_p(e_i, \\cdot) = \\sum_j g_{ij}(u) du^j$, since $g_p(e_i, e_k) = g_{ik}$ and the 1-form sending $e_k \\mapsto g_{ik}$ is precisely $\\sum_j g_{ij} du^j$. For a general vector $X = \\sum_i \\xi^i e_i$, we have $Lg_p(X) = \\sum_i \\xi^i Lg_p(e_i) = \\sum_{i,j} g_{ij} \\xi^i du^j$.",
    "5", "5.6")

# ===================================================================
# CONCEPT 3: Area Element (Definition 5.6.6, Example 3)
# ===================================================================
write_concept("area-element-two-form", "definition",
    "Area Element (Volume Form) on an Oriented Riemannian Surface",
    "geometry", "differential-geometry",
    "Let $M$ be an oriented Riemannian surface. The **area element** is the 2-form $dM$ defined by\n$$dM(X, Y) := \\sqrt{g(X, X) g(Y, Y) - g(X, Y)^2}$$\nwhenever $\\{X, Y\\}$ is a positively oriented basis of $T_pM$. In local coordinates, $dM = \\sqrt{\\det g} \\, du^1 \\wedge du^2 = \\sqrt{g} \\, du^1 \\wedge du^2$.",
    "The area element is the unique 2-form that assigns unit area to any positively oriented orthonormal frame. It generalizes $dx \\wedge dy$ from the Euclidean plane. In coordinates, $\\sqrt{g} = \\sqrt{g_{11}g_{22} - g_{12}^2}$ is the area scaling factor. The interior product $i_X dM$ is the 1-form that pairs with $Y$ to give the signed area of the parallelogram spanned by $X$ and $Y$.",
    "5", "5.6", "intermediate")

# ===================================================================
# CONCEPT 4: Singular Polygon (Definition 5.6.7)
# ===================================================================
write_concept("singular-polygon-on-surface", "definition",
    "Singular Polygon on a Surface",
    "geometry", "differential-geometry",
    "Let $F \\subset \\mathbb{R}^2$ be a closed subset homeomorphic to a disk whose boundary $\\partial F$ is a piecewise smooth simple closed curve with all exterior angles strictly less than $\\pi$. A **(singular) polygon** on a surface $M$ is a differentiable mapping $P: F \\to M$ (extended to a neighborhood of $F$).",
    "A singular polygon is the two-dimensional analog of a piecewise smooth curve. It serves as the domain for surface integration and is the fundamental building block for polygonal decompositions of a compact surface, which are required for the global Gauss-Bonnet theorem.",
    "5", "5.6", "intermediate")

# ===================================================================
# CONCEPT 5: Integral of 2-Form on Polygon (Definition 5.6.8)
# ===================================================================
write_concept("integral-of-two-form-on-polygon", "definition",
    "Integral of a 2-Form on a Polygon",
    "geometry", "differential-geometry",
    "Let $\\Omega$ be a 2-form on a surface $M$ and $P: F \\to M$ a polygon. The **integral** of $\\Omega$ over $P$ is\n$$\\iint_P \\Omega := \\iint_F \\Omega\\!\\left(\\frac{\\partial P}{\\partial t^1}, \\frac{\\partial P}{\\partial t^2}\\right) dt^1 dt^2.$$\nThis integral is invariant under orientation-preserving changes of variables of the polygon.",
    "The integral of a 2-form over a polygon generalizes the double integral from calculus. Invariance under orientation-preserving reparametrization ensures it is well-defined on the surface. Together with the line integral of 1-forms, it provides the foundation for the Gauss/Stokes theorem on surfaces.",
    "5", "5.6", "intermediate")

# ===================================================================
# CONCEPT 6: Gauss Divergence Theorem on Surface (Theorem 5.6.9)
# ===================================================================
write_concept("gauss-divergence-theorem-surface", "theorem",
    "Gauss's Theorem (Divergence Theorem) on a Surface",
    "geometry", "differential-geometry",
    "Let $M$ be an oriented surface with a Riemannian metric and let $X$ be a vector field on $M$. Then for every polygon $P: F \\to M$,\n$$\\iint_P (\\operatorname{div} X) \\, dM = \\int_{\\partial P} i_X dM.$$\nIn local coordinates where $dM = \\sqrt{g} \\, du^1 \\wedge du^2$ and $X = \\sum \\xi^i e_i$:\n$$\\operatorname{div} X = \\frac{1}{\\sqrt{g}} \\sum_i \\frac{\\partial}{\\partial u^i}(\\sqrt{g} \\, \\xi^i), \\quad i_X dM = -\\xi^2 \\sqrt{g} \\, du^1 + \\xi^1 \\sqrt{g} \\, du^2.$$",
    "Gauss's theorem on surfaces is the generalization of the two-dimensional Stokes theorem. The integral of the divergence of a vector field over a polygon equals the flux of $X$ across the boundary. When $M = \\mathbb{R}^2$ with the standard metric, $dM = du^1 \\wedge du^2$ and the theorem reduces to the classical Stokes/Green theorem.",
    "5", "5.6", "advanced")

write_proof("gauss-divergence-theorem-surface",
    "**Proof.** \n\n1. Without loss of generality, we may assume that $P$ lies entirely within one coordinate system. If not, subdivide $F$ into $\\{F_\\rho\\}$, $1 \\leq \\rho \\leq k$, so that each $P_\\rho := P|_{F_\\rho}$ lies inside a coordinate system. If the theorem holds for each $P_\\rho$, summing yields\n$$\\iint_P (\\operatorname{div} X) dM = \\sum_\\rho \\iint_{P_\\rho} (\\operatorname{div} X) dM = \\sum_\\rho \\int_{\\partial P_\\rho} i_X dM.$$\nThe interior edges appear twice with opposite orientations and their line integrals cancel, leaving only the boundary integral $\\int_{\\partial P} i_X dM$.\n\n2. Now assume $P$ lies in a single coordinate chart $(U, (u^1, u^2))$. In local coordinates:\n$$\\operatorname{div} X = \\frac{1}{\\sqrt{g}} \\sum_i \\frac{\\partial}{\\partial u^i}(\\sqrt{g} \\, \\xi^i), \\quad dM = \\sqrt{g} \\, du^1 \\wedge du^2,$$\nand $i_X dM = -\\xi^2 \\sqrt{g} \\, du^1 + \\xi^1 \\sqrt{g} \\, du^2$.\n\nThus\n$$\\iint_P (\\operatorname{div} X) dM = \\iint_F \\frac{1}{\\sqrt{g}} \\left(\\frac{\\partial}{\\partial u^1}(\\sqrt{g} \\xi^1) + \\frac{\\partial}{\\partial u^2}(\\sqrt{g} \\xi^2)\\right) \\sqrt{g} \\, du^1 du^2$$\n$$= \\iint_F \\left(\\frac{\\partial}{\\partial u^1}(\\sqrt{g} \\xi^1) + \\frac{\\partial}{\\partial u^2}(\\sqrt{g} \\xi^2)\\right) du^1 du^2.$$\n\nNow set $f_1 = -\\xi^2 \\sqrt{g}$, $f_2 = +\\xi^1 \\sqrt{g}$. Then\n$$\\frac{\\partial f_2}{\\partial u^1} - \\frac{\\partial f_1}{\\partial u^2} = \\frac{\\partial}{\\partial u^1}(\\xi^1 \\sqrt{g}) + \\frac{\\partial}{\\partial u^2}(\\xi^2 \\sqrt{g}).$$\n\nBy the classical Stokes theorem for two dimensions:\n$$\\iint_F \\left(\\frac{\\partial f_2}{\\partial u^1} - \\frac{\\partial f_1}{\\partial u^2}\\right) du^1 du^2 = \\int_{\\partial F} (f_1 du^1 + f_2 du^2) = \\int_{\\partial F} i_X dM = \\int_{\\partial P} i_X dM.$$\nThis completes the proof. $\\square$",
    "5", "5.6")

# ===================================================================
# CONCEPT 7: Independence of 2-Form Integral from Decomposition (Proposition 5.6.11)
# ===================================================================
write_concept("integral-of-two-form-independence-decomposition", "proposition",
    "Integral of a 2-Form is Independent of Polygonal Decomposition",
    "geometry", "differential-geometry",
    "Let $M$ be a compact oriented surface. Suppose $\\Pi = \\{P_\\rho\\}$ and $\\Pi' = \\{P'_\\rho\\}$ are two polygonal decompositions of $M$. If $\\Omega$ is a 2-form on $M$, then\n$$\\sum_\\rho \\iint_{P_\\rho} \\Omega = \\sum_{\\rho'} \\iint_{P'_{\\rho'}} \\Omega.$$\nHence $\\iint_M \\Omega$ is well-defined independent of the choice of polygonal decomposition.",
    "This proposition ensures that the surface integral of a 2-form is well-defined for compact oriented surfaces. The proof uses the common refinement $\\{P_\\rho \\cap P'_{\\rho'}\\}$ of the two decompositions, over which both sums yield the same value.",
    "5", "5.6", "intermediate")

write_proof("integral-of-two-form-independence-decomposition",
    "**Proof.** Consider the common refinement $\\{P_\\rho \\cap P'_{\\rho'}\\}$, which is also a polygonal decomposition of $M$.\n\nFor the decomposition $\\Pi$, we have\n$$\\sum_\\rho \\iint_{P_\\rho} \\Omega = \\sum_\\rho \\sum_{\\rho'} \\iint_{P_\\rho \\cap P'_{\\rho'}} \\Omega,$$\nsince each $P_\\rho$ can be subdivided into the pieces $P_\\rho \\cap P'_{\\rho'}$ and the integral is additive over such subdivisions.\n\nSimilarly, for the decomposition $\\Pi'$:\n$$\\sum_{\\rho'} \\iint_{P'_{\\rho'}} \\Omega = \\sum_{\\rho'} \\sum_\\rho \\iint_{P_\\rho \\cap P'_{\\rho'}} \\Omega.$$\n\nBoth sums equal $\\sum_{\\rho,\\rho'} \\iint_{P_\\rho \\cap P'_{\\rho'}} \\Omega$, hence they are equal to each other. $\\square$",
    "5", "5.6")

# ===================================================================
# CONCEPT 8: Gauss Theorem for Compact Surfaces (Theorem 5.6.12)
# ===================================================================
write_concept("gauss-theorem-compact-surface", "theorem",
    "Gauss's Theorem for Compact Surfaces",
    "geometry", "differential-geometry",
    "Let $M$ be a compact surface with a Riemannian metric. Then for any vector field $X$ on $M$,\n$$\\iint_M (\\operatorname{div} X) \\, dM = 0.$$",
    "On a compact surface without boundary, the total divergence of any vector field vanishes — there is no net flux. This is the surface analog of the divergence theorem on a closed manifold and an essential tool for global results: it implies that the integral of the Laplacian of a function is zero, which is used in proving the Gauss-Bonnet theorem and Hodge decomposition.",
    "5", "5.6", "advanced")

write_proof("gauss-theorem-compact-surface",
    "**Proof.** Write the integral over $M$ in terms of some polygonal decomposition $\\Pi$ of $M$:\n$$\\iint_M (\\operatorname{div} X) dM = \\sum_\\rho \\iint_{P_\\rho} (\\operatorname{div} X) dM.$$\n\nApply Gauss's theorem (5.6.9) to each polygon $P_\\rho$:\n$$\\sum_\\rho \\iint_{P_\\rho} (\\operatorname{div} X) dM = \\sum_\\rho \\int_{\\partial P_\\rho} i_X dM.$$\n\nIn the sum over all polygons, each interior edge appears as a boundary curve on exactly two adjacent polygons, but with opposite orientations. Therefore the corresponding line integrals cancel pairwise. The only remaining terms come from boundary edges, but since $M$ is a compact surface without boundary (in the manifold sense), there are no such edges. Hence the total sum is zero. $\\square$",
    "5", "5.6")

# ===================================================================
# CONCEPT 9: Gradient Vector Field (Definition 5.7.1)
# ===================================================================
write_concept("gradient-vector-field-riemannian", "definition",
    "Gradient Vector Field on a Riemannian Manifold",
    "geometry", "differential-geometry",
    "Let $M$ be a Riemannian manifold and $\\psi: M \\to \\mathbb{R}$ a differentiable function. The **gradient** of $\\psi$ is the vector field\n$$\\operatorname{grad} \\psi(p) := Lg_p^{-1}(d\\psi_p),$$\nwhere $Lg_p: T_pM \\to T_p^*M$ is the metric isomorphism $X \\mapsto g_p(X, \\cdot)$. Equivalently, $\\operatorname{grad} \\psi$ is the unique vector field satisfying\n$$g(\\operatorname{grad} \\psi, X) = d\\psi(X)$$\nfor all vector fields $X$ on $M$.",
    "The gradient generalizes the Euclidean gradient to curved spaces. It points in the direction of steepest ascent of $\\psi$ and its length is the maximal directional derivative. In coordinates, $(\\operatorname{grad} \\psi)^i = \\sum_j g^{ij} \\partial_j \\psi$. The gradient is essential for defining the Laplace-Beltrami operator via $\\Delta\\psi = \\operatorname{div} \\operatorname{grad} \\psi$.",
    "5", "5.7", "intermediate")

# ===================================================================
# CONCEPT 10: Green's Formulae (Theorem 5.7.2)
# ===================================================================
write_concept("greens-formulae-riemannian", "theorem",
    "Green's Formulae on a Riemannian Surface",
    "geometry", "differential-geometry",
    "Let $M$ be an oriented Riemannian surface and $P \\subset M$ a polygon. For differentiable functions $\\psi_1, \\psi_2$ on $M$:\n\n**Green's first identity:**\n$$\\iint_P \\psi_1 \\Delta\\psi_2 + g(\\operatorname{grad} \\psi_1, \\operatorname{grad} \\psi_2) \\, dM = \\int_{\\partial P} \\psi_1 \\frac{\\partial\\psi_2}{\\partial n} \\, ds,$$\nwhere $\\partial\\psi_2/\\partial n = d\\psi_2(n)$ with $n$ the outward pointing normal to $\\partial P$.\n\n**Green's second identity:**\n$$\\iint_P (\\psi_1 \\Delta\\psi_2 - \\psi_2 \\Delta\\psi_1) \\, dM = \\int_{\\partial P} \\left(\\psi_1 \\frac{\\partial\\psi_2}{\\partial n} - \\psi_2 \\frac{\\partial\\psi_1}{\\partial n}\\right) ds.$$",
    "Green's formulae are the surface analogs of the classical Green's identities in $\\mathbb{R}^2$. They follow from Gauss's theorem applied to the vector fields $\\psi_1 \\operatorname{grad} \\psi_2$ and $\\psi_1 \\operatorname{grad} \\psi_2 - \\psi_2 \\operatorname{grad} \\psi_1$, using the product rule $\\operatorname{div}(\\psi X) = \\psi \\operatorname{div} X + d\\psi(X)$.",
    "5", "5.7", "intermediate")

write_proof("greens-formulae-riemannian",
    "**Proof.** First, establish the product rule for divergence:\n$$\\operatorname{div}(\\psi X) = \\frac{1}{\\sqrt{g}} \\sum_i \\frac{\\partial}{\\partial u^i}(\\sqrt{g} \\, \\psi \\xi^i) = \\psi \\frac{1}{\\sqrt{g}} \\sum_i \\frac{\\partial}{\\partial u^i}(\\sqrt{g} \\xi^i) + \\sum_i \\xi^i \\frac{\\partial \\psi}{\\partial u^i} = \\psi \\operatorname{div} X + d\\psi(X).$$\n\nIn particular, for $X = \\operatorname{grad} \\psi_2$:\n$$\\operatorname{div}(\\psi_1 \\operatorname{grad} \\psi_2) = \\psi_1 \\Delta\\psi_2 + d\\psi_1(\\operatorname{grad} \\psi_2) = \\psi_1 \\Delta\\psi_2 + g(\\operatorname{grad} \\psi_1, \\operatorname{grad} \\psi_2).$$\n\nApply Gauss's theorem (5.6.9) to the vector field $\\psi_1 \\operatorname{grad} \\psi_2$:\n$$\\iint_P \\operatorname{div}(\\psi_1 \\operatorname{grad} \\psi_2) \\, dM = \\int_{\\partial P} i_{\\psi_1 \\operatorname{grad} \\psi_2} dM.$$\n\nThe left side equals $\\iint_P \\psi_1 \\Delta\\psi_2 + g(\\operatorname{grad} \\psi_1, \\operatorname{grad} \\psi_2) \\, dM$.\n\nFor the right side, using the physical interpretation of the line integral from the remark after (5.6.9): on $\\partial P$, parameterized by arc length $c(t)$ with Frenet frame $\\{e_1 = \\dot{c}, e_2 = n\\}$ (where $n$ is the inward normal), we have $i_X dM(\\dot{c}) = -X \\cdot e_2$. Identifying the outward normal as $-e_2$, we obtain\n$$i_{\\psi_1 \\operatorname{grad} \\psi_2} dM(\\dot{c}) = \\psi_1 g(\\operatorname{grad} \\psi_2, n) = \\psi_1 d\\psi_2(n) = \\psi_1 \\frac{\\partial\\psi_2}{\\partial n}.$$\nThus the right side equals $\\int_{\\partial P} \\psi_1 \\frac{\\partial\\psi_2}{\\partial n} ds$, proving Green's first identity.\n\nGreen's second identity follows by subtracting the first identity with $\\psi_1$ and $\\psi_2$ swapped from the original. $\\square$",
    "5", "5.7")

# ===================================================================
# CONCEPT 11: Harmonic Function (Definition 5.7.3)
# ===================================================================
write_concept("harmonic-function-riemannian", "definition",
    "Harmonic Function on a Riemannian Manifold",
    "geometry", "differential-geometry",
    "A differentiable function $\\psi: M \\to \\mathbb{R}$ on a Riemannian manifold is called **harmonic** if\n$$\\Delta\\psi = 0,$$\nwhere $\\Delta$ is the Laplace-Beltrami operator. Locally, every point $p \\in M$ has a neighborhood on which there exists a harmonic function $\\psi$ with $d\\psi \\neq 0$.",
    "Harmonic functions are the solutions to Laplace's equation on a Riemannian manifold. They are the higher-dimensional generalization of holomorphic functions (the real and imaginary parts of a holomorphic function are harmonic). On a compact manifold, the only harmonic functions are constants by the maximum principle.",
    "5", "5.7", "intermediate")

# ===================================================================
# CONCEPT 12: Isothermal Coordinates (Definition 5.7.3)
# ===================================================================
write_concept("isothermal-coordinates-riemannian", "definition",
    "Isothermal Coordinates on a Riemannian Surface",
    "geometry", "differential-geometry",
    "**Isothermal coordinates** on a Riemannian surface are local coordinates $(u^1, u^2)$ in which the metric takes the conformally flat form\n$$ds^2 = \\lambda(u)((du^1)^2 + (du^2)^2),$$\nwhere $\\lambda(u) > 0$ is a positive function. A change of variables between two isothermal coordinate systems is a conformal mapping: if $\\phi: (v^1, v^2) \\mapsto (u^1, u^2)$ is such a change, then $u^1(v^1, v^2), u^2(v^1, v^2)$ satisfy the Cauchy-Riemann equations\n$$\\frac{\\partial u^1}{\\partial v^1} = \\frac{\\partial u^2}{\\partial v^2}, \\quad \\frac{\\partial u^1}{\\partial v^2} = -\\frac{\\partial u^2}{\\partial v^1}.$$",
    "Isothermal coordinates show that every Riemannian surface admits a complex structure, making it a Riemann surface. The transition maps between isothermal charts are holomorphic functions. This deep connection between Riemannian geometry and complex analysis is fundamental to the uniformization theorem for surfaces.",
    "5", "5.7", "advanced")

# ===================================================================
# CONCEPT 13: Mean Curvature via Laplacian (Proposition 5.7.4)
# ===================================================================
write_concept("mean-curvature-via-laplacian", "proposition",
    "Mean Curvature via the Laplace-Beltrami Operator",
    "geometry", "differential-geometry",
    "Let $f: U \\to \\mathbb{R}^3$ be a parameterized surface with coordinates $(x, y, z)$ in $\\mathbb{R}^3$. Consider $x \\circ f(u), y \\circ f(u), z \\circ f(u)$ as functions on the surface with the metric $(U, g) = (U, I)$ given by the first fundamental form. Then\n$$\\Delta f(u) := (\\Delta(x \\circ f(u)), \\Delta(y \\circ f(u)), \\Delta(z \\circ f(u))) = 2H(u) \\, n(u),$$\nwhere $H$ is the mean curvature and $n$ is the unit normal vector field.",
    "This remarkable formula expresses the Laplace-Beltrami operator applied to the position vector $f$ of an embedded surface: the result is $2H$ times the unit normal. It connects the intrinsic Laplacian with the extrinsic mean curvature. In particular, minimal surfaces ($H = 0$) are characterized by $\\Delta f = 0$ — the coordinate functions are harmonic.",
    "5", "5.7", "advanced")

# ===================================================================
# CONCEPT 14: Minimal Surface Laplacian Characterization (Corollary 5.7.4)
# ===================================================================
write_concept("minimal-surface-laplacian-characterization", "corollary",
    "Characterization of Minimal Surfaces via Harmonic Coordinates",
    "geometry", "differential-geometry",
    "Let $f: U \\to \\mathbb{R}^3$ be a parameterized surface. Then $f$ is a **minimal surface** ($H \\equiv 0$) if and only if each coordinate function $x \\circ f$, $y \\circ f$, $z \\circ f$ is harmonic with respect to the Laplace-Beltrami operator of the first fundamental form:\n$$\\Delta f = 0.$$",
    "A surface is minimal exactly when its position vector is harmonic. This provides a powerful analytic characterization of minimal surfaces: the coordinate functions (restricted to the surface) are harmonic functions on the Riemannian manifold $(U, I)$. This connects the geometric theory of minimal surfaces with the analytic theory of harmonic maps.",
    "5", "5.7", "advanced")

# ===================================================================
# EXERCISES from Section 5.7
# ===================================================================

# Exercise 5.7.2a: Product rule for divergence
write_exercise("greens-formulae-riemannian", "5.7.2a", "5", "5.7",
    "Prove the product rule for divergence:\n$$\\operatorname{div}(\\psi X) = \\psi \\operatorname{div} X + d\\psi(X).$$")

# Exercise 5.7.2b: Divergence of scalar times gradient
write_exercise("greens-formulae-riemannian", "5.7.2b", "5", "5.7",
    "Prove:\n$$\\operatorname{div}(\\psi_1 \\operatorname{grad} \\psi_2) = \\psi_1 \\Delta\\psi_2 + g(\\operatorname{grad} \\psi_1, \\operatorname{grad} \\psi_2).$$")

# Exercise 5.7.2c: Green's first identity via Gauss theorem
write_exercise("greens-formulae-riemannian", "5.7.2c", "5", "5.7",
    "Use Gauss's theorem (5.6.9) to show Green's first identity:\n$$\\iint_P \\psi_1 \\Delta\\psi_2 + g(\\operatorname{grad} \\psi_1, \\operatorname{grad} \\psi_2) \\, dM = \\int_{\\partial P} \\psi_1 \\frac{\\partial\\psi_2}{\\partial n} \\, ds,$$\nwhere $\\partial\\psi_2/\\partial n = d\\psi_2(n)$ and $n$ is the outward pointing normal to $\\partial P$.")

# Exercise 5.7.3a: Cauchy-Riemann from isothermal coordinates
write_exercise("isothermal-coordinates-riemannian", "5.7.3", "5", "5.7",
    "Suppose $\\phi: (v^1, v^2) \\mapsto (u^1, u^2)$ is a change of variables between isothermal coordinate systems (a conformal mapping). Prove that the functions $u^1(v^1, v^2)$ and $u^2(v^1, v^2)$ satisfy the Cauchy-Riemann equations:\n$$\\frac{\\partial u^1}{\\partial v^1} = \\frac{\\partial u^2}{\\partial v^2}, \\quad \\frac{\\partial u^1}{\\partial v^2} = -\\frac{\\partial u^2}{\\partial v^1}.$$\nConclude that $\\phi$ can be written as a holomorphic function between open sets in $\\mathbb{C}$.")

# Exercise 5.7.4a: Mean curvature via Laplacian
write_exercise("mean-curvature-via-laplacian", "5.7.4a", "5", "5.7",
    "Let $f: U \\to \\mathbb{R}^3$ be a parameterized surface. Show:\n$$\\Delta f(u) := (\\Delta(x \\circ f(u)), \\Delta(y \\circ f(u)), \\Delta(z \\circ f(u))) = 2H(u) \\, n(u),$$\nwhere $H$ is the mean curvature and $n$ is the unit normal vector field on the surface $f$.")

# Exercise 5.7.4b: Minimal surface characterization
write_exercise("minimal-surface-laplacian-characterization", "5.7.4b", "5", "5.7",
    "Conclude from $\\Delta f = 2H n$ that a surface $f$ is minimal (i.e., $H = 0$) if and only if its three coordinate functions are harmonic with respect to the Laplace-Beltrami operator of the first fundamental form.")

# ===================================================================
# Write .done for already-extracted concepts (proof/exercise only)
# ===================================================================

# integral-of-one-form: already has concept.yaml/theorem.tex/introduce.en.md from extract_all.py
# but we write them fresh here for completeness
write_concept("integral-of-one-form", "definition",
    "Integral of a 1-Form on a Curve",
    "geometry", "differential-geometry",
    "Let $\\omega$ be a 1-form on a manifold $M$ and $c: I \\to M$ a curve with $I$ compact. The **integral** of $\\omega$ along $c$ is\n$$\\int_c \\omega := \\int_I \\omega(\\dot{c}(t)) \\, dt.$$\nThis integral is invariant under orientation-preserving change of variables of the curve.",
    "The line integral of a 1-form generalizes the work integral from vector calculus. It is independent of (orientation-preserving) parametrization and serves as the fundamental building block for integration theory on manifolds. Together with the integral of 2-forms, it enables the formulation of Stokes' theorem on surfaces.",
    "5", "5.6", "intermediate")

# laplace-beltrami-operator (already extracted, but we still write for idx-31)
write_concept("laplace-beltrami-operator", "definition",
    "Laplace-Beltrami Operator on a Riemannian Manifold",
    "geometry", "differential-geometry",
    "Let $F(M)$ denote the algebra of differentiable functions on a Riemannian manifold $M$. The **Laplace-Beltrami operator** is the mapping $\\Delta: F(M) \\to F(M)$ defined by\n$$\\Delta\\psi := \\operatorname{div} \\operatorname{grad} \\psi.$$\nIn local coordinates on a surface:\n$$\\Delta\\psi = \\frac{1}{\\sqrt{\\det g}} \\sum_{i,j} \\frac{\\partial}{\\partial u^i}\\left(\\sqrt{\\det g} \\, g^{ij} \\frac{\\partial \\psi}{\\partial u^j}\\right).$$",
    "The Laplace-Beltrami operator is the intrinsic generalization of the Laplacian to curved spaces. It is self-adjoint, elliptic, and governs heat flow, wave propagation, and the spectrum of the manifold. It connects intrinsically to extrinsic geometry via the formula $\\Delta f = 2Hn$ for embedded surfaces.",
    "5", "5.7", "intermediate")

print("SUCCESS: All idx-31 concepts extracted.")
print(f"Output directory: {BASE}")
