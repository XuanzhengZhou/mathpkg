#!/bin/bash
# Batch-populate s016 concepts 26-31 + exercises
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

# 26. intersection-number (Definition)
write_yaml "$BASE/intersection-number" "intersection-number" "Intersection Number of Oriented Subspaces" "definition" "IV" "§8"
write_intro "$BASE/intersection-number" "For oriented subspaces $E_1$ and $E_2$ of $E$ with $E = E_1 + E_2$, an orientation is induced on their intersection $E_{12} = E_1 \cap E_2$. In the case of a direct decomposition, this yields the intersection number."
write_tex "$BASE/intersection-number" 'Let $E_1$ and $E_2$ be two oriented subspaces of $E$ such that $E = E_1 + E_2$ with $\dim E_1 = p$, $\dim E_2 = q$, $\dim E = n$, $\dim(E_1 \cap E_2) = r = p+q-n$. Using the isomorphisms
$$\varphi: E/E_1 \xrightarrow{\cong} E_2/E_{12}, \quad \psi: E/E_2 \xrightarrow{\cong} E_1/E_{12},$$
orientations are induced in $E_2/E_{12}$ and $E_1/E_{12}$, and consequently an orientation is induced in $E_{12}$ via the determinant function
$$\Delta_{12}(z_1, \ldots, z_r) = \Delta(z_1, \ldots, z_r, a_{r+1}, \ldots, a_p, b_{r+1}, \ldots, b_q).$$
In the special case $E = E_1 \oplus E_2$, the \textbf{intersection number} is
$$\frac{\alpha_{12}}{|\alpha_{12}|}, \quad \alpha_{12} = \Delta(a_1, \ldots, a_p, b_1, \ldots, b_q) \neq 0.$$
It satisfies $\alpha_{21} = (-1)^{p(n-p)} \alpha_{12}.$'

# 27. basis-deformation-theorem (Theorem)
write_yaml "$BASE/basis-deformation-theorem" "basis-deformation-theorem" "Basis Deformation Theorem" "theorem" "IV" "§8"
write_intro "$BASE/basis-deformation-theorem" "Two bases of a real vector space can be continuously deformed into each other (through linearly independent vectors) if and only if the determinant of the basis change is positive."
write_tex "$BASE/basis-deformation-theorem" 'Two bases $a_v$ and $b_v$ ($v = 1, \ldots, n$) of a real vector space $E$ can be deformed into each other (i.e., there exist $n$ continuous mappings $x_v: [t_0, t_1] \to E$ with $x_v(t_0) = a_v$, $x_v(t_1) = b_v$, and $x_v(t)$ linearly independent for each $t$) if and only if the linear transformation $\varphi: a_v \mapsto b_v$ has positive determinant:
$$\det \varphi > 0.$$'

# 28. basis-deformation-in-oriented-space (Theorem)
write_yaml "$BASE/basis-deformation-in-oriented-space" "basis-deformation-in-oriented-space" "Basis Deformation in an Oriented Space" "theorem" "IV" "§8"
write_intro "$BASE/basis-deformation-in-oriented-space" "In an oriented vector space, two bases are deformable into each other if and only if they have the same sign (both positive or both negative) with respect to the orientation. Thus the two deformation classes correspond exactly to the two orientations."
write_tex "$BASE/basis-deformation-in-oriented-space" 'In an oriented real linear space $E$, two bases $a_v$ and $b_v$ can be deformed into each other if and only if they are both positive or both negative with respect to the given orientation. Thus the two classes of deformable bases consist of all positive bases and all negative bases respectively.'

# 29. complex-basis-deformation-theorem (Theorem)
write_yaml "$BASE/complex-basis-deformation-theorem" "complex-basis-deformation-theorem" "Deformation of Bases in a Complex Vector Space" "theorem" "IV" "§8"
write_intro "$BASE/complex-basis-deformation-theorem" "In a complex vector space, any two bases can be deformed into each other. The proof uses the complex exponential to handle arbitrary non-zero complex coefficients (which unlike reals cannot be separated into positive and negative), constructing explicit continuous paths."
write_tex "$BASE/complex-basis-deformation-theorem" 'In a complex linear space $E$, any two bases $a_v$ and $b_v$ ($v = 1, \ldots, n$) can be deformed into each other.
The construction uses the complex exponential: write the coefficient $\beta^n$ in $b_n = \sum_v \beta^v a_v$ as $\beta^n = r e^{i\vartheta}$ with $r > 0$, and define $r(t) = 1 - t + tr$, $\vartheta(t) = t\vartheta$. Then the mappings
$$x_v(t) = a_v \quad (v = 1, \ldots, n-1), \quad x_n(t) = t\sum_{v=1}^{n-1} \beta^v a_v + r(t) e^{i\vartheta(t)} a_n$$
define a deformation $(a_1, \ldots, a_n) \to (a_1, \ldots, a_{n-1}, b_n)$.'

