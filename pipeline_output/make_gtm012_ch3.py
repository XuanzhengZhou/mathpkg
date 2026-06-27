#!/usr/bin/env python3
"""Chapter 3 concepts for GTM012: Periodic Functions and Periodic Distributions."""

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

# §1 Continuous periodic functions
make("periodic-function-definition", "definition",
    "Periodic Function", "analysis", "fourier-analysis", "basic",
    "3", "§1. Continuous periodic functions",
    r"$u: \mathbb{R} \to \mathbb{C}$ is periodic with period $a \neq 0$ if $u(x+a)=u(x)$ for all $x$. By convention, 'periodic' means period $2\pi$. The set of all continuous periodic functions is $\mathcal{C}$.")

make("c-norm-definition", "definition",
    "Supremum Norm on $\mathcal{C}$", "analysis", "functional-analysis", "basic",
    "3", "§1. Continuous periodic functions",
    r"For $u \in \mathcal{C}$, $|u| = \sup_{x\in\mathbb{R}} |u(x)| = \sup_{x\in[0,2\pi]} |u(x)|$. Properties: $|u|\geq 0$, $|u|=0$ iff $u=0$; $|au|=|a||u|$; $|u+v|\leq|u|+|v|$.")

make("c-complete-normed-space", "theorem",
    "$\mathcal{C}$ is a Complete Normed Vector Space (Banach Space)", "analysis", "functional-analysis", "intermediate",
    "3", "§1. Continuous periodic functions",
    r"$\mathcal{C}$ with operations $(u+v)(x)=u(x)+v(x)$, $(au)(x)=au(x)$, norm $|u|=\sup|u(x)|$, and metric $d(u,v)=|u-v|$ is a complete normed vector space (Banach space).")

make("bounded-linear-functional-definition", "definition",
    "Bounded Linear Functional", "analysis", "functional-analysis", "intermediate",
    "3", "§1. Continuous periodic functions",
    r"A linear functional $F: X \to \mathbb{C}$ on a normed linear space is bounded if $\exists c\geq 0$ such that $|F(u)| \leq c|u|$ for all $u\in X$.")

make("linear-functional-continuous-iff-bounded", "proposition",
    "Linear Functional is Continuous iff Bounded", "analysis", "functional-analysis", "intermediate",
    "3", "§1. Continuous periodic functions",
    r"A linear functional $F$ on a normed linear space is continuous iff it is bounded.")

# §2 Smooth periodic functions
make("smooth-periodic-function-definition", "definition",
    "Smooth Periodic Functions $\mathcal{P}$", "analysis", "fourier-analysis", "intermediate",
    "3", "§2. Smooth periodic functions",
    r"$\mathcal{P} \subset \mathcal{C}$ is the set of smooth (infinitely differentiable) periodic functions. If $u \in \mathcal{P}$, all derivatives $Du, D^2u, \ldots$ are in $\mathcal{P}$.")

make("p-convergence-definition", "definition",
    "Convergence in the Sense of $\mathcal{P}$", "analysis", "functional-analysis", "intermediate",
    "3", "§2. Smooth periodic functions",
    r"$(u_n) \subset \mathcal{P}$ converges to $u \in \mathcal{P}$ in the sense of $\mathcal{P}$ if for each $k=0,1,2,\ldots$, $|D^k u_n - D^k u| \to 0$ as $n\to\infty$.")

make("p-completeness", "theorem",
    "$\mathcal{P}$ is Complete with Respect to $\mathcal{P}$-Convergence", "analysis", "functional-analysis", "intermediate",
    "3", "§2. Smooth periodic functions",
    r"If $(u_n)\subset\mathcal{P}$ and $(D^k u_n)$ is uniformly Cauchy for each $k$, the limit $u$ is in $\mathcal{P}$ and $D^k u_n \to D^k u$ uniformly.")

