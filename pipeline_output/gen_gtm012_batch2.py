#!/usr/bin/env python3
"""Generate GTM012 concept files (3-file format) for all sections read so far."""
import os, json

BASE = "/home/a123/文档/mathpkg/pipeline_output/concepts_v7/gtm012"
DATE = "2026-06-25"
AGENT = "v7-section-test"
BOOK = {"book_id":"gtm012","author":"Richard Beals","title":"Advanced Mathematical Analysis","chapter":"","section":"","pages":"","role_in_book":""}

def write_concept(slug, ctype, title_en, domain, subdomain, difficulty, chapter, section, tex, intro):
    d = os.path.join(BASE, slug)
    os.makedirs(d, exist_ok=True)
    book_info = dict(BOOK)
    book_info["chapter"] = chapter
    book_info["section"] = section

    yaml = {
        "id": slug, "title_en": title_en, "title_zh": "", "type": ctype,
        "domain": domain, "subdomain": subdomain, "difficulty": difficulty,
        "tags": [], "depends_on": {"required":[],"recommended":[],"suggested":[]},
        "source_books": [book_info], "content_hash": "",
        "extraction_date": DATE, "extraction_agent": AGENT
    }
    with open(os.path.join(d, "concept.yaml"), "w") as f:
        json.dump(yaml, f, indent=2)
    with open(os.path.join(d, "theorem.tex"), "w") as f:
        f.write(tex.strip() + "\n")
    with open(os.path.join(d, "introduce.en.md"), "w") as f:
        f.write("---\nrole: introduce\nlocale: en\ncontent_hash: \"\"\nwritten_against: \"\"\n---\n\n")
        f.write(intro.strip() + "\n")

# ==================== Chapter 1, Section 4: Series ====================
S = "4. Series"

write_concept("series-convergence", "definition", "Convergence and Divergence of Series",
    "analysis", "series", "basic", "1", S,
    r"""Given a sequence $(z_n)_{n=1}^{\infty}$ in $\mathbb{C}$, the associated series $\sum_{n=1}^{\infty} z_n$ has partial sums $s_n = \sum_{m=1}^{n} z_m$. The series \textit{converges} if $(s_n)_{n=1}^{\infty}$ converges to a limit $s$, written $\sum z_n = s$. Otherwise it \textit{diverges}. A necessary condition for convergence is $z_n \to 0$.""",
    r"""A series is the infinite sum of a sequence. It converges if the sequence of partial sums converges. This generalizes finite addition, but convergence requires the terms to approach zero.""")

write_concept("absolute-convergence", "proposition", "Absolute Convergence Implies Convergence",
    "analysis", "series", "basic", "1", S,
    r"""If $\sum_{n=1}^{\infty} |z_n|$ converges, then $\sum_{n=1}^{\infty} z_n$ converges. A series with this property is called \textit{absolutely convergent}.""",
    r"""Absolute convergence is a stronger condition than ordinary convergence. If the series of absolute values converges, the original series must converge. This follows from the Cauchy criterion and the triangle inequality.""")

write_concept("comparison-test", "proposition", "Comparison Test for Series",
    "analysis", "series", "basic", "1", S,
    r"""Suppose $(z_n)_{n=1}^{\infty} \subset \mathbb{C}$, $(a_n)_{n=1}^{\infty} \subset \mathbb{R}$ with $a_n \geq 0$, and there exist $M > 0$ and $N$ such that $|z_n| \leq M a_n$ for all $n \geq N$. If $\sum a_n$ converges, then $\sum z_n$ converges.""",
    r"""The comparison test allows deducing convergence of a complex series by comparing its terms to those of a known convergent series with nonnegative terms. It is a direct consequence of the Cauchy criterion.""")

write_concept("ratio-test", "proposition", "Ratio Test for Series",
    "analysis", "series", "intermediate", "1", S,
    r"""Suppose $(z_n)_{n=1}^{\infty} \subset \mathbb{C}$ with $z_n \neq 0$ for all $n$.
\begin{enumerate}
\item If $\limsup_{n \to \infty} |z_{n+1}/z_n| < 1$, then $\sum z_n$ converges.
\item If $\liminf_{n \to \infty} |z_{n+1}/z_n| > 1$, then $\sum z_n$ diverges.
\end{enumerate}""",
    r"""The ratio test compares successive terms to determine convergence. If the ratio of successive absolute values is eventually bounded below 1, the series behaves like a geometric series with ratio < 1 and converges. If the ratio is eventually above 1, terms do not approach zero.""")

