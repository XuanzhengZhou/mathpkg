#!/bin/bash
# Batch create all concept files for s016_58_Preliminaries
BASE="/home/a123/文档/mathpkg/pipeline_output/concepts_v7/gtm015/s016_58_Preliminaries"

# Helper function
write_concept() {
  local slug=$1; local type=$2; local title_en=$3; local tex=$4; local intro=$5
  local d="$BASE/$slug"
  # concept.yaml
  cat > "$d/concept.yaml" <<YAML_END
id: $slug
title_en: "$title_en"
title_zh: ""
type: $type
domain: analysis
subdomain: functional-analysis
difficulty: advanced
tags: []
depends_on: {required: [], recommended: [], suggested: []}
source_books:
  - book_id: "gtm015"
    author: "Sterling K. Berberian"
    title: "Lectures in Functional Analysis and Operator Theory"
    chapter: "Chapter 7: C*-Algebras"
    section: "58. Preliminaries"
    pages: ""
    role_in_book: ""
content_hash: ""
extraction_date: "2026-06-25"
extraction_agent: "v7-section-test"
YAML_END
  # theorem.tex
  echo "$tex" > "$d/theorem.tex"
  # introduce.en.md
  cat > "$d/introduce.en.md" <<MD_END
---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

$intro
MD_END
}

# ============ SECTION 58 ============

write_concept "isometric-involution-c-star" "theorem" \
  "Isometric Involution in C*-Algebras" \
  'If $A$ is a normed *-algebra with *-quadratic norm, then the involution is isometric, that is, $\|x^*\| = \|x\|$ for all $x \in A$.' \
  'In any C*-algebra (or more generally any normed *-algebra with *-quadratic norm), the involution $x \mapsto x^*$ is an isometry. This follows directly from the *-quadratic property and is one of the first structural consequences of the C*-axiom.'

write_concept "spectral-radius-self-adjoint-c-star" "theorem" \
  "Spectral Radius Formula for C*-Algebras" \
  'If $A$ is a $C^*$-algebra, then $r(x^*x) = \|x\|^2$ for all $x \in A$. In particular, if $x$ is self-adjoint, then $r(x) = \|x\|$.' \
  'In a C*-algebra, the spectral radius of a self-adjoint element equals its norm, and more generally $r(x^*x) = \|x\|^2$ for every element. This identity is fundamental: it shows the norm is determined by purely algebraic (spectral) data, and it underpins the entire spectral theory of C*-algebras.'

write_concept "self-adjoint-spectrum-real" "theorem" \
  "Self-Adjoint Elements Have Real Spectrum" \
  'If $A$ is a $C^*$-algebra with unity and if $x \in A$ is self-adjoint, then $\sigma_A(x) \subset \mathbb{R}$.' \
  'In a unital C*-algebra, every self-adjoint element has real spectrum. This generalizes the familiar fact from operator theory that self-adjoint (Hermitian) operators on Hilbert space have real spectrum. The proof uses the *-quadratic norm property and an algebraic maneuver showing $x - i1$ must be invertible.'

write_concept "closed-star-subalgebra-full" "corollary" \
  "Closed *-Subalgebra is Full" \
  'If $A$ is a $C^*$-algebra with unity and if $B$ is a closed $*$-subalgebra of $A$ containing $1$, then $B$ is a full subalgebra of $A$.' \
  'A closed *-subalgebra $B$ of a unital C*-algebra $A$ that contains the unit is a full subalgebra, meaning every element of $B$ that is invertible in $A$ is already invertible in $B$. This follows from the real-spectrum theorem (58.4) and is essential for relating spectral properties in subalgebras.'

# ============ SECTION 59 ============

write_concept "continuous-functions-compact-c-star" "definition" \
  "C(T) as Commutative C*-Algebra" \
  'Let $T$ be a compact space and let $\mathcal{C}(T)$ be the set of all continuous functions $x: T \to \mathbb{C}$, equipped with pointwise algebra operations, pointwise involution $x^*(t) = \overline{x(t)}$, and the supremum norm $\|x\|_\infty = \sup\{|x(t)| : t \in T\}$. Then $\mathcal{C}(T)$ is a commutative $C^*$-algebra with unity.' \
  'The algebra $\mathcal{C}(T)$ of continuous complex-valued functions on a compact space $T$, with the supremum norm and complex-conjugation involution, is the canonical example of a commutative unital C*-algebra. The commutative Gel\''fand-Naimark theorem shows that every commutative unital C*-algebra is isomorphic to $\mathcal{C}(T)$ for some compact $T$.'

write_concept "commutative-gelfand-naimark" "theorem" \
  "Commutative Gel'fand-Naimark Theorem" \
  'If $A$ is a commutative $C^*$-algebra with unity and if $\mathcal{M}$ is its character space, then the Gel\''fand transform $a \mapsto \hat{a}$ is an isometric $*$-isomorphism of $A$ onto $\mathcal{C}(\mathcal{M})$.' \
  'The commutative Gel\''fand-Naimark theorem states that every commutative unital C*-algebra is isometrically *-isomorphic to $\mathcal{C}(\mathcal{M})$, the continuous functions on its character space $\mathcal{M}$ (a compact Hausdorff space). This theorem is the foundation of spectral theory for normal operators and provides the functional representation of commutative C*-algebras.'

# ============ SECTION 60 ============

