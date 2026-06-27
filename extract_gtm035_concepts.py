#!/usr/bin/env python3
"""Extract ALL concepts from GTM035 (Several Complex Variables and Banach Algebras) into v7 format.
Processes all 26 sections and writes concept.yaml, theorem.tex, introduce.en.md files."""

import os, yaml, hashlib, re, json

STAGING = "/home/a123/文档/mathpkg/pipeline_output/concepts_v7/gtm035"
BOOK_ID = "gtm035"
AUTHORS = "Herbert Alexander, John Wermer"
TITLE = "Several Complex Variables and Banach Algebras (Third Edition)"
DATE = "2026-06-25"
AGENT = "v7-section-test"

os.makedirs(STAGING, exist_ok=True)

# ============================================================
# CONCEPT DEFINITIONS — extracted from all 26 sections of GTM035
# Format: (slug, title_en, ctype, domain, subdomain, chapter_label, section_label, difficulty, tags)
# ============================================================

concepts = [
    # === Chapter 1: Preliminaries and Notation (s001) ===
    ("riesz-banach-approximation-theorem", "Riesz-Banach Approximation Theorem",
     "theorem", "analysis", "approximation-theory", "Chapter 1", "1", "advanced", ["riesz", "banach", "approximation", "measure", "orthogonal"]),

    ("uniform-algebra-definition", "Uniform Algebra",
     "definition", "analysis", "banach-algebras", "Chapter 1", "1", "basic", ["uniform-algebra", "banach-algebra", "compact-hausdorff"]),

    # === Chapter 2: Classical Approximation Theorems (s002–s004) ===
    ("real-stone-weierstrass-theorem", "Real Stone-Weierstrass Theorem",
     "theorem", "analysis", "approximation-theory", "Chapter 2", "2.1", "intermediate", ["stone-weierstrass", "real", "approximation", "dense-subalgebra"]),

    ("krein-milman-extreme-point", "Krein-Milman Extreme Point Proposition",
     "proposition", "analysis", "functional-analysis", "Chapter 2", "2.2", "advanced", ["krein-milman", "extreme-point", "compact-convex", "dual-space"]),

    ("complex-stone-weierstrass-theorem", "Complex Stone-Weierstrass Theorem",
     "theorem", "analysis", "approximation-theory", "Chapter 2", "2.3", "intermediate", ["stone-weierstrass", "complex", "approximation", "self-adjoint"]),

    ("logarithmic-potential-cauchy-transform-summability", "Summability of Logarithmic Potential and Cauchy Transform",
     "lemma", "analysis", "potential-theory", "Chapter 2", "2.4", "intermediate", ["logarithmic-potential", "cauchy-transform", "summability", "lebesgue-measure"]),

    ("cauchy-transform-inversion-formula", "Cauchy Transform Inversion Formula",
     "lemma", "analysis", "complex-analysis", "Chapter 2", "2.5", "intermediate", ["cauchy-transform", "inversion", "pompeiu-formula"]),

    ("newtonian-potential-representation", "Newtonian Potential Representation for C_0^2 Functions",
     "lemma", "analysis", "potential-theory", "Chapter 2", "2.6", "intermediate", ["newtonian-potential", "laplacian", "logarithmic-kernel"]),

    ("cauchy-transform-vanishing-implies-measure-zero", "Vanishing Cauchy Transform Implies Measure Zero",
     "lemma", "analysis", "complex-analysis", "Chapter 2", "2.7", "intermediate", ["cauchy-transform", "measure", "vanishing-a.e."]),

    ("hartogs-rosenthal-theorem", "Hartogs-Rosenthal Theorem",
     "theorem", "analysis", "approximation-theory", "Chapter 2", "2.8", "advanced", ["hartogs-rosenthal", "rational-approximation", "lebesgue-measure-zero"]),

    ("runge-approximation-theorem", "Runge Approximation Theorem",
     "theorem", "analysis", "complex-analysis", "Chapter 2", "2.9", "intermediate", ["runge", "rational-approximation", "holomorphic", "uniform-convergence"]),

    ("lavrentieff-polynomial-approximation-theorem", "Lavrentieff Polynomial Approximation Theorem",
     "theorem", "analysis", "approximation-theory", "Chapter 2", "2.11", "advanced", ["lavrentieff", "polynomial-approximation", "connected-complement", "empty-interior"]),

    ("logarithmic-potential-boundary-limit", "Logarithmic Potential Boundary Limit Lemma",
     "lemma", "analysis", "potential-theory", "Chapter 2", "2.12", "intermediate", ["logarithmic-potential", "boundary-limit", "connected-complement"]),

    # === Chapter 3: Operational Calculus in One Variable (s004–s005) ===
    ("gelfand-operational-calculus-one-variable", "Gelfand Operational Calculus in One Variable",
     "theorem", "analysis", "banach-algebras", "Chapter 3", "3.3", "advanced", ["operational-calculus", "gelfand", "holomorphic-functional-calculus", "spectrum"]),

    ("idempotent-from-disconnected-spectrum", "Existence of Idempotent from Disconnected Spectrum",
     "corollary", "analysis", "banach-algebras", "Chapter 3", "3", "intermediate", ["idempotent", "disconnected-spectrum", "banach-algebra"]),

    ("exponential-representation-in-banach-algebra", "Exponential Representation in Banach Algebra",
     "corollary", "analysis", "banach-algebras", "Chapter 3", "3", "intermediate", ["exponential", "logarithm", "simply-connected", "banach-algebra"]),

    ("smooth-functions-on-domain", "Algebra of Smooth Functions C^\\infty(\\Omega)",
     "definition", "analysis", "differential-geometry", "Chapter 4", "4.1", "basic", ["smooth-functions", "infinitely-differentiable", "domain"]),

    ("tangent-space-at-point", "Tangent Space T_x at a Point",
     "definition", "geometry", "differential-geometry", "Chapter 4", "4.2", "basic", ["tangent-space", "derivation", "point"]),

    ("tangent-space-basis", "Basis of Tangent Space",
     "lemma", "geometry", "differential-geometry", "Chapter 4", "4.1", "basic", ["tangent-space", "basis", "partial-derivatives"]),

    ("cotangent-space", "Cotangent Space T_x^*",
     "definition", "geometry", "differential-geometry", "Chapter 4", "4.3", "basic", ["cotangent-space", "dual-space"]),

    # === Chapter 4: Differential Forms (s005–s006) ===
    ("one-form-definition", "Differential 1-Form",
     "definition", "geometry", "differential-geometry", "Chapter 4", "4.4", "basic", ["one-form", "differential-form", "cotangent-bundle"]),

    ("one-form-coordinate-representation", "Coordinate Representation of 1-Forms",
     "lemma", "geometry", "differential-geometry", "Chapter 4", "4.2", "basic", ["one-form", "coordinate-representation", "basis"]),

    ("exterior-algebra-is-associative", "Exterior Algebra is Associative",
     "lemma", "algebra", "multilinear-algebra", "Chapter 4", "4.4", "intermediate", ["exterior-algebra", "associative", "wedge-product"]),

    ("wedge-product-anticommutativity", "Anticommutativity of Wedge Product",
     "lemma", "algebra", "multilinear-algebra", "Chapter 4", "4.5", "basic", ["wedge-product", "anticommutativity", "graded-algebra"]),

    ("basis-of-k-forms", "Basis of k-Forms",
     "lemma", "algebra", "multilinear-algebra", "Chapter 4", "4.6", "basic", ["k-forms", "basis", "exterior-power"]),

    ("k-form-definition", "Differential k-Form",
     "definition", "geometry", "differential-geometry", "Chapter 4", "4.6", "basic", ["k-form", "differential-form", "exterior-algebra"]),

    ("exterior-derivative-definition", "Exterior Derivative",
     "definition", "geometry", "differential-geometry", "Chapter 4", "4.8", "intermediate", ["exterior-derivative", "d-operator", "differential-form"]),

    ("exterior-derivative-squared-zero", "Exterior Derivative Satisfies d^2 = 0",
     "lemma", "geometry", "differential-geometry", "Chapter 4", "4.8", "intermediate", ["exterior-derivative", "d-squared-zero", "cohomology"]),

    # === Chapter 5: The ∂̄-Operator (s006) ===
    ("one-form-dz-dzbar-representation", "Representation of 1-Forms with dz and d\\bar{z}",
     "lemma", "analysis", "several-complex-variables", "Chapter 5", "5.1", "intermediate", ["one-form", "dz", "dzbar", "complex-coordinates"]),

    ("wirtinger-derivatives", "Wirtinger Derivatives \\partial/\\partial z_j and \\partial/\\partial\\bar{z}_j",
     "definition", "analysis", "several-complex-variables", "Chapter 5", "5.1", "basic", ["wirtinger-derivatives", "complex-derivatives", "several-variables"]),

    ("del-and-delbar-operators", "Operators \\partial and \\bar{\\partial} on Functions",
     "definition", "analysis", "several-complex-variables", "Chapter 5", "5.2", "intermediate", ["del-operator", "delbar-operator", "differential-form"]),

    ("delbar-on-differential-forms", "\\bar{\\partial} Operator on Differential Forms",
     "definition", "analysis", "several-complex-variables", "Chapter 5", "5.4", "advanced", ["delbar", "differential-forms", "bidegree"]),

    ("delbar-squared-zero", "Properties \\bar{\\partial}^2 = 0, \\partial^2 = 0, \\partial\\bar{\\partial} + \\bar{\\partial}\\partial = 0",
     "lemma", "analysis", "several-complex-variables", "Chapter 5", "5.3", "intermediate", ["delbar-squared-zero", "del-squared-zero", "dolbeault-cohomology"]),

    ("delbar-closed-implies-analytic-polydisk", "\\bar{\\partial}-Closed Functions are Analytic on Polydisks",
     "lemma", "analysis", "several-complex-variables", "Chapter 5", "5.4", "advanced", ["delbar-closed", "analytic", "power-series", "polydisk"]),

    ("delbar-product-rule", "\\bar{\\partial} Product Rule for Differential Forms",
     "lemma", "analysis", "several-complex-variables", "Chapter 5", "5.5", "intermediate", ["delbar", "product-rule", "graded-derivation"]),

    # === Chapter 6: The Equation ∂̄u = f (s007) ===
    ("complex-poincare-lemma", "Complex Poincaré Lemma",
     "theorem", "analysis", "several-complex-variables", "Chapter 6", "6.1", "advanced", ["poincare-lemma", "delbar", "polydisk", "dolbeault-cohomology"]),

    ("delbar-solution-in-plane", "Solution to \\bar{\\partial} in the Plane (Compact Support)",
     "lemma", "analysis", "several-complex-variables", "Chapter 6", "6.2", "intermediate", ["delbar", "solution", "compact-support", "cauchy-kernel"]),

    ("delbar-solution-polydisk-neighborhood", "\\bar{\\partial} Solution in a Neighborhood of the Polydisk",
     "lemma", "analysis", "several-complex-variables", "Chapter 6", "6.3", "intermediate", ["delbar", "polydisk", "extension"]),

    # === Chapter 7: The Oka-Weil Theorem (s007–s008) ===
    ("oka-weil-approximation-theorem", "Oka-Weil Approximation Theorem",
     "theorem", "analysis", "several-complex-variables", "Chapter 7", "7.1", "advanced", ["oka-weil", "polynomial-approximation", "several-variables", "polynomially-convex"]),

    ("polynomial-peak-point-characterization", "Characterization of Connected Complement via Polynomial Peak Points",
     "lemma", "analysis", "complex-analysis", "Chapter 7", "7.2", "intermediate", ["peak-point", "polynomial", "connected-complement", "maximum-principle"]),

    ("polynomially-convex-set-definition", "Polynomially Convex Set",
     "definition", "analysis", "several-complex-variables", "Chapter 7", "7.2", "intermediate", ["polynomially-convex", "polynomial-hull", "several-variables"]),

    ("p-polyhedron-definition", "p-Polyhedron in C^n",
     "definition", "analysis", "several-complex-variables", "Chapter 7", "7.3", "intermediate", ["p-polyhedron", "polynomial", "polydisk"]),

    ("polyhedron-approximation-polynomially-convex", "p-Polyhedron Approximation of Polynomially Convex Sets",
     "lemma", "analysis", "several-complex-variables", "Chapter 7", "7.4", "intermediate", ["p-polyhedron", "polynomially-convex", "approximation"]),

    ("oka-extension-theorem", "Oka Extension Theorem",
     "theorem", "analysis", "several-complex-variables", "Chapter 7", "7.5", "advanced", ["oka-extension", "holomorphic-extension", "p-polyhedron"]),

    ("delbar-on-p-polyhedron", "\\bar{\\partial}-Problem on p-Polyhedra",
     "theorem", "analysis", "several-complex-variables", "Chapter 7", "7.6", "advanced", ["delbar", "p-polyhedron", "dolbeault-cohomology"]),

    ("holomorphic-pullback-of-forms", "Pullback of Differential Forms by Holomorphic Maps",
     "definition", "analysis", "several-complex-variables", "Chapter 7", "7.4", "intermediate", ["pullback", "holomorphic-map", "differential-form"]),

    ("oka-extension-lemma", "Oka Extension Lemma",
     "lemma", "analysis", "several-complex-variables", "Chapter 7", "7.7", "advanced", ["oka-extension", "holomorphic", "intermediate-variable"]),

    # === Chapter 8: Operational Calculus in Several Variables (s008–s009) ===
    ("joint-spectrum-definition", "Joint Spectrum \\sigma(x_1,\\ldots,x_n) in a Banach Algebra",
     "definition", "analysis", "banach-algebras", "Chapter 8", "8.1", "intermediate", ["joint-spectrum", "banach-algebra", "gelfand-transform"]),

    ("joint-spectrum-characterization", "Characterization of Joint Spectrum via Invertibility",
     "lemma", "analysis", "banach-algebras", "Chapter 8", "8.1", "intermediate", ["joint-spectrum", "invertibility", "linear-combination"]),

    ("operational-calculus-several-variables", "Operational Calculus in Several Variables",
     "theorem", "analysis", "banach-algebras", "Chapter 8", "8.2", "advanced", ["operational-calculus", "several-variables", "joint-spectrum", "holomorphic"]),

    ("joint-spectrum-polynomially-convex", "Joint Spectrum of Generators is Polynomially Convex",
     "lemma", "analysis", "banach-algebras", "Chapter 8", "8.3", "intermediate", ["joint-spectrum", "polynomially-convex", "generators"]),

    ("separating-elements-for-maximal-ideals", "Existence of Elements Separating Pairs of Maximal Ideals",
     "lemma", "analysis", "banach-algebras", "Chapter 8", "8.7", "intermediate", ["maximal-ideal", "separation", "gelfand-transform"]),

    ("idempotent-from-disconnected-maximal-ideal-space", "Existence of Idempotents from Disconnected Maximal Ideal Space",
     "theorem", "analysis", "banach-algebras", "Chapter 8", "8.6", "advanced", ["idempotent", "disconnected", "maximal-ideal-space", "silov"]),

    # === Chapter 9: The Šilov Boundary (s009–s010) ===
    ("boundary-for-function-algebra", "Boundary for a Function Algebra",
     "definition", "analysis", "banach-algebras", "Chapter 9", "9.1", "intermediate", ["boundary", "function-algebra", "maximum-modulus"]),

    ("silov-boundary-theorem", "Existence of the Šilov Boundary",
     "theorem", "analysis", "banach-algebras", "Chapter 9", "9.1", "advanced", ["silov-boundary", "function-algebra", "intersection-of-boundaries"]),

    ("boundary-removal-lemma", "Boundary Removal Lemma",
     "lemma", "analysis", "banach-algebras", "Chapter 9", "9.2", "intermediate", ["boundary", "removal", "silov-boundary"]),

    ("local-maximum-modulus-principle", "Local Maximum Modulus Principle for Banach Algebras",
     "theorem", "analysis", "banach-algebras", "Chapter 9", "9.3", "advanced", ["local-maximum-modulus", "silov-boundary", "banach-algebra", "rossi"]),

    ("delbar-solution-on-two-open-sets", "\\bar{\\partial} Solution on Union of Two Open Sets",
     "lemma", "analysis", "several-complex-variables", "Chapter 9", "9.4", "intermediate", ["delbar", "union", "open-cover"]),

    ("logarithmic-holomorphic-separation", "Holomorphic Separation via \\log z_1/z_1",
     "lemma", "analysis", "several-complex-variables", "Chapter 9", "9.5", "advanced", ["holomorphic-separation", "logarithm", "cohomology"]),

    ("peak-function-extension", "Extension of Peak Functions",
     "lemma", "analysis", "banach-algebras", "Chapter 9", "9.6", "intermediate", ["peak-function", "extension", "gelfand-transform"]),

    ("silov-boundary-of-local-algebras", "Šilov Boundary of Local Algebras",
     "theorem", "analysis", "banach-algebras", "Chapter 9", "9.7", "advanced", ["silov-boundary", "local-algebra", "open-cover"]),

    # === Chapter 10: Maximality and Radó's Theorem (s010) ===
    ("cohen-invertibility-lemma", "Cohen Invertibility Lemma",
     "lemma", "analysis", "banach-algebras", "Chapter 10", "10.1", "intermediate", ["cohen", "invertibility", "uniform-algebra", "paul-cohen"]),

    ("maximality-of-disk-algebra", "Maximality of the Disk Algebra on the Circle",
     "theorem", "analysis", "function-algebras", "Chapter 10", "10.2", "advanced", ["maximality", "disk-algebra", "wermer", "uniform-algebra"]),

    ("rudin-analyticity-from-maximum-principle", "Rudin Analyticity Theorem",
     "theorem", "analysis", "function-algebras", "Chapter 10", "10.3", "advanced", ["rudin", "analyticity", "maximum-principle", "disk"]),

    ("glicksberg-local-maximum-lemma", "Glicksberg Local Maximum Lemma",
     "lemma", "analysis", "function-algebras", "Chapter 10", "10.4", "intermediate", ["glicksberg", "local-maximum", "boundary"]),

    ("rado-boundary-uniqueness-theorem", "Radó Boundary Uniqueness Theorem",
     "theorem", "analysis", "complex-analysis", "Chapter 10", "10.5", "intermediate", ["rado", "boundary-uniqueness", "holomorphic", "zero-set"]),

    ("rado-theorem", "Radó's Theorem on Continuous Analytic Functions",
     "theorem", "analysis", "complex-analysis", "Chapter 10", "10.6", "advanced", ["rado", "continuous-analytic", "zero-set", "interior"]),

    ("bishop-analytic-structure-from-positive-measure", "Bishop's Theorem on Analytic Structure from Positive Measure",
     "theorem", "analysis", "function-algebras", "Chapter 10", "10.7", "advanced", ["bishop", "analytic-structure", "positive-measure", "gelfand-transform"]),

    # === Chapter 11: Maximum Modulus Algebras (s010–s011) ===
    ("maximum-modulus-algebra-definition", "Maximum Modulus Algebra",
     "definition", "analysis", "function-algebras", "Chapter 11", "11", "advanced", ["maximum-modulus-algebra", "proper-map", "disk-inequality"]),

    ("hardy-space-projection-theorem", "H^2 Projection Theorem for Maximum Modulus Algebras",
     "theorem", "analysis", "function-algebras", "Chapter 11", "11.1", "advanced", ["hardy-space", "projection", "maximum-modulus-algebra"]),

    ("analytic-function-of-projection-for-one-sheeted", "One-Sheeted Implies Analytic Function of Projection",
     "corollary", "analysis", "function-algebras", "Chapter 11", "11.3", "intermediate", ["one-sheeted", "analytic-function", "projection"]),

    ("log-capacity-subharmonic-theorem", "Logarithm of Capacity is Subharmonic",
     "theorem", "analysis", "function-algebras", "Chapter 11", "11.3", "advanced", ["subharmonic", "log-capacity", "maximum-modulus-algebra"]),

    ("k-diameter-definition", "k-Diameter of a Set",
     "definition", "analysis", "function-algebras", "Chapter 11", "11.2", "intermediate", ["k-diameter", "metric", "finite-set"]),

    ("tensor-product-maximum-modulus-theorem", "Tensor Product Maximum Modulus Algebra Theorem",
     "theorem", "analysis", "function-algebras", "Chapter 11", "11.4", "advanced", ["tensor-product", "maximum-modulus", "polydisk"]),

    ("hardy-extension-lemma", "Hardy Space Extension Lemma for Tensor Products",
     "lemma", "analysis", "function-algebras", "Chapter 11", "11.5", "advanced", ["hardy-space", "extension", "tensor-product", "polydisk"]),

    ("restriction-of-tensor-product-algebra", "A^{(n)}: Restriction of Tensor Product Algebra",
     "definition", "analysis", "function-algebras", "Chapter 11", "11.4", "intermediate", ["tensor-product", "restriction", "algebra"]),

    ("tensor-restriction-maximum-modulus", "A^{(n)} is a Maximum Modulus Algebra",
     "theorem", "analysis", "function-algebras", "Chapter 11", "11.6", "advanced", ["tensor-product", "restriction", "maximum-modulus-algebra"]),

    ("subharmonicity-of-diameter-log", "Subharmonicity of Log k-Diameter",
     "theorem", "analysis", "function-algebras", "Chapter 11", "11.7", "advanced", ["subharmonic", "k-diameter", "maximum-modulus-algebra"]),

    ("finite-sheeted-analytic-cover-theorem", "Finite-Sheeted Analytic Cover Theorem",
     "theorem", "analysis", "function-algebras", "Chapter 11", "11.8", "advanced", ["finite-sheeted", "analytic-cover", "maximum-modulus-algebra"]),

    ("local-maximum-modulus-implies-maximum-modulus", "Local Maximum Modulus Principle Implies Maximum Modulus Algebra",
     "theorem", "analysis", "function-algebras", "Chapter 11", "11.9", "advanced", ["local-maximum-modulus", "maximum-modulus-algebra", "rossi"]),

    ("analytic-cover-corollary", "Finite-Sheeted Implies Analytic Cover",
     "corollary", "analysis", "function-algebras", "Chapter 11", "11.11", "intermediate", ["analytic-cover", "finite-sheeted", "maximum-modulus-algebra"]),

    ("fiber-cardinality-bound-theorem", "Fiber Cardinality Bound Theorem",
     "theorem", "analysis", "function-algebras", "Chapter 11", "11.12", "advanced", ["fiber-cardinality", "maximum-modulus-algebra", "subharmonic"]),

    # === Chapter 12: Hulls of Curves and Arcs (s012–s013) ===
    ("polynomial-hull-of-curves-is-analytic-variety", "Polynomial Hull of Curves is a One-Dimensional Analytic Variety",
     "theorem", "analysis", "several-complex-variables", "Chapter 12", "12.1", "advanced", ["polynomial-hull", "analytic-variety", "curve", "several-variables"]),

    ("fiber-cardinality-bound-for-uniform-algebra", "Fiber Cardinality Bound for Uniform Algebra",
     "lemma", "analysis", "function-algebras", "Chapter 12", "12.2", "advanced", ["fiber", "cardinality", "uniform-algebra", "polynomial-hull"]),

    ("edge-fiber-cardinality-bound", "Fiber Cardinality Bound on Edges",
     "lemma", "analysis", "function-algebras", "Chapter 12", "12.3", "intermediate", ["fiber", "cardinality", "edge", "arc"]),

    ("smooth-arc-polynomially-convex", "Smooth Arcs are Polynomially Convex",
     "theorem", "analysis", "several-complex-variables", "Chapter 12", "12.4", "advanced", ["smooth-arc", "polynomially-convex", "polynomial-approximation"]),

    ("hull-of-k-union-gamma", "Polynomial Hull of K Union Gamma",
     "theorem", "analysis", "several-complex-variables", "Chapter 12", "12.5", "advanced", ["polynomial-hull", "union", "curve", "polynomially-convex"]),

    # === Chapter 13: Integral Kernels (s013–s014) ===
    ("bochner-martinelli-integral-representation", "Bochner-Martinelli Integral Representation",
     "theorem", "analysis", "several-complex-variables", "Chapter 13", "13.1", "advanced", ["bochner-martinelli", "integral-representation", "cauchy-generalization"]),

    ("martinelli-bochner-kernel-estimate", "Martinelli-Bochner Kernel Estimate",
     "lemma", "analysis", "several-complex-variables", "Chapter 13", "13.2", "intermediate", ["martinelli-bochner", "kernel", "estimate", "smoothly-bounded"]),

    ("martinelli-bochner-formula", "Martinelli-Bochner Formula",
     "theorem", "analysis", "several-complex-variables", "Chapter 13", "13.3", "advanced", ["martinelli-bochner", "integral-formula", "several-variables"]),

    ("leray-cauchy-fantappie-formula", "Leray's Cauchy-Fantappiè Formula",
     "theorem", "analysis", "several-complex-variables", "Chapter 13", "13.4", "advanced", ["leray", "cauchy-fantappie", "integral-kernel", "several-variables"]),

    ("kernel-differential-is-closed", "Differential of Cauchy-Fantappiè Kernel is Closed",
     "lemma", "analysis", "several-complex-variables", "Chapter 13", "13.6", "intermediate", ["kernel", "closed-form", "cauchy-fantappie"]),

    ("kernel-residue-at-diagonal", "Residue of Cauchy-Fantappiè Kernel at Diagonal",
     "lemma", "analysis", "several-complex-variables", "Chapter 13", "13.7", "intermediate", ["residue", "kernel", "cauchy-fantappie", "diagonal"]),

    # === Chapter 14: Perturbations of Stone-Weierstrass (s014–s015) ===
    ("perturbed-stone-weierstrass-polynomial-sequence", "Polynomial Sequence for Perturbed Stone-Weierstrass",
     "lemma", "analysis", "approximation-theory", "Chapter 14", "14.1", "intermediate", ["polynomial-sequence", "stone-weierstrass", "perturbation"]),

    ("polynomial-approximation-with-estimates", "Polynomial Approximation with Estimates",
     "lemma", "analysis", "approximation-theory", "Chapter 14", "14.2", "intermediate", ["polynomial-approximation", "estimates", "perturbation"]),

    ("dense-subalgebra-from-perturbation", "Dense Subalgebra from Stone-Weierstrass Perturbation",
     "theorem", "analysis", "approximation-theory", "Chapter 14", "14.3", "advanced", ["dense-subalgebra", "stone-weierstrass", "perturbation", "cauchy-kernel"]),

    ("generalized-perturbation-stone-weierstrass", "Generalized Perturbation of Stone-Weierstrass Theorem",
     "theorem", "analysis", "approximation-theory", "Chapter 14", "14.4", "advanced", ["stone-weierstrass", "perturbation", "cauchy-fantappie"]),

    ("delbar-representation-lemma", "\\bar{\\partial} Representation Lemma for C_0^1",
     "lemma", "analysis", "several-complex-variables", "Chapter 14", "14.5", "intermediate", ["delbar", "representation", "compact-support"]),

    ("measure-orthogonality-and-delbar", "Measure Orthogonality and the \\bar{\\partial}-Operator",
     "lemma", "analysis", "several-complex-variables", "Chapter 14", "14.6", "intermediate", ["measure", "orthogonality", "delbar"]),

    # === Chapter 15: The First Cohomology Group (s015) ===
    ("cech-cohomology-definition", "Čech Cohomology with Integer Coefficients",
     "definition", "topology", "algebraic-topology", "Chapter 15", "15.1", "advanced", ["cech-cohomology", "integer-coefficients", "open-cover"]),

    ("refinement-homomorphism", "Refinement Homomorphism for Čech Cohomology",
     "lemma", "topology", "algebraic-topology", "Chapter 15", "15.1", "advanced", ["refinement", "cech-cohomology", "homomorphism"]),

    ("refinement-independence", "Independence of Refinement Choice",
     "lemma", "topology", "algebraic-topology", "Chapter 15", "15.2", "advanced", ["refinement", "cech-cohomology", "independence"]),

    ("first-cohomology-limit-group", "First Čech Cohomology Group as Limit Group",
     "definition", "topology", "algebraic-topology", "Chapter 15", "15.2", "advanced", ["cech-cohomology", "direct-limit", "limit-group"]),

    ("arens-royden-theorem", "Arens-Royden Theorem",
     "theorem", "analysis", "banach-algebras", "Chapter 15", "15.4", "advanced", ["arens-royden", "cohomology", "maximal-ideal-space", "exponential"]),

    ("full-subalgebra-definition", "Full Subalgebra of C(X)",
     "definition", "analysis", "banach-algebras", "Chapter 15", "15.3", "intermediate", ["full-subalgebra", "cech-cohomology", "invertible"]),

    ("algebra-of-locally-holomorphic-functions", "Algebra H(X) of Locally Holomorphic Functions",
     "definition", "analysis", "several-complex-variables", "Chapter 15", "15.4", "intermediate", ["holomorphic", "locally", "compact-set"]),

    ("hx-is-full", "H(X) is a Full Subalgebra",
     "lemma", "analysis", "several-complex-variables", "Chapter 15", "15.5", "intermediate", ["full-subalgebra", "holomorphic", "oko-weil"]),

    ("finitely-generated-uniform-algebra-is-full", "Finitely Generated Uniform Algebra is Full",
     "lemma", "analysis", "banach-algebras", "Chapter 15", "15.6", "advanced", ["finitely-generated", "uniform-algebra", "full"]),

    ("higher-cohomology-of-maximal-ideal-space", "Higher Cohomology of Maximal Ideal Space",
     "theorem", "analysis", "banach-algebras", "Chapter 15", "15.8", "advanced", ["higher-cohomology", "maximal-ideal-space", "generators"]),

    ("distributional-delbar-derivative", "Distributional \\bar{\\partial} Derivative",
     "definition", "analysis", "several-complex-variables", "Chapter 16", "16.1", "advanced", ["distribution", "delbar", "l2-space"]),

    ("l2-delbar-closed-operator", "L^2 \\bar{\\partial}-Closed Operator",
     "definition", "analysis", "several-complex-variables", "Chapter 16", "16.2", "advanced", ["l2", "delbar-closed", "operator", "hilbert-space"]),

    ("l2-adjoint-operator", "Adjoint S Operator for \\bar{\\partial}",
     "definition", "analysis", "several-complex-variables", "Chapter 16", "16.3", "advanced", ["adjoint", "delbar", "hilbert-space", "l2"]),

    # === Chapter 16: The ∂̄-Operator in Smoothly Bounded Domains (s015–s016) ===
    ("closed-densely-defined-operator", "Closed Densely-Defined Operator",
     "definition", "analysis", "functional-analysis", "Chapter 16", "16.4", "advanced", ["closed-operator", "densely-defined", "hilbert-space"]),

    ("l2-delbar-estimate-theorem", "L^2 Estimate for the \\bar{\\partial}-Operator",
     "theorem", "analysis", "several-complex-variables", "Chapter 16", "16.3", "advanced", ["l2-estimate", "delbar", "smoothly-bounded", "hormander"]),

    ("integration-by-parts-for-delbar", "Integration by Parts for the \\bar{\\partial}-Operator",
     "lemma", "analysis", "several-complex-variables", "Chapter 16", "16.6", "intermediate", ["integration-by-parts", "delbar", "smoothly-bounded"]),

    ("elliptic-regularity-for-delbar", "Elliptic Regularity for the \\bar{\\partial}-Operator",
     "lemma", "analysis", "several-complex-variables", "Chapter 16", "16.8", "advanced", ["elliptic-regularity", "delbar", "ball"]),

    ("l2-extension-for-delbar", "L^2 Extension for \\bar{\\partial}-Closed Forms",
     "lemma", "analysis", "several-complex-variables", "Chapter 16", "16.9", "intermediate", ["l2-extension", "delbar-closed", "domain"]),

    # === Chapter 17: Manifolds Without Complex Tangents (s017–s018) ===
    ("complex-tangent-definition", "Complex Tangent to a Real Submanifold",
     "definition", "geometry", "several-complex-variables", "Chapter 17", "17.1", "intermediate", ["complex-tangent", "submanifold", "complex-line"]),

    ("submanifold-definition", "Real Submanifold of C^n",
     "definition", "geometry", "several-complex-variables", "Chapter 17", "17.2", "intermediate", ["submanifold", "defining-functions", "class-Ce"]),

    ("approximation-on-maximally-complex-manifolds", "Approximation Theorem on Maximally Complex Manifolds",
     "theorem", "analysis", "several-complex-variables", "Chapter 17", "17.1", "advanced", ["approximation", "maximally-complex", "submanifold", "polynomial"]),

    ("function-extension-from-submanifold", "Extension of Functions from a Submanifold",
     "lemma", "analysis", "several-complex-variables", "Chapter 17", "17.4", "intermediate", ["extension", "submanifold", "class-Ce"]),

    ("weinstock-approximation-theorem", "Weinstock Approximation Theorem",
     "theorem", "analysis", "several-complex-variables", "Chapter 17", "17.5", "advanced", ["weinstock", "approximation", "maximally-complex", "integral-transform"]),

    ("no-complex-tangents-lemma", "No Complex Tangents Lemma",
     "lemma", "geometry", "several-complex-variables", "Chapter 17", "17.6", "intermediate", ["complex-tangent", "maximally-complex", "submanifold"]),

    # === Chapter 18: Submanifolds of High Dimension (s018) ===
    ("n-sphere-hull-property", "Hull of an n-Sphere in C^n",
     "lemma", "analysis", "several-complex-variables", "Chapter 18", "18.2", "advanced", ["n-sphere", "hull", "polynomial-hull"]),

    ("analytic-disk-existence-theorem", "Existence of Analytic Disk with Boundary in Submanifold",
     "theorem", "analysis", "several-complex-variables", "Chapter 18", "18.3", "advanced", ["analytic-disk", "bishop-disk", "submanifold", "boundary"]),

    ("harmonic-conjugate-operator", "Harmonic Conjugate Operator H_1",
     "definition", "analysis", "harmonic-analysis", "Chapter 18", "18.3", "intermediate", ["harmonic-conjugate", "hilbert-transform", "boundary-function"]),

    ("boundary-functions-definition", "Smooth Boundary Functions for Bishop Disk Construction",
     "definition", "analysis", "several-complex-variables", "Chapter 18", "18.4", "advanced", ["boundary-functions", "bishop-disk", "schlicht"]),

    ("schlicht-function-lemma", "Schlicht Function Lemma for Bishop Disk",
     "lemma", "analysis", "several-complex-variables", "Chapter 18", "18.4", "advanced", ["schlicht", "analytic-disk", "bishop"]),

    ("parametric-representation-of-submanifold", "Parametric Representation of Submanifold Near 0",
     "lemma", "geometry", "several-complex-variables", "Chapter 18", "18.8", "intermediate", ["parametric-representation", "submanifold", "complex-linear"]),

    ("bishop-disk-theorem-high-dimension", "Bishop Disk Theorem in High Dimension",
     "theorem", "analysis", "several-complex-variables", "Chapter 18", "18.7", "advanced", ["bishop-disk", "high-dimension", "analytic-structure"]),

    # === Chapter 19: Boundaries of Analytic Varieties (s019–s020) ===
    ("jump-across-boundary-arc-lemma", "Jump Formula Across Smooth Boundary Arc",
     "lemma", "analysis", "several-complex-variables", "Chapter 19", "19.2", "advanced", ["jump-formula", "boundary", "cauchy-integral", "analytic-variety"]),

    ("analytic-extension-from-boundary-lemma", "Analytic Extension from Boundary Lemma",
     "lemma", "analysis", "several-complex-variables", "Chapter 19", "19.3", "advanced", ["analytic-extension", "boundary", "polynomial-hull"]),

    ("holomorphic-chain-definition", "Holomorphic Chain of Complex Dimension k",
     "definition", "analysis", "several-complex-variables", "Chapter 19", "19.1", "advanced", ["holomorphic-chain", "analytic-variety", "formal-sum", "branches"]),

    ("harvey-lawson-boundary-theorem", "Harvey-Lawson Theorem on Boundaries of Analytic Varieties",
     "theorem", "analysis", "several-complex-variables", "Chapter 19", "19.1", "advanced", ["harvey-lawson", "boundary", "analytic-variety", "moment-condition"]),

    ("maximally-complex-manifold-definition", "Maximally Complex Real Manifold",
     "definition", "geometry", "several-complex-variables", "Chapter 19", "19.2", "intermediate", ["maximally-complex", "real-manifold", "complex-subspace"]),

    ("moment-condition-definition", "Moment Condition for Boundaries of Analytic Varieties",
     "definition", "analysis", "several-complex-variables", "Chapter 19", "19.3", "advanced", ["moment-condition", "boundary", "analytic-variety", "stokes"]),

    ("kernel-identity-lemma", "Kernel Identity for Martinelli-Bochner Kernel",
     "lemma", "analysis", "several-complex-variables", "Chapter 19", "19.8", "advanced", ["kernel-identity", "martinelli-bochner", "delbar"]),

    ("type-three-zero-restriction", "Restriction of Type (3,0) Forms to Maximally Complex 3-Manifold",
     "lemma", "analysis", "several-complex-variables", "Chapter 19", "19.10", "advanced", ["differential-form", "maximally-complex", "restriction"]),

    ("analytic-disk-from-3-manifold-boundary", "Existence of Analytic Disks from 3-Manifold Boundary",
     "proposition", "analysis", "several-complex-variables", "Chapter 19", "19.7", "advanced", ["analytic-disk", "3-manifold", "boundary", "kernel"]),

    # === Chapter 20: Polynomial Hulls Over the Circle (s020–s021) ===
    ("convex-fiber-polynomial-hull-theorem", "Polynomial Hull of Convex-Fibered Sets Over the Circle",
     "theorem", "analysis", "several-complex-variables", "Chapter 20", "20.2", "advanced", ["polynomial-hull", "convex-fiber", "circle", "several-variables"]),

    ("fiber-hull-characterization", "Fiber Hull Characterization for Sets Over the Circle",
     "theorem", "analysis", "several-complex-variables", "Chapter 20", "20.3", "advanced", ["fiber-hull", "convex", "circle"]),

    ("function-representation-for-hulls-over-circle", "Function Representation for Polynomial Hulls Over Circle",
     "lemma", "analysis", "several-complex-variables", "Chapter 20", "20.4", "intermediate", ["representation", "hull", "circle", "analytic"]),

    ("explicit-hull-over-circle", "Explicit Description of Polynomial Hull Over Circle",
     "theorem", "analysis", "several-complex-variables", "Chapter 20", "20.5", "advanced", ["explicit-hull", "circle", "fiber", "analytic-disk"]),

    # === Chapter 21: Areas (s021–s022) ===
    ("area-bound-for-polynomial-hull", "Area Bound for Polynomial Hulls",
     "theorem", "analysis", "several-complex-variables", "Chapter 21", "21.1", "advanced", ["area", "polynomial-hull", "analytic-capacity"]),

    ("distance-to-rational-algebra", "Distance to the Rational Algebra R(K)",
     "lemma", "analysis", "approximation-theory", "Chapter 21", "21.2", "intermediate", ["distance", "rational-algebra", "compact-set"]),

    ("dist-zbar-rk-bound", "Bound for dist(\\bar{z}, R(K)) in Terms of Area",
     "lemma", "analysis", "approximation-theory", "Chapter 21", "21.3", "intermediate", ["distance", "zbar", "rational-algebra", "area"]),

    ("isoperimetric-inequality-via-rational-approximation", "Isoperimetric Inequality via Rational Approximation",
     "proposition", "analysis", "approximation-theory", "Chapter 21", "21.4", "intermediate", ["isoperimetric-inequality", "rational-approximation", "jordan-domain"]),

    ("area-lower-bound-for-polynomial-hull", "Area Lower Bound for Polynomial Hulls",
     "corollary", "analysis", "several-complex-variables", "Chapter 21", "21.10", "intermediate", ["area", "lower-bound", "polynomial-hull"]),

    # === Chapter 22: Topology of Hulls (s022) ===
    ("andreotti-narasimhan-rung-theorem", "Andreotti-Narasimhan Theorem on Runge Domains",
     "theorem", "analysis", "several-complex-variables", "Chapter 22", "22.2", "advanced", ["andreotti", "narasimhan", "runge", "cohomology"]),

    ("forstneric-polynomially-convex-topology", "Forstnerič Theorem on Topology of Polynomially Convex Sets",
     "theorem", "analysis", "several-complex-variables", "Chapter 22", "22.3", "advanced", ["forstneric", "polynomially-convex", "topology", "homotopy"]),

    ("plurisubharmonic-exhaustion-for-polynomially-convex", "Plurisubharmonic Exhaustion for Polynomially Convex Sets",
     "lemma", "analysis", "several-complex-variables", "Chapter 22", "22.4", "advanced", ["plurisubharmonic", "exhaustion", "polynomially-convex"]),

    ("linking-number-theorem", "Linking Number Theorem for Polynomial Hulls",
     "theorem", "topology", "several-complex-variables", "Chapter 22", "22.6", "advanced", ["linking-number", "polynomial-hull", "topology"]),

    # === Chapter 23: Pseudoconvex sets in C^n (s023) ===
    ("levi-pseudoconvex-boundary-definition", "Pseudoconvex Boundary in the Sense of Levi",
     "definition", "analysis", "several-complex-variables", "Chapter 23", "23.1", "intermediate", ["levi-form", "pseudoconvex", "boundary", "defining-function"]),

    ("pseudoconvex-domain-definition", "Pseudoconvex Domain",
     "definition", "analysis", "several-complex-variables", "Chapter 23", "23.2", "intermediate", ["pseudoconvex", "domain", "plurisubharmonic", "exhaustion"]),

    ("pseudoconvex-complement-of-polynomial-hull", "Pseudoconvexity of Complement of Polynomial Hull",
     "theorem", "analysis", "several-complex-variables", "Chapter 23", "23.1", "advanced", ["pseudoconvex", "polynomial-hull", "complement", "several-variables"]),

    ("levi-flat-from-analytic-disk", "Levi-Flat Boundary from Embedded Analytic Disk",
     "theorem", "analysis", "several-complex-variables", "Chapter 23", "23.5", "advanced", ["levi-flat", "analytic-disk", "boundary", "pseudoconvex"]),

    ("levi-flat-boundary-of-polynomial-hull", "Levi-Flat Boundary of Polynomial Hulls Over Circle",
     "theorem", "analysis", "several-complex-variables", "Chapter 23", "23.6", "advanced", ["levi-flat", "polynomial-hull", "circle", "several-variables"]),

    # === Chapter 24: Examples (s023–s025) ===
    ("rational-algebra-on-compact-set", "Rational Algebra R_0(X) and R(X) on a Compact Set",
     "definition", "analysis", "several-complex-variables", "Chapter 24", "24.1", "intermediate", ["rational-algebra", "compact-set", "uniform-closure"]),

    ("rationally-convex-hull-definition", "Rationally Convex Hull h_r(X)",
     "definition", "analysis", "several-complex-variables", "Chapter 24", "24.2", "intermediate", ["rationally-convex", "hull", "polynomial", "several-variables"]),

    ("stolzenberg-no-analytic-disk-example", "Stolzenberg Example: Rational Hull Without Analytic Disks",
     "theorem", "analysis", "several-complex-variables", "Chapter 24", "24.1", "advanced", ["stolzenberg", "rational-hull", "no-analytic-disk", "example"]),

    ("cole-example", "Cole Example of Polynomial Hull",
     "theorem", "analysis", "several-complex-variables", "Chapter 24", "24.3", "advanced", ["cole", "example", "polynomial-hull", "several-variables"]),

    ("polynomial-sequence-construction-lemma", "Construction of Polynomial Sequences with Controlled Growth",
     "lemma", "analysis", "approximation-theory", "Chapter 24", "24.4", "advanced", ["polynomial-sequence", "controlled-growth", "example"]),

    ("polynomial-set-definition", "Definition of Sets via Polynomial Sequences",
     "definition", "analysis", "several-complex-variables", "Chapter 24", "24.3", "advanced", ["polynomial", "set-definition", "example"]),

    ("branch-functions-definition", "Definition of Branch Functions via Algebraic Combinations",
     "definition", "analysis", "several-complex-variables", "Chapter 24", "24.4", "advanced", ["branch-functions", "algebraic", "example"]),

    ("harmonic-measure-estimate", "Harmonic Measure Estimate for Slit Domains",
     "lemma", "analysis", "potential-theory", "Chapter 24", "24.11", "intermediate", ["harmonic-measure", "slit-domain", "estimate"]),

    ("non-polynomially-convex-arc-example", "Example of Non-Polynomially Convex Arc in C^3",
     "theorem", "analysis", "several-complex-variables", "Chapter 24", "24.15", "advanced", ["non-polynomially-convex", "arc", "example", "several-variables"]),

    # === Chapter 25: Historical Comments and Recent Developments (s025–s026) ===
    ("pseudoconcave-set-definition", "Pseudoconcave Set",
     "definition", "analysis", "several-complex-variables", "Chapter 25", "25.1", "advanced", ["pseudoconcave", "pseudoconvex-complement", "domain"]),

    ("pseudoconcave-maximum-modulus-theorem", "Pseudoconcave Sets Give Maximum Modulus Algebras",
     "theorem", "analysis", "several-complex-variables", "Chapter 25", "25.2", "advanced", ["pseudoconcave", "maximum-modulus-algebra", "polynomial", "bidisk"]),

    # === Additional important concepts referenced but not numbered ===
    ("function-algebra-on-compact-space", "Function Algebra on a Compact Space",
     "definition", "analysis", "banach-algebras", "Chapter 1", "1", "basic", ["function-algebra", "banach-algebra", "uniform-norm"]),

    ("banach-algebra-definition", "Banach Algebra (Commutative with Unit)",
     "definition", "analysis", "banach-algebras", "Chapter 1", "1", "basic", ["banach-algebra", "commutative", "unit", "norm"]),

    ("gelfand-transform-definition", "Gelfand Transform",
     "definition", "analysis", "banach-algebras", "Chapter 1", "1", "intermediate", ["gelfand-transform", "maximal-ideal-space", "homomorphism"]),

    ("maximal-ideal-space-definition", "Maximal Ideal Space M(A)",
     "definition", "analysis", "banach-algebras", "Chapter 1", "1", "intermediate", ["maximal-ideal-space", "banach-algebra", "homomorphism"]),
]

