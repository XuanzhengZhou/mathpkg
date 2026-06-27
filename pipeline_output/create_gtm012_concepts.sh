#!/bin/bash
# Batch create concept files for GTM012
set -e
BASE="/home/a123/文档/mathpkg/pipeline_output/concepts_v7/gtm012"
DATE="2026-06-25"
AGENT="v7-section-test"
BOOK='{book_id:"gtm012",author:"Richard Beals",title:"Advanced Mathematical Analysis",chapter:"",section:"",pages:"",role_in_book:""}'

write_concept() {
    local slug="$1" type="$2" title_en="$3" domain="$4" subdomain="$5" difficulty="$6"
    local chapter="$7" section="$8" tex="$9" intro="${10}"
    local D="$BASE/$slug"
    mkdir -p "$D"

    cat > "$D/concept.yaml" << EOF
id: ${slug}
title_en: "${title_en}"
title_zh: ""
type: ${type}
domain: ${domain}
subdomain: ${subdomain}
difficulty: ${difficulty}
tags: []
depends_on: {required:[], recommended:[], suggested:[]}
source_books: [{book_id:"gtm012",author:"Richard Beals",title:"Advanced Mathematical Analysis",chapter:"${chapter}",section:"${section}",pages:"",role_in_book:""}]
content_hash: ""
extraction_date: "${DATE}"
extraction_agent: "${AGENT}"
EOF

    echo "${tex}" > "$D/theorem.tex"
    echo "${intro}" > "$D/introduce.en.md"
}

# ============ CHAPTER 1, SECTION 2: Real and complex numbers ============

write_concept "field-axioms-of-addition" "axiom" "Field Axioms of Addition (A1-A4)" \
  "algebra" "field-axioms" "basic" "1" "2. Real and complex numbers" \
  '\textbf{Axioms of addition.} For any $x, y, z \in \mathbb{R}$:
\begin{align}
\text{A1.}&\quad (x + y) + z = x + (y + z) \\
\text{A2.}&\quad x + y = y + x \\
\text{A3.}&\quad \text{There exists an element } 0 \in \mathbb{R} \text{ such that } x + 0 = x \text{ for every } x \in \mathbb{R} \\
\text{A4.}&\quad \text{For each } x \in \mathbb{R} \text{ there exists } -x \in \mathbb{R} \text{ such that } x + (-x) = 0
\end{align}' \
  'The field axioms of addition define the additive structure of the real numbers. A1 (associativity) and A2 (commutativity) make addition well-behaved. A3 establishes an additive identity $0$, and A4 guarantees additive inverses. Together they make $(\mathbb{R}, +)$ an abelian group.'

write_concept "field-axioms-of-multiplication" "axiom" "Field Axioms of Multiplication (M1-M4)" \
  "algebra" "field-axioms" "basic" "1" "2. Real and complex numbers" \
  '\textbf{Axioms of multiplication.} For any $x, y, z \in \mathbb{R}$:
\begin{align}
\text{M1.}&\quad (xy)z = x(yz) \\
\text{M2.}&\quad xy = yx \\
\text{M3.}&\quad \text{There exists an element } 1 \in \mathbb{R}, 1 \neq 0, \text{ such that } x \cdot 1 = x \text{ for every } x \in \mathbb{R} \\
\text{M4.}&\quad \text{For each } x \in \mathbb{R}, x \neq 0, \text{ there exists } x^{-1} \in \mathbb{R} \text{ such that } x \cdot x^{-1} = 1
\end{align}' \
  'The field axioms of multiplication define the multiplicative structure of the real numbers. M1 (associativity) and M2 (commutativity) make multiplication well-behaved. M3 establishes a multiplicative identity $1$, distinct from $0$. M4 guarantees multiplicative inverses for all nonzero elements. Together with the addition axioms and the distributive law, these make $\mathbb{R}$ a field.'

write_concept "distributive-law" "axiom" "Distributive Law (DL)" \
  "algebra" "field-axioms" "basic" "1" "2. Real and complex numbers" \
  '\textbf{Distributive law.} For any $x, y, z \in \mathbb{R}$:
