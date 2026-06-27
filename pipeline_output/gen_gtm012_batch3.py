#!/usr/bin/env python3
"""Generate GTM012 concept files - Batch 3: Chapters 4-7"""
import os, json

BASE = "/home/a123/文档/mathpkg/pipeline_output/concepts_v7/gtm012"
DATE = "2026-06-25"
AGENT = "v7-section-test"
BOOK = {"book_id":"gtm012","author":"Richard Beals","title":"Advanced Mathematical Analysis","chapter":"","section":"","pages":"","role_in_book":""}

def write_concept(slug, ctype, title_en, domain, subdomain, difficulty, chapter, section, tex, intro):
    d = os.path.join(BASE, slug)
    os.makedirs(d, exist_ok=True)
    bi = dict(BOOK)
    bi["chapter"] = chapter; bi["section"] = section
    yaml = {"id": slug, "title_en": title_en, "title_zh": "", "type": ctype,
        "domain": domain, "subdomain": subdomain, "difficulty": difficulty,
        "tags": [], "depends_on": {"required":[],"recommended":[],"suggested":[]},
        "source_books": [bi], "content_hash": "",
        "extraction_date": DATE, "extraction_agent": AGENT}
    with open(os.path.join(d, "concept.yaml"), "w") as f:
        json.dump(yaml, f, indent=2)
    with open(os.path.join(d, "theorem.tex"), "w") as f:
        f.write(tex.strip() + "\n")
    with open(os.path.join(d, "introduce.en.md"), "w") as f:
        f.write("---\nrole: introduce\nlocale: en\ncontent_hash: \"\"\nwritten_against: \"\"\n---\n\n")
        f.write(intro.strip() + "\n")

# ==================== Chapter 4: Hilbert Spaces and Fourier Series ====================

S = "1. An inner product in C, and the space L2"
write_concept("inner-product-periodic", "definition", "Inner Product on Continuous Periodic Functions",
    "analysis", "hilbert-spaces", "intermediate", "4", S,
    r"""For $u, v \in \mathcal{C}$, the \textit{inner product} $(u, v)$ is defined by:
\[
(u, v) = \frac{1}{2\pi} \int_0^{2\pi} u(x)v(x)^* \, dx.
\]
It satisfies: $(au, v) = a(u, v) = (u, a^*v)$, $(u_1+u_2, v) = (u_1, v)+(u_2, v)$, $(v, u) = (u, v)^*$, and $(u, u) \geq 0$ with equality only if $u = 0$.""",
    r"""The inner product on the space of continuous periodic functions generalizes the dot product from finite-dimensional vector spaces to function spaces. It satisfies conjugate symmetry, linearity in the first argument, and positive definiteness. The associated norm $\|u\| = (u, u)^{1/2}$ is the $L^2$ norm.""")

write_concept("schwarz-inequality-l2", "lemma", "Schwarz Inequality for the L2 Inner Product",
    "analysis", "hilbert-spaces", "intermediate", "4", S,
    r"""For $u, v \in \mathcal{C}$:
\[
|(u, v)| \leq \|u\| \, \|v\|,
\]
where $\|u\| = (u, u)^{1/2} = \left(\frac{1}{2\pi} \int_0^{2\pi} |u(x)|^2 \, dx\right)^{1/2}$.

\textbf{Corollary.} The function $u \mapsto \|u\|$ is a norm on $\mathcal{C}$, satisfying the triangle inequality $\|u + v\| \leq \|u\| + \|v\|$.""",
    r"""The Schwarz inequality (also called Cauchy-Schwarz) bounds the inner product by the product of norms. It is proved by considering the nonnegative quantity $(u - av, u - av)$ and choosing $a = (u, v)/\|v\|^2$. This inequality is fundamental to Hilbert space theory and justifies the triangle inequality for the $L^2$ norm.""")

