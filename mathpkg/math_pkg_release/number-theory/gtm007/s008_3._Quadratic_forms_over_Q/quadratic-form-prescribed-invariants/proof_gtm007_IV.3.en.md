---
role: proof
locale: en
of_concept: quadratic-form-prescribed-invariants
source_book: gtm007
source_chapter: "IV"
source_section: "§3. Quadratic forms over Q"
---

The necessity of the conditions follows from basic properties: $arepsilon_\infty(f) = (-1)^{s(s-1)/2}$ by Sylvester's law of inertia, the product formula gives $\prod_v arepsilon_v(f) = 1$, and the relations for small $n$ are from Chapter IV, §2.

For sufficiency, we construct the form by induction on $n$:

\medskip

oindent 	extbf{$n = 1$:} Take $f = dX^2$. Then $arepsilon_v = 1$ for all $v$, and the signature is determined by the sign of $d$ (positive: $(1,0)$, negative: $(0,1)$).

\medskip

oindent 	extbf{$n = 2$:} For each $v$, the condition $arepsilon_v = (d_v, -1)_v$ must hold. By Theorem 4 of Chapter III (existence of $x \in \mathbf{Q}^*$ with prescribed Hilbert symbols), there exists $x \in \mathbf{Q}^*$ such that $(x, -d)_v = arepsilon_v$ for all $v$. The form $f = xX^2 + xdY^2$ then has the prescribed invariants.

\medskip

oindent 	extbf{$n = 3$:} Let $S$ be the finite set of $v$ such that $(-d, -1)_v = -arepsilon_v$. For each $v \in S$, choose $c_v \in \mathbf{Q}_v^*/\mathbf{Q}_v^{*2}$ distinct from $-d_v$. By the approximation theorem (Lemma 2, Chapter III, §2.2), find $c \in \mathbf{Q}^*$ whose image in each $\mathbf{Q}_v^*/\mathbf{Q}_v^{*2}$ ($v \in S$) equals $c_v$. Using the $n = 2$ case, construct a rank-2 form $g$ with $d(g) = cd$ and $arepsilon_v(g) = (c, -d)_v arepsilon_v$. Then $f = cZ^2 + g$ has the required invariants.

\medskip

oindent 	extbf{$n \geq 4$:} Use induction. If $r \geq 1$, apply the induction hypothesis to obtain a rank-$(n-1)$ form $g$ with invariants $d$, $(arepsilon_v)$, and signature $(r-1, s)$. Then $f = X^2 + g$ works. The case $r = 0$ is handled similarly by subtracting a positive definite form.