make("seminorm-definition", "definition",
    "Seminorm", "analysis", "functional-analysis", "intermediate",
    "3", "§2. Smooth periodic functions",
    r"A seminorm on a vector space $X$ is $u\mapsto |u|$ with $|u|\geq 0$, $|au|=|a||u|$, $|u+v|\leq|u|+|v|$. A seminorm is a norm iff $|u|=0 \implies u=0$.")

make("frechet-space-definition", "definition",
    "Fréchet Space", "analysis", "functional-analysis", "advanced",
    "3", "§2. Smooth periodic functions",
    r"$X$ with a countable sequence of seminorms $|u|_k$ satisfying $|u|_k=0$ for all $k \implies u=0$ is a Fréchet space if complete under $d'(u,v)=\sum 2^{-k}|u-v|_k[1+|u-v|_k]^{-1}$.")

make("p-frechet-space", "theorem",
    "$\mathcal{P}$ is a Fréchet Space", "analysis", "functional-analysis", "advanced",
    "3", "§2. Smooth periodic functions",
    r"$(\mathcal{P}, d')$ with $d'(u,v)=\sum_{k=0}^{\infty} 2^{-k-1}|D^k u - D^k v|[1+|D^k u - D^k v|]^{-1}$ is a complete metric space, hence a Fréchet space. Convergence in this metric is equivalent to convergence in the sense of $\mathcal{P}$.")

# §3 Translation, convolution, approximation
make("translation-definition", "definition",
    "Translation Operator $T_t$", "analysis", "fourier-analysis", "basic",
    "3", "§3. Translation, convolution, and approximation",
    r"For $u \in \mathcal{C}$ and $t \in \mathbb{R}$, the translate is $T_t u(x) = u(x-t)$.")

make("convolution-definition", "definition",
    "Convolution of Periodic Functions", "analysis", "fourier-analysis", "basic",
    "3", "§3. Translation, convolution, and approximation",
    r"For $u,v \in \mathcal{C}$, the convolution is $(u * v)(x) = \frac{1}{2\pi} \int_0^{2\pi} u(x-y)v(y)dy$.")

make("convolution-properties", "proposition",
    "Algebraic Properties of Convolution", "analysis", "fourier-analysis", "basic",
    "3", "§3. Translation, convolution, and approximation",
    r"$u*v = v*u$, $(au)*v = a(u*v)$, $(u+v)*w = u*w + v*w$, $(u*v)*w = u*(v*w)$, $T_t(u*v) = (T_t u)*v = u*(T_t v)$, $|u*v| \leq |u|\,|v|$.")

make("difference-quotient-convergence", "lemma",
    "Uniform Convergence of Difference Quotient to Derivative", "analysis", "fourier-analysis", "intermediate",
    "3", "§3. Translation, convolution, and approximation",
    r"If $u \in \mathcal{P}$, then $|t^{-1}(T_{-t}u - u) - Du| \to 0$ as $t \to 0$.")

make("convolution-with-smooth-is-smooth", "proposition",
    "Convolution with Smooth Function is Smooth", "analysis", "fourier-analysis", "intermediate",
    "3", "§3. Translation, convolution, and approximation",
    r"If $u \in \mathcal{P}$ and $v \in \mathcal{C}$, then $u * v \in \mathcal{P}$ and $D^k(u*v) = (D^k u)*v$.")

make("convolution-continuity", "proposition",
    "Continuity of Convolution in $\mathcal{P}$", "analysis", "fourier-analysis", "intermediate",
    "3", "§3. Translation, convolution, and approximation",
    r"If $u_n \to u$ in $\mathcal{P}$ and $v \in \mathcal{C}$, then $u_n * v \to u * v$ in $\mathcal{P}$.")

make("approximate-identity-definition", "definition",
    "Approximate Identity", "analysis", "fourier-analysis", "intermediate",
    "3", "§3. Translation, convolution, and approximation",
    r"$(\varphi_n) \subset \mathcal{C}$ is an approximate identity if: (i) $\varphi_n(x)\geq 0$; (ii) $\frac{1}{2\pi}\int_0^{2\pi}\varphi_n=1$; (iii) for $0<\delta<\pi$, $\int_0^{2\pi-\delta}\varphi_n \to 0$ as $n\to\infty$.")