write_concept("root-test", "proposition", "Root Test for Series",
    "analysis", "series", "intermediate", "1", S,
    r"""Suppose $(z_n)_{n=1}^{\infty} \subset \mathbb{C}$. Let $\rho = \limsup_{n \to \infty} |z_n|^{1/n}$.
\begin{enumerate}
\item If $\rho < 1$, then $\sum z_n$ converges.
\item If $\rho > 1$, then $\sum z_n$ diverges.
\end{enumerate}
\textbf{Corollary.} If $\lim |z_n|^{1/n}$ exists, the series converges if the limit is $< 1$ and diverges if $> 1$.""",
    r"""The root test uses the $n$th root of the absolute value of terms. If $\limsup |z_n|^{1/n} < 1$, the terms are eventually bounded by a geometric series. It is generally more powerful than the ratio test but harder to compute.""")

write_concept("power-series-radius", "definition", "Power Series and Radius of Convergence",
    "analysis", "power-series", "intermediate", "1", S,
    r"""A \textit{power series} around $z_0$ with coefficients $(a_n)_{n=0}^{\infty}$ is:
\[
\sum_{n=0}^{\infty} a_n (z - z_0)^n.
\]
The \textit{radius of convergence} $R$ is:
\[
R = \left(\limsup_{n \to \infty} |a_n|^{1/n}\right)^{-1},
\]
with $R = 0$ if the limsup is $\infty$, and $R = \infty$ if the limsup is $0$. The series converges absolutely for $|z - z_0| < R$ and diverges for $|z - z_0| > R$.""",
    r"""A power series is a series whose terms are multiples of powers of $(z - z_0)$. The radius of convergence $R$ determines the disc in which the series converges. It is given by the Cauchy-Hadamard formula using the limsup of $|a_n|^{1/n}$.""")

write_concept("radius-from-ratio", "theorem", "Radius of Convergence from Ratio Test",
    "analysis", "power-series", "intermediate", "1", S,
    r"""Suppose $a_n \neq 0$ for $n \geq N$ and $\lim |a_{n+1}/a_n|$ exists. Then the radius of convergence $R$ of $\sum a_n (z - z_0)^n$ is:
\[
R = \left(\lim_{n \to \infty} |a_{n+1}/a_n|\right)^{-1},
\]
with $R = \infty$ if the limit is $0$.""",
    r"""When the limit of successive coefficient ratios exists, the radius of convergence can be computed directly from the ratio test. This is often easier than computing the limsup of roots, but only applies when the ratio limit exists.""")

print("Series concepts done")

# ==================== Chapter 2, Section 1: Continuity ====================
S = "1. Continuity, uniform continuity, and compactness"

write_concept("continuity-at-point", "definition", "Continuity at a Point",
    "analysis", "continuity", "basic", "2", S,
    r"""Let $(S, d)$ and $(S', d')$ be metric spaces. A function $f: S \to S'$ is \textit{continuous at} $x \in S$ if for each $\varepsilon > 0$ there exists $\delta > 0$ such that:
\[
d'(f(x), f(y)) < \varepsilon \quad \text{whenever } d(x, y) < \delta.
\]
Equivalently, $f(x_n) \to f(x)$ whenever $x_n \to x$ in $S$.""",
    r"""A function is continuous at a point if small changes in the input produce arbitrarily small changes in the output. This $\varepsilon$-$\delta$ definition generalizes the familiar notion from calculus to arbitrary metric spaces. The sequential characterization is equivalent in metric spaces.""")

write_concept("uniform-continuity", "definition", "Uniform Continuity",
    "analysis", "continuity", "intermediate", "2", S,
    r"""A function $f: S \to S'$ between metric spaces is \textit{uniformly continuous} if for each $\varepsilon > 0$ there exists $\delta > 0$ such that:
\[
d'(f(x), f(y)) < \varepsilon \quad \text{whenever } d(x, y) < \delta,
\]
where $\delta$ depends only on $\varepsilon$, not on the particular points $x, y$.""",
    r"""Uniform continuity strengthens continuity by requiring the same $\delta$ to work for all pairs of points. The key distinction is that in ordinary continuity, $\delta$ may depend on the point $x$, while in uniform continuity it depends only on $\varepsilon$.""")

