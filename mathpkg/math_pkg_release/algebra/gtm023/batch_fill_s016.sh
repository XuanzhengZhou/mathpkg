#!/bin/bash
# Batch-populate s016 (Characteristic Polynomial, Trace, Oriented Spaces)
# 31 concepts from GTM023 Ch.IV §6-8
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

write_intro() {
  local dir="$1" text="$2"
  cat > "$dir/introduce.en.md" << MDEOF
---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
$text
MDEOF
}

write_tex() {
  local dir="$1" text="$2"
  cat > "$dir/theorem.tex" << TEXEOF
$text
TEXEOF
}

# --- Concept 1: eigenvalues-as-solutions-of-characteristic-equation (Proposition) ---
write_yaml "$BASE/eigenvalues-as-solutions-of-characteristic-equation" \
  "eigenvalues-as-solutions-of-characteristic-equation" \
  "Eigenvalues as Solutions of the Characteristic Equation" \
  "proposition" "IV" "§6"
write_intro "$BASE/eigenvalues-as-solutions-of-characteristic-equation" \
  "The eigenvalues of a linear transformation are precisely the solutions of the characteristic equation. The condition that $\varphi - \lambda \iota$ is not regular is equivalent to the vanishing of its determinant, establishing the fundamental link between eigenvalues and the characteristic polynomial."
write_tex "$BASE/eigenvalues-as-solutions-of-characteristic-equation" \
'Assume that $a$ is an eigenvector of $\varphi$ and that $\lambda$ is the corresponding eigenvalue. Then
$$\varphi a = \lambda a, \quad a \neq 0.$$
This equation can be written as
$$(\varphi - \lambda \iota) a = 0$$
showing that $\varphi - \lambda \iota$ is not regular. This implies that
$$\det (\varphi - \lambda \iota) = 0.$$

Hence, every eigenvalue of $\varphi$ satisfies the characteristic equation. Conversely, if $\lambda$ satisfies $\det(\varphi - \lambda \iota) = 0$, then $\varphi - \lambda \iota$ is not regular, so there exists $a \neq 0$ with $(\varphi - \lambda \iota)a = 0$, i.e., $\varphi a = \lambda a$. Thus the eigenvalues are precisely the solutions of $\det(\varphi - \lambda \iota) = 0$.'

# --- Concept 2: characteristic-polynomial (Definition) ---
write_yaml "$BASE/characteristic-polynomial" \
  "characteristic-polynomial" \
  "Characteristic Polynomial of a Linear Transformation" \
  "definition" "IV" "§6"
write_intro "$BASE/characteristic-polynomial" \
  "The characteristic polynomial of a linear transformation $\varphi$ is a monic polynomial of degree $n = \dim E$ whose roots are the eigenvalues of $\varphi$. It is defined via a determinant function and provides the fundamental invariant connecting eigenvalues, trace, and determinant."
write_tex "$BASE/characteristic-polynomial" \
'Let $\Delta \neq 0$ be a determinant function in $E$. The characteristic polynomial of $\varphi$ is defined by
$$\Delta(\varphi x_1 - \lambda x_1, \ldots, \varphi x_n - \lambda x_n) = \det(\varphi - \lambda \iota) \Delta(x_1, \ldots, x_n), \quad x_v \in E.$$
Expanding the left-hand side yields
$$\det(\varphi - \lambda \iota) = \sum_{p=0}^{n} \alpha_p \lambda^{n-p}$$
which is a polynomial in $\lambda$ of degree $n$.'

# --- Concept 3: characteristic-polynomial-coefficients (Theorem) ---
write_yaml "$BASE/characteristic-polynomial-coefficients" \
  "characteristic-polynomial-coefficients" \
  "Coefficients of the Characteristic Polynomial" \
  "theorem" "IV" "§6"
write_intro "$BASE/characteristic-polynomial-coefficients" \
  "Expanding the characteristic polynomial determinant yields a sum of $2^n$ terms. Collecting terms by the number of arguments replaced by $\varphi x_v$ gives explicit formulas for the coefficients $\alpha_p$ in terms of skew-symmetric multilinear functions."