make("approximate-identity-approximation", "theorem",
    "Approximation by an Approximate Identity", "analysis", "fourier-analysis", "intermediate",
    "3", "§3. Translation, convolution, and approximation",
    r"If $(\varphi_n)\subset\mathcal{C}$ is an approximate identity, then for $u\in\mathcal{C}$, $|\varphi_n * u - u|\to 0$. If $u\in\mathcal{P}$, $\varphi_n * u \to u$ in $\mathcal{P}$.")

# §4 Weierstrass approximation
make("trigonometric-polynomial-definition", "definition",
    "Trigonometric Polynomial", "analysis", "fourier-analysis", "basic",
    "3", "§4. The Weierstrass approximation theorems",
    r"A trigonometric polynomial is $\varphi(x) = \sum_{k=-n}^{n} a_k \exp(ikx)$ with $a_k \in \mathbb{C}$.")

make("trig-approximate-identity-existence", "lemma",
    "Existence of Trigonometric Polynomial Approximate Identity", "analysis", "fourier-analysis", "intermediate",
    "3", "§4. The Weierstrass approximation theorems",
    r"There is a sequence of trigonometric polynomials which is an approximate identity. In particular, $\varphi_n(x) = c_n(1+\cos x)^n$ with suitable $c_n$.")

make("trig-convolution-preserves-trig", "lemma",
    "Convolution of a Trigonometric Polynomial with $\mathcal{C}$ is Trigonometric Polynomial", "analysis", "fourier-analysis", "basic",
    "3", "§4. The Weierstrass approximation theorems",
    r"If $\varphi$ is a trigonometric polynomial and $u \in \mathcal{C}$, then $\varphi * u$ is a trigonometric polynomial.")

make("weierstrass-trigonometric-approximation", "theorem",
    "Weierstrass Trigonometric Approximation Theorem", "analysis", "fourier-analysis", "intermediate",
    "3", "§4. The Weierstrass approximation theorems",
    r"Any $u\in\mathcal{C}$ is the uniform limit of a sequence of trigonometric polynomials. If $u\in\mathcal{P}$, the sequence converges in $\mathcal{P}$.")

make("p-dense-in-c", "corollary",
    "$\mathcal{P}$ is Dense in $\mathcal{C}$", "analysis", "fourier-analysis", "intermediate",
    "3", "§4. The Weierstrass approximation theorems",
    r"$\mathcal{P}$ is dense in $\mathcal{C}$ with respect to the uniform norm.")

make("weierstrass-polynomial-approximation", "theorem",
    "Weierstrass Polynomial Approximation Theorem", "analysis", "real-analysis", "intermediate",
    "3", "§4. The Weierstrass approximation theorems",
    r"Any continuous complex-valued function on a closed interval $[a,b]$ is the uniform limit of a sequence of polynomials.")

# §5 Periodic distributions
make("periodic-distribution-definition", "definition",
    "Periodic Distribution", "analysis", "distribution-theory", "advanced",
    "3", "§5. Periodic distributions",
    r"A periodic distribution is a linear functional $F: \mathcal{P} \to \mathbb{C}$ such that $F(u_n) \to F(u)$ whenever $u_n \to u$ in $\mathcal{P}$. The space of all periodic distributions is $\mathcal{P}'$.")

make("function-as-distribution", "definition",
    "Function as a Periodic Distribution $F_v$", "analysis", "distribution-theory", "intermediate",
    "3", "§5. Periodic distributions",
    r"If $v\in\mathcal{C}$, $F_v(u) = \frac{1}{2\pi}\int_0^{2\pi} v(x)u(x)dx$ defines a periodic distribution. $F$ is a function if $F=F_v$ for some $v\in\mathcal{C}$.")