write_concept("compact-implies-uniform-continuous", "theorem", "Compactness Implies Uniform Continuity",
    "analysis", "continuity", "intermediate", "2", S,
    r"""Suppose $(S, d)$ and $(S', d')$ are metric spaces and $f: S \to S'$ is continuous. If $S$ is compact, then $f$ is uniformly continuous.""",
    r"""On a compact domain, continuity automatically implies uniform continuity. This is a fundamental result linking the topological notion of compactness with the analytic notion of uniform continuity. The proof uses the finite subcover property of compact sets.""")

write_concept("intermediate-value-theorem", "theorem", "Intermediate Value Theorem",
    "analysis", "continuity", "basic", "2", S,
    r"""Suppose $f: [a, b] \to \mathbb{R}$ is continuous. If $f(a) \leq c \leq f(b)$ or $f(b) \leq c \leq f(a)$, then there exists $x_0 \in [a, b]$ such that $f(x_0) = c$.""",
    r"""The Intermediate Value Theorem states that a continuous real-valued function on a closed interval attains every value between its values at the endpoints. This reflects the connectedness of intervals and the continuity of $f$.""")

print("Continuity concepts done")

# ==================== Chapter 2, Sections 2-3: Integration & Differentiation ====================

write_concept("riemann-integral", "definition", "Riemann Integral",
    "analysis", "integration", "basic", "2", "2. Integration of complex-valued functions",
    r"""Let $f: [a, b] \to \mathbb{C}$ be bounded. For a partition $P = (x_0, \ldots, x_n)$ of $[a, b]$, the \textit{Riemann sum} is:
\[
S(f; P) = \sum_{i=1}^{n} f(x_i)(x_i - x_{i-1}).
\]
$f$ is \textit{Riemann integrable} if $\lim_{|P| \to 0} S(f; P)$ exists, where $|P| = \max\{x_i - x_{i-1}\}$ is the mesh of $P$. The limit is the integral $\int_a^b f$. $f$ is integrable iff its real and imaginary parts are integrable.""",
    r"""The Riemann integral defines the area under a curve by approximating with rectangles. A bounded function is integrable if Riemann sums converge as the partition mesh tends to zero. Complex-valued functions are integrable iff their real and imaginary parts are.""")

write_concept("fundamental-theorem-calculus", "theorem", "Fundamental Theorem of Calculus",
    "analysis", "integration", "basic", "2", "3. Differentiation of complex-valued functions",
    r"""Suppose $f: [a, b] \to \mathbb{C}$ is continuous and $c \in [a, b]$. Define:
\[
F(x) = \int_c^x f(t)\,dt, \quad x \in [a, b].
\]
Then $F$ is differentiable at each $x \in (a, b)$ and $F'(x) = f(x)$. Conversely, if $G$ is differentiable and $G' = f$, then $\int_a^b f = G(b) - G(a)$.""",
    r"""The Fundamental Theorem of Calculus connects differentiation and integration as inverse operations. The integral of a continuous function is differentiable and its derivative recovers the original function. Any antiderivative gives the definite integral via evaluation at the endpoints.""")

write_concept("mean-value-theorem", "theorem", "Mean Value Theorem",
    "analysis", "differentiation", "basic", "2", "3. Differentiation of complex-valued functions",
    r"""Suppose $f: [a, b] \to \mathbb{R}$ is continuous on $[a, b]$ and differentiable on $(a, b)$. Then there exists $c \in (a, b)$ such that:
\[
f'(c) = \frac{f(b) - f(a)}{b - a}.
\]""",
    r"""The Mean Value Theorem guarantees the existence of a point where the instantaneous rate of change equals the average rate of change over an interval. It is a cornerstone of differential calculus, used to prove monotonicity, the constancy of functions with zero derivative, and Taylor expansions.""")

write_concept("inverse-function-theorem", "theorem", "Inverse Function Theorem (Real)",
    "analysis", "differentiation", "intermediate", "2", "3. Differentiation of complex-valued functions",
    r"""Suppose $f: [a, b] \to \mathbb{R}$ is continuous, differentiable on $(a, b)$, and $f'(x) > 0$ for all $x \in (a, b)$. Then $f$ is strictly increasing, and its inverse $g = f^{-1}: [f(a), f(b)] \to [a, b]$ is differentiable on $(f(a), f(b))$ with:
\[
g'(y) = \left[f'(g(y))\right]^{-1}.
\]""",
    r"""The Inverse Function Theorem for real functions states that a continuously differentiable function with nonvanishing derivative has a differentiable local inverse. The derivative of the inverse is the reciprocal of the derivative of the original function at the corresponding point.""")