write_concept "star-homomorphism-norm-decreasing" "theorem" \
  "Unital *-Homomorphisms are Norm-Decreasing" \
  'If $A$ and $B$ are $C^*$-algebras with unity, and if $\varphi: A \to B$ is a *-homomorphism such that $\varphi(1) = 1$, then $\|\varphi(a)\| \leq \|a\|$ for all $a \in A$. In particular, $\varphi$ is continuous.' \
  'A unital *-homomorphism between C*-algebras is automatically norm-decreasing (hence continuous). This remarkable theorem shows that algebraic *-homomorphisms automatically have desirable geometric and topological features. In particular, an injective *-homomorphism is necessarily isometric.'

write_concept "orthogonal-sum-hilbert-spaces" "definition" \
  "Orthogonal Sum of Hilbert Spaces" \
  'With notation as in (60.4), the Hilbert space $H$ is called the orthogonal sum of the family $(H_i)_{i \in I}$. Notation: $H = \bigoplus_{i \in I} H_i$.' \
  'The orthogonal sum (also called Hilbert sum or direct sum) of a family of Hilbert spaces $(H_i)_{i\in I}$ is the Hilbert space $H = \bigoplus_i H_i$ consisting of all families $(x_i)$ with $x_i \in H_i$ and $\sum_i \|x_i\|^2 < \infty$, equipped with the coordinatewise inner product. This construction is used to build *-representations as direct sums of cyclic representations.'

# ============ SECTION 61 ============

write_concept "positive-element-c-star" "definition" \
  "Positive Element in a C*-Algebra" \
  'Let $A$ be a $C^*$-algebra with unity. We say that $a \in A$ is positive (relative to $A$) if $a^* = a$ and $\sigma(a) \subset [0, \infty)$. Notation: $a \geq 0$.' \
  'An element $a$ of a unital C*-algebra is called positive if it is self-adjoint and its spectrum is contained in the nonnegative real numbers $[0,\infty)$. Positivity defines a partial order on the self-adjoint elements and is the C*-algebraic generalization of positive semidefinite operators on Hilbert space.'

write_concept "positivity-independent-subalgebra" "lemma" \
  "Positivity Independent of Containing Subalgebra" \
  'If $a \in B \subset A$, where $A$ is a $C^*$-algebra with unity and $B$ is a closed $*$-subalgebra of $A$ containing the unity element, then $a \geq 0$ relative to $B$ iff $a \geq 0$ relative to $A$.' \
  'The positivity of an element in a C*-algebra is independent of the containing closed *-subalgebra: if $B$ is a closed unital *-subalgebra of $A$, then $a \in B$ is positive in $B$ precisely when it is positive in $A$. This follows from the fact that $B$ is a full subalgebra of $A$ (58.5).'

write_concept "positive-square-root-c-star" "theorem" \
  "Existence and Uniqueness of Positive Square Root" \
  'Let $A$ be a $C^*$-algebra with unity and let $a \in A$, $a \geq 0$. There exists a unique element $b \in A$ such that $b \geq 0$ and $b^2 = a$.' \
  'Every positive element in a unital C*-algebra has a unique positive square root. This is a fundamental structural result that generalizes the existence of positive square roots of positive operators. The square root lies in the bicommutant $\{a\}''$ and is obtained via the continuous functional calculus.'

write_concept "a-star-a-positive-c-star" "theorem" \
  "Elements of the Form a*a are Positive" \
  'If $A$ is a $C^*$-algebra with unity, then $a^*a \geq 0$ for every $a \in A$.' \
  'In any unital C*-algebra, every element of the form $a^*a$ is positive. This is a crucial property (sometimes called symmetry) that is needed in the proof of the Gel\''fand-Naimark representation theorem. The proof uses the commutative Gel\''fand-Naimark theorem applied to the bicommutant of $a^*a$.'

write_concept "state-on-c-star-algebra" "definition" \
  "State on a C*-Algebra" \
  'Let $A$ be a $C^*$-algebra with unity. A state on $A$ is a continuous linear form $f: A \to \mathbb{C}$ such that $f(1) = 1$ and $f(a^*a) \geq 0$ for all $a \in A$.' \
  'A state on a unital C*-algebra is a positive normalized linear functional. States are the C*-algebraic analogues of probability measures (via the Riesz representation theorem for $\mathcal{C}(T)$) and of vector states $x \mapsto (Tx|x)$ on $\mathcal{L}(H)$. The set of all states is a weak* compact convex set.'

write_concept "states-separate-points-existence" "theorem" \
  "States Separate Points" \
  'For every $a \in A$ there exists a state $f$ on $A$ such that $f(a^*a) = \|a\|^2$. In particular, if $a \neq b$ there exists a state $f$ with $f(a) \neq f(b)$.' \
  'States on a unital C*-algebra separate points: for each element $a$ there is a state $f$ satisfying $f(a^*a) = \|a\|^2$. Equivalently, the set of all states is rich enough to distinguish elements. The proof uses the Hahn-Banach theorem to extend a positive functional defined on a commutative subalgebra.'

write_concept "gns-construction" "theorem" \
  "GNS Construction" \
  'If $A$ is a $C^*$-algebra with unity and if $f$ is a state on $A$, then there exist a unital $*$-representation $\varphi: A \to \mathcal{L}(H)$ and a vector $u \in H$ such that $f(a) = (\varphi(a)u|u)$ for all $a \in A$.' \
  'The Gelfand-Naimark-Segal (GNS) construction associates to every state $f$ on a unital C*-algebra a cyclic *-representation $(\varphi, H, u)$ such that $f(a) = (\varphi(a)u|u)$. The Hilbert space $H$ is obtained by completing $A/N_f$ with respect to the inner product $(x_f|y_f) = f(y^*x)$, and $\varphi$ is the left regular representation.'

