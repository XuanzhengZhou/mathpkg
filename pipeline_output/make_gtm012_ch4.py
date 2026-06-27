#!/usr/bin/env python3
"""Chapter 4 concepts for GTM012: Hilbert Spaces and Fourier Series."""

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

# §1 Inner product and L2
make("inner-product-c-definition", "definition",
    "Inner Product on $\mathcal{C}$", "analysis", "hilbert-spaces", "basic",
    "4", "§1. An inner product in $\mathcal{C}$, and the space $L^2$",
    r"For $u,v \in \mathcal{C}$, $(u,v) = \frac{1}{2\pi}\int_0^{2\pi} u(x)v(x)^* dx$. Properties: $(au,v)=a(u,v)=(u,a^*v)$, $(u_1+u_2,v)=(u_1,v)+(u_2,v)$, $(v,u)=(u,v)^*$, $(u,u)\geq 0$ with equality iff $u=0$.")

make("schwarz-inequality-c", "lemma",
    "Schwarz Inequality in $\mathcal{C}$", "analysis", "hilbert-spaces", "basic",
    "4", "§1. An inner product in $\mathcal{C}$, and the space $L^2$",
    r"For $u,v \in \mathcal{C}$, $|(u,v)| \leq \|u\| \|v\|$ where $\|u\| = (u,u)^{1/2}$.")

make("l2-norm", "corollary",
    "The $L^2$ Norm on $\mathcal{C}$", "analysis", "hilbert-spaces", "basic",
    "4", "§1. An inner product in $\mathcal{C}$, and the space $L^2$",
    r"$\|u\| = (\frac{1}{2\pi}\int_0^{2\pi} |u(x)|^2 dx)^{1/2}$ is a norm on $\mathcal{C}$, dominated by the sup norm: $\|u\| \leq |u|$.")

make("l2-space-definition", "definition",
    "The Space $L^2$ of Periodic Distributions", "analysis", "hilbert-spaces", "intermediate",
    "4", "§1. An inner product in $\mathcal{C}$, and the space $L^2$",
    r"$L^2$ is the set of all $F \in \mathcal{P}'$ for which there is a sequence $(u_n)\subset\mathcal{C}$ with $\|u_n-u_m\|\to 0$ and $F_{u_n} \to F$ in $\mathcal{P}'$. If $u_n \to F$ and $v_n \to G$ in $L^2$, $(F,G)=\lim(u_n,v_n)$.")

make("l2-uniqueness", "lemma",
    "Uniqueness of $L^2$ Limits", "analysis", "hilbert-spaces", "intermediate",
    "4", "§1. An inner product in $\mathcal{C}$, and the space $L^2$",
    r"If $u_n \to F$ and $v_n \to F$ in $L^2$, then $\|u_n - v_n\| \to 0$.")

make("l2-hilbert-space", "theorem",
    "$L^2$ is a Hilbert Space", "analysis", "hilbert-spaces", "intermediate",
    "4", "§1. An inner product in $\mathcal{C}$, and the space $L^2$",
    r"$L^2$ with inner product $(F,G)=\lim(u_n,v_n)$ and norm $\|F\|=(F,F)^{1/2}$ is a complete inner product space, i.e., a Hilbert space.")

# §2 Hilbert space
make("hilbert-space-definition", "definition",
    "Hilbert Space", "analysis", "hilbert-spaces", "intermediate",
    "4", "§2. Hilbert space",
    r"A Hilbert space $H$ is a vector space with an inner product $(u,v)$ satisfying $(au,v)=a(u,v)$, $(u_1+u_2,v)=(u_1,v)+(u_2,v)$, $(v,u)=(u,v)^*$, $(u,u)>0$ if $u\neq 0$, and complete with respect to $\|u\|=(u,u)^{1/2}$.")

make("orthogonality-definition", "definition",
    "Orthogonality in a Hilbert Space", "analysis", "hilbert-spaces", "basic",
    "4", "§2. Hilbert space",
    r"$u,v \in H$ are orthogonal, $u \perp v$, if $(u,v)=0$. $u \perp S$ if $u\perp v$ for all $v \in S$.")

make("pythagorean-theorem-hilbert", "proposition",
    "Pythagorean Theorem in Hilbert Space", "analysis", "hilbert-spaces", "basic",
    "4", "§2. Hilbert space",
    r"If $u \perp v$, then $\|u+v\|^2 = \|u\|^2 + \|v\|^2$.")

make("parallelogram-law", "proposition",
    "Parallelogram Law", "analysis", "hilbert-spaces", "basic",
    "4", "§2. Hilbert space",
    r"$\|u-v\|^2 + \|u+v\|^2 = 2\|u\|^2 + 2\|v\|^2$.")

make("inner-product-continuity", "lemma",
    "Continuity of the Inner Product", "analysis", "hilbert-spaces", "basic",
    "4", "§2. Hilbert space",
    r"If $u_n \to u$ and $v_n \to v$, then $(u_n, v_n) \to (u,v)$.")

make("orthogonal-closure", "corollary",
    "Orthogonal to Set Implies Orthogonal to Closure", "analysis", "hilbert-spaces", "basic",
    "4", "§2. Hilbert space",
    r"If $u \perp S$, then $u$ is orthogonal to the closure of $S$.")

make("closest-point-lemma", "lemma",
    "Closest Point in a Closed Subspace", "analysis", "hilbert-spaces", "intermediate",
    "4", "§2. Hilbert space",
    r"If $H_1 \subset H$ is a closed subspace and $u \in H$, there is a unique $v \in H_1$ minimizing $\|u-v\|$: $\|u-v\| \leq \|u-w\|$ for all $w\in H_1$.")