# 30. natural-orientation-from-complex-structure (Definition/Proposition)
write_yaml "$BASE/natural-orientation-from-complex-structure" "natural-orientation-from-complex-structure" "Natural Orientation from a Complex Structure" "definition" "IV" "§8"
write_intro "$BASE/natural-orientation-from-complex-structure" "A complex structure $j$ on a real vector space $E$ (of even dimension $2n$) induces a natural orientation: a non-zero determinant function satisfying $\Delta(x_1, \ldots, x_n, jx_1, \ldots, jx_n) > 0$ always exists."
write_tex "$BASE/natural-orientation-from-complex-structure" 'Let $j$ be a complex structure in $E$ where $\dim E = 2n$. For any determinant function $\Delta$, either
$$\Delta(x_1, \ldots, x_n, jx_1, \ldots, jx_n) \geq 0 \quad \text{or} \quad \Delta(x_1, \ldots, x_n, jx_1, \ldots, jx_n) \leq 0$$
for all $x_v \in E$. The \textbf{natural orientation} of $(E,j)$ is the orientation represented by a non-zero determinant function satisfying the first inequality. The natural orientations of $(E,j)$ and $(E,-j)$ coincide iff $n$ is even.'

# 31. Exercises for s016
for i in 1 2 3 4 5 6 7 8 9 10 11; do
  exdir="$BASE/exercise_gtm023_4.${i}"
  mkdir -p "$exdir"
done

# Write main exercise descriptions (consolidated)
cat > "$BASE/exercises_index.md" << 'EOF'
---
role: exercise-index
locale: en
chapter: "IV"
sections: "§6-§8"
---
## §6 Problems (Characteristic Polynomial)
1. Compute eigenvalues of a 3x3 matrix.
2. Show eigenvalues of a real symmetric 2x2 matrix are real.
3. Characteristic polynomial of a projection: $f(\lambda) = (-1)^{n-p} \lambda^{n-p}(1-\lambda)^p$.
4. Coefficients of characteristic polynomial of an involution: $\alpha_p = \varepsilon \alpha_{n-p}$.
5. Characteristic polynomial of direct sum = product of characteristic polynomials.
6. Characteristic polynomial of induced transformation on $E/E_1$.
7. $\varphi$ is nilpotent iff characteristic polynomial is $(-\lambda)^n$.
8. (continued) Given two linear transformations...

## §7 Problems (Trace)
1. Characteristic polynomial in 2 dimensions: $f(\lambda) = \lambda^2 - \lambda \operatorname{tr} \varphi + \det \varphi$. Cayley-Hamilton for $n=2$.
2. $\operatorname{tr}(\chi \circ \psi \circ \varphi) \neq \operatorname{tr}(\chi \circ \varphi \circ \psi)$ in general.
3. Trace of a projection = dimension of its image.
4. Duality of $L(E;F)$ and $L(E^*;F^*)$ via $\langle \varphi, \psi \rangle = \operatorname{tr}(\varphi^* \circ \psi)$.
5. Every linear function on $L(E;E)$ can be written as $f(\varphi) = \operatorname{tr}(\varphi \circ \alpha)$.
6. If $f(\psi \circ \varphi) = f(\varphi \circ \psi)$, then $f(\varphi) = \lambda \cdot \operatorname{tr} \varphi$.
7. Bilinear function $B(\varphi, \psi) = \operatorname{tr} \varphi \operatorname{tr} \psi - \operatorname{tr}(\psi \circ \varphi)$ and relation to $\alpha_2$.
8. $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ for matrices.
9. Commutation relation for 2-dimensional transformations.
10. Trace preservation under algebra automorphisms.
11. $\varphi^2 = -\lambda \iota$, $\lambda > 0$ iff $\det \varphi > 0$ and $\operatorname{tr} \varphi = 0$.

## §8 Problems (Oriented Spaces)
1. (Complex structure and natural orientation)
2. Intersection number of 1-dim subspaces in 2-dim oriented space.
3. Basis orientation and deformation in 4-dim space.
4. Complex structures and natural orientation.
EOF

echo "Concepts 26-31 + exercises complete."