\[
x(y + z) = xy + xz.
\]' \
  'The distributive law connects addition and multiplication in $\mathbb{R}$. It is the final field axiom needed to make $\mathbb{R}$ a complete ordered field. Together with A2, it also implies $(x + y)z = xz + yz$.'

write_concept "order-axioms" "axiom" "Order Axioms (O1-O2)" \
  "algebra" "ordered-field" "basic" "1" "2. Real and complex numbers" \
  '\textbf{Axioms of order.} There exists a subset $P \subset \mathbb{R}$, called the set of positive elements, such that:
\begin{align}
\text{O1.}&\quad \text{If } x \in \mathbb{R}, \text{ then exactly one holds: } x \in P, x = 0, \text{ or } -x \in P. \\
\text{O2.}&\quad \text{If } x, y \in P, \text{ then } x + y \in P \text{ and } xy \in P.
\end{align}' \
  'The order axioms define positivity in $\mathbb{R}$. O1 (trichotomy) says every real number is either positive, zero, or negative. O2 says the sum and product of positive numbers are positive. These axioms make $\mathbb{R}$ an ordered field.'

write_concept "completeness-axiom" "axiom" "Completeness Axiom (O5)" \
  "analysis" "completeness" "basic" "1" "2. Real and complex numbers" \
  '\textbf{Completeness axiom (O5).} If $A$ is a nonempty subset of $\mathbb{R}$ which is bounded above, then $A$ has a least upper bound in $\mathbb{R}$.
\[
A \subset \mathbb{R}, A \neq \varnothing, A \text{ bounded above} \implies \exists\, \operatorname{lub} A \in \mathbb{R}.
\]' \
  'The completeness axiom distinguishes $\mathbb{R}$ from $\mathbb{Q}$. It asserts that every nonempty set of real numbers that is bounded above has a least upper bound (supremum) in $\mathbb{R}$. Equivalently, every nonempty set bounded below has a greatest lower bound (infimum). This axiom, together with the field and order axioms, uniquely characterizes the real numbers.'

write_concept "least-upper-bound" "definition" "Least Upper Bound (Supremum)" \
  "analysis" "order-theory" "basic" "1" "2. Real and complex numbers" \
  '\textbf{Definition.} A number $x \in \mathbb{R}$ is a \textit{least upper bound} (or supremum) for a nonempty set $A \subset \mathbb{R}$ if:
\begin{enumerate}
\item $x$ is an upper bound for $A$: $y \leq x$ for all $y \in A$,
\item $x$ is the least such: if $x''$ is any upper bound for $A$, then $x \leq x''$.
\end{enumerate}
If such an $x$ exists, it is unique and we write $x = \operatorname{lub} A = \sup A$.' \
  'The least upper bound (or supremum) of a set $A$ is the smallest real number that is greater than or equal to every element of $A$. It is unique when it exists. The existence of suprema for bounded sets is guaranteed by the completeness axiom of $\mathbb{R}$.'

write_concept "greatest-lower-bound" "definition" "Greatest Lower Bound (Infimum)" \
  "analysis" "order-theory" "basic" "1" "2. Real and complex numbers" \
  '\textbf{Definition.} A number $x \in \mathbb{R}$ is a \textit{greatest lower bound} (or infimum) for a nonempty set $A \subset \mathbb{R}$ if:
\begin{enumerate}
\item $x$ is a lower bound for $A$: $x \leq y$ for all $y \in A$,
\item $x$ is the greatest such: if $x''$ is any lower bound for $A$, then $x'' \leq x$.
\end{enumerate}
If such an $x$ exists, it is unique and we write $x = \operatorname{glb} A = \inf A$.' \
  'The greatest lower bound (or infimum) of a set $A$ is the largest real number that is less than or equal to every element of $A$. It is unique when it exists. The existence of infima for bounded sets follows from the completeness axiom, since $\operatorname{glb} A = -\operatorname{lub}(-A)$.'