write_concept "ordering-self-adjoint-c-star" "definition" \
  "Ordering of Self-Adjoint Elements" \
  'Let $A$ be a $C^*$-algebra with unity. If $a$ and $b$ are self-adjoint elements of $A$ such that $b - a \geq 0$ in the sense of (61.3), we write $a \leq b$ (or $b \geq a$).' \
  'The set of self-adjoint elements $A_s$ in a unital C*-algebra is partially ordered by defining $a \leq b$ whenever $b-a$ is positive (i.e., self-adjoint with nonnegative spectrum). This makes $A_s$ an ordered real vector space with order unit $1$, and a state is precisely a linear functional whose restriction to $A_s$ is positive.'

write_concept "self-adjoint-ordered-vector-space-c-star" "theorem" \
  "Self-Adjoint Elements Form Ordered Vector Space" \
  'Let $A$ be a $C^*$-algebra with unity and let $A_s$ be the set of all self-adjoint elements of $A$. With respect to the relation $a \leq b$ defined in (61.12), $A_s$ is an ordered real vector space. A linear form $f: A \to \mathbb{C}$ is a state on $A$ iff the restriction of $f$ to $A_s$ is a positive linear form.' \
  'The self-adjoint elements $A_s$ of a unital C*-algebra form an ordered real vector space under the positivity ordering. The positive cone $P = \{a \in A_s : a \geq 0\}$ is salient, pointed, and convex. Moreover, states correspond exactly to those linear functionals whose restriction to $A_s$ is a positive linear form.'

write_concept "numerical-status-definition" "definition" \
  "Numerical Status (Numerical Range)" \
  '$\Sigma(a) = \{f(a) : f \in \Sigma\}$ where $\Sigma$ is the set of all states on $A$.' \
  'The numerical status (or numerical range) $\Sigma(a)$ of an element $a$ in a unital C*-algebra is the set of values $f(a)$ as $f$ runs over all normalized states. It generalizes the numerical range of an operator on Hilbert space and is a compact convex subset of the complex plane.'

write_concept "sigma-weak-star-compact-convex" "theorem" \
  "State Space is Weak* Compact and Convex" \
  'The set $\Sigma$ of all states on a unital $C^*$-algebra $A$ is a nonempty, weak* compact, convex subset of the dual space $A'$.' \
  'The state space $\Sigma$ of a unital C*-algebra is a weak* compact convex subset of the dual space. This follows from the Banach-Alaoglu theorem and the fact that $\Sigma$ is the intersection of the closed unit ball with the positive cone. The extremal points of $\Sigma$ correspond to irreducible representations.'

write_concept "numerical-status-independent" "theorem" \
  "Numerical Status Independent of Containing Algebra" \
  'If $A$ is a $C^*$-algebra with unity and if $B$ is a closed $*$-subalgebra of $A$ containing the unity element, then $\Sigma_B(b) = \Sigma_A(b)$ for all $b \in B$.' \
  'The numerical status (numerical range) of an element is independent of the containing C*-algebra: if $B$ is a closed unital *-subalgebra of $A$, then $\Sigma_B(b) = \Sigma_A(b)$ for every $b \in B$. This follows from the Hahn-Banach theorem applied to states.'

write_concept "sigma-equals-convex-hull-spectrum" "theorem" \
  "Numerical Status Equals Convex Hull of Spectrum" \
  'If $A$ is a $C^*$-algebra with unity and if $a \in A$ is self-adjoint, then $\Sigma(a) = \operatorname{conv} \sigma(a)$.' \
  'For a self-adjoint element $a$ in a unital C*-algebra, the numerical status $\Sigma(a)$ equals the convex hull of the spectrum $\sigma(a)$. Since the spectrum is real for self-adjoint elements, this means $\Sigma(a)$ is precisely the real interval $[m, M]$ where $m = \min \sigma(a)$ and $M = \max \sigma(a)$.'

write_concept "positivity-via-numerical-status" "corollary" \
  "Positivity Characterized by Numerical Status" \
  'Let $A$ be a $C^*$-algebra with unity and let $a \in A$ be self-adjoint. Then $a \geq 0$ iff $\Sigma(a) \subset [0, \infty)$.' \
  'A self-adjoint element $a$ in a unital C*-algebra is positive if and only if its numerical status $\Sigma(a)$ is contained in $[0,\infty)$. This provides a useful characterization of positivity in terms of state evaluations, complementary to the spectral definition.'

# ============ SECTION 62 ============

write_concept "gelfand-naimark-representation-theorem" "theorem" \
  "Gel'fand-Naimark Representation Theorem" \
  'Let $A$ be a $C^*$-algebra with unity. There exist a Hilbert space $H$ and an isometric unital $*$-representation $\varphi: A \to \mathcal{L}(H)$.' \
  'The Gel\''fand-Naimark theorem is the climax of C*-algebra theory: every C*-algebra can be represented isometrically as a norm-closed *-subalgebra of $\mathcal{L}(H)$ for some Hilbert space $H$. The proof constructs the universal representation as the direct sum of the GNS representations associated to all states.'

# ============ SECTION 63 ============

write_concept "wiener-theorem-absolutely-convergent" "theorem" \
  "Wiener's Theorem on Absolutely Convergent Fourier Series" \
  'The reciprocal of a nowhere vanishing absolutely convergent trigonometric series is also an absolutely convergent trigonometric series.' \
  'Wiener\''s theorem states that if a function on the circle has an absolutely convergent Fourier series and never vanishes, then its reciprocal also has an absolutely convergent Fourier series. Gel\''fand\''s elegant proof uses the Gel\''fand transform on the Banach algebra $l^1(\mathbb{Z})$ and the fact that the character space of $l^1(\mathbb{Z})$ is the unit circle.'

