---
role: proof
locale: en
of_concept: parameterized-end-in-functor-category
source_book: gtm005
source_chapter: "IX"
source_section: "7"
---

The functor $T^{\#}: C^{\mathrm{op}} \times C \rightarrow X^P$ is defined by the exponential adjunction: for each pair of objects (or arrows) $f, f'$ in $C$, set $T^{\#}(f, f') = T(-, f, f'): P \rightarrow X$, which is a functor from $P$ to $X$, hence an object of $X^P$.

By Theorem 2, the functor $\int_c T(-, c, c): P \rightarrow X$ exists and is an object of $X^P$. For each $c \in C$, the components $(\omega_p)_c: \int_c T(p, c, c) \rightarrow T(p, c, c)$, as $p$ varies, assemble into a natural transformation
\[
\omega^{\#}_c: \int_c T(-, c, c) \rightarrow T(-, c, c) = T^{\#}(c, c)
\]
in $X^P$, whose component at $p$ is $(\omega^{\#}_c)_p = (\omega_p)_c$. Varying $c$, the family $\omega^{\#} = \{\omega^{\#}_c\}_{c \in C}$ is a wedge from the object $\int_c T(-, c, c) \in X^P$ to the functor $T^{\#}$.

To verify the wedge condition in $X^P$: for any arrow $f: c \rightarrow d$ in $C$, we must check that $T^{\#}(1, f) \circ \omega^{\#}_c = T^{\#}(f, 1) \circ \omega^{\#}_d$ as natural transformations $P \rightarrow X$. Evaluating at an arbitrary $p \in P$, this becomes
\[
T(p, 1, f) \circ (\omega_p)_c = T(p, f, 1) \circ (\omega_p)_d,
\]
which holds because $\omega_p$ is a wedge for the end of $T(p, -, -)$.

To establish universality, let $F \in X^P$ be any object (a functor $F: P \rightarrow X$) and let $\beta: F \rightarrow T^{\#}$ be any wedge. For each $p \in P$, the component $\beta_p: F(p) \rightarrow T^{\#}(-)(p) = T(p, -, -)$ is a wedge to $T(p, -, -)$. By the universal property of the end $\omega_p$ of $T(p, -, -)$, there exists a unique arrow $\alpha_p: F(p) \rightarrow \int_c T(p, c, c)$ such that $(\omega_p)_c \circ \alpha_p = (\beta_p)_c$ for all $c \in C$. The assignment $p \mapsto \alpha_p$ is natural in $p$ (by uniqueness), giving a morphism $\alpha: F \rightarrow \int_c T(-, c, c)$ in $X^P$ with $\omega^{\#}_c \circ \alpha = \beta_c$ for all $c$. Thus $\omega^{\#}$ is a universal wedge, exhibiting $\int_c T(-, c, c)$ as the end of $T^{\#}$ in $X^P$.