write_concept("l2-space-periodic", "definition", "The L2 Space of Periodic Distributions",
    "analysis", "hilbert-spaces", "intermediate", "4", S,
    r"""The space $L^2$ consists of all periodic distributions $F$ which are limits, in the sense of $L^2$, of sequences $(u_n)_{n=1}^{\infty} \subset \mathcal{C}$:
\[
\|u_n - u_m\| \to 0, \quad F_{u_n} \to F \;(\mathcal{P}').
\]
$L^2$ is a Hilbert space: its inner product is defined by $(F, G) = \lim (u_n, v_n)$ where $F_{u_n} \to F$, $F_{v_n} \to G$.""",
    r"""$L^2$ is the completion of $\mathcal{C}$ with respect to the $L^2$ norm. Unlike $\mathcal{C}$, which is not complete in this norm, $L^2$ is a Hilbert space—a complete inner product space. Its elements are periodic distributions, and the identification of functions with distributions gives a natural embedding $\mathcal{C} \subset L^2$.""")

S = "6. Fourier series"
write_concept("fourier-coefficients-l2", "definition", "Fourier Coefficients in L2",
    "analysis", "fourier-analysis", "intermediate", "4", S,
    r"""Let $e_n(x) = \exp(inx)$, $n = 0, \pm 1, \pm 2, \ldots$. For $F \in L^2$, the \textit{Fourier coefficients} of $F$ are:
\[
a_n = (F, F_{e_n}) = F(e_{-n}), \quad n \in \mathbb{Z}.
\]
The formal series $\sum_{n=-\infty}^{\infty} a_n e_n$ is the \textit{Fourier series} of $F$. For $u \in \mathcal{C}$, the coefficients are $a_n = \frac{1}{2\pi} \int_0^{2\pi} u(x) e^{-inx}\,dx$.""",
    r"""Fourier coefficients decompose a function or distribution into frequency components. For $L^2$ distributions, the coefficients are given by the inner product with the complex exponentials. The sequence $(e_n)_{n=-\infty}^{\infty}$ forms an orthonormal basis for $L^2$, meaning every element has a unique Fourier expansion.""")

write_concept("fourier-series-l2-convergence", "theorem", "Fourier Series in L2: Completeness and Parseval Identity",
    "analysis", "fourier-analysis", "intermediate", "4", S,
    r"""The sequence $(e_n)_{n=-\infty}^{\infty}$ is an orthonormal basis for $L^2$. Every $F \in L^2$ has a unique representation:
\[
F = \sum_{n=-\infty}^{\infty} a_n e_n, \quad a_n = F(e_{-n}),
\]
where the series converges in the sense of $L^2$. The \textit{Parseval identity} holds:
\[
\|F\|^2 = \sum_{n=-\infty}^{\infty} |a_n|^2.
\]
Conversely, any sequence $(a_n)_{-\infty}^{\infty}$ with $\sum |a_n|^2 < \infty$ determines a unique $F \in L^2$.""",
    r"""This theorem establishes that the complex exponentials form a complete orthonormal system in $L^2$. The Parseval identity equates the $L^2$ norm of a distribution with the $\ell^2$ norm of its Fourier coefficient sequence. The Riesz-Fischer theorem is the converse: any $\ell^2$ sequence corresponds to an $L^2$ element.""")

write_concept("fourier-uniform-convergence-c1", "theorem", "Uniform Convergence of Fourier Series for C1 Functions",
    "analysis", "fourier-analysis", "intermediate", "4", S,
    r"""If $u \in \mathcal{C}$ is continuously differentiable, then the partial sums of its Fourier series converge uniformly to $u$:
\[
u(x) = \sum_{n=-\infty}^{\infty} a_n \exp(inx), \quad a_n = \frac{1}{2\pi} \int_0^{2\pi} u(x)e^{-inx}\,dx,
\]
and the convergence is uniform in $x$. If $u \in \mathcal{P}$, the convergence is in the sense of $\mathcal{P}$.""",
    r"""For continuously differentiable periodic functions, the Fourier series converges uniformly—not just in $L^2$. The key is the relation $b_n = in a_n$ between the Fourier coefficients of $u'$ and $u$, which via the Schwarz inequality yields $\sum |a_n| < \infty$, ensuring uniform convergence by the Weierstrass M-test.""")

# ==================== Chapter 5: Applications of Fourier Series ====================

