#!/usr/bin/env python3
"""Extract ALL concepts from GTM012 sections and write 3 files each."""

import os, json

BASE = '/home/a123/文档/mathpkg/pipeline_output/concepts_v7/gtm012/共 34 个 section 文件：'
os.makedirs(BASE, exist_ok=True)

def make(slug, typ, title_en, domain, subdomain, difficulty, chapter, section, tex):
    d = os.path.join(BASE, slug)
    os.makedirs(d, exist_ok=True)

    # concept.yaml
    yaml = f"""id: "{slug}"
title_en: "{title_en}"
title_zh: ""
type: {typ}
domain: {domain}
subdomain: {subdomain}
difficulty: {difficulty}
tags: []
depends_on: {{required: [], recommended: [], suggested: []}}
source_books: [{{book_id: "gtm012", author: "Richard Beals", title: "Advanced Mathematical Analysis", chapter: "{chapter}", section: "{section}", pages: "", role_in_book: ""}}]
content_hash: ""
extraction_date: "2026-06-25"
extraction_agent: "v7-section-test"
"""
    with open(os.path.join(d, "concept.yaml"), "w") as f:
        f.write(yaml)

    # theorem.tex
    with open(os.path.join(d, "theorem.tex"), "w") as f:
        f.write(tex + "\n")

    # introduce.en.md
    md = f"""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

{title_en}. A fundamental {typ} in {domain}, from {chapter} of Beals'"'"' Advanced Mathematical Analysis.
"""
    with open(os.path.join(d, "introduce.en.md"), "w") as f:
        f.write(md)

    print(f"Created: {slug}")

###############################################################################
# CHAPTER 1: BASIC CONCEPTS
###############################################################################

# §2 - Axioms of real numbers
make("axiom-addition-associativity", "axiom",
    "Associativity of Addition (A1)", "analysis", "real-numbers", "basic",
    "1", "§2. Real and complex numbers",
    r"$$(x + y) + z = x + (y + z), \quad \text{for any } x, y, z \in \mathbb{R}.$$")

make("axiom-addition-commutativity", "axiom",
    "Commutativity of Addition (A2)", "analysis", "real-numbers", "basic",
    "1", "§2. Real and complex numbers",
    r"$$x + y = y + x, \quad \text{for any } x, y \in \mathbb{R}.$$")

make("axiom-additive-identity", "axiom",
    "Existence of Additive Identity (A3)", "analysis", "real-numbers", "basic",
    "1", "§2. Real and complex numbers",
    r"There is an element $0 \in \mathbb{R}$ such that $x + 0 = x$ for every $x \in \mathbb{R}.$")

make("axiom-additive-inverse", "axiom",
    "Existence of Additive Inverse (A4)", "analysis", "real-numbers", "basic",
    "1", "§2. Real and complex numbers",
    r"For each $x \in \mathbb{R}$ there is an element $-x \in \mathbb{R}$ such that $x + (-x) = 0.$")

make("axiom-multiplication-associativity", "axiom",
    "Associativity of Multiplication (M1)", "analysis", "real-numbers", "basic",
    "1", "§2. Real and complex numbers",
    r"$$(xy)z = x(yz), \quad \text{for any } x, y, z \in \mathbb{R}.$$")

make("axiom-multiplication-commutativity", "axiom",
    "Commutativity of Multiplication (M2)", "analysis", "real-numbers", "basic",
    "1", "§2. Real and complex numbers",
    r"$$xy = yx, \quad \text{for any } x, y \in \mathbb{R}.$$")

make("axiom-multiplicative-identity", "axiom",
    "Existence of Multiplicative Identity (M3)", "analysis", "real-numbers", "basic",
    "1", "§2. Real and complex numbers",
    r"There is an element $1 \in \mathbb{R}$ with $1 \neq 0$ such that $x \cdot 1 = x$ for every $x \in \mathbb{R}.$")

make("axiom-multiplicative-inverse", "axiom",
    "Existence of Multiplicative Inverse (M4)", "analysis", "real-numbers", "basic",
    "1", "§2. Real and complex numbers",
    r"For each $x \in \mathbb{R}$ with $x \neq 0$, there is an element $x^{-1} \in \mathbb{R}$ such that $x \cdot x^{-1} = 1.$")