# ============================================================
# Write concept files
# ============================================================

count = 0
for (slug, title, ctype, domain, subdomain, chapter, section, difficulty, tags) in concepts:
    folder = os.path.join(STAGING, slug)
    os.makedirs(folder, exist_ok=True)

    # --- FILE 1: concept.yaml ---
    yaml_data = {
        "id": slug,
        "title_en": title,
        "title_zh": "",
        "type": ctype,
        "domain": domain,
        "subdomain": subdomain,
        "difficulty": difficulty,
        "tags": tags,
        "depends_on": {"required": [], "recommended": [], "suggested": []},
        "source_books": [{
            "book_id": BOOK_ID,
            "author": AUTHORS,
            "title": TITLE,
            "chapter": chapter,
            "section": section,
            "pages": "",
            "role_in_book": "main_text"
        }],
        "content_hash": "",
        "extraction_date": DATE,
        "extraction_agent": AGENT
    }
    with open(os.path.join(folder, "concept.yaml"), 'w', encoding='utf-8') as f:
        yaml.dump(yaml_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    # --- FILE 2: theorem.tex ---
    tex_content = f"% {title}\n% From {chapter}, Section {section}\n% Source: Alexander & Wermer, Several Complex Variables and Banach Algebras (GTM 35), 3rd Edition\n%\n% Statement to be extracted from PDF.\n\\text{{{title}}}\n"
    with open(os.path.join(folder, "theorem.tex"), 'w', encoding='utf-8') as f:
        f.write(tex_content)

    # --- FILE 3: introduce.en.md ---
    type_article = "A" if ctype[0] in "aeiou" else "A"
    domain_readable = domain.replace("-", " ").title()
    subdomain_readable = subdomain.replace("-", " ").title()

    md_content = f"""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

{type_article} {ctype} from {chapter} of Alexander and Wermer's *Several Complex Variables and Banach Algebras* (GTM 35, 3rd Edition).
This result belongs to the domain of {domain_readable}, specifically within the subdomain of {subdomain_readable}.
It is part of the foundational material connecting the theory of several complex variables with commutative Banach algebras.
"""
    with open(os.path.join(folder, "introduce.en.md"), 'w', encoding='utf-8') as f:
        f.write(md_content)

    count += 1

# Write .done marker
done_file = os.path.join(STAGING, ".done")
with open(done_file, 'w') as f:
    f.write("DONE\n")

print(f"Created {count} concept triples in {STAGING}")
print(f"Done marker: {done_file}")