write_concept "l1-z-character-space-circle" "lemma" \
  "Character Space of l^1(Z) is the Unit Circle" \
  'The correspondence $\mu \mapsto f_\mu$ is a homeomorphism of the unit circle $\mathbb{T} = \{\mu \in \mathbb{C} : |\mu| = 1\}$ with the character space $\mathcal{X}$ of $l^1(\mathbb{Z})$, where $f_\mu(x) = \sum_{n=-\infty}^\infty x(n)\mu^n$.' \
  'The character space (maximal ideal space) of the convolution algebra $l^1(\mathbb{Z})$ is homeomorphic to the unit circle $\mathbb{T}$. Each character is given by evaluation of the Fourier series at a point on the circle. This identification is the key to Gel\''fand\''s proof of Wiener\''s theorem.'

# ============ SECTION 64 ============

write_concept "stone-cech-compactification" "theorem" \
  "Stone-Čech Compactification" \
  'Every completely regular space $T$ may be embedded as a dense subspace of a compact space $\mathcal{X}$ such that every bounded continuous function $x: T \to \mathbb{R}$ extends uniquely to a continuous function on $\mathcal{X}$.' \
  'The Stone-Čech compactification $\beta T$ of a completely regular space $T$ is the maximal compactification with respect to extension of bounded continuous functions. The functional-analytic proof takes $\mathcal{X}$ as the character space of the commutative C*-algebra $\mathcal{C}^\infty(T)$ of bounded continuous functions on $T$.'

write_concept "phi-injective-stone-cech" "lemma" \
  "Embedding into Stone-Čech Compactification is Injective" \
  'The mapping $\varphi: T \to \mathcal{X}$ defined by $\varphi(t) = f_t$ where $f_t(x) = x(t)$ is injective.' \
  'The canonical map from a completely regular space $T$ into its Stone-Čech compactification $\mathcal{X}$ (the character space of $\mathcal{C}^\infty(T)$) is injective. This follows from the complete regularity property: distinct points can be separated by a bounded continuous function.'

write_concept "extension-property-stone-cech" "lemma" \
  "Extension Property of Stone-Čech Compactification" \
  'Every bounded continuous real-valued function $x$ on $T$ extends uniquely to a real-valued continuous function $F$ on $\mathcal{X}$ such that $F \circ \varphi = x$.' \
  'The defining property of the Stone-Čech compactification is that every bounded continuous real-valued function on $T$ extends uniquely to a continuous function on the compactification $\mathcal{X}$. In the functional-analytic construction, the extension is precisely the Gel\''fand transform $\hat{x}$ of the function $x \in \mathcal{C}^\infty(T)$.'

# ============ SECTION 65 ============

write_concept "continuous-functional-calculus-normal" "theorem" \
  "Continuous Functional Calculus for Normal Elements" \
  'Let $A$ be a $C^*$-algebra with unity, let $a \in A$ be a normal element, and let $C$ be the closed $*$-subalgebra generated by $1$ and $a$. There exists a unique isometric unital $*$-isomorphism $\Phi: \mathcal{C}(\sigma(a)) \to C$ such that $\Phi(u) = a$, where $u(\lambda) \equiv \lambda$ on $\sigma(a)$.' \
  'The continuous functional calculus assigns to each continuous function $f$ on the spectrum $\sigma(a)$ of a normal element $a$ in a unital C*-algebra an element $f(a)$ in the C*-subalgebra generated by $a$ and $1$, in such a way that $f \mapsto f(a)$ is an isometric *-isomorphism from $\mathcal{C}(\sigma(a))$ onto that subalgebra. This generalizes the spectral theorem for normal operators.'

write_concept "f-of-a-definition-continuous-calculus" "definition" \
  "Notation f(a) via Continuous Functional Calculus" \
  'With notation as in (65.1), we define $f(a) = \Phi(f)$ for every $f \in \mathcal{C}(\sigma(a))$.' \
  'For a normal element $a$ in a unital C*-algebra and a continuous function $f$ on $\sigma(a)$, the notation $f(a)$ denotes the image of $f$ under the continuous functional calculus isomorphism $\Phi$. This generalizes polynomial evaluation $p(a)$ to arbitrary continuous functions.'

write_concept "spectral-mapping-theorem-continuous" "theorem" \
  "Spectral Mapping Theorem (Continuous Functional Calculus)" \
  'If $a$ is a normal element of a $C^*$-algebra with unity, and if $f \in \mathcal{C}(\sigma(a))$, then $\sigma(f(a)) = f(\sigma(a))$.' \
  'The spectral mapping theorem for the continuous functional calculus states that the spectrum of $f(a)$ is the image of the spectrum of $a$ under $f$: $\sigma(f(a)) = f(\sigma(a))$. This generalizes the polynomial spectral mapping theorem to arbitrary continuous functions and follows from the fact that the continuous functional calculus is an isometric *-isomorphism.'

write_concept "star-homomorphism-commutes-continuous-calculus" "theorem" \
  "*-Homomorphisms Commute with Continuous Functional Calculus" \
  'Let $A$ and $B$ be $C^*$-algebras with unity, let $\varphi: A \to B$ be a unital $*$-homomorphism, and let $a \in A$ be normal. Then $\varphi(f(a)) = f(\varphi(a))$ for all $f \in \mathcal{C}(\sigma(a))$.' \
  'Unital *-homomorphisms between C*-algebras commute with the continuous functional calculus: applying $\varphi$ after forming $f(a)$ is the same as forming $f(\varphi(a))$. This is because both sides define *-homomorphisms $\mathcal{C}(\sigma(a)) \to B$ sending the identity function to $\varphi(a)$, and the continuous functional calculus is uniquely determined by this property.'

# ============ SECTION 66 ============

