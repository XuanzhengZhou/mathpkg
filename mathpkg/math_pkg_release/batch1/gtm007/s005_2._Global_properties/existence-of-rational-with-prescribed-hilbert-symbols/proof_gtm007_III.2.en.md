---
role: proof
locale: en
of_concept: existence-of-rational-with-prescribed-hilbert-symbols
source_book: gtm007
source_chapter: "III"
source_section: "§2. Global properties"
---

The necessity of (1) and (2) follows from Theorem 3 (the product formula): since $(a_i, x)_v = 1$ for almost all $v$, almost all $arepsilon_{i,v}$ equal $1$, and $\prod_v arepsilon_{i,v} = \prod_v (a_i, x)_v = 1$. The necessity of (3) is trivial by taking $x_v = x$.

For sufficiency, assume $(arepsilon_{i,v})$ satisfies (1), (2), (3). After multiplying the $a_i$ by squares of integers, we may assume all $a_i$ are integers. Let $S$ be the finite subset of $V$ consisting of $\infty$, $2$, and the primes dividing the $a_i$. Let $T$ be the finite set of $v \in V$ such that $arepsilon_{i,v} = -1$ for some $i$.

\medskip

oindent 	extbf{Case 1:} $S \cap T = arnothing$.

Set $a = \prod_{\ell \in T} \ell$ and $m = 8 \prod_{\ell \in S \setminus \{\infty\}} \ell$. Using Dirichlet's theorem (Lemma 3), choose a prime $p$ such that $p \equiv a \pmod{m}$ and $p 
otin S \cup T$. One checks that $x = p$ (or $x = ap$ in some subcases) satisfies the required Hilbert symbol conditions. The verification uses the explicit formulas for Hilbert symbols from Chapter III, §1. The remaining prime $p$ is handled via the product formula:
$$
(a_i, x)_p = \prod_{v 
eq p} (a_i, x)_v = \prod_{v 
eq p} arepsilon_{i,v} = arepsilon_{i,p}.
$$

\medskip

oindent 	extbf{Case 2:} General case.

The squares of $\mathbf{Q}^*_v$ form an open subgroup of $\mathbf{Q}^*_v$. By Lemma 2 (approximation theorem), there exists $x' \in \mathbf{Q}^*$ such that $x'/x_v$ is a square in $\mathbf{Q}^*_v$ for all $v \in S$. In particular, $(a_i, x')_v = (a_i, x_v)_v = arepsilon_{i,v}$ for all $v \in S$. Define $\eta_{i,v} = arepsilon_{i,v}(a_i, x')_v$. The family $(\eta_{i,v})$ satisfies (1), (2), (3) and additionally $\eta_{i,v} = 1$ for $v \in S$. By Case 1, there exists $y \in \mathbf{Q}^*$ such that $(a_i, y)_v = \eta_{i,v}$ for all $i, v$. Setting $x = y x'$ completes the proof.
