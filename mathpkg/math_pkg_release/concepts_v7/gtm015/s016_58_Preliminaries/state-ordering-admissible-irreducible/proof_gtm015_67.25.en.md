---
role: proof
locale: en
of_concept: state-ordering-admissible-irreducible
source_book: gtm015
source_chapter: "67"
source_section: "States and representations"
---

# Proof of Ordering of states and irreducibility

Proof. The equivalence of (b) and (c) was proved in (67.22). The equivalence of (a) and (c) turns out to be a proposition in elementary linear algebra.

(c) implies (a): Suppose $f = \lambda g + (1 - \lambda)h$, where $g, h \in \Omega$ and $0 < \lambda < 1$; it is to be shown that $g = h = f$. Obviously $\lambda g \leq f$, therefore $\lambda g = \alpha f$ with $0 \leq \alpha \leq 1$; since $g(1) = f(1) = 1$, we conclude that $\lambda = \alpha$, whence $g = f$ and therefore also $h = f$.

(a) implies (c): Let $g$ be a state such that $g \leq f$. Then $f - g$ is also a state. If $g = 0$ or $g = f$, there is nothing to prove. Otherwise, by the remarks following (67.23), we have $g(1) > 0$ and $(f - g)(1) > 0$, thus $0 < g(1) < f(1) = 1$. Write $\alpha = g(1)$ and define $f_1 = \alpha^{-1}g$, $f_2 = (1 - \alpha)^{-1}(f - g)$; clearly $f_1, f_2$ are normalized states, $0 < \alpha < 1$, and $f = \alpha f_1 + (1 - \alpha)f_2$. Since $f$ is extremal and $f_1, f_2 \in \Omega$, we must have $f_1 = f_2 = f$, whence $g = \alpha f$.