print("Integration/differentiation concepts done")

# ==================== Chapter 2, Section 4: Uniform Convergence ====================
S = "4. Sequences and series of functions"

write_concept("uniform-convergence", "definition", "Uniform Convergence of Functions",
    "analysis", "function-sequences", "intermediate", "2", S,
    r"""A sequence of bounded functions $(f_n)_{n=1}^{\infty}$ from a set $S$ to $\mathbb{C}$ \textit{converges uniformly} to $f$ if:
\[
\lim_{n \to \infty} \sup_{x \in S} |f_n(x) - f(x)| = 0.
\]
The sequence is a \textit{uniform Cauchy sequence} if for each $\varepsilon > 0$ there exists $N$ such that $\sup_x |f_n(x) - f_m(x)| < \varepsilon$ for all $n, m \geq N$.""",
    r"""Uniform convergence means the maximum difference between $f_n$ and $f$ over the entire domain tends to zero. It is stronger than pointwise convergence and preserves continuity: the uniform limit of continuous functions is continuous.""")

write_concept("uniform-limit-continuous", "theorem", "Uniform Limit of Continuous Functions is Continuous",
    "analysis", "function-sequences", "intermediate", "2", S,
    r"""Suppose $(f_n)_{n=1}^{\infty}$ is a uniform Cauchy sequence of bounded continuous functions on a metric space $S$. Then there exists a unique bounded continuous function $f$ such that $f_n \to f$ uniformly.""",
    r"""The space of bounded continuous functions is complete with respect to the uniform norm. If a sequence of continuous functions satisfies the uniform Cauchy condition, the pointwise limit exists and is continuous, and the convergence is uniform.""")

write_concept("uniform-convergence-integral", "theorem", "Interchange of Uniform Limit and Integral",
    "analysis", "function-sequences", "intermediate", "2", S,
    r"""If $(f_n)_{n=1}^{\infty}$ is a sequence of continuous functions on $[a, b]$ converging uniformly to $f$, then:
\[
\int_a^b f = \lim_{n \to \infty} \int_a^b f_n.
\]""",
    r"""Under uniform convergence, the integral of the limit equals the limit of the integrals. This justifies interchanging limit and integration operations, which is not generally valid under pointwise convergence alone.""")

print("Uniform convergence concepts done")

# ==================== Chapter 2, Section 6: Trigonometric Functions ====================
S = "6. Trigonometric functions and the logarithm"

write_concept("sine-cosine-existence", "theorem", "Existence and Uniqueness of Sine and Cosine",
    "analysis", "trigonometric-functions", "basic", "2", S,
    r"""There exist unique functions $S, C: \mathbb{R} \to \mathbb{C}$ of class $C^2$ such that:
\begin{align}
S(0) = 0, \quad S'(0) = 1, \quad S'' + S = 0, \\
C(0) = 1, \quad C'(0) = 0, \quad C'' + C = 0.
\end{align}
These are the sine and cosine functions, satisfying $C(x) = \operatorname{Re}(e^{ix})$, $S(x) = \operatorname{Im}(e^{ix})$.""",
    r"""Sine and cosine are defined as the unique solutions to the second-order differential equation $f'' + f = 0$ with specific initial conditions. This analytic definition avoids geometric circular reasoning. The connection to the complex exponential $e^{ix} = \cos x + i \sin x$ follows naturally.""")

write_concept("sine-cosine-properties", "theorem", "Properties of Sine and Cosine",
    "analysis", "trigonometric-functions", "basic", "2", S,
    r"""The functions $S$ (sine) and $C$ (cosine) are real-valued, of class $C^\infty$, and satisfy:
\begin{align}
S' &= C, \quad C' = -S, \\
S(x)^2 + C(x)^2 &= 1, \\
S(x + 4p) &= S(x), \quad C(x + 4p) = C(x),
\end{align}
where $p$ is the smallest positive number with $C(p) = 0$. The number $\pi$ is defined as $\pi = 2p$.""",
    r"""The basic properties of sine and cosine—the Pythagorean identity $S^2 + C^2 = 1$, the differentiation rules, and periodicity—are all derived from the differential equation definition. The number $\pi$ is defined analytically as twice the smallest positive zero of cosine.""")