write_concept "rational-functions-q-sigma" "definition" \
  "Rational Functions Regular on a Subset" \
  'If $\sigma$ is a nonempty subset of the Riemann sphere $\mathfrak{S}$ and if $f \in \mathbb{C}(t; \sigma)$ (a rational form with no poles in $\sigma$), then $Q(\sigma)$ denotes the set of all restrictions $f|\sigma: \sigma \to \mathbb{C}$.' \
  'For a subset $\sigma$ of the Riemann sphere, $Q(\sigma)$ is the algebra of restrictions to $\sigma$ of rational functions having no poles in $\sigma$. When $\sigma$ is compact, $Q(\sigma) \subset \mathcal{C}(\sigma)$. This is the starting point for the theory of spectral sets and the analytic functional calculus for nonnormal operators.'

write_concept "q-sigma-algebra-proposition" "proposition" \
  "Q(sigma) is a Function Algebra" \
  '(i) $Q(\sigma)$ is an algebra of functions, for every $\sigma \subset \mathfrak{S}$. (ii) If $\sigma$ is a closed (i.e., compact) subset of $\mathfrak{S}$, then $Q(\sigma) \subset \mathcal{C}(\sigma)$.' \
  'For any subset $\sigma$ of the Riemann sphere, the rational functions $Q(\sigma)$ form an algebra. When $\sigma$ is compact, these are continuous complex-valued functions, so $Q(\sigma)$ is a subalgebra of the commutative C*-algebra $\mathcal{C}(\sigma)$.'

write_concept "sup-norm-on-subset-riemann-sphere" "definition" \
  "Uniform Norm on a Subset of Riemann Sphere" \
  'If $\sigma \subset \mathfrak{S}$ and $f$ is a function defined on $\sigma$, then $\|f\|_\sigma = \sup\{|f(\lambda)| : \lambda \in \sigma\}$, with the convention that $|\infty| = \infty$.' \
  'The uniform norm $\|f\|_\sigma$ of a function on a subset $\sigma$ of the Riemann sphere is the supremum of absolute values over $\sigma$, with $|\infty| = \infty$. A function has finite norm iff it is bounded on $\sigma$ and does not take the value $\infty$.'

write_concept "spectral-set-characterization-inequality" "proposition" \
  "Spectral Set Characterization via Norm Inequality" \
  'Let $\sigma(T) \subset \sigma \subset \mathfrak{S}$. Then $\sigma$ is a spectral set for $T$ iff whenever $f \in \mathbb{C}(t)$ and $\|f\|_\sigma \leq 1$, then $\|f(T)\| \leq 1$.' \
  'A set $\sigma$ containing the spectrum is a spectral set for an operator $T$ precisely when $\|f\|_\sigma \leq 1$ implies $\|f(T)\| \leq 1$ for all rational functions $f$. This reformulation of the definition is technically convenient for verifying spectral set properties.'

write_concept "superset-of-spectral-set" "proposition" \
  "Superset of a Spectral Set is a Spectral Set" \
  'If $\sigma$ is a spectral set for $T$ and if $\tau \supset \sigma$, then $\tau$ is also a spectral set for $T$.' \
  'The property of being a spectral set is monotone with respect to inclusion: any superset $\tau \supseteq \sigma$ of a spectral set $\sigma$ is also a spectral set for the same operator $T$. This is immediate from the definition since rational functions with no poles in $\tau$ also have no poles in $\sigma$.'

write_concept "normal-spectrum-is-spectral-set" "corollary" \
  'Spectrum of a Normal Operator is a Spectral Set' \
  'If $T$ is normal then $\sigma(T)$ is a spectral set for $T$.' \
  'For a normal operator $T$, the spectrum $\sigma(T)$ is a spectral set. This is because normal operators are normaloid ($\|T\| = r(T)$), and $f(T)$ is normal when $T$ is normal and $f$ is rational with no poles on $\sigma(T)$. The continuous functional calculus provides an even stronger result for normal operators.'

write_concept "unitary-iff-circle-spectral-set" "theorem" \
  "Characterization of Unitary Operators via Spectral Sets" \
  'An operator $T$ is unitary (i.e., $T^*T = TT^* = I$) iff the unit circle $\mathbb{T} = \{\lambda \in \mathbb{C} : |\lambda| = 1\}$ is a spectral set for $T$.' \
  'An operator on Hilbert space is unitary precisely when the unit circle is a spectral set for it. This gives an involution-free characterization of unitary operators purely in terms of rational function estimates, and shows how spectral sets can capture operator-theoretic properties algebraically.'

write_concept "self-adjoint-iff-real-spectral-set" "theorem" \
  "Characterization of Self-Adjoint Operators via Spectral Sets" \
  'An operator $T$ is self-adjoint ($T^* = T$) iff $\mathbb{R}$ is a spectral set for $T$.' \
  'An operator is self-adjoint exactly when the real line is a spectral set for it. This perfects the analogy between self-adjointness and reality: while an operator with real spectrum need not be self-adjoint, requiring $\mathbb{R}$ to be a spectral set (a stronger condition) is equivalent to self-adjointness.'

write_concept "homomorphism-from-spectral-set-q-sigma" "proposition" \
  "Functional Calculus Homomorphism from Spectral Set" \
  'If $\sigma$ is a spectral set for $T$, then the correspondence $f|\sigma \mapsto f(T)$ defines a unital algebra homomorphism $Q(\sigma) \to \mathcal{L}(H)$.' \
  'A spectral set $\sigma$ for $T$ yields a functional calculus: the map sending the restriction $f|\sigma$ of a rational function to the operator $f(T)$ is a well-defined unital algebra homomorphism from $Q(\sigma)$ into $\mathcal{L}(H)$. This homomorphism is automatically continuous when $\sigma$ is closed.'