make("axiom-distributive-law", "axiom",
    "Distributive Law (DL)", "analysis", "real-numbers", "basic",
    "1", "§2. Real and complex numbers",
    r"$$x(y + z) = xy + xz, \quad \text{for any } x, y, z \in \mathbb{R}.$$")

make("axiom-order-trichotomy", "axiom",
    "Order Axiom: Trichotomy (O1)", "analysis", "real-numbers", "basic",
    "1", "§2. Real and complex numbers",
    r"If $x \in \mathbb{R}$, exactly one holds: $x \in P$, $x = 0$, or $-x \in P$, where $P \subset \mathbb{R}$ is the set of positive elements.")

make("axiom-order-addition-closure", "axiom",
    "Order Axiom: Addition Closure (O2)", "analysis", "real-numbers", "basic",
    "1", "§2. Real and complex numbers",
    r"If $x, y \in P$, then $x + y \in P.$")

make("axiom-order-multiplication-closure", "axiom",
    "Order Axiom: Multiplication Closure (O3)", "analysis", "real-numbers", "basic",
    "1", "§2. Real and complex numbers",
    r"If $x, y \in P$, then $xy \in P.$")

make("completeness-axiom", "axiom",
    "Completeness Axiom (O5)", "analysis", "real-numbers", "basic",
    "1", "§2. Real and complex numbers",
    r"If $A$ is a nonempty subset of $\mathbb{R}$ which is bounded above, then $A$ has a least upper bound.")

# Definitions from §2
make("upper-bound-definition", "definition",
    "Upper Bound and Bounded Above", "analysis", "real-numbers", "basic",
    "1", "§2. Real and complex numbers",
    r"A nonempty subset $A \subset \mathbb{R}$ is \text{bounded above} if there is $x \in \mathbb{R}$ such that every $y \in A$ satisfies $y \leq x$. Such $x$ is an \text{upper bound} for $A$.")

make("least-upper-bound-definition", "definition",
    "Least Upper Bound (Supremum) and Greatest Lower Bound (Infimum)", "analysis", "real-numbers", "basic",
    "1", "§2. Real and complex numbers",
    r"A number $x$ is a \text{least upper bound} for $A \subset \mathbb{R}$ if $x$ is an upper bound and $x' \geq x$ for every upper bound $x'$. We write $x = \operatorname{lub} A$. Similarly for greatest lower bound $x = \operatorname{glb} A$.")

make("rationals-not-complete", "theorem",
    "Rational Numbers Do Not Satisfy Completeness", "analysis", "real-numbers", "basic",
    "1", "§2. Real and complex numbers",
    r"$\mathbb{Q}$ does not satisfy the completeness axiom O5.")

make("complex-numbers-construction", "definition",
    "Complex Numbers via $\mathbb{R}^2$", "analysis", "complex-analysis", "basic",
    "1", "§2. Real and complex numbers",
    r"Let $\mathbb{C}^0 = \mathbb{R}^2$. Define $(x,y)+(u,v) = (x+u, y+v)$ and $(x,y)(u,v) = (xu-yv, xv+yu)$. With $i = (0,1)$, $i^2 = -1$ and $(x,y) = x+iy$.")

make("complex-conjugate-definition", "definition",
    "Complex Conjugation", "analysis", "complex-analysis", "basic",
    "1", "§2. Real and complex numbers",
    r"For $z = x + iy \in \mathbb{C}$, the complex conjugate is $z^* = x - iy$.")

make("complex-modulus-definition", "definition",
    "Modulus of a Complex Number", "analysis", "complex-analysis", "basic",
    "1", "§2. Real and complex numbers",
    r"For $z = x + iy \in \mathbb{C}$, the modulus is $|z| = (z^*z)^{1/2} = (x^2 + y^2)^{1/2}.$")

# §3 Sequences
make("sequence-convergence-definition", "definition",
    "Convergence of a Sequence in $\mathbb{C}$", "analysis", "real-analysis", "basic",
    "1", "§3. Sequences of real and complex numbers",
    r"A sequence $(z_n)_{n=1}^{\infty} \subset \mathbb{C}$ converges to $z \in \mathbb{C}$ if $\forall \varepsilon > 0$, $\exists N$ such that $|z_n - z| < \varepsilon$ for $n \geq N$. Write $z_n \to z$ or $\lim z_n = z$.")