make("dirac-delta-definition", "definition",
    "Dirac $\delta$-Distribution", "analysis", "distribution-theory", "intermediate",
    "3", "§5. Periodic distributions",
    r"The Dirac $\delta$-distribution is $\delta(u) = u(0)$ for $u \in \mathcal{P}$. It is not a function.")

make("p-prime-vector-space", "definition",
    "Vector Space Structure of $\mathcal{P}'$", "analysis", "distribution-theory", "advanced",
    "3", "§5. Periodic distributions",
    r"$\mathcal{P}'$ is a vector space: $(F+G)(u)=F(u)+G(u)$, $(aF)(u)=aF(u)$. $F_{v}+F_w=F_{v+w}$, $F_{av}=aF_v$.")

make("p-prime-convergence-definition", "definition",
    "Convergence in $\mathcal{P}'$", "analysis", "distribution-theory", "advanced",
    "3", "§5. Periodic distributions",
    r"$(F_n) \subset \mathcal{P}'$ converges to $F \in \mathcal{P}'$ if $F_n(u) \to F(u)$ for all $u \in \mathcal{P}$.")

make("distribution-operations", "definition",
    "Operations on Periodic Distributions (Reversal, Translation, Derivative)", "analysis", "distribution-theory", "advanced",
    "3", "§5. Periodic distributions",
    r"Reversal: $F^\sim(u)=F(\tilde{u})$ where $\tilde{u}(x)=u(-x)$. Translation: $(T_tF)(u)=F(T_{-t}u)$. Derivative: $(DF)(u)=-F(Du)$. Inductively, $(D^kF)(u)=(-1)^kF(D^ku)$.")

make("distribution-operations-continuity", "proposition",
    "Continuity of Operations on $\mathcal{P}'$", "analysis", "distribution-theory", "advanced",
    "3", "§5. Periodic distributions",
    r"If $F_n \to F$ in $\mathcal{P}'$, then $F_n^\sim \to F^\sim$, $T_tF_n \to T_tF$, and $D^kF_n \to D^kF$ in $\mathcal{P}'$.")

make("distribution-derivative-as-limit", "proposition",
    "Derivative as Limit of Difference Quotient in $\mathcal{P}'$", "analysis", "distribution-theory", "advanced",
    "3", "§5. Periodic distributions",
    r"If $F \in \mathcal{P}'$, then $t^{-1}(T_{-t}F - F) \to DF$ in $\mathcal{P}'$ as $t \to 0$.")

make("distribution-reality-definitions", "definition",
    "Real, Imaginary, Even, and Odd Distributions", "analysis", "distribution-theory", "advanced",
    "3", "§5. Periodic distributions",
    r"$\operatorname{Re}F = (F+F^*)/2$, $\operatorname{Im}F = (F-F^*)/(2i)$. $F$ is real if $F=F^*$. $F$ is even if $F=F^\sim$, odd if $F=-F^\sim$.")

# §6 Determining periodic distributions
make("distribution-order-definition", "definition",
    "Order of a Periodic Distribution", "analysis", "distribution-theory", "advanced",
    "3", "§6. Determining the periodic distributions",
    r"$F \in \mathcal{P}'$ is of order $k$ ($k \geq 0$) if $\exists c$ such that $|F(u)| \leq c(|u|+|Du|+\cdots+|D^k u|)$ for all $u\in\mathcal{P}$.")

make("distribution-finite-order", "theorem",
    "Every Periodic Distribution Has Finite Order", "analysis", "distribution-theory", "advanced",
    "3", "§6. Determining the periodic distributions",
    r"If $F \in \mathcal{P}'$, there is an integer $k \geq 0$ such that $F$ is of order $k$.")

make("order-zero-distribution-extension", "theorem",
    "Extension of Order 0 Distribution to $\mathcal{C}$", "analysis", "distribution-theory", "advanced",
    "3", "§6. Determining the periodic distributions",
    r"If $F \in \mathcal{P}'$ is of order 0, then $F$ extends uniquely to a continuous linear functional on $\mathcal{C}$.")

