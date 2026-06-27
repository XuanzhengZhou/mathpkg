#!/usr/bin/env python3
"""Chapter 2 concepts for GTM012."""

import os

BASE = '/home/a123/文档/mathpkg/pipeline_output/concepts_v7/gtm012/共 34 个 section 文件：'
os.makedirs(BASE, exist_ok=True)

def make(slug, typ, title_en, domain, subdomain, difficulty, chapter, section, tex):
    d = os.path.join(BASE, slug)
    os.makedirs(d, exist_ok=True)
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
    with open(os.path.join(d, "theorem.tex"), "w") as f:
        f.write(tex + "\n")
    md = f"""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

{title_en}. A fundamental {typ} in {domain}, from Ch.{chapter} of Beals' Advanced Mathematical Analysis.
"""
    with open(os.path.join(d, "introduce.en.md"), "w") as f:
        f.write(md)

# §1 Continuity
make("continuity-definition", "definition",
    "Continuous Function at a Point", "analysis", "real-analysis", "basic",
    "2", "§1. Continuity, uniform continuity, and compactness",
    r"$f: S \to S'$ is continuous at $x \in S$ if $\forall\varepsilon>0$, $\exists\delta>0$ such that $d'(f(x),f(y))<\varepsilon$ whenever $d(x,y)<\delta$.")

make("continuity-algebraic-properties", "proposition",
    "Algebraic Properties of Continuous Functions", "analysis", "real-analysis", "basic",
    "2", "§1. Continuity, uniform continuity, and compactness",
    r"If $f,g: S \to \mathbb{C}$ are continuous at $x$, then $f+g$, $af$, and $fg$ are continuous at $x$. If $g(x)\neq 0$, $f/g$ is defined near $x$ and is continuous at $x$.")

make("uniform-continuity-definition", "definition",
    "Uniform Continuity", "analysis", "real-analysis", "basic",
    "2", "§1. Continuity, uniform continuity, and compactness",
    r"$f: S \to S'$ is uniformly continuous if $\forall\varepsilon>0$, $\exists\delta>0$ such that $d'(f(x),f(y))<\varepsilon$ whenever $d(x,y)<\delta$.")

make("compact-uniform-continuity", "theorem",
    "Continuous on Compact Implies Uniformly Continuous", "analysis", "real-analysis", "intermediate",
    "2", "§1. Continuity, uniform continuity, and compactness",
    r"If $S$ is compact and $f: S \to S'$ is continuous, then $f$ is uniformly continuous.")

make("compact-continuous-bounded", "theorem",
    "Continuous on Compact: Boundedness and Extrema", "analysis", "real-analysis", "intermediate",
    "2", "§1. Continuity, uniform continuity, and compactness",
    r"If $S$ is compact and $f: S \to \mathbb{C}$ is continuous, then $f$ is bounded and $|f|$ attains its maximum. If $f$ is real-valued, $f$ attains both maximum and minimum.")

make("intermediate-value-theorem", "theorem",
    "Intermediate Value Theorem", "analysis", "real-analysis", "basic",
    "2", "§1. Continuity, uniform continuity, and compactness",
    r"If $f: [a,b] \to \mathbb{R}$ is continuous and $c$ lies between $f(a)$ and $f(b)$, then $\exists x_0 \in [a,b]$ such that $f(x_0) = c$.")

# §2 Integration
make("riemann-integral-definition", "definition",
    "Riemann Integral", "analysis", "real-analysis", "basic",
    "2", "§2. Integration of complex-valued functions",
    r"For bounded $f: [a,b] \to \mathbb{C}$, a partition $P = (x_0,\ldots,x_n)$ has $|P|=\max(x_i-x_{i-1})$. Riemann sum: $S(f;P)=\sum f(x_i)(x_i-x_{i-1})$. $f$ is integrable if $\lim_{|P|\to 0} S(f;P)$ exists; the limit is $\int_a^b f$.")

make("integral-linearity", "proposition",
    "Linearity of the Riemann Integral", "analysis", "real-analysis", "basic",
    "2", "§2. Integration of complex-valued functions",
    r"If $f,g: [a,b] \to \mathbb{C}$ are integrable and $c \in \mathbb{C}$, then $\int (f+g) = \int f + \int g$, $\int cf = c\int f$.")

make("riemann-criterion", "proposition",
    "Cauchy Criterion for Riemann Integrability", "analysis", "real-analysis", "basic",
    "2", "§2. Integration of complex-valued functions",
    r"$f$ is integrable iff $\forall\varepsilon>0$, $\exists\delta>0$ such that $|S(f;P)-S(f;Q)|<\varepsilon$ whenever $|P|,|Q|<\delta$.")