make("limit-properties", "proposition",
    "Algebraic Properties of Limits", "analysis", "real-analysis", "basic",
    "1", "§3. Sequences of real and complex numbers",
    r"Suppose $z_n \to z$, $w_n \to w$. Then (a) $z_n + w_n \to z + w$; (b) $a z_n \to a z$; (c) $z_n w_n \to z w$; (d) if $w \neq 0$, $z_n/w_n \to z/w$.")

make("bounded-sequence-definition", "definition",
    "Bounded Sequence", "analysis", "real-analysis", "basic",
    "1", "§3. Sequences of real and complex numbers",
    r"A sequence $(z_n) \subset \mathbb{C}$ is bounded if there is $M \geq 0$ such that $|z_n| \leq M$ for all $n$.")

make("bounded-monotone-convergence", "proposition",
    "Convergence of Bounded Monotone Sequences", "analysis", "real-analysis", "basic",
    "1", "§3. Sequences of real and complex numbers",
    r"A bounded monotone sequence in $\mathbb{R}$ converges.")

make("liminf-limsup-definition", "definition",
    "Limit Inferior and Limit Superior", "analysis", "real-analysis", "basic",
    "1", "§3. Sequences of real and complex numbers",
    r"For bounded $(x_n) \subset \mathbb{R}$, let $x'_n = \sup\{x_k \mid k \geq n\}$, $x''_n = \inf\{x_k \mid k \geq n\}$. Then $\liminf x_n = \lim x''_n$ and $\limsup x_n = \lim x'_n$.")

make("cauchy-sequence-definition", "definition",
    "Cauchy Sequence", "analysis", "real-analysis", "basic",
    "1", "§3. Sequences of real and complex numbers",
    r"A sequence $(z_n) \subset \mathbb{C}$ is Cauchy if $\forall \varepsilon > 0$, $\exists N$ such that $|z_n - z_m| < \varepsilon$ for $n, m \geq N$.")

make("cauchy-completeness", "theorem",
    "Completeness of $\mathbb{R}$ and $\mathbb{C}$ (Cauchy Criterion)", "analysis", "real-analysis", "basic",
    "1", "§3. Sequences of real and complex numbers",
    r"A sequence in $\mathbb{C}$ (or $\mathbb{R}$) converges if and only if it is a Cauchy sequence.")

make("liminf-limsup-characterization", "proposition",
    "Characterization of $\liminf$ and $\limsup$", "analysis", "real-analysis", "basic",
    "1", "§3. Sequences of real and complex numbers",
    r"$\liminf x_n$ is the unique $x'$ such that: (i) $\forall\varepsilon>0$, $\exists N$, $x_n > x'-\varepsilon$ for $n\geq N$; (ii) $\forall\varepsilon>0$, $\forall N$, $\exists n\geq N$, $x_n < x'+\varepsilon$. $\limsup x_n$ is analogous.")

# §4 Series
make("infinite-series-definition", "definition",
    "Infinite Series", "analysis", "real-analysis", "basic",
    "1", "§4. Series",
    r"The series $\sum z_n$ has partial sums $s_n = \sum_{m=1}^n z_m$. If $(s_n)$ converges to $s$, the series converges with sum $s$.")

make("series-term-zero", "proposition",
    "Term of Convergent Series Tends to Zero", "analysis", "real-analysis", "basic",
    "1", "§4. Series",
    r"If $\sum z_n$ converges, then $z_n \to 0$ as $n \to \infty$.")

make("absolute-convergence", "proposition",
    "Absolute Convergence Implies Convergence", "analysis", "real-analysis", "basic",
    "1", "§4. Series",
    r"If $\sum |z_n|$ converges, then $\sum z_n$ converges.")

make("comparison-test", "proposition",
    "Comparison Test", "analysis", "real-analysis", "basic",
    "1", "§4. Series",
    r"Suppose $|z_n| \leq M a_n$ with $a_n \geq 0$. If $\sum a_n$ converges, then $\sum z_n$ converges.")

make("ratio-test", "proposition",
    "Ratio Test", "analysis", "real-analysis", "basic",
    "1", "§4. Series",
    r"Suppose $z_n \neq 0$ for all $n$. (a) If $\limsup |z_{n+1}/z_n| < 1$, $\sum z_n$ converges. (b) If $\liminf |z_{n+1}/z_n| > 1$, $\sum z_n$ diverges.")

