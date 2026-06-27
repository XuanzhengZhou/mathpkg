#!/bin/bash
# Batch-populate s016 concepts 10-31 (Trace §7 and Oriented Spaces §8)
set -e
BASE="/home/a123/文档/mathpkg/pipeline_output/math_pkg_tmp/concepts_batch3/gtm023/s016_6._The_characteristic_polynomial"
DATE="2026-06-27"

write_yaml() {
  local dir="$1" id="$2" title="$3" type="$4" chapter="$5" section="$6"
  cat > "$dir/concept.yaml" << YAMLEOF
id: $id
title_en: "$title"
title_zh: ""
type: $type
domain: algebra
subdomain: linear-algebra
difficulty: basic
tags: []
depends_on: {required:[], recommended:[], suggested:[]}
source_books: [{book_id:"gtm023",author:"Werner Greub",title:"Linear Algebra",chapter:"$chapter",section:"$section",pages:"",role_in_book:""}]
content_hash: ""
extraction_date: "$DATE"
extraction_agent: "v8-full-extract"
YAMLEOF
}

write_intro() { local dir="$1" text="$2"; cat > "$dir/introduce.en.md" << MDEOF
---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
$text
MDEOF
}

write_tex() { local dir="$1" text="$2"; cat > "$dir/theorem.tex" << TEXEOF
$text
TEXEOF
}

# === §7 TRACE CONCEPTS ===

# 10. trace-of-linear-transformation (Definition)
write_yaml "$BASE/trace-of-linear-transformation" "trace-of-linear-transformation" "Trace of a Linear Transformation" "definition" "IV" "§7"
write_intro "$BASE/trace-of-linear-transformation" "The trace of a linear transformation is a scalar invariant defined via a determinant function. It sums the diagonal elements in any matrix representation and is fundamental to character theory, the characteristic polynomial, and duality."
write_tex "$BASE/trace-of-linear-transformation" 'Let $\Delta \neq 0$ be a determinant function in $E$. Consider the sum
$$\sum_{i=1}^{n} \Delta(x_1, \ldots, \varphi x_i, \ldots, x_n).$$
This sum is again a determinant function and can be written as
$$\sum_{i=1}^{n} \Delta(x_1, \ldots, \varphi x_i, \ldots, x_n) = \alpha \cdot \Delta(x_1, \ldots, x_n)$$
where $\alpha$ is a scalar uniquely determined by $\varphi$. This scalar is called the \textbf{trace} of $\varphi$ and is denoted by $\operatorname{tr} \varphi$.'

# 11. trace-is-linear (Proposition)
write_yaml "$BASE/trace-is-linear" "trace-is-linear" "Linearity of the Trace" "proposition" "IV" "§7"
write_intro "$BASE/trace-is-linear" "The trace depends linearly on the transformation: the trace of a linear combination of transformations equals the same linear combination of their traces."
write_tex "$BASE/trace-is-linear" 'The trace depends linearly on $\varphi$:
$$\operatorname{tr} (\lambda \varphi + \mu \psi) = \lambda \operatorname{tr} \varphi + \mu \operatorname{tr} \psi.$$'

# 12. trace-of-composition-is-symmetric (Theorem)
write_yaml "$BASE/trace-of-composition-is-symmetric" "trace-of-composition-is-symmetric" "Symmetry of Trace Under Composition" "theorem" "IV" "§7"
write_intro "$BASE/trace-of-composition-is-symmetric" "The trace is symmetric with respect to composition: the trace of $\psi \circ \varphi$ equals the trace of $\varphi \circ \psi$. This is a fundamental property used throughout linear algebra."
write_tex "$BASE/trace-of-composition-is-symmetric" 'For any two linear transformations $\varphi$ and $\psi$ of $E$,
$$\operatorname{tr} (\psi \circ \varphi) = \operatorname{tr} (\varphi \circ \psi).$$
In particular, for any regular $\psi$,
$$\operatorname{tr} (\psi \circ \varphi \circ \psi^{-1}) = \operatorname{tr} \varphi.$$'