write_concept "sigma-analytic-functions-definition" "definition" \
  "Sigma-Analytic Functions" \
  'Let $\sigma$ be a closed subset of $\mathfrak{S}$. The closure of $Q(\sigma)$ in $\mathcal{C}(\sigma)$ with respect to the sup norm is denoted $\mathcal{A}(\sigma)$; a function in $\mathcal{A}(\sigma)$ is said to be $\sigma$-analytic.' \
  'A function $f$ on a closed set $\sigma \subset \mathfrak{S}$ is called $\sigma$-analytic if it can be uniformly approximated on $\sigma$ by rational functions with no poles in $\sigma$. The algebra $\mathcal{A}(\sigma)$ is the uniform closure of $Q(\sigma)$ in $\mathcal{C}(\sigma)$, and it supports an extended functional calculus for operators admitting $\sigma$ as a spectral set.'

write_concept "sigma-analytic-functional-calculus-theorem" "theorem" \
  "Sigma-Analytic Functional Calculus" \
  'If $\sigma$ is a closed spectral set for $T$, the homomorphism $Q(\sigma) \to \mathcal{L}(H)$ extends uniquely to a continuous unital algebra homomorphism $\mathcal{A}(\sigma) \to \mathcal{L}(H)$, also of norm $\leq 1$.' \
  'When $\sigma$ is a closed spectral set for $T$, the rational functional calculus extends by continuity to a unital algebra homomorphism from the $\sigma$-analytic functions $\mathcal{A}(\sigma)$ into $\mathcal{L}(H)$. This yields an analytic functional calculus applicable to nonnormal operators, extending the continuous functional calculus for normal operators.'

write_concept "spectral-set-operator-notation" "definition" \
  "Notation f^sigma(T) for Spectral Set Calculus" \
  'If $f \in \mathcal{A}(\sigma)$, the operator $\Phi(f)$ is denoted $f^\sigma(T)$ (or briefly $f(T)$, with the dependence on $\sigma$ tacitly understood).' \
  'For a closed spectral set $\sigma$, the image of a $\sigma$-analytic function $f$ under the extended functional calculus is denoted $f^\sigma(T)$ or simply $f(T)$. This generalizes the functional calculus notation $f(T)$ from the normal case to operators with a given spectral set.'

write_concept "sigma-analytic-implies-analytic-interior" "proposition" \
  "Sigma-Analytic Functions are Analytic on the Interior" \
  'If $\sigma$ is a closed subset of $\mathfrak{S}$ and if $f \in \mathcal{A}(\sigma)$, then $f$ is analytic at every interior point of $\sigma$.' \
  'Every $\sigma$-analytic function is analytic (holomorphic) at interior points of $\sigma$, since it is the uniform limit of rational (hence analytic) functions on neighborhoods of interior points. This shows that $\mathcal{A}(\sigma)$ is generally a proper subalgebra of $\mathcal{C}(\sigma)$ when $\sigma$ has nonempty interior.'

write_concept "von-neumann-inequality-polynomial" "lemma" \
  "von Neumann Inequality for Polynomials" \
  'If $\|T\| \leq 1$ then $\|p(T)\| \leq \|p\|_{\Delta_1}$ for every complex polynomial $p$, where $\Delta_1$ is the closed unit disc.' \
  'The von Neumann inequality states that for any Hilbert space contraction $T$ ($\|T\| \leq 1$) and any polynomial $p$, the operator norm of $p(T)$ is bounded by the supremum norm of $p$ on the unit disc $\Delta_1$. This is the key lemma leading to von Neumann\''s theorem that the unit disc is a spectral set for every contraction.'

write_concept "polynomial-approximation-rational-disk" "lemma" \
  "Polynomial Approximation of Rational Functions on the Disc" \
  'If $\|T\| \leq 1$ and $f \in \mathbb{C}(t; \Delta_1)$, then there exists a sequence of complex polynomials $f_n$ such that $\|f_n(T) - f(T)\| \to 0$.' \
  'For a contraction $T$, every rational function $f$ with poles outside the closed unit disc $\Delta_1$ can be approximated in the operator norm topology by polynomials evaluated at $T$. The proof uses Taylor series expansion and the fact that $\|T\| \leq 1$ ensures convergence of the series in operator norm.'

write_concept "von-neumann-unit-ball-spectral-set" "theorem" \
  "von Neumann Theorem: Unit Disc is Spectral Set for Contractions" \
  '$\|T\| \leq 1$ iff the closed unit disc $\Delta_1 = \{\lambda \in \mathbb{C} : |\lambda| \leq 1\}$ is a spectral set for $T$.' \
  'Von Neumann\''s fundamental theorem on spectral sets: an operator on Hilbert space is a contraction ($\|T\| \leq 1$) if and only if the closed unit disc is a spectral set for it. This is a deep result showing that the operator norm condition $\|T\| \leq 1$ is equivalent to a much stronger rational function estimate, and it launched the theory of spectral sets for nonnormal operators.'

# ============ SECTION 67 ============

write_concept "hilbert-space-derived-from-psf" "definition" \
  "Hilbert Space Derived from a Positive Sesquilinear Form" \
  'Let $\varphi$ be a positive sesquilinear form on a complex vector space $A$. Let $N_\varphi = \{x \in A : \varphi(x,x) = 0\}$, $A_\varphi = A/N_\varphi$, and define $(x_\varphi|y_\varphi) = \varphi(x,y)$ on $A_\varphi$. The completion $H_\varphi$ of the pre-Hilbert space $A_\varphi$ is called the Hilbert space derived from $\varphi$.' \
  'From any positive sesquilinear form $\varphi$ on a complex vector space $A$, one constructs a Hilbert space $H_\varphi$ by quotienting out the null space $N_\varphi = \{x: \varphi(x,x)=0\}$ and completing. This general construction underlies the GNS construction (where $\varphi(x,y) = f(y^*x)$) and the theory of representations of *-algebras.'

