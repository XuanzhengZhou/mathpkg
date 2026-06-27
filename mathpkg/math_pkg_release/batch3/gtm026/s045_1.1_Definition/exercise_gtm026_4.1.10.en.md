---
role: exercise
locale: en
chapter: "4"
section: "1"
exercise_number: 10
---

Let $T$ be a dynamic theory, let $(X, \xi)$ be a $T$-algebra, let $E = E(X, \xi)$ and let $I$ be a minimal right ideal of $E$. Points $x, y$ in $X$ are *distal* if $xp \neq yp$ for all $p$ in $E$, and $x, y$ are *proximal* if $x, y$ are not distal.

(a) ([Auslander '63, Theorem 2].) Show that if $(X, \xi)$ is minimal and if $f: (X, \xi) \longrightarrow (X, \xi)$ is a $T$-endomorphism with $f \neq \mathrm{id}_X$, then $x$ and $xf$ are distal for all $x$ in $X$. [Hint: if there exists $x$ with $x, xf$ proximal then $xp = xfp$ for some $p$ in $E$; as $xpE = X$, $xpq = x$ for some $q$ in $E$; as $x$ is in $\mathrm{eq}(f, \mathrm{id}_X)$, $f = \mathrm{id}_X$, a contradiction.]

(b) ([Auslander '63, Theorem 4].) Let $(X, \xi)$ be minimal. Prove that $(X, \xi)$ is a universal minimal set in $\mathrm{SMP}(X, \xi)$ if and only if for every $x, y$ in $X$ there exists a $T$-endomorphism $f: (X, \xi) \longrightarrow (X, \xi)$ such that $xf$ and $y$ are proximal. [Hint: if $p, q$ are in $I$ let $ap$ be a left unit of $I$; then $(pL_{qa})ap = q(ap)$, $L_{qa}$ is a $T$-endomorphism of $I$, and $-ap$ is in $E(I)$ using exercise 3; conversely, it suffices to show that the map $I \longrightarrow X$, $p \mapsto xp$ is injective for any fixed $x$.]