write_concept "bounded-above" "definition" "Bounded Above and Bounded Below" \
  "analysis" "order-theory" "basic" "1" "2. Real and complex numbers" \
  '\textbf{Definition.} A nonempty subset $A \subset \mathbb{R}$ is:
\begin{itemize}
\item \textit{bounded above} if there exists $x \in \mathbb{R}$ such that $y \leq x$ for all $y \in A$. Such $x$ is called an \textit{upper bound} for $A$.
\item \textit{bounded below} if there exists $x \in \mathbb{R}$ such that $x \leq y$ for all $y \in A$. Such $x$ is called a \textit{lower bound} for $A$.
\end{itemize}
$A$ is \textit{bounded} if it is both bounded above and bounded below.' \
  'A set is bounded above if there exists some real number that is at least as large as every element of the set. Similarly, a set is bounded below if there exists some real number at most as large as every element. These concepts are fundamental to the completeness axiom and the construction of suprema and infima.'

write_concept "q-fails-completeness" "theorem" "Rationals Do Not Satisfy Completeness" \
  "analysis" "completeness" "basic" "1" "2. Real and complex numbers" \
  '\textbf{Theorem 2.1.} $\mathbb{Q}$ does not satisfy the completeness axiom O5. In particular, there is no rational number $x > 0$ such that $x^2 = 2$. Let $A = \{y \mid y \in \mathbb{Q}, y^2 < 2\}$. Then $A$ is bounded above in $\mathbb{Q}$ but has no least upper bound in $\mathbb{Q}$.' \
  'Theorem 2.1 shows that the rational numbers $\mathbb{Q}$ do not satisfy the completeness axiom. The set of rationals whose square is less than 2 is bounded above but has no rational least upper bound. This demonstrates the necessity of extending $\mathbb{Q}$ to $\mathbb{R}$ to obtain completeness.'

write_concept "complex-numbers-construction" "definition" "Construction of Complex Numbers" \
  "algebra" "complex-numbers" "basic" "1" "2. Real and complex numbers" \
  '\textbf{Definition.} The set $\mathbb{C}$ of complex numbers is $\mathbb{R}^2 = \mathbb{R} \times \mathbb{R}$, the set of ordered pairs $(x, y)$ of real numbers. Addition and multiplication are defined by:
\begin{align}
(x, y) + (u, v) &= (x + u, y + v), \\
(x, y) \cdot (u, v) &= (xu - yv, xv + yu).
\end{align}
Writing $z = (x, y) = x + iy$, the real and imaginary parts are $\operatorname{Re}(z) = x$, $\operatorname{Im}(z) = y$.' \
  'Complex numbers are constructed as ordered pairs of real numbers with component-wise addition and a special multiplication rule. With the identification $i = (0, 1)$ satisfying $i^2 = -1$, each complex number can be written as $z = x + iy$. This construction avoids postulating the existence of $\sqrt{-1}$.'

write_concept "complex-conjugation" "definition" "Complex Conjugation" \
  "algebra" "complex-numbers" "basic" "1" "2. Real and complex numbers" \
  '\textbf{Definition.} For $z = x + iy \in \mathbb{C}$, the \textit{complex conjugate} of $z$ is:
\[
z^* = (x + iy)^* = x - iy.
\]
\textbf{Properties:} For all $z, w \in \mathbb{C}$:
\begin{align}
(z + w)^* &= z^* + w^*, \\
(zw)^* &= z^* w^*, \\
(z^*)^* &= z, \\
z^* z &= x^2 + y^2 \geq 0.
\end{align}' \
  'Complex conjugation sends $x + iy$ to $x - iy$. It is an involutive automorphism of $\mathbb{C}$ that fixes the real numbers. The product $z^*z$ is always a nonnegative real number, equal to the square of the Euclidean norm of $(x, y)$.'