make("continuous-implies-integrable", "theorem",
    "Continuity Implies Riemann Integrability", "analysis", "real-analysis", "basic",
    "2", "§2. Integration of complex-valued functions",
    r"If $f: [a,b] \to \mathbb{C}$ is continuous, then $f$ is Riemann integrable.")

make("integral-over-subintervals", "proposition",
    "Integral over Subintervals", "analysis", "real-analysis", "basic",
    "2", "§2. Integration of complex-valued functions",
    r"For $a<b<c$, $f$ is integrable on $[a,c]$ iff integrable on $[a,b]$ and $[b,c]$. Then $\int_a^c f = \int_a^b f + \int_b^c f$.")

# §3 Differentiation
make("derivative-definition", "definition",
    "Derivative", "analysis", "real-analysis", "basic",
    "2", "§3. Differentiation of complex-valued functions",
    r"$f: (a,b) \to \mathbb{C}$ is differentiable at $x$ if $\lim_{y\to x} [f(y)-f(x)](y-x)^{-1}$ exists. The limit is $f'(x)$.")

make("differentiable-implies-continuous", "proposition",
    "Differentiability Implies Continuity", "analysis", "real-analysis", "basic",
    "2", "§3. Differentiation of complex-valued functions",
    r"If $f$ is differentiable at $x$, then $f$ is continuous at $x$.")

make("derivative-rules", "proposition",
    "Derivative Rules", "analysis", "real-analysis", "basic",
    "2", "§3. Differentiation of complex-valued functions",
    r"$(f+g)' = f' + g'$, $(cf)' = cf'$, $(fg)' = f'g + fg'$, $(f/g)' = (f'g - fg')/g^2$ when $g(x)\neq 0$.")

make("mean-value-theorem", "theorem",
    "Mean Value Theorem", "analysis", "real-analysis", "basic",
    "2", "§3. Differentiation of complex-valued functions",
    r"If $f: [a,b] \to \mathbb{R}$ is continuous on $[a,b]$ and differentiable on $(a,b)$, then $\exists c \in (a,b)$ with $f(b)-f(a) = f'(c)(b-a)$.")

make("derivative-zero-implies-constant", "corollary",
    "Zero Derivative Implies Constant", "analysis", "real-analysis", "basic",
    "2", "§3. Differentiation of complex-valued functions",
    r"If $f: [a,b] \to \mathbb{C}$ is continuous, differentiable on $(a,b)$, and $f'(x)=0$ for all $x \in (a,b)$, then $f$ is constant.")

make("fundamental-theorem-calculus", "theorem",
    "Fundamental Theorem of Calculus", "analysis", "real-analysis", "basic",
    "2", "§3. Differentiation of complex-valued functions",
    r"If $f: [a,b] \to \mathbb{C}$ is continuous and $c \in [a,b]$, then $F(x) = \int_c^x f$ is differentiable and $F'(x) = f(x)$.")

make("inverse-function-theorem", "theorem",
    "Inverse Function Theorem (Strictly Monotone)", "analysis", "real-analysis", "intermediate",
    "2", "§3. Differentiation of complex-valued functions",
    r"If $f: [a,b] \to \mathbb{R}$ is continuous, $f'(x)>0$ on $(a,b)$, then $f$ is strictly increasing, has inverse $g=f^{-1}$ on $[f(a),f(b)]$, and $g'(y) = [f'(g(y))]^{-1}$.")

make("higher-derivatives-definition", "definition",
    "Higher Derivatives and Classes $C^k$, $C^\infty$", "analysis", "real-analysis", "basic",
    "2", "§3. Differentiation of complex-valued functions",
    r"$f^{(0)} = f$, $f^{(k+1)} = (f^{(k)})'$. $f$ is $C^k$ if $f,f',\ldots,f^{(k)}$ are continuous. $f$ is $C^\infty$ if it has continuous derivatives of all orders.")

# §4 Uniform convergence
make("uniform-convergence-definition", "definition",
    "Uniform Convergence of Functions", "analysis", "real-analysis", "intermediate",
    "2", "§4. Sequences and series of functions",
    r"For bounded $f_n,f: S \to \mathbb{C}$, $|f| = \sup\{|f(x)| : x\in S\}$. $(f_n)$ converges uniformly to $f$ if $\lim |f_n - f| = 0$.")

make("uniform-cauchy-criterion", "theorem",
    "Uniform Cauchy Criterion", "analysis", "real-analysis", "intermediate",
    "2", "§4. Sequences and series of functions",
    r"If $(f_n)$ is a uniform Cauchy sequence of bounded functions $S \to \mathbb{C}$, there is a unique bounded $f$ to which it converges uniformly. If $S$ is a metric space and each $f_n$ is continuous, $f$ is continuous.")