write_tex "$BASE/characteristic-polynomial-coefficients" \
'Expanding $\Delta(\varphi x_1 - \lambda x_1, \ldots, \varphi x_n - \lambda x_n)$ gives a sum of $2^n$ terms. Denote by $S_p$ the sum of terms with $p$ arguments equal to $\varphi x_v$ and $n-p$ equal to $-\lambda x_v$. Then
$$S_p = (-\lambda)^{n-p} \sum_{\sigma} \varepsilon_{\sigma} \Delta(\varphi x_{\sigma(1)}, \ldots, \varphi x_{\sigma(p)}, x_{\sigma(p+1)}, \ldots, x_{\sigma(n)})$$
where the sum extends over permutations satisfying $\sigma(p+1) < \cdots < \sigma(n)$. Define
$$\Phi_p(x_1, \ldots, x_n) = \sum_{\sigma} \varepsilon_{\sigma} \Delta(\varphi x_{\sigma(1)}, \ldots, \varphi x_{\sigma(p)}, x_{\sigma(p+1)}, \ldots, x_{\sigma(n)}).$$
Then $\Phi_p$ is skew-symmetric and $\Phi_p = (-1)^{n-p} p!(n-p)! \alpha_p \cdot \Delta$ for a scalar $\alpha_p$, yielding
$$\det(\varphi - \lambda \iota) = \sum_{p=0}^{n} \alpha_p \lambda^{n-p}.$$'

# --- Concept 4: complex-transformation-has-eigenvalue (Proposition) ---
write_yaml "$BASE/complex-transformation-has-eigenvalue" \
  "complex-transformation-has-eigenvalue" \
  "Every Linear Transformation of a Complex Space Has an Eigenvalue" \
  "proposition" "IV" "§6"
write_intro "$BASE/complex-transformation-has-eigenvalue" \
  "By the fundamental theorem of algebra, every non-constant polynomial over the complex numbers has at least one root. Since the characteristic polynomial has degree $n \geq 1$, every linear transformation of a complex linear space possesses at least one eigenvalue."
write_tex "$BASE/complex-transformation-has-eigenvalue" \
'Assume that $E$ is a complex linear space. Then, according to the fundamental theorem of algebra, the characteristic polynomial $f$ has at least one zero. Consequently, every linear transformation of a complex linear space has at least one eigenvalue.'

# --- Concept 5: odd-dim-real-transformation-has-eigenvalue (Proposition) ---
write_yaml "$BASE/odd-dim-real-transformation-has-eigenvalue" \
  "odd-dim-real-transformation-has-eigenvalue" \
  "Odd-Dimensional Real Linear Transformations Have an Eigenvalue" \
  "proposition" "IV" "§6"
write_intro "$BASE/odd-dim-real-transformation-has-eigenvalue" \
  "For an odd-dimensional real linear space, the limits of the characteristic polynomial as $\lambda \to \pm\infty$ have opposite signs, guaranteeing a real root by the intermediate value theorem. Moreover, the sign of the determinant determines the sign of at least one eigenvalue."
write_tex "$BASE/odd-dim-real-transformation-has-eigenvalue" \
'If $\dim E$ is odd, then
$$\lim_{\lambda \to \infty} f(\lambda) = -\infty \quad \text{and} \quad \lim_{\lambda \to -\infty} f(\lambda) = +\infty$$
so $f$ has at least one real zero. Hence every linear transformation of an odd-dimensional real space has at least one eigenvalue. Moreover, $f(0) = \alpha_n = \det \varphi$, so:
\begin{itemize}
  \item If $\det \varphi > 0$, there is at least one positive eigenvalue.
  \item If $\det \varphi < 0$, there is at least one negative eigenvalue.
\end{itemize}
If $\dim E$ is even and $\det \varphi < 0$, there exists at least one positive and one negative eigenvalue.'

# --- Concept 6: characteristic-polynomial-of-dual ---
write_yaml "$BASE/characteristic-polynomial-of-dual" \
  "characteristic-polynomial-of-dual" \
  "Characteristic Polynomial of the Dual Transformation" \
  "proposition" "IV" "§6"