make("root-test", "proposition",
    "Root Test", "analysis", "real-analysis", "basic",
    "1", "§4. Series",
    r"(a) If $\limsup |z_n|^{1/n} < 1$, $\sum z_n$ converges. (b) If $\limsup |z_n|^{1/n} > 1$, $\sum z_n$ diverges.")

make("root-test-limit-form", "corollary",
    "Limit Form of Root Test", "analysis", "real-analysis", "basic",
    "1", "§4. Series",
    r"If $\lim |z_n|^{1/n}$ exists, $\sum z_n$ converges if the limit $< 1$, diverges if $> 1$.")

make("power-series-definition", "definition",
    "Power Series", "analysis", "real-analysis", "basic",
    "1", "§4. Series",
    r"A power series around $z_0$ with coefficients $(a_n)_{n=0}^{\infty}$ is $\sum_{n=0}^{\infty} a_n(z - z_0)^n$.")

make("radius-of-convergence-hadamard", "theorem",
    "Hadamard Formula for Radius of Convergence", "analysis", "real-analysis", "basic",
    "1", "§4. Series",
    r"The radius of convergence is $R = (\limsup |a_n|^{1/n})^{-1}$. The series converges absolutely for $|z-z_0|<R$ and diverges for $|z-z_0|>R$.")

make("radius-of-convergence-ratio", "theorem",
    "Radius of Convergence from Ratio Test", "analysis", "real-analysis", "basic",
    "1", "§4. Series",
    r"If $\lim |a_{n+1}/a_n|$ exists, then $R = (\lim |a_{n+1}/a_n|)^{-1}$ if the limit $>0$, and $R=\infty$ if the limit $=0$.")

# §5 Metric spaces
make("metric-space-definition", "definition",
    "Metric Space", "analysis", "metric-spaces", "basic",
    "1", "§5. Metric spaces",
    r"A metric on $S$ is $d: S\times S \to \mathbb{R}$ with: D1. $d(x,x)=0$, $d(x,y)>0$ if $x\neq y$; D2. $d(x,y)=d(y,x)$; D3. $d(x,z)\leq d(x,y)+d(y,z)$. $(S,d)$ is a metric space.")

make("ball-definition", "definition",
    "Ball in a Metric Space", "analysis", "metric-spaces", "basic",
    "1", "§5. Metric spaces",
    r"In $(S,d)$, the ball of radius $r>0$ about $x$ is $B_r(x) = \{y \in S \mid d(x,y) < r\}$.")

make("open-set-definition", "definition",
    "Open Set in a Metric Space", "analysis", "metric-spaces", "basic",
    "1", "§5. Metric spaces",
    r"$A \subset S$ is open if for each $x \in A$ there is $r > 0$ such that $B_r(x) \subset A$.")

make("limit-point-definition", "definition",
    "Limit Point (Accumulation Point)", "analysis", "metric-spaces", "basic",
    "1", "§5. Metric spaces",
    r"$x \in S$ is a limit point of $A \subset S$ if $\forall r>0$, $B_r(x) \cap A \neq \varnothing$.")

make("closed-set-definition", "definition",
    "Closed Set", "analysis", "metric-spaces", "basic",
    "1", "§5. Metric spaces",
    r"$A \subset S$ is closed if it contains all its limit points.")

make("balls-are-open", "proposition",
    "Balls Are Open Sets", "analysis", "metric-spaces", "basic",
    "1", "§5. Metric spaces",
    r"Each ball $B_r(x)$ is an open subset of $S$.")

make("topology-properties", "proposition",
    "Topological Properties of Open and Closed Sets", "analysis", "metric-spaces", "basic",
    "1", "§5. Metric spaces",
    r"Finite intersections and arbitrary unions of open sets are open. Finite unions and arbitrary intersections of closed sets are closed.")

make("open-complement-closed", "proposition",
    "Complement of Open is Closed", "analysis", "metric-spaces", "basic",
    "1", "§5. Metric spaces",
    r"$A \subset S$ is open iff its complement is closed.")

