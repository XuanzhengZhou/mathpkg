---
role: proof
locale: en
of_concept: non-transitive-perturbation
source_book: gtm002
source_chapter: "18"
source_section: "18"
---
Suppose $T$ is transitive and $x$ is a point whose positive semiorbit is dense. Let $\varepsilon > 0$ be small enough so that the disk with radius $\varepsilon$ and center $x$ is contained in $X$. Let $n$ be the least positive integer such that $|x - T^n x| < \varepsilon$.

Choose an open disk $U$ with center $x$ and radius less than $\varepsilon$ such that $T^n x$ is interior to $U$ and $Tx, T^2 x, \ldots, T^{n-1} x$ belong to $X \setminus \bar{U}$. (This is possible because $n$ is the least return time and there are only finitely many points $Tx, \ldots, T^{n-1}x$ to avoid.)

Now choose a closed disk $D$ with center $x$ such that $D \subset U$, $T^n(D) \subset U$, and $T(D), T^2(D), \ldots, T^{n-1}(D)$ are contained in $X \setminus U$. (This can be done by taking $D$ sufficiently small, using continuity of $T, T^2, \ldots, T^n$.)

Let $S$ be an automorphism of $X$ that is equal to the identity outside $U$, and inside $U$ is a radial contraction (centered at $x$) that maps $T^n(D)$ onto a subset of the interior of $D$.

Then $(S \circ T)^n(D) = S(T^n(D)) \subset \text{int}(D)$. Consequently, no point of $D$ can have a dense orbit under $S \circ T$, since iterates remain trapped in the contracting region. Therefore $S \circ T$ is not transitive.

Moreover, if an automorphism $R$ is sufficiently close to $S \circ T$ in the uniform metric $\varrho$, then $(R)^n(D)$ will also be mapped into the interior of $D$ (by continuity of the $n$-fold composition as a function of the automorphism in the uniform metric). Hence any automorphism sufficiently close to $S \circ T$ is also non-transitive.

Since the perturbation can be made with an arbitrarily small disk $U$ (by taking $n$ large), $S \circ T$ can be made arbitrarily close to $T$ in the uniform metric. This shows that the set of transitive automorphisms contains no interior points in $H$.
