---
role: proof
locale: en
of_concept: kummers-theorem
source_book: gtm043
source_chapter: "10"
source_section: "18"
---

**Proof of Theorem 10.3.**

**(a)** The following are evidently equivalent: $\tau'$ is an isomorphism; $\tau'g = 0$ implies $g = 0$; $g(\tau x) = 0$ for all $x \in X$ implies $g = 0$; $\tau[X]$ is dense in $Y$ (since $Y$ is completely regular).

**(b) Necessity.** The hypothesis asserts that for each $f \in C(X)$ there exists $g \in C(Y)$ such that $f = \tau'g = g \circ \tau$. Then for any $x_1, x_2 \in X$, if $\tau x_1 = \tau x_2$, we have $f(x_1) = g(\tau x_1) = g(\tau x_2) = f(x_2)$ for every $f \in C(X)$. Since $X$ is completely regular, this implies $x_1 = x_2$; hence $\tau$ is one-one. Moreover, if $h \in C(\tau[X])$, then $h \circ \tau \in C(X)$, so there exists $g \in C(Y)$ with $g \circ \tau = h \circ \tau$. Since $\tau$ is one-one, $g$ coincides with $h$ on $\tau[X]$; thus $h$ extends to $g$ on $Y$. Therefore $\tau[X]$ is $C$-embedded in $Y$. The continuity of $\tau^{-1}$ follows from Theorem 3.8, because any $f \in C(X)$ can be written as $g \circ \tau$, so $f \circ \tau^{-1} = g$ is continuous on $\tau[X]$. Hence $\tau$ is a homeomorphism.

**Sufficiency.** If $\tau$ is a homeomorphism and $\tau[X]$ is $C$-embedded, then every $f \in C(X)$ gives $f \circ \tau^{-1} \in C(\tau[X])$, which extends to some $g \in C(Y)$. Then $\tau'g = g \circ \tau = f$, so $\tau'$ is onto. The proof for $C^*$ is analogous.