write_concept("complex-exponential-periodicity", "theorem", "Periodicity of the Complex Exponential",
    "analysis", "complex-analysis", "basic", "2", S,
    r"""For all $z \in \mathbb{C}$:
\begin{align}
\exp(iz) &= \cos z + i \sin z, \\
\exp(z + 2\pi i) &= \exp z, \\
\sin(z + 2\pi) &= \sin z, \quad \cos(z + 2\pi) = \cos z.
\end{align}
Every nonzero $w \in \mathbb{C}$ can be written as $w = \exp(z)$ for some $z$, and if also $w = \exp(z')$, then $z' = z + 2n\pi i$ for some integer $n$.""",
    r"""The complex exponential is periodic with period $2\pi i$, and sine and cosine inherit periodicity with period $2\pi$. The exponential maps $\mathbb{C}$ onto $\mathbb{C} \setminus \{0\}$, making the logarithm a multi-valued inverse. Euler's formula $\exp(iz) = \cos z + i \sin z$ connects all these functions.""")

print("Trigonometric concepts done")

# ==================== Chapter 2, Section 7: Functions of Two Variables ====================
S = "7. Functions of two variables"

write_concept("equality-mixed-partials", "theorem", "Equality of Mixed Partial Derivatives",
    "analysis", "multivariable-calculus", "intermediate", "2", S,
    r"""If $f: A \to \mathbb{C}$ is of class $C^2$ on an open set $A \subset \mathbb{R}^2$, then:
\[
D_1 D_2 f = D_2 D_1 f.
\]
That is, $\frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x}$.""",
    r"""For sufficiently smooth functions of two variables, the order of partial differentiation does not matter. This theorem justifies the commutativity of mixed partial derivatives. The proof uses the Fundamental Theorem of Calculus and relies on the continuity of second-order partials.""")

write_concept("fubini-rectangle", "theorem", "Change of Order of Integration over a Rectangle",
    "analysis", "multivariable-calculus", "intermediate", "2", S,
    r"""If $f$ is continuous on the rectangle $[a, b] \times [c, d]$, then:
\[
\int_a^b \left( \int_c^d f(x, y)\,dy \right) dx = \int_c^d \left( \int_a^b f(x, y)\,dx \right) dy.
\]""",
    r"""For a continuous function on a rectangle, the order of integration can be interchanged. This is a special case of Fubini's theorem for Riemann integrals. The proof uses differentiation under the integral sign and the equality of mixed partials.""")

write_concept("polar-coordinates-integration", "theorem", "Integration in Polar Coordinates",
    "analysis", "multivariable-calculus", "intermediate", "2", S,
    r"""If $f$ is continuous on the disc $D_R = \{(x, y) \mid x^2 + y^2 < R\}$ and $g(r, \theta) = f(r\cos\theta, r\sin\theta)$, then:
\[
\iint_{D_R} f(x, y)\,dx\,dy = \int_0^R \int_0^{2\pi} g(r, \theta)\, r\,d\theta\,dr.
\]""",
    r"""The change of variables from Cartesian to polar coordinates introduces the Jacobian factor $r$. This theorem justifies the standard formula for double integrals in polar coordinates, essential for computing integrals with radial symmetry.""")

print("Multivariable concepts done")

# ==================== Chapter 2, Section 8: Smooth Non-Analytic Functions ====================
S = "8. Some infinitely differentiable functions"

write_concept("smooth-nonanalytic-function", "proposition", "Existence of Smooth Non-Analytic Functions",
    "analysis", "smooth-functions", "intermediate", "2", S,
    r"""There exists an infinitely differentiable function $f: \mathbb{R} \to \mathbb{R}$ such that:
\[
f(x) = 0 \text{ for } x \leq 0, \quad f(x) > 0 \text{ for } x > 0.
\]
Specifically, $f(x) = \exp(-1/x)$ for $x > 0$ and $f(x) = 0$ for $x \leq 0$. All derivatives of $f$ vanish at $0$, yet $f$ is not identically zero.""",
    r"""This function demonstrates that a smooth ($C^\infty$) function need not be analytic (representable by a convergent power series). All derivatives at $0$ are zero, so the Taylor series at $0$ is identically zero, but the function itself is not. This is a crucial counterexample in analysis.""")