write_concept "ordering-hermitian-sesquilinear-forms" "definition" \
  "Partial Ordering of Hermitian Sesquilinear Forms" \
  'Let $\varphi$ and $\psi$ be Hermitian sesquilinear forms on a complex vector space $A$. We write $\psi \leq \varphi$ in case $\psi(x,x) \leq \varphi(x,x)$ for all $x \in A$.' \
  'Hermitian sesquilinear forms on a complex vector space are partially ordered by pointwise comparison of their quadratic forms: $\psi \leq \varphi$ iff $\psi(x,x) \leq \varphi(x,x)$ for all $x$. This is a genuine partial order because of the polarization identity: if $\psi \leq \varphi$ and $\varphi \leq \psi$, then $\psi = \varphi$.'

write_concept "psf-dominated-by-inner-product-lemma" "lemma" \
  "PSF Dominated by Inner Product Comes from a Contraction" \
  'If $\psi$ is a PSF on a dense subspace $A$ of a Hilbert space $H$ and $\psi(x,x) \leq (x|x)$ for all $x \in A$, then there exists $T \in \mathcal{L}(H)$ with $0 \leq T \leq I$ such that $\psi(x,y) = (Tx|y)$ for all $x, y \in A$.' \
  'A positive sesquilinear form $\psi$ dominated by the inner product on a Hilbert space arises from a positive contraction $T$ ($0 \leq T \leq I$) via $\psi(x,y) = (Tx|y)$. This lemma is a key linking device between the order structure of PSFs and the operator order on $\mathcal{L}(H)$.'

write_concept "state-adjunctive-psf-bijection" "proposition" \
  "Bijection Between States and Adjunctive PSFs" \
  'If $f$ is a state on a $*$-algebra $A$, then $\varphi_f(x,y) = f(y^*x)$ defines an adjunctive PSF on $A$. Conversely, if $A$ has a unity element $1$ and $\varphi$ is an adjunctive PSF, then $f_\varphi(x) = \varphi(x,1)$ defines a state. These correspondences are mutually inverse bijections preserving convex combinations.' \
  'On a unital *-algebra, there is a natural bijective correspondence between states and adjunctive positive sesquilinear forms, given by $\varphi(x,y) = f(y^*x)$ and $f(x) = \varphi(x,1)$. Both sets are convex and the correspondence is affine, allowing one to translate freely between the language of states and the language of PSFs.'

write_concept "gns-notation-from-state" "definition" \
  "GNS Hilbert Space Notation for a State" \
  'If $f$ is a state on a $*$-algebra $A$, the notations $N_f$, $x_f$, $A_f$, $H_f$ denote: $N_f = \{x \in A : f(x^*x) = 0\}$, $x_f = x + N_f$, the inner product on $A_f = A/N_f$ is $(x_f|y_f) = f(y^*x)$, and $H_f$ is the Hilbert space completion of $A_f$.' \
  'The GNS construction from a state $f$ on a *-algebra $A$ produces a Hilbert space $H_f$ by completing $A/N_f$ with inner product $(x_f|y_f) = f(y^*x)$. The subspace $N_f$ is a left ideal (when $f$ is admissible), and the left regular representation yields a *-representation of $A$ on $H_f$.'

write_concept "algebra-homomorphism-left-multiplication-psf" "proposition" \
  "Left Multiplication Homomorphism from PSF" \
  'Let $\varphi$ be an adjunctive PSF on a $*$-algebra $A$. The correspondence $a \mapsto T_a$ defined by $T_a x_\varphi = (ax)_\varphi$ is an algebra homomorphism of $A$ into the algebra of linear mappings on $A_\varphi$, satisfying $(T_a x_\varphi|y_\varphi) = (x_\varphi|T_{a^*} y_\varphi)$.' \
  'From an adjunctive PSF $\varphi$ on a *-algebra $A$, the left multiplication $a \mapsto T_a$ (where $T_a x_\varphi = (ax)_\varphi$) defines an algebra homomorphism into the linear endomorphisms of $A_\varphi$ that respects the adjoint operation: $T_a$ and $T_{a^*}$ are formal adjoints with respect to the inner product induced by $\varphi$.'

write_concept "admissible-psf-definition" "definition" \
  "Admissible Positive Sesquilinear Form" \
  'A PSF $\varphi$ on a $*$-algebra $A$ is said to be admissible if (i) $\varphi$ is adjunctive, and (ii) for each $a \in A$ there exists a constant $K_a \geq 0$ such that $\varphi(ax,ax) \leq K_a \varphi(x,x)$ for all $x \in A$.' \
  'Admissibility of a PSF on a *-algebra is the condition that left multiplication by any fixed element $a$ is bounded with respect to the quadratic form $\varphi$. This ensures that the left multiplication operators $T_a$ extend continuously to the Hilbert space completion $H_\varphi$, yielding a genuine *-representation on a Hilbert space.'