make("uniform-convergence-integration", "theorem",
    "Uniform Convergence and Integration", "analysis", "real-analysis", "intermediate",
    "2", "§4. Sequences and series of functions",
    r"If $(f_n)$ are continuous on $[a,b]$ and $f_n \to f$ uniformly, then $\int_a^b f = \lim_{n\to\infty} \int_a^b f_n$.")

make("power-series-continuity", "theorem",
    "Continuity of Power Series", "analysis", "real-analysis", "intermediate",
    "2", "§4. Sequences and series of functions",
    r"A power series $\sum a_n(z-z_0)^n$ with radius $R>0$ defines a continuous function on $|z-z_0|<R$, and partial sums converge uniformly on any closed disc $|z-z_0|\leq r < R$.")

make("power-series-termwise-differentiation", "theorem",
    "Term-by-Term Differentiation of Power Series", "analysis", "real-analysis", "intermediate",
    "2", "§4. Sequences and series of functions",
    r"A power series with radius $R>0$ defines a differentiable function on $|z-z_0|<R$, with $f'(x) = \sum_{n=1}^{\infty} n a_n (x - x_0)^{n-1}$.")

make("power-series-infinitely-differentiable", "corollary",
    "Power Series Are Infinitely Differentiable", "analysis", "real-analysis", "intermediate",
    "2", "§4. Sequences and series of functions",
    r"A power series with positive radius defines a $C^\infty$ function, and $a_k = (k!)^{-1} f^{(k)}(x_0)$.")

# §5 Differential equations / exponential
make("exponential-differential-equation", "theorem",
    "Existence and Uniqueness for $f' = af$", "analysis", "real-analysis", "intermediate",
    "2", "§5. Differential equations",
    r"For $a,c \in \mathbb{C}$ there is a unique $C^1$ $f: \mathbb{R} \to \mathbb{C}$ with $f(0)=c$, $f'(x)=af(x)$. The solution is $f(x)=cE(ax)$ where $E(x)=\sum_{n=0}^{\infty} (n!)^{-1}x^n$.")

make("first-order-linear-ode", "theorem",
    "First-Order Linear Differential Equation", "analysis", "real-analysis", "intermediate",
    "2", "§5. Differential equations",
    r"For $a,c \in \mathbb{C}$ and continuous $h$, there is a unique $C^1$ solution to $f(0)=c$, $f'(x)=af(x)+h(x)$: $f(x)=c e^{ax} + \int_0^x e^{a(x-t)}h(t)dt$.")

make("second-order-linear-ode", "theorem",
    "Second-Order Linear ODE with Constant Coefficients", "analysis", "real-analysis", "intermediate",
    "2", "§5. Differential equations",
    r"For $b,c,d_0,d_1 \in \mathbb{C}$ and continuous $h$, there is a unique solution $f$ to $f(0)=d_0$, $f'(0)=d_1$, $f''+bf'+cf=h$.")

make("exponential-function-definition", "definition",
    "Exponential Function", "analysis", "complex-analysis", "basic",
    "2", "§5. Differential equations",
    r"The exponential function is $E(z) = \exp(z) = e^z = \sum_{n=0}^{\infty} (n!)^{-1} z^n$, convergent for all $z \in \mathbb{C}$.")

make("real-exponential-properties", "theorem",
    "Properties of the Real Exponential", "analysis", "real-analysis", "basic",
    "2", "§5. Differential equations",
    r"$E: \mathbb{R} \to \mathbb{R}$ is strictly increasing, $E(0)=1$, $E>0$, $E(x)\to\infty$ as $x\to\infty$, $E(x)\to 0$ as $x\to-\infty$, and $E(x+y)=E(x)E(y)$.")

make("complex-exponential-properties", "theorem",
    "Properties of the Complex Exponential", "analysis", "complex-analysis", "basic",
    "2", "§5. Differential equations",
    r"For $z,w \in \mathbb{C}$: $\exp(z+w)=\exp(z)\exp(w)$, $\exp(z)\neq 0$, $\exp(z^*) = (\exp z)^*$, $|\exp(iy)|=1$ for $y\in\mathbb{R}$.")

# §6 Trigonometric functions
make("sine-cosine-existence", "theorem",
    "Existence and Uniqueness of Sine and Cosine", "analysis", "real-analysis", "basic",
    "2", "§6. Trigonometric functions and the logarithm",
    r"There are unique $C^2$ functions $S,C: \mathbb{R} \to \mathbb{C}$ with $S(0)=0$, $S'(0)=1$, $S''+S=0$ and $C(0)=1$, $C'(0)=0$, $C''+C=0$.")

make("sine-cosine-properties", "theorem",
    "Properties of Sine and Cosine", "analysis", "real-analysis", "basic",
    "2", "§6. Trigonometric functions and the logarithm",
    r"$S,C$ are $C^\infty$, real-valued. $S' = C$, $C' = -S$, $S^2+C^2 = 1$. There is a smallest positive $p$ with $C(p)=0$. Set $\pi = 2p$. Then $S(x+2\pi)=S(x)$, $C(x+2\pi)=C(x)$.")