write_concept "complex-modulus" "definition" "Modulus of a Complex Number" \
  "algebra" "complex-numbers" "basic" "1" "2. Real and complex numbers" \
  '\textbf{Definition.} The \textit{modulus} (or absolute value) of $z = x + iy \in \mathbb{C}$ is:
\[
|z| = (z^* z)^{1/2} = (x^2 + y^2)^{1/2}.
\]
For $z \neq 0$, the multiplicative inverse is given by:
\[
z^{-1} = z^* |z|^{-2}.
\]' \
  'The modulus $|z|$ of a complex number $z = x + iy$ is the Euclidean distance from the origin to the point $(x, y)$ in the plane. It satisfies $|zw| = |z| |w|$ and $|z + w| \leq |z| + |w|$. The inverse formula $z^{-1} = z^* |z|^{-2}$ follows from $z^*z = |z|^2$.'

# ============ CHAPTER 1, SECTION 3: Sequences ============

write_concept "sequence-convergence" "definition" "Convergence of a Sequence" \
  "analysis" "sequences" "basic" "1" "3. Sequences of real and complex numbers" \
  '\textbf{Definition.} A sequence $(z_n)_{n=1}^{\infty}$ of complex numbers \textit{converges} to $z \in \mathbb{C}$ if for each $\varepsilon > 0$, there exists an integer $N$ such that:
\[
|z_n - z| < \varepsilon \quad \text{whenever } n \geq N.
\]
We write $z_n \to z$, $\lim_{n \to \infty} z_n = z$, or $\lim z_n = z$. The limit $z$ is unique.' \
  'A sequence converges to a limit $z$ if the terms eventually stay arbitrarily close to $z$. Geometrically, all but finitely many terms lie inside any given disc centered at $z$. The limit is unique: if $z_n \to z$ and $z_n \to w$, then $z = w$.'

write_concept "cauchy-criterion" "theorem" "Cauchy Criterion for Sequences" \
  "analysis" "sequences" "intermediate" "1" "3. Sequences of real and complex numbers" \
  '\textbf{Theorem 3.3.} A sequence in $\mathbb{C}$ (or $\mathbb{R}$) converges if and only if it is a Cauchy sequence.
\[
(z_n)_{n=1}^{\infty} \text{ converges} \iff \forall \varepsilon > 0, \exists N: |z_n - z_m| < \varepsilon \text{ for all } n, m \geq N.
\]' \
  'The Cauchy criterion characterizes convergence purely in terms of the sequence itself, without reference to a limit. A sequence is Cauchy if its terms eventually become arbitrarily close to each other. In $\mathbb{R}$ and $\mathbb{C}$, every Cauchy sequence converges — these spaces are complete. This theorem is fundamental to analysis.'

write_concept "limit-supremum-infimum" "definition" "Limit Superior and Limit Inferior" \
  "analysis" "sequences" "intermediate" "1" "3. Sequences of real and complex numbers" \
  '\textbf{Definition.} For a bounded real sequence $(x_n)_{n=1}^{\infty}$, define:
\begin{align}
x''_n &= \sup\{x_k \mid k \geq n\}, \\
x''_n &= \inf\{x_k \mid k \geq n\}.
\end{align}
Then:
\[
\limsup_{n \to \infty} x_n = \lim_{n \to \infty} x''_n, \qquad
\liminf_{n \to \infty} x_n = \lim_{n \to \infty} x''_n.
\]' \
  'The limit superior (limsup) and limit inferior (liminf) capture the asymptotic extremal behavior of a sequence. The limsup is the largest limit point (or $+\infty$ if unbounded above), and the liminf is the smallest limit point. A sequence converges if and only if its limsup equals its liminf.'

# ============ CHAPTER 1, SECTION 5: Metric spaces ============

write_concept "metric-space-definition" "definition" "Metric and Metric Space" \
  "topology" "metric-spaces" "basic" "1" "5. Metric spaces" \
  '\textbf{Definition.} A \textit{metric} on a set $S$ is a function $d: S \times S \to \mathbb{R}$ satisfying:
\begin{align}
\text{D1.}&\quad d(x, x) = 0, \quad d(x, y) > 0 \text{ if } x \neq y, \\
\text{D2.}&\quad d(x, y) = d(y, x) \quad \text{for all } x, y \in S, \\
\text{D3.}&\quad d(x, z) \leq d(x, y) + d(y, z) \quad \text{for all } x, y, z \in S.
\end{align}
A \textit{metric space} is a set $S$ together with a given metric $d$. D3 is called the \textit{triangle inequality}.' \
  'A metric formalizes the notion of distance between points in a set. D1 requires distance to be nonnegative and zero only for identical points. D2 imposes symmetry. D3, the triangle inequality, encodes that the direct path between two points is never longer than going via a third point. Metric spaces provide a uniform framework for convergence, continuity, and compactness.'

write_concept "open-set-definition" "definition" "Open Set in a Metric Space" \
  "topology" "metric-spaces" "basic" "1" "5. Metric spaces" \
  '\textbf{Definition.} Let $(S, d)$ be a metric space. A subset $A \subset S$ is \textit{open} if for each $x \in A$ there exists $r > 0$ such that the ball $B_r(x) = \{y \in S \mid d(x, y) < r\}$ is contained in $A$. A set $A$ is a \textit{neighborhood} of $x$ if $x \in A$ and $A$ is open.' \
  'A set is open if every point in it is surrounded by some open ball entirely contained in the set. Open sets generalize the notion of open intervals in $\mathbb{R}$. The collection of open sets satisfies: arbitrary unions of open sets are open, and finite intersections of open sets are open.'

write_concept "closed-set-definition" "definition" "Closed Set and Limit Point" \
  "topology" "metric-spaces" "basic" "1" "5. Metric spaces" \
  '\textbf{Definition.} Let $(S, d)$ be a metric space and $A \subset S$.
\begin{itemize}
\item A point $x \in S$ is a \textit{limit point} of $A$ if for every $r > 0$, $B_r(x) \cap A \neq \varnothing$ (and $x$ may or may not be in $A$).
\item $A$ is \textit{closed} if it contains all its limit points.
\end{itemize}
\textbf{Proposition 5.3.} A subset $A \subset S$ is open if and only if its complement is closed.' \
  'A limit point of $A$ is a point that can be approximated arbitrarily closely by points of $A$ (distinct from itself or not). A set is closed precisely when it is closed under the operation of taking limits of sequences from the set. The complement of an open set is closed, and vice versa.'

write_concept "compactness-definition" "definition" "Compact Set" \
  "topology" "compactness" "intermediate" "1" "6. Compactness" \
  '\textbf{Definition.} Let $(S, d)$ be a metric space. A subset $A \subset S$ is \textit{compact} if, given any collection of open sets whose union contains $A$, there is a finite subcollection whose union also contains $A$. Equivalently: every open cover of $A$ has a finite subcover.' \
  'Compactness is a fundamental topological property generalizing the notion of closed and bounded sets in $\mathbb{R}^n$. A set is compact if every open cover admits a finite subcover. Compact sets are always closed and bounded; in $\mathbb{R}^n$ with the Euclidean metric, the converse also holds (Heine-Borel theorem).'

write_concept "sequential-compactness" "definition" "Sequential Compactness" \
  "topology" "compactness" "intermediate" "1" "6. Compactness" \
  '\textbf{Definition.} Let $(S, d)$ be a metric space. A set $A \subset S$ is \textit{sequentially compact} if every sequence $(x_n)_{n=1}^{\infty} \subset A$ has a subsequence that converges to a point of $A$.' \
  'Sequential compactness requires that every sequence in the set has a convergent subsequence whose limit also lies in the set. In metric spaces, compactness and sequential compactness are equivalent. Sequentially compact sets are always closed and bounded. Examples include finite sets and the set $\{0\} \cup \{1/n \mid n \in \mathbb{N}\}$ in $\mathbb{R}$.'

echo "=== Ch1 core concepts written ==="