make("closest-point-characterization", "lemma",
    "Characterization of Closest Point via Orthogonality", "analysis", "hilbert-spaces", "intermediate",
    "4", "§2. Hilbert space",
    r"$v \in H_1$ is closest to $u$ iff $u-v \perp H_1$.")

make("orthogonal-complement-nonzero", "corollary",
    "Existence of Nonzero Orthogonal Vector", "analysis", "hilbert-spaces", "intermediate",
    "4", "§2. Hilbert space",
    r"If $H_1 \subset H$ is a proper closed subspace, there is a nonzero $u \in H$ with $u \perp H_1$.")

make("riesz-representation-theorem", "theorem",
    "Riesz Representation Theorem", "analysis", "hilbert-spaces", "intermediate",
    "4", "§2. Hilbert space",
    r"For every continuous linear functional $L$ on a Hilbert space $H$, there is a unique $v \in H$ such that $L(u) = (u,v)$ for all $u \in H$.")

# §3 Sequence spaces
make("l2-plus-definition", "definition",
    "The Sequence Space $\ell_+^2$", "analysis", "hilbert-spaces", "intermediate",
    "4", "§3. Hilbert spaces of sequences",
    r"$\ell_+^2 = \{(a_n)_{n=1}^{\infty} \subset \mathbb{C} \mid \sum_{n=1}^{\infty} |a_n|^2 < \infty\}$ with inner product $(\mathbf{x},\mathbf{y}) = \sum a_n b_n^*$ is a Hilbert space.")

make("l2-plus-hilbert", "theorem",
    "$\ell_+^2$ is a Hilbert Space", "analysis", "hilbert-spaces", "intermediate",
    "4", "§3. Hilbert spaces of sequences",
    r"$\ell_+^2$ with $(\mathbf{x},\mathbf{y})=\sum_{n=1}^{\infty} a_n b_n^*$ is a complete inner product space (Hilbert space).")

make("l2-two-sided-definition", "definition",
    "Two-Sided Sequence Space $\ell^2$", "analysis", "hilbert-spaces", "intermediate",
    "4", "§3. Hilbert spaces of sequences",
    r"$\ell^2 = \{(a_n)_{n=-\infty}^{\infty} \subset \mathbb{C} \mid \sum_{n=-\infty}^{\infty} |a_n|^2 < \infty\}$.")

make("l2-two-sided-hilbert", "theorem",
    "$\ell^2$ (Two-Sided) is a Hilbert Space", "analysis", "hilbert-spaces", "intermediate",
    "4", "§3. Hilbert spaces of sequences",
    r"$\ell^2$ of two-sided complex sequences with $\sum |a_n|^2 < \infty$ and inner product $\langle\mathbf{x},\mathbf{y}\rangle = \sum_{n=-\infty}^{\infty} a_n b_n^*$ is a Hilbert space.")

# §4 Orthonormal bases
make("orthonormal-set-definition", "definition",
    "Orthonormal Set", "analysis", "hilbert-spaces", "intermediate",
    "4", "§4. Orthonormal bases",
    r"A set $S \subset H$ is orthonormal if $\|e\|=1$ for all $e\in S$ and $(e,f)=0$ for distinct $e,f\in S$.")

make("orthonormal-basis-definition", "definition",
    "Orthonormal Basis", "analysis", "hilbert-spaces", "intermediate",
    "4", "§4. Orthonormal bases",
    r"An orthonormal set $S$ is an orthonormal basis if the set of finite linear combinations of elements of $S$ is dense in $H$.")

make("gram-schmidt", "lemma",
    "Gram-Schmidt Orthonormalization", "analysis", "hilbert-spaces", "intermediate",
    "4", "§4. Orthonormal bases",
    r"Given a finite or countable set $\{u_1,u_2,\ldots\}$ in an inner product space, there is an orthonormal set $\{e_1,e_2,\ldots\}$ with the same span at each step.")

make("separable-hilbert-orthonormal-basis", "lemma",
    "Existence of Orthonormal Basis in Separable Hilbert Space", "analysis", "hilbert-spaces", "intermediate",
    "4", "§4. Orthonormal bases",
    r"A separable Hilbert space has a countable orthonormal basis.")

make("orthonormal-basis-cardinality", "theorem",
    "Cardinality of Orthonormal Bases", "analysis", "hilbert-spaces", "intermediate",
    "4", "§4. Orthonormal bases",
    r"If $\dim H = N < \infty$, any orthonormal basis is a vector space basis with $N$ elements. If $H$ is infinite dimensional, any orthonormal basis is countable.")

# Fourier series concepts
make("fourier-coefficients-definition", "definition",
    "Fourier Coefficients", "analysis", "fourier-analysis", "basic",
    "4", "§4. Orthonormal bases",
    r"For $u \in \mathcal{C}$, the Fourier coefficients are $\hat{u}(n) = \frac{1}{2\pi}\int_0^{2\pi} u(x)e^{-inx}dx$, $n \in \mathbb{Z}$.")

make("bessel-inequality", "theorem",
    "Bessel's Inequality", "analysis", "fourier-analysis", "intermediate",
    "4", "§4. Orthonormal bases",
    r"For any orthonormal set $\{e_n\}$ in a Hilbert space $H$ and any $u\in H$, $\sum |(u,e_n)|^2 \leq \|u\|^2$.")

print("=== Chapter 4 concepts created ===")