S = "1. Fourier series of smooth periodic functions and of periodic distributions"
write_concept("rapid-decrease-sequence", "definition", "Sequences of Rapid Decrease",
    "analysis", "fourier-analysis", "intermediate", "5", S,
    r"""A two-sided sequence $(a_n)_{-\infty}^{\infty} \subset \mathbb{C}$ is of \textit{rapid decrease} if for every $r > 0$ there exists a constant $c = c(r)$ such that:
\[
|a_n| \leq c |n|^{-r}, \quad \text{for all } n \neq 0.
\]""",
    r"""A sequence decreases rapidly if it decays faster than any negative power of $|n|$. This condition characterizes exactly those sequences that arise as Fourier coefficients of smooth ($C^\infty$) periodic functions. Rapid decrease is the Fourier dual of smoothness.""")

write_concept("fourier-coefficients-smooth", "theorem", "Characterization of Fourier Coefficients of Smooth Functions",
    "analysis", "fourier-analysis", "intermediate", "5", S,
    r"""A sequence $(a_n)_{-\infty}^{\infty} \subset \mathbb{C}$ is the sequence of Fourier coefficients of a function $u \in \mathcal{P}$ if and only if it is of rapid decrease.

If $u \in \mathcal{P}$ with coefficients $(a_n)$, then the coefficients of $D^k u$ are $((in)^k a_n)$, and $|n|^k |a_n| \leq \|D^k u\|$, giving the estimate $|a_n| \leq c|n|^{-k}$.""",
    r"""Smoothness of a periodic function is equivalent to rapid decay of its Fourier coefficients. Differentiation corresponds to multiplication by $in$ in Fourier space, so each derivative that exists forces an additional power of decay. This is a fundamental principle of Fourier analysis: smoothness in physical space equals decay in frequency space.""")

write_concept("slow-growth-sequence", "definition", "Sequences of Slow Growth",
    "analysis", "fourier-analysis", "intermediate", "5", S,
    r"""A two-sided sequence $(a_n)_{-\infty}^{\infty} \subset \mathbb{C}$ is of \textit{slow growth} if there exist constants $c > 0$ and $r > 0$ such that:
\[
|a_n| \leq c |n|^r, \quad \text{for all } n \neq 0.
\]""",
    r"""A sequence is of slow growth if it grows at most polynomially. This condition characterizes exactly those sequences that arise as Fourier coefficients of periodic distributions. Slow growth is the Fourier dual of being a distribution (of finite order).""")

write_concept("fourier-coefficients-distribution", "theorem", "Characterization of Fourier Coefficients of Distributions",
    "analysis", "fourier-analysis", "intermediate", "5", S,
    r"""A sequence $(a_n)_{-\infty}^{\infty} \subset \mathbb{C}$ is the sequence of Fourier coefficients of a periodic distribution $F \in \mathcal{P}'$ if and only if it is of slow growth.

Moreover, if $F \in \mathcal{P}'$ has coefficients $(a_n)$ and $u \in \mathcal{P}$ has coefficients $(b_n)$, then:
\[
F(u) = \sum_{n=-\infty}^{\infty} a_n b_{-n} = \sum_{n=-\infty}^{\infty} a_{-n} b_n.
\]""",
    r"""Periodic distributions correspond precisely to Fourier coefficient sequences of slow (polynomial) growth. The action of a distribution on a test function is given by the pairing of their Fourier coefficients. This provides an alternative, purely sequence-based approach to the theory of periodic distributions.""")

# ==================== Chapter 5, Section 6: Laplace Equation ====================

S = "6. Laplace's equation and the Dirichlet problem"
write_concept("harmonic-function", "definition", "Harmonic Function",
    "analysis", "partial-differential-equations", "intermediate", "5", S,
    r"""A function $u$ defined on an open subset of $\mathbb{R}^2$ is \textit{harmonic} if it satisfies \textit{Laplace's equation}:
\[
\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0.
\]
In polar coordinates $(r, \theta)$, this becomes:
\[
\frac{\partial^2 u}{\partial r^2} + \frac{1}{r}\frac{\partial u}{\partial r} + \frac{1}{r^2}\frac{\partial^2 u}{\partial \theta^2} = 0.
\]""",
    r"""Harmonic functions are solutions to Laplace's equation, one of the most important partial differential equations in mathematics and physics. They describe equilibrium states: steady-state heat distribution, electrostatic potential, and irrotational fluid flow. Harmonic functions are infinitely differentiable and satisfy the mean value property.""")