write_concept("smooth-bump-function", "corollary", "Existence of Smooth Bump Functions",
    "analysis", "smooth-functions", "intermediate", "2", S,
    r"""Given $a < b$, there exists an infinitely differentiable function $g: \mathbb{R} \to \mathbb{R}$ such that:
\[
g(x) = 0 \text{ for } x \notin (a, b), \quad g(x) > 0 \text{ for } x \in (a, b).
\]
Specifically, $g(x) = f(x - a)f(b - x)$ where $f$ is as in Proposition 8.1.""",
    r"""A bump function is a smooth function supported precisely on a given interval. They are constructed from the smooth non-analytic function by translation and multiplication. Bump functions are fundamental tools for partitions of unity and localization arguments in analysis.""")

print("Smooth function concepts done")

# ==================== Chapter 3, Section 1: Continuous Periodic Functions ====================
S = "1. Continuous periodic functions"

write_concept("continuous-periodic-space", "theorem", "The Space of Continuous Periodic Functions is a Banach Space",
    "analysis", "functional-analysis", "intermediate", "3", S,
    r"""The set $\mathcal{C}$ of continuous $2\pi$-periodic functions from $\mathbb{R}$ to $\mathbb{C}$, with the sup norm $\|u\| = \sup_x |u(x)|$, is a complete normed vector space (Banach space).""",
    r"""The space $\mathcal{C}$ with the uniform norm is a Banach space. Completeness follows from the fact that a uniform Cauchy sequence of continuous functions converges uniformly to a continuous limit, and periodicity is preserved in the limit. This provides the foundational function space for the study of Fourier series.""")

write_concept("bounded-linear-functional", "proposition", "Boundedness Equals Continuity for Linear Functionals",
    "analysis", "functional-analysis", "intermediate", "3", S,
    r"""A linear functional $F$ on a normed linear space $X$ is continuous if and only if it is bounded, i.e., there exists $c \geq 0$ such that $|F(u)| \leq c \|u\|$ for all $u \in X$.""",
    r"""For linear maps between normed spaces, continuity and boundedness are equivalent. This crucial fact simplifies the study of continuous linear functionals: one only needs to verify a uniform bound estimate rather than the $\varepsilon$-$\delta$ definition.""")

print("Periodic function space concepts done")

# ==================== Chapter 3, Section 2: Smooth Periodic Functions ====================
S = "2. Smooth periodic functions"

write_concept("smooth-periodic-space", "definition", "Smooth Periodic Functions and Frechet Spaces",
    "analysis", "functional-analysis", "advanced", "3", S,
    r"""$\mathcal{P}$ is the subspace of $\mathcal{C}$ consisting of infinitely differentiable periodic functions. A sequence $(u_n) \subset \mathcal{P}$ \textit{converges in the sense of $\mathcal{P}$} if for each $k \geq 0$, $\|D^k u_n - D^k u\| \to 0$ uniformly. $\mathcal{P}$ with this notion of convergence is a complete metric space (a Fr\'echet space), with metric:
\[
d'(u, v) = \sum_{k=0}^{\infty} 2^{-k-1} \|D^k u - D^k v\| \left[1 + \|D^k u - D^k v\|\right]^{-1}.
\]""",
    r"""$\mathcal{P}$ is not a Banach space because its topology cannot be given by a single norm. Instead, it is a Frechet space whose topology is defined by a countable family of seminorms $\|D^k u\|$. Convergence means that all derivatives converge uniformly. This space is the natural domain for periodic distributions.""")

print("Smooth periodic concepts done")

# ==================== Chapter 3, Section 3: Convolution ====================
S = "3. Translation, convolution, and approximation"

write_concept("convolution-periodic", "definition", "Convolution of Periodic Functions",
    "analysis", "harmonic-analysis", "intermediate", "3", S,
    r"""For $u, v \in \mathcal{C}$, the \textit{convolution} $u * v$ is defined by:
\[
(u * v)(x) = \frac{1}{2\pi} \int_0^{2\pi} u(x - y)v(y)\,dy.
\]
Convolution is commutative, associative, distributive, and commutes with translations. If $u \in \mathcal{P}$ and $v \in \mathcal{C}$, then $u * v \in \mathcal{P}$ and $D^k(u * v) = (D^k u) * v$.""",
    r"""Convolution is a smoothing operation: convolving a merely continuous function with a smooth function produces a smooth function. This is because differentiation can be transferred to the smooth factor. Convolution forms the basis for approximation by smooth functions.""")