make("complete-metric-space-definition", "definition",
    "Complete Metric Space", "analysis", "metric-spaces", "basic",
    "1", "§5. Metric spaces",
    r"A metric space $(S,d)$ is complete if every Cauchy sequence converges.")

# §6 Compactness
make("compact-set-definition", "definition",
    "Compact Set", "analysis", "topology", "intermediate",
    "1", "§5. Metric spaces",
    r"$A \subset S$ is compact if every open cover has a finite subcover.")

make("compact-implies-closed-bounded", "proposition",
    "Compact Implies Closed and Bounded", "analysis", "topology", "intermediate",
    "1", "§5. Metric spaces",
    r"If $A \subset S$ is compact, then $A$ is closed and bounded.")

make("heine-borel", "theorem",
    "Heine-Borel Theorem", "analysis", "topology", "intermediate",
    "1", "§5. Metric spaces",
    r"A closed bounded interval $[a,b] \subset \mathbb{R}$ is compact.")

make("sequentially-compact-definition", "definition",
    "Sequentially Compact", "analysis", "topology", "intermediate",
    "1", "§5. Metric spaces",
    r"$A \subset S$ is sequentially compact if every sequence in $A$ has a subsequence converging to a point of $A$.")

make("sequentially-compact-closed-bounded", "proposition",
    "Sequentially Compact Implies Closed and Bounded", "analysis", "topology", "intermediate",
    "1", "§5. Metric spaces",
    r"If $A \subset S$ is sequentially compact, then $A$ is closed and bounded.")

# §7 Vector spaces
make("vector-space-definition", "definition",
    "Vector Space", "algebra", "linear-algebra", "basic",
    "1", "§5. Metric spaces",
    r"A vector space over $\mathbb{R}$ (or $\mathbb{C}$) is a set $X$ with addition $X \times X \to X$ and scalar multiplication satisfying V1-V8 (associativity, commutativity, identity, inverses, distributivity).")

make("subspace-definition", "definition",
    "Subspace of a Vector Space", "algebra", "linear-algebra", "basic",
    "1", "§5. Metric spaces",
    r"A nonempty $Y \subset X$ is a subspace if $x,y \in Y$, $a$ scalar $\implies x+y \in Y$, $ay \in Y$.")

make("linear-combination-definition", "definition",
    "Linear Combination", "algebra", "linear-algebra", "basic",
    "1", "§5. Metric spaces",
    r"A linear combination of $x_1,\ldots,x_n \in X$ is $x = a_1x_1 + \cdots + a_nx_n$ with scalars $a_j$.")

make("span-definition", "definition",
    "Span", "algebra", "linear-algebra", "basic",
    "1", "§5. Metric spaces",
    r"The span of $S \subset X$ is the set of all linear combinations of elements of $S$; the smallest subspace containing $S$.")

make("linear-dependence-definition", "definition",
    "Linear Dependence and Independence", "algebra", "linear-algebra", "basic",
    "1", "§5. Metric spaces",
    r"$x_1,\ldots,x_n$ are linearly dependent if some nontrivial linear combination is zero. Otherwise they are linearly independent.")

make("linear-dependence-characterization", "lemma",
    "Linear Dependence and Linear Combinations", "algebra", "linear-algebra", "basic",
    "1", "§5. Metric spaces",
    r"$x_1,\ldots,x_n$ ($n \geq 2$) are linearly dependent iff some $x_j$ is a linear combination of the others.")

make("basis-definition", "definition",
    "Basis and Finite-Dimensional Vector Space", "algebra", "linear-algebra", "basic",
    "1", "§5. Metric spaces",
    r"A basis of $X$ is a linearly independent set that spans $X$. $X$ is finite-dimensional if it has a finite basis.")

make("basis-existence-cardinality", "theorem",
    "Existence and Cardinality of Basis", "algebra", "linear-algebra", "intermediate",
    "1", "§5. Metric spaces",
    r"Every finite-dimensional vector space has a basis. Any two bases have the same number of elements, the dimension of $X$.")

make("linear-transformation-definition", "definition",
    "Linear Transformation", "algebra", "linear-algebra", "basic",
    "1", "§5. Metric spaces",
    r"$T: X \to Y$ is linear if $T(x+x') = T(x) + T(x')$ and $T(ax) = aT(x)$ for all vectors $x,x'$ and scalars $a$.")

print("=== Chapter 1 concepts created ===")