write_concept "star-representation-admissible-psf" "theorem" \
  "*-Representation from Admissible PSF" \
  'If $\varphi$ is an admissible PSF on a $*$-algebra $A$, then there exists a unique $*$-representation $a \mapsto T_a$ of $A$ on $H_\varphi$ such that $\varphi(ax,y) = (T_a x_\varphi|y_\varphi)$ for all $a,x,y \in A$. Moreover, the adjunctive PSFs $\psi$ on $A$ with $\psi \leq \varphi$ correspond precisely to operators $T \in \{T_a : a \in A\}''$ with $0 \leq T \leq I$ via $\psi = \varphi_T$.' \
  'Every admissible PSF on a *-algebra yields a *-representation on the derived Hilbert space $H_\varphi$ via left multiplication. Additionally, the order structure of PSFs below $\varphi$ is in bijection with positive contractions in the commutant of the representation, a powerful structural result linking the order theory of forms with operator theory.'

write_concept "irreducible-psf-definition" "definition" \
  "Irreducible Positive Sesquilinear Form" \
  'An admissible PSF $\varphi$ is said to be irreducible if the only adjunctive PSFs $\psi$ on $A$ such that $\psi \leq \varphi$ are the scalar multiples $\psi = \alpha \varphi$, $0 \leq \alpha \leq 1$.' \
  'An admissible PSF $\varphi$ on a *-algebra is called irreducible if its only dominated adjunctive PSFs are the scalar multiples $\alpha\varphi$ ($0 \leq \alpha \leq 1$). This definition captures the notion that the associated *-representation has no nontrivial invariant subspaces (is irreducible in the operator-theoretic sense).'

write_concept "irreducible-psf-characterization" "corollary" \
  "Characterization of Irreducible PSF" \
  'An admissible PSF $\varphi$ is irreducible iff the only operators in the commutant $\{T_a : a \in A\}''$ that are hermitian ($T = T^*$) and satisfy $0 \leq T \leq I$ are the scalar multiples of the identity.' \
  'By the correspondence theorem, irreducibility of an admissible PSF $\varphi$ is equivalent to the condition that the only hermitian operators in the positive unit ball of the commutant are scalars. Equivalently (by considering spectral projections), the commutant of the representation is trivial, i.e., consists only of scalar multiples of the identity.'

write_concept "state-ordering-admissible-irreducible" "definition" \
  "Ordering, Admissibility, and Irreducibility for States" \
  'For states $f,g$ on a $*$-algebra $A$: $g \leq f$ means $f-g$ is a state (i.e., $g(x^*x) \leq f(x^*x)$). $f$ is admissible if $\varphi_f$ is an admissible PSF. $f$ is irreducible if $\varphi_f$ is an irreducible PSF.' \
  'The concepts of ordering, admissibility, and irreducibility for PSFs transfer to states via the bijection $f \leftrightarrow \varphi_f$. A state $f$ is admissible when left multiplication by any fixed element is bounded with respect to the quadratic form $f(x^*x)$, ensuring the GNS construction yields a genuine *-representation on a Hilbert space.'

write_concept "star-representation-admissible-state" "theorem" \
  "*-Representation from Admissible State" \
  'Let $A$ be a $*$-algebra with unity element $1$, and let $f$ be an admissible state on $A$. There exists a unique $*$-representation $a \mapsto T_a$ of $A$ on $H_f$ and a cyclic vector $u = 1_f \in H_f$ such that $f(a) = (T_a u|u)$ for all $a \in A$. The states $g$ on $A$ with $g \leq f$ correspond to operators $T$ in the commutant with $0 \leq T \leq I$ via $g(a) = (T T_a u|u)$.' \
  'The GNS representation theorem for admissible states on a unital *-algebra: to each admissible state $f$ corresponds a cyclic *-representation $(T_a, H_f, u = 1_f)$ with $f(a) = (T_a u|u)$. The order interval $[0,f]$ of states is isomorphic to the positive unit ball of the commutant, generalizing the Radon-Nikodym theorem for states on C*-algebras.'

write_concept "extremal-state-equals-irreducible" "theorem" \
  "Extremal States are Precisely Irreducible States" \
  'Let $A$ be a $*$-algebra with unity and let $\Omega$ be the set of normalized admissible states on $A$. For $f \in \Omega$, the following are equivalent: (a) $f$ is an extremal point of $\Omega$; (b) $f$ is irreducible; (c) if $g$ is any state on $A$ such that $g \leq f$, then $g = \alpha f$ with $0 \leq \alpha \leq 1$.' \
  'For normalized admissible states on a unital *-algebra, the concepts of extremal point (in the convex set of all such states), irreducibility (of the associated PSF), and minimality with respect to the state ordering coincide. This is a fundamental result linking convexity theory with representation theory, and it underpins the proof that every C*-algebra has a complete set of irreducible representations.'

write_concept "state-on-c-star-algebra-admissible" "lemma" \
  "Every State on a C*-Algebra is Admissible" \
  'If $A$ is a $C^*$-algebra with unity, then every state on $A$ is admissible.' \
  'In a unital C*-algebra, every state is automatically admissible. This is proved in the GNS construction: for any state $f$ and element $a$, the inequality $f(x^*a^*ax) \leq \|a\|^2 f(x^*x)$ follows from the positivity of $\|a\|^2 1 - a^*a$, ensuring the boundedness condition required for admissibility.'

write_concept "complete-set-irreducible-representations" "theorem" \
  "Gel'fand-Naimark: Complete Set of Irreducible *-Representations" \
  'Every $C^*$-algebra with unity has a complete set of irreducible $*$-representations. That is, if $a,b \in A$ with $a \neq b$, there exists an irreducible $*$-representation $\pi$ of $A$ on a Hilbert space $H$ such that $\pi(a) \neq \pi(b)$.' \
  'A deep reformulation of the Gel\''fand-Naimark theorem: every unital C*-algebra has sufficiently many irreducible *-representations to separate its elements. The proof combines the Krein-Mil\''man theorem (the state space is the weak* closed convex hull of its extreme points) with the equivalence between extremal states and irreducible representations.'