write_concept("approximate-identity", "definition", "Approximate Identity",
    "analysis", "harmonic-analysis", "intermediate", "3", S,
    r"""A sequence $(\varphi_n)_{n=1}^{\infty} \subset \mathcal{C}$ is an \textit{approximate identity} if:
\begin{enumerate}
\item $\varphi_n(x) \geq 0$ for all $n, x$,
\item $\frac{1}{2\pi} \int_0^{2\pi} \varphi_n(x)\,dx = 1$ for all $n$,
\item For each $\delta \in (0, \pi)$, $\int_\delta^{2\pi-\delta} \varphi_n(x)\,dx \to 0$ as $n \to \infty$.
\end{enumerate}""",
    r"""An approximate identity is a sequence of nonnegative functions with unit average that concentrate near $0$ (and $2\pi$) as $n$ increases. Convolving with an approximate identity produces smooth approximations: $\varphi_n * u \to u$ uniformly for any $u \in \mathcal{C}$, and in the sense of $\mathcal{P}$ if $u \in \mathcal{P}$.""")

write_concept("convolution-approximation", "theorem", "Approximation by Convolution with Approximate Identity",
    "analysis", "harmonic-analysis", "intermediate", "3", S,
    r"""If $(\varphi_n)_{n=1}^{\infty}$ is an approximate identity, then for each $u \in \mathcal{C}$:
\[
\|\varphi_n * u - u\| \to 0 \quad \text{as } n \to \infty.
\]
If $u \in \mathcal{P}$, then $\varphi_n * u \to u$ in the sense of $\mathcal{P}$.""",
    r"""Convolution with an approximate identity provides a general method for approximating functions by smooth functions. The convolution $\varphi_n * u$ is a weighted average of translates of $u$, which becomes smoother while remaining close to $u$ as the weight concentrates near the identity translation.""")

print("Convolution concepts done")

# ==================== Chapter 3, Section 4: Weierstrass Theorems ====================
S = "4. The Weierstrass approximation theorems"

write_concept("weierstrass-trigonometric-approximation", "theorem", "Weierstrass Trigonometric Approximation Theorem",
    "analysis", "approximation-theory", "intermediate", "3", S,
    r"""Every continuous $2\pi$-periodic function $u \in \mathcal{C}$ is the uniform limit of a sequence of trigonometric polynomials. Every $u \in \mathcal{P}$ is the limit in the sense of $\mathcal{P}$ of a sequence of trigonometric polynomials.

A \textit{trigonometric polynomial} is a function $\varphi(x) = \sum_{k=-n}^{n} a_k \exp(ikx)$ with $a_k \in \mathbb{C}$.""",
    r"""The Weierstrass trigonometric approximation theorem states that trigonometric polynomials are dense in the continuous periodic functions with respect to uniform convergence. The proof constructs an approximate identity consisting of trigonometric polynomials $\varphi_n(x) = c_n(1 + \cos x)^n$.""")

write_concept("weierstrass-polynomial-approximation", "theorem", "Weierstrass Polynomial Approximation Theorem",
    "analysis", "approximation-theory", "intermediate", "3", S,
    r"""Let $u$ be a complex-valued continuous function on a closed interval $[a, b] \subset \mathbb{R}$. Then there exists a sequence of polynomials converging uniformly to $u$ on $[a, b]$.""",
    r"""Every continuous function on a closed interval can be uniformly approximated by polynomials. This classical theorem follows from the trigonometric version by extending the function periodically and using power series expansions of trigonometric polynomials. It shows that polynomials are dense in $C([a, b])$.""")

print("Weierstrass concepts done")

# ==================== Chapter 3, Section 5: Periodic Distributions ====================
S = "5. Periodic distributions"

write_concept("periodic-distribution", "definition", "Periodic Distribution",
    "analysis", "distribution-theory", "advanced", "3", S,
    r"""A \textit{periodic distribution} is a continuous linear functional $F: \mathcal{P} \to \mathbb{C}$, i.e.:
\begin{align}
F(au) &= aF(u), \\
F(u + v) &= F(u) + F(v), \\
F(u_n) &\to F(u) \text{ if } u_n \to u \text{ in the sense of } \mathcal{P}.
\end{align}
The space of all periodic distributions is denoted $\mathcal{P}'$. Each $v \in \mathcal{C}$ defines a distribution $F_v(u) = \frac{1}{2\pi} \int_0^{2\pi} v(x)u(x)\,dx$.""",
    r"""A periodic distribution generalizes the notion of a function. While every continuous periodic function defines a distribution via integration, not every distribution comes from a function. The Dirac $\delta$-distribution, defined by $\delta(u) = u(0)$, is the prototypical example of a distribution that is not a function.""")