make("distribution-structure-theorem", "theorem",
    "Structure Theorem for Periodic Distributions", "analysis", "distribution-theory", "advanced",
    "3", "§6. Determining the periodic distributions",
    r"Every $F \in \mathcal{P}'$ can be written as $F = D^k F_v + F_f$ for some integer $k \geq 0$, $v \in \mathcal{C}$, and constant function $f$.")

make("antiderivative-lemma", "lemma",
    "Existence and Uniqueness of Distributional Antiderivative", "analysis", "distribution-theory", "advanced",
    "3", "§6. Determining the periodic distributions",
    r"Given $F\in\mathcal{P}'$, there is a unique $G\in\mathcal{P}'$ with $DG=F$ and $G(e)=0$, where $e(x)=1$. If $F$ is of order $k$, $G$ is of order $k-1$.")

make("derivative-zero-implies-constant-distribution", "corollary",
    "Distribution with Zero Derivative is Constant", "analysis", "distribution-theory", "advanced",
    "3", "§6. Determining the periodic distributions",
    r"If $G \in \mathcal{P}'$ and $DG = 0$, then $G = F_f$ where $f$ is a constant function.")

# §7 Convolution of distributions
make("convolution-distribution-function-definition", "definition",
    "Convolution of a Distribution with a Smooth Function", "analysis", "distribution-theory", "advanced",
    "3", "§7. Convolution of distributions",
    r"For $F\in\mathcal{P}'$ and $u\in\mathcal{P}$, $(F * u)(x) = F(T_x \tilde{u})$ where $\tilde{u}(x)=u(-x)$.")

make("convolution-distribution-function-properties", "proposition",
    "$F * u$ is Smooth and Its Properties", "analysis", "distribution-theory", "advanced",
    "3", "§7. Convolution of distributions",
    r"$F * u \in \mathcal{P}$, $(aF)*u = a(F*u) = F*(au)$, $(F+G)*u = F*u + G*u$, $F*(u+v) = F*u + F*v$, $T_t(F*u) = (T_tF)*u = F*(T_tu)$, $D^k(F*u) = (D^kF)*u = F*(D^ku)$, $\delta * u = u$, $(D^k\delta)*u = D^ku$.")

make("distribution-convolution-definition", "definition",
    "Convolution of Distributions $F * G$", "analysis", "distribution-theory", "advanced",
    "3", "§7. Convolution of distributions",
    r"For $F,G\in\mathcal{P}'$, $(F * G)(u) = F(G^\sim * u)$ for $u\in\mathcal{P}$.")

make("distribution-convolution-continuity", "lemma",
    "Continuity of $F * u$ in $\mathcal{P}$", "analysis", "distribution-theory", "advanced",
    "3", "§7. Convolution of distributions",
    r"If $F\in\mathcal{P}'$ and $u_n \to u$ in $\mathcal{P}$, then $F * u_n \to F * u$ in $\mathcal{P}$.")

make("distribution-convolution-approx-theorem", "theorem",
    "Approximation of Distributions by Smooth Functions", "analysis", "distribution-theory", "advanced",
    "3", "§7. Convolution of distributions",
    r"If $(\varphi_n)\subset\mathcal{P}$ is an approximate identity and $F\in\mathcal{P}'$, then $F * \varphi_n \to F$ in $\mathcal{P}'$. If the $\varphi_n$ are trigonometric polynomials, so are $F*\varphi_n$.")

make("distribution-convolution-algebraic-properties", "proposition",
    "Algebraic Properties of Distribution Convolution", "analysis", "distribution-theory", "advanced",
    "3", "§7. Convolution of distributions",
    r"$F*G = G*F$, $(aF)*G = a(F*G) = F*(aG)$, $(F+G)*H = F*H + G*H$, $(F*G)*H = F*(G*H)$, $T_t(F*G) = (T_tF)*G = F*(T_tG)$, $D^k(F*G) = (D^kF)*G = F*(D^kG)$.")

print("=== Chapter 3 concepts created ===")