write_intro "$BASE/characteristic-polynomial-of-dual" \
  "The characteristic polynomial of the dual transformation $\varphi^*$ coincides with that of $\varphi$, reflecting the duality between $E$ and $E^*$."
write_tex "$BASE/characteristic-polynomial-of-dual" \
'The characteristic polynomial of the dual transformation $\varphi^*$ coincides with the characteristic polynomial of $\varphi$.'

# --- Concept 7: characteristic-polynomial-of-direct-sum ---
write_yaml "$BASE/characteristic-polynomial-of-direct-sum" \
  "characteristic-polynomial-of-direct-sum" \
  "Characteristic Polynomial of Direct Sum of Transformations" \
  "proposition" "IV" "§6"
write_intro "$BASE/characteristic-polynomial-of-direct-sum" \
  "When $E = E_1 \oplus E_2$ with stable subspaces, the characteristic polynomial of $\varphi$ equals the product of the characteristic polynomials of the induced transformations on each summand."
write_tex "$BASE/characteristic-polynomial-of-direct-sum" \
'If $E = E_1 \oplus E_2$ where $E_1$ and $E_2$ are stable subspaces, then the characteristic polynomial of $\varphi$ is the product of the characteristic polynomials of the induced transformations $\varphi_1: E_1 \to E_1$ and $\varphi_2: E_2 \to E_2$:
$$\chi_{\varphi} = \chi_{\varphi_1} \cdot \chi_{\varphi_2}.$$'

# --- Concept 8: characteristic-polynomial-of-inverse ---
write_yaml "$BASE/characteristic-polynomial-of-inverse" \
  "characteristic-polynomial-of-inverse" \
  "Characteristic Polynomial of the Inverse Transformation" \
  "proposition" "IV" "§6"
write_intro "$BASE/characteristic-polynomial-of-inverse" \
  "For a regular linear transformation $\varphi$, the characteristic polynomial of $\varphi^{-1}$ is related to that of $\varphi$ by a reciprocal formula involving $(-\lambda)^n$ and $\det \varphi^{-1}$."
write_tex "$BASE/characteristic-polynomial-of-inverse" \
'Let $\varphi: E \to E$ be a regular linear transformation and let $F$ be the characteristic polynomial of $\varphi^{-1}$ and $f$ that of $\varphi$. Then
$$\det(\varphi^{-1} - \lambda \iota) = (-\lambda)^n \det \varphi^{-1} \cdot \det(\varphi - \lambda^{-1} \iota)$$
so
$$F(\lambda) = (-\lambda)^n \det \varphi^{-1} f(\lambda^{-1}).$$
Expanding $F(\lambda) = \sum_{v=0}^{n} \beta_v \lambda^{n-v}$ yields
$$\beta_v = (-1)^n \det \varphi^{-1} \alpha_{n-v} \quad (v = 0, \ldots, n).$$'

# --- Concept 9: characteristic-polynomial-of-matrix ---
write_yaml "$BASE/characteristic-polynomial-of-matrix" \
  "characteristic-polynomial-of-matrix" \
  "Characteristic Polynomial of a Matrix" \
  "definition" "IV" "§6"
write_intro "$BASE/characteristic-polynomial-of-matrix" \
  "The characteristic polynomial of a matrix $A$ is defined as $\det(A - \lambda J)$ where $J$ is the identity matrix. Its roots are the eigenvalues of $A$."
write_tex "$BASE/characteristic-polynomial-of-matrix" \
'Let $e_v$ be a basis of $E$ and $A = M(\varphi)$ the matrix of $\varphi$. Then
$$M(\varphi - \lambda \iota) = A - \lambda J$$
whence
$$\det(\varphi - \lambda \iota) = \det(A - \lambda J).$$
The polynomial $f(\lambda) = \det(A - \lambda J)$ is called the \textbf{characteristic polynomial} of the matrix $A$. Its roots are the \textbf{eigenvalues} of $A$.'

echo "Concepts 1-9 complete."