write_concept("dirac-delta", "definition", "Dirac Delta Distribution",
    "analysis", "distribution-theory", "advanced", "3", S,
    r"""The \textit{Dirac $\delta$-distribution} is defined by:
\[
\delta(u) = u(0), \quad u \in \mathcal{C}.
\]
Its restriction to $\mathcal{P}$ is a periodic distribution. $\delta$ is not a function: if $u_n(x) = (\frac{1}{2} + \frac{1}{2}\cos x)^n$, then $\delta(u_n) = 1$ but $F_v(u_n) \to 0$ for any $v \in \mathcal{C}$.""",
    r"""The Dirac delta is the most fundamental example of a distribution that is not a function. It ``evaluates'' a function at the origin. Despite not being a function, it can be differentiated, translated, and manipulated algebraically within the framework of distribution theory.""")

write_concept("distribution-derivative", "definition", "Derivative of a Periodic Distribution",
    "analysis", "distribution-theory", "advanced", "3", S,
    r"""For $F \in \mathcal{P}'$, its \textit{derivative} $DF \in \mathcal{P}'$ is defined by:
\[
(DF)(u) = -F(Du), \quad u \in \mathcal{P}.
\]
Inductively, $(D^k F)(u) = (-1)^k F(D^k u)$. Differentiation is a continuous operation on $\mathcal{P}'$: if $F_n \to F$ in $\mathcal{P}'$, then $DF_n \to DF$.""",
    r"""Every distribution is infinitely differentiable. The derivative is defined by transferring the differentiation onto the test function via integration by parts (with a sign change). This extends classical differentiation and allows functions with jump discontinuities to have distributional derivatives.""")

write_concept("distribution-convergence", "definition", "Convergence of Periodic Distributions",
    "analysis", "distribution-theory", "advanced", "3", S,
    r"""A sequence $(F_n)_{n=1}^{\infty} \subset \mathcal{P}'$ \textit{converges} to $F \in \mathcal{P}'$ in the sense of $\mathcal{P}'$ if:
\[
F_n(u) \to F(u) \quad \text{for all } u \in \mathcal{P}.
\]
This is weak-$*$ convergence. Differentiation, translation, and reflection are continuous with respect to this convergence.""",
    r"""Convergence of distributions is defined pointwise on test functions. This weak topology makes the space of distributions well-behaved: limits of distributions are distributions, and operations like differentiation and translation are continuous. This allows series of distributions (e.g., Fourier series) to be studied.""")

# Section 6 concepts
S = "6. Determining the periodic distributions"

write_concept("distribution-representation", "theorem", "Representation of Periodic Distributions",
    "analysis", "distribution-theory", "advanced", "3", S,
    r"""Every periodic distribution $F \in \mathcal{P}'$ can be represented as:
\[
F = D^k F_v + F_f,
\]
for some integer $k \geq 0$, a continuous periodic function $v \in \mathcal{C}$, and a constant function $f$. Here $F_v$ and $F_f$ are the distributions defined by $v$ and $f$ respectively.""",
    r"""This structure theorem shows that every periodic distribution is (up to a constant) a finite-order derivative of a continuous periodic function. This characterizes the space $\mathcal{P}'$ completely and shows that distributions, while more general than functions, are not ``too wild'': they are derivatives of continuous functions.""")

write_concept("distribution-order", "definition", "Order of a Distribution",
    "analysis", "distribution-theory", "advanced", "3", S,
    r"""A periodic distribution $F \in \mathcal{P}'$ is of \textit{order} $k \geq 0$ if there exists a constant $c$ such that:
\[
|F(u)| \leq c \left( \|u\| + \|Du\| + \cdots + \|D^k u\| \right), \quad \text{for all } u \in \mathcal{P}.
\]
Every $F \in \mathcal{P}'$ is of finite order. The Dirac $\delta$ is of order $0$, while $D^k F_v$ is of order $k$.""",
    r"""The order of a distribution measures how many derivatives are needed to control its action on test functions. A distribution of order $0$ extends continuously to $\mathcal{C}$. The representation theorem shows that every distribution is of finite order, which is the key to proving the structure theorem.""")

print("=== ALL BATCH 2 CONCEPTS DONE ===")
