---
role: proof
locale: en
of_concept: three-square-theorem
source_book: gtm007
source_chapter: "IV"
source_section: "§3. Quadratic forms over Q"
---

The proof uses the Hasse-Minkowski theorem (Theorem 8) to handle the representation over $\mathbf{Q}$, and the Davenport-Cassels lemma (Lemma B) to descend from rational to integral representations.

\medskip

oindent 	extbf{Step 1: Local conditions.}
For the quadratic form $f = X_1^2 + X_2^2 + X_3^2$, one determines when $n$ is represented by $f$ over each $\mathbf{Q}_v$. At the real place ($v = \infty$), $f_\infty$ represents all positive numbers. For an odd prime $p$, $f$ has rank $3$ and discriminant $1$; using the local criterion (Chapter IV, §2, Corollary to Theorem 6), one checks that $f$ represents every $p$-adic integer $n$. At $p = 2$, the computation of the Hilbert symbols yields:
$$
(-1, -d_2(f))_2 = (-1, -1)_2 = 1 = arepsilon_2(f),
$$
so by the corollary to Theorem 6, $n$ is represented at $2$ if and only if $n 
eq -1$ in $\mathbf{Q}_2^*/\mathbf{Q}_2^{*2}$, i.e., if $-n$ is not a square in $\mathbf{Q}_2$. This happens precisely when $n$ is not of the form $4^a(8b-1)$. Thus the local conditions are satisfied exactly for such $n$, and by the Hasse-Minkowski theorem, $f$ represents $n$ over $\mathbf{Q}$.

\medskip

oindent 	extbf{Step 2: From rational to integral representation.}
Apply the Davenport-Cassels lemma (Lemma B). The form $f = X_1^2 + X_2^2 + X_3^2$ satisfies hypothesis (H) of the lemma: for any $x = (x_1, x_2, x_3) \in \mathbf{Q}^3$, choose $y_i \in \mathbf{Z}$ such that $|x_i - y_i| \leq 1/2$; then $f(x-y) \leq 3/4 < 1$. Hence, if $n \in \mathbf{Z}$ is represented by $f$ over $\mathbf{Q}$, it is also represented over $\mathbf{Z}$. This completes the proof.