# 13. trace-as-coefficient-in-characteristic-polynomial (Proposition)
write_yaml "$BASE/trace-as-coefficient-in-characteristic-polynomial" "trace-as-coefficient-in-characteristic-polynomial" "Trace as Coefficient in the Characteristic Polynomial" "proposition" "IV" "§7"
write_intro "$BASE/trace-as-coefficient-in-characteristic-polynomial" "The coefficient of $\lambda^{n-1}$ in the characteristic polynomial equals $(-1)^{n-1}$ times the trace of $\varphi$, connecting two fundamental invariants."
write_tex "$BASE/trace-as-coefficient-in-characteristic-polynomial" 'The coefficient $\alpha_1$ of $\lambda^{n-1}$ in the characteristic polynomial satisfies
$$\alpha_1 = (-1)^{n-1} \operatorname{tr} \varphi.$$
Equivalently,
$$\sum_{i} \Delta(x_1, \ldots, \varphi x_i, \ldots, x_n) = (-1)^{n-1} \alpha_1 \Delta(x_1, \ldots, x_n).$$'

# 14. trace-via-matrix (Proposition)
write_yaml "$BASE/trace-via-matrix" "trace-via-matrix" "Trace Expressed via Matrix" "proposition" "IV" "§7"
write_intro "$BASE/trace-via-matrix" "Relative to a basis, the trace of a linear transformation equals the sum of diagonal entries of its matrix. In the dual basis formulation, it equals the sum of pairings with the dual basis."
write_tex "$BASE/trace-via-matrix" 'Let $e_v$ be a basis of $E$ and $(\alpha_v^\mu)$ the matrix of $\varphi$. Then
$$\operatorname{tr} \varphi = \sum_i \alpha_i^i.$$
If $e^{*v}$ is the dual basis, then also
$$\operatorname{tr} \varphi = \sum_i \langle e^{*i}, \varphi e_i \rangle.$$'

# 15. trace-of-matrix (Definition)
write_yaml "$BASE/trace-of-matrix" "trace-of-matrix" "Trace of a Matrix" "definition" "IV" "§7"
write_intro "$BASE/trace-of-matrix" "The trace of a square matrix is the sum of its diagonal entries. It satisfies $\operatorname{tr} \varphi = \operatorname{tr} M(\varphi)$ for any matrix representation."
write_tex "$BASE/trace-of-matrix" 'For any $n \times n$-matrix $A = (\alpha_v^\mu)$, the \textbf{trace} of $A$ is defined by
$$\operatorname{tr} A = \sum_i \alpha_i^i.$$
For a linear transformation $\varphi$ and its matrix $M(\varphi)$,
$$\operatorname{tr} \varphi = \operatorname{tr} M(\varphi).$$'

# 16. scalar-product-via-trace (Definition)
write_yaml "$BASE/scalar-product-via-trace" "scalar-product-via-trace" "Scalar Product via Trace on $L(E;F) \times L(F;E)$" "definition" "IV" "§7"
write_intro "$BASE/scalar-product-via-trace" "For two linear spaces $E$ and $F$, a bilinear scalar product is defined on $L(E;F) \times L(F;E)$ by $\langle \varphi, \psi \rangle = \operatorname{tr}(\psi \circ \varphi)$. This pairing establishes a duality between the two spaces."
write_tex "$BASE/scalar-product-via-trace" 'For linear spaces $E$ and $F$, define a scalar product on $L(E;F) \times L(F;E)$ by
$$\langle \varphi, \psi \rangle = \operatorname{tr} (\psi \circ \varphi), \quad \varphi \in L(E;F), \quad \psi \in L(F;E).$$
This bilinear function is non-degenerate.'