write_concept("poisson-kernel", "definition", "Poisson Kernel for the Unit Disc",
    "analysis", "partial-differential-equations", "intermediate", "5", S,
    r"""The \textit{Poisson kernel} for the unit disc is the function $P_r(\theta)$, $0 \leq r < 1$, defined by:
\[
P_r(\theta) = \sum_{n=-\infty}^{\infty} r^{|n|} e^{in\theta}
= \frac{1 - r^2}{1 - 2r\cos\theta + r^2}.
\]
The functions $P_r$ form an approximate identity as $r \to 1$.""",
    r"""The Poisson kernel provides the solution to the Dirichlet problem on the unit disc. For each $r < 1$, $P_r$ is a smooth positive function whose Fourier coefficients are $r^{|n|}$. As $r \to 1^-$, the family $\{P_r\}$ forms an approximate identity, so convolutions $g * P_r$ converge to $g$.""")

write_concept("dirichlet-problem-disc", "theorem", "Solution of the Dirichlet Problem for the Disc",
    "analysis", "partial-differential-equations", "intermediate", "5", S,
    r"""Suppose $F$ is a periodic distribution. There exists a unique function $u(r, \theta)$ smooth in the open unit disc, satisfying Laplace's equation in polar coordinates, such that the distributions defined by $u_r(\theta) = u(r, \theta)$ converge to $F$ in $\mathcal{P}'$ as $r \to 1$. The solution is given by convolution with the Poisson kernel:
\[
u_r = F * P_r.
\]
If $F = F_g$ with $g \in \mathcal{C}$, then $u_r \to g$ uniformly as $r \to 1$.""",
    r"""This theorem solves the Dirichlet problem: find a harmonic function in the unit disc with prescribed boundary values. The solution is obtained by convolving the boundary data with the Poisson kernel. For continuous boundary data, the convergence to the boundary values is uniform, giving a classical solution.""")

# ==================== Chapter 6: Holomorphic Functions ====================

S = "4. The local behavior of a holomorphic function"
write_concept("local-form-holomorphic", "lemma", "Local Form of a Holomorphic Function",
    "analysis", "complex-analysis", "intermediate", "6", S,
    r"""Suppose $f$ is holomorphic in an open set $\Omega$ and $z_0 \in \Omega$. If $f$ is not constant near $z_0$, then:
\[
f(z) = a_0 + a_m (z - z_0)^m h(z),
\]
where $a_0 = f(z_0)$, $a_m \neq 0$, $m \geq 1$, and $h$ is holomorphic in $\Omega$ with $h(z_0) = 1$.""",
    r"""Near any point, a nonconstant holomorphic function behaves like a polynomial of degree $m$ plus a constant, where $m$ is the order of the first nonvanishing derivative. This factorization isolates the first nonconstant term and a unit factor $h$, and is fundamental to understanding the local mapping properties of holomorphic functions.""")

write_concept("inverse-function-theorem-holomorphic", "theorem", "Inverse Function Theorem for Holomorphic Functions",
    "analysis", "complex-analysis", "intermediate", "6", S,
    r"""Suppose $f$ is holomorphic in an open set $\Omega$ and $z_0 \in \Omega$. If $f'(z_0) \neq 0$, then $f$ is one-to-one near $z_0$, and the inverse function $g$ is holomorphic near $w_0 = f(z_0)$. Moreover:
\[
g'(w_0) = \frac{1}{f'(z_0)}.
\]""",
    r"""The holomorphic Inverse Function Theorem states that a holomorphic function with nonvanishing derivative is locally biholomorphic. The inverse is also holomorphic, and its derivative is the reciprocal of the original derivative. This is used to define branches of the logarithm and nth roots as holomorphic functions.""")