make("sine-cosine-geometric", "theorem",
    "Geometric Interpretation of Sine and Cosine", "analysis", "real-analysis", "intermediate",
    "2", "§6. Trigonometric functions and the logarithm",
    r"$\gamma(t)=(\cos t,\sin t)$ maps $[0,2\pi]$ onto the unit circle. Arc length from $\gamma(0)$ to $\gamma(t)$ is $t$; circumference is $2\pi$.")

make("trigonometric-complex-properties", "theorem",
    "Complex Trigonometric and Exponential Identities", "analysis", "complex-analysis", "basic",
    "2", "§6. Trigonometric functions and the logarithm",
    r"(a) $\exp(iz) = \cos z + i\sin z$; (b) $\sin(z+2\pi)=\sin z$, $\cos(z+2\pi)=\cos z$, $\exp(z+2\pi i)=\exp z$; (c) $\forall w\neq 0$, $\exists z$ with $w=\exp(z)$; if also $w=\exp(z')$, then $z' = z + 2n\pi i$.")

make("logarithm-definition", "definition",
    "Complex Logarithm", "analysis", "complex-analysis", "basic",
    "2", "§6. Trigonometric functions and the logarithm",
    r"If $w = \exp z$, $z$ is a logarithm of $w$, $z=\log w$. For $x>0$, $\log x$ is the unique real $y$ with $\exp y = x$, and $\frac{d}{dx}(\log x)=1/x$.")

# §7 Functions of two variables
make("partial-derivative-definition", "definition",
    "Partial Derivatives", "analysis", "real-analysis", "basic",
    "2", "§7. Functions of two variables",
    r"For $f: A \to \mathbb{C}$ with $A \subset \mathbb{R}^2$ open, $D_1f(x_0,y_0)=\lim_{x\to x_0}[f(x,y_0)-f(x_0,y_0)](x-x_0)^{-1}$ and $D_2f(x_0,y_0)=\lim_{y\to y_0}[f(x_0,y)-f(x_0,y_0)](y-y_0)^{-1}$.")

make("equality-mixed-partials", "theorem",
    "Equality of Mixed Partial Derivatives", "analysis", "real-analysis", "intermediate",
    "2", "§7. Functions of two variables",
    r"If $f: A \to \mathbb{C}$ is $C^2$, then $D_1 D_2 f = D_2 D_1 f$.")

make("change-order-integration-rectangle", "theorem",
    "Change of Order of Integration (Rectangle)", "analysis", "real-analysis", "intermediate",
    "2", "§7. Functions of two variables",
    r"If $f$ is continuous on $[a,b]\times[c,d]$, then $\int_a^b (\int_c^d f(x,t)dt)dx = \int_c^d (\int_a^b f(s,y)ds)dy$.")

make("change-order-integration-triangle", "theorem",
    "Change of Order of Integration (Triangle)", "analysis", "real-analysis", "intermediate",
    "2", "§7. Functions of two variables",
    r"If $f$ is continuous on $\{(x,y) \mid 0\leq x\leq a, 0\leq y\leq x\}$, then $\int_0^a (\int_0^x f(x,y)dy)dx = \int_0^a (\int_y^a f(x,y)dx)dy$.")

make("polar-coordinates-integration", "theorem",
    "Integration in Polar Coordinates", "analysis", "real-analysis", "intermediate",
    "2", "§7. Functions of two variables",
    r"For continuous $f$ on $D_R=\{(x,y)\mid x^2+y^2<R\}$ with $g(r,\theta)=f(r\cos\theta,r\sin\theta)$: $\iint_{D_R} f = \int_0^R \int_0^{2\pi} g(r,\theta)\, r\, d\theta\, dr$.")

# §8 Smooth functions
make("smooth-bump-function", "proposition",
    "Existence of Nonzero $C^\infty$ Function Vanishing for $x\leq 0$", "analysis", "real-analysis", "intermediate",
    "2", "§8. Some infinitely differentiable functions",
    r"There is a $C^\infty$ function $f: \mathbb{R} \to \mathbb{R}$ with $f(x)=0$ for $x\leq 0$, $f(x)>0$ for $x>0$, and all derivatives vanish at $0$.")

make("smooth-cutoff-function", "corollary",
    "Existence of Smooth Cutoff (Bump) Functions", "analysis", "real-analysis", "intermediate",
    "2", "§8. Some infinitely differentiable functions",
    r"Given $a<b$, there is a $C^\infty$ function $g: \mathbb{R} \to \mathbb{R}$ with $g(x)=0$ for $x\notin(a,b)$ and $g(x)>0$ for $x\in(a,b)$.")

print("=== Chapter 2 concepts created ===")