# 17. trace-pairing-is-nondegenerate (Proposition)
write_yaml "$BASE/trace-pairing-is-nondegenerate" "trace-pairing-is-nondegenerate" "Non-Degeneracy of the Trace Pairing" "proposition" "IV" "§7"
write_intro "$BASE/trace-pairing-is-nondegenerate" "The bilinear pairing $\langle \varphi, \psi \rangle = \operatorname{tr}(\psi \circ \varphi)$ on $L(E;F) \times L(F;E)$ is non-degenerate: if $\langle \varphi, \psi \rangle = 0$ for all $\psi$, then $\varphi = 0$."
write_tex "$BASE/trace-pairing-is-nondegenerate" 'Assume that $\langle \varphi, \psi \rangle = 0$ for a fixed $\varphi \in L(E;F)$ and all $\psi \in L(F;E)$. Then $\varphi = 0$.
In fact, if $\varphi \neq 0$, choose $a \in E$ with $b_1 = \varphi a \neq 0$, extend $b_1$ to a basis of $F$, and define $\psi$ by $\psi b_1 = a$, $\psi b_i = 0$ for $i > 1$. Then $\langle \varphi, \psi \rangle = 1 \neq 0$, contradiction.'

# === §8 ORIENTED VECTOR SPACES ===

# 18. orientation-by-determinant-function (Definition)
write_yaml "$BASE/orientation-by-determinant-function" "orientation-by-determinant-function" "Orientation by a Determinant Function" "definition" "IV" "§8"
write_intro "$BASE/orientation-by-determinant-function" "In a real vector space, two non-zero determinant functions are equivalent if one is a positive scalar multiple of the other. The two equivalence classes are the two possible orientations of the space."
write_tex "$BASE/orientation-by-determinant-function" 'Let $\Delta_1 \neq 0$ and $\Delta_2 \neq 0$ be two determinant functions in a real vector space $E$. Then $\Delta_2 = \lambda \Delta_1$ with $\lambda \neq 0$. Define the equivalence relation
$$\Delta_1 \sim \Delta_2 \quad \text{if} \quad \lambda > 0.$$
The two equivalence classes are called the \textbf{orientations} of $E$. If $(\Delta)$ is an orientation and $\Delta \in (\Delta)$, we say $\Delta$ \textbf{represents} the orientation.'

# 19. positive-basis (Definition)
write_yaml "$BASE/positive-basis" "positive-basis" "Positive Basis in an Oriented Vector Space" "definition" "IV" "§8"
write_intro "$BASE/positive-basis" "In an oriented vector space, a basis is called positive if a representing determinant function evaluates to a positive number on it. Permuting a positive basis by an even permutation preserves positivity."
write_tex "$BASE/positive-basis" 'A basis $e_v$ ($v = 1, \ldots, n$) of an oriented vector space is called \textbf{positive} if
$$\Delta(e_1, \ldots, e_n) > 0$$
where $\Delta$ is a representing determinant function. If $(e_1, \ldots, e_n)$ is a positive basis and $\sigma$ is a permutation, then $(e_{\sigma(1)}, \ldots, e_{\sigma(n)})$ is positive if and only if $\sigma$ is even.'

# 20. orientation-of-dual-space (Definition)
write_yaml "$BASE/orientation-of-dual-space" "orientation-of-dual-space" "Orientation Induced in the Dual Space" "definition" "IV" "§8"
write_intro "$BASE/orientation-of-dual-space" "An orientation in $E$ induces an orientation in the dual space $E^*$ via the dual determinant function, which depends only on the original orientation."
write_tex "$BASE/orientation-of-dual-space" 'If an orientation is defined in $E$, then the dual determinant function (cf. sec. 4.10) determines an orientation in $E^*$. This orientation depends only on the orientation of $E$.'

# 21. orientation-preserving-linear-map (Definition)
write_yaml "$BASE/orientation-preserving-linear-map" "orientation-preserving-linear-map" "Orientation-Preserving Linear Mapping" "definition" "IV" "§8"
write_intro "$BASE/orientation-preserving-linear-map" "A linear isomorphism between oriented spaces of the same dimension preserves orientation if it maps a positive basis to a positive basis. Given an isomorphism and an orientation on the domain, there exists a unique orientation on the codomain making the map orientation-preserving."
write_tex "$BASE/orientation-preserving-linear-map" 'Let $E$ and $F$ be two oriented vector spaces of the same dimension $n$ and $\varphi: E \to F$ a linear isomorphism. Then $\varphi$ is called \textbf{orientation-preserving} if it maps a positive basis of $E$ to a positive basis of $F$.
Given a linear isomorphism $\varphi: E \to F$ and an orientation in $E$, there exists precisely one orientation in $F$ such that $\varphi$ preserves the orientation, called the \textbf{orientation induced by $\varphi$}.'