write_concept("open-mapping-theorem", "theorem", "Open Mapping Theorem for Holomorphic Functions",
    "analysis", "complex-analysis", "intermediate", "6", S,
    r"""If $f$ is holomorphic and nonconstant on a connected open set $\Omega$, then $f$ maps open subsets of $\Omega$ to open sets. In particular, $f(\Omega)$ is open.""",
    r"""The Open Mapping Theorem states that nonconstant holomorphic functions send open sets to open sets. This is a fundamental result with many consequences: the Maximum Modulus Principle, the fact that holomorphic functions are either constant or open, and the local behavior $f(z) \approx a_0 + a_m(z - z_0)^m$ showing $m$-to-1 mapping near critical points.""")

# ==================== Chapter 7: Laplace Transform ====================

S = "1. Introduction"
write_concept("laplace-transform", "definition", "Laplace Transform",
    "analysis", "integral-transforms", "intermediate", "7", S,
    r"""The \textit{Laplace transform} of a function $u: [0, \infty) \to \mathbb{C}$ is defined by:
\[
(Lu)(z) = \int_0^\infty u(t) e^{-zt} \, dt,
\]
for $z \in \mathbb{C}$ where the integral converges absolutely. If $|u(t)|$ is bounded by $Ce^{at}$, then the integral converges for $\operatorname{Re} z > a$, and $Lu$ is holomorphic in this half-plane.

Key property: $(L(Du))(z) = z (Lu)(z)$ (formally, via integration by parts).""",
    r"""The Laplace transform converts functions on the half-line into holomorphic functions on a half-plane. It diagonalizes differentiation: $L(Du) = z Lu$, turning differential equations into algebraic equations. This makes it a powerful tool for solving linear ODEs with constant coefficients. The inversion formula recovers $u$ via a contour integral.""")

S = "2. The space L"
write_concept("space-l", "definition", "The Space L of Rapidly Decaying Smooth Functions",
    "analysis", "functional-analysis", "advanced", "7", S,
    r"""$\mathcal{L}$ is the set of all smooth functions $u: \mathbb{R} \to \mathbb{C}$ such that for every integer $k \geq 0$ and every $a \in \mathbb{R}$:
\[
\lim_{t \to +\infty} e^{at} D^k u(t) = 0.
\]
Equivalently, for each $k, a, M$, the seminorm:
\[
\|u\|_{k,a,M} = \sup\{e^{at} |D^k u(t)| \mid t \in [M, \infty)\}
\]
is finite. $\mathcal{L}$ is a Fr\'echet space with convergence defined by these seminorms.""",
    r"""$\mathcal{L}$ consists of smooth functions whose derivatives all decay faster than any exponential as $t \to +\infty$. It is the natural domain for the Laplace transform on distributions. Operations like differentiation, translation, and integration are continuous on $\mathcal{L}$, making it well-suited for the study of convolution and differential equations on the half-line.""")

S = "6. Laplace transforms of distributions"
write_concept("laplace-transform-distribution", "definition", "Laplace Transform of a Distribution",
    "analysis", "integral-transforms", "advanced", "7", S,
    r"""For $F \in \mathcal{L}'$ (a continuous linear functional on $\mathcal{L}$), its \textit{Laplace transform} is defined for $\operatorname{Re} z > a$ (where $a$ depends on $F$) by:
\[
(LF)(z) = \lim_{n \to \infty} F(u_n) =: F(e_z),
\]
where $(u_n) \subset \mathcal{L}$ approximates $e_z(t) = e^{-zt}$ in the sense of $\mathcal{L}$.

Properties for $F \in \mathcal{L}'$:
\begin{align}
L(T_s F)(z) &= e^{-zs} LF(z), \\
L(DF)(z) &= z LF(z), \\
L(e_w F)(z) &= LF(z + w).
\end{align}""",
    r"""The Laplace transform extends to distributions in $\mathcal{L}'$ by approximating the exponential $e_z \notin \mathcal{L}$ with functions from $\mathcal{L}$. The transform converts translation to multiplication by an exponential, and differentiation to multiplication by $z$, just as for ordinary functions. This extension allows solving distributional differential equations using algebraic methods.""")

print("=== BATCH 3 DONE ===")