# 22. automorphism-preserves-orientation-iff-positive-determinant (Proposition)
write_yaml "$BASE/automorphism-preserves-orientation-iff-positive-determinant" "automorphism-preserves-orientation-iff-positive-determinant" "Automorphism Preserves Orientation iff Determinant is Positive" "proposition" "IV" "§8"
write_intro "$BASE/automorphism-preserves-orientation-iff-positive-determinant" "A linear automorphism preserves orientation if and only if its determinant is positive. In particular, the map $-\iota$ preserves orientation exactly when the dimension is even."
write_tex "$BASE/automorphism-preserves-orientation-iff-positive-determinant" 'A linear automorphism $\varphi: E \to E$ preserves the orientation if and only if
$$\det \varphi > 0.$$
For $\varphi = -\iota$, we have $\det(-\iota) = (-1)^n$, so $-\iota$ preserves orientation iff $n$ is even.'

# 23. orientation-of-factor-space (Definition)
write_yaml "$BASE/orientation-of-factor-space" "orientation-of-factor-space" "Orientation in a Factor Space" "definition" "IV" "§8"
write_intro "$BASE/orientation-of-factor-space" "Given an oriented space $E$ and an oriented subspace $F$, an orientation is induced in the factor space $E/F$ by fixing a positive basis of $F$ and using a representing determinant function."
write_tex "$BASE/orientation-of-factor-space" 'Let $E$ be an oriented vector space and $F$ be an oriented subspace. Let $\Delta$ be a representing determinant function in $E$ and $a_1, \ldots, a_p$ a positive basis of $F$. Then the function
$$\bar{\Delta}(\bar{x}_{p+1}, \ldots, \bar{x}_n) = \Delta(a_1, \ldots, a_p, x_{p+1}, \ldots, x_n)$$
defines a determinant function on $E/F$, independent of the choice of representing $\Delta$ and positive basis of $F$, inducing an orientation in $E/F$.'

# 24. orientation-from-direct-decomposition (Definition)
write_yaml "$BASE/orientation-from-direct-decomposition" "orientation-from-direct-decomposition" "Orientation Induced from a Direct Decomposition" "definition" "IV" "§8"
write_intro "$BASE/orientation-from-direct-decomposition" "Given orientations on $E_1$ and $E_2$, an orientation is induced on $E = E_1 \oplus E_2$ by concatenating positive bases. This orientation is independent of the choices made."
write_tex "$BASE/orientation-from-direct-decomposition" 'Consider a direct decomposition $E = E_1 \oplus E_2$ and assume orientations are defined in $E_1$ and $E_2$. Let $a_i$ ($i = 1, \ldots, p$) and $b_j$ ($j = 1, \ldots, q$) be positive bases of $E_1$ and $E_2$. Then choose the orientation of $E$ such that the basis $a_1, \ldots, a_p, b_1, \ldots, b_q$ is positive. This orientation depends only on the orientations of $E_1$ and $E_2$.'

# 25. orientation-coincidence-theorem (Theorem)
write_yaml "$BASE/orientation-coincidence-theorem" "orientation-coincidence-theorem" "Coincidence of Induced and Original Orientations" "theorem" "IV" "§8"
write_intro "$BASE/orientation-coincidence-theorem" "When a subspace $E_2$ induces an orientation in $E_1$, this induced orientation coincides with the original orientation of $E_1$ if and only if $p(n-p)$ is even, where $p = \dim E_1$ and $n = \dim E$."
write_tex "$BASE/orientation-coincidence-theorem" 'Let $E = E_1 \oplus E_2$ with oriented $E_1, E_2, E$. Let $\dim E_1 = p$, $\dim E = n$. The orientation induced in $E_1$ by $E_2$ coincides with the original orientation of $E_1$ if and only if $p(n-p)$ is even. Equivalently,
$$\Delta_1(e_1, \ldots, e_p) = (-1)^{p(n-p)} \Delta(e_{p+1}, \ldots, e_n, e_1, \ldots, e_p).$$'

echo "Concepts 10-25 complete."
