---
role: proof
locale: en
of_concept: parameter-theorem-for-ends-continued
source_book: gtm005
source_chapter: "IX"
source_section: "7"
---

The end $\int_c T(-, c, c)$ is an object of $X^P$, while $T^\#$ is a functor with codomain $X^P$. By Theorem 2, the arrows $(\omega_p)_c$ of $X$ provide, for each $c \in C$, an arrow of $X^P$ (i.e., a natural transformation)

$$\omega_c^\#: \int_c T(-, c, c) \to T(-, c, c),$$

whose component at $p \in P$ is $(\omega_c^\#)_p = (\omega_p)_c$.

We claim that, as $c$ varies over $C$, the family $\omega^\# = \{\omega_c^\#\}_{c \in C}$ is a wedge

$$\omega^\#: \int_c T(-, c, c) \to T^\#$$

in the functor category $X^P$. Indeed, for any morphism $f: c \to d$ in $C$, the wedge condition in $X^P$ requires that for each $p \in P$ the diagram

$$
\begin{CD}
\int_c T(p, c, c) @>{(\omega_p)_c}>> T(p, c, c) \\
@V{\mathrm{id}}VV @VV{T(p, c, f)}V \\
\int_c T(p, c, c) @>>{(\omega_p)_d}> T(p, c, d)
\end{CD}
$$

commutes, which holds because $\omega_p$ is a wedge over $T(p, -, -)$ for each $p$.

It remains to verify universality. Given any object $F \in X^P$ (a functor $F: P \to X$) and any wedge $\beta: F \to T^\#$ in $X^P$, each component $\beta_p: Fp \to T(p, -, -)$ is a wedge in $X$ over $T(p, -, -)$. By the universal property of the end $\int_c T(p, c, c)$ for the slice at $p$, there exists a unique arrow $\alpha_p: Fp \to \int_c T(p, c, c)$ such that $(\omega_p)_c \circ \alpha_p = (\beta_p)_c$ for all $c \in C$. The assignment $p \mapsto \alpha_p$ is natural in $p$ (by the uniqueness part of the universal property and the naturality of $\beta$), hence defines a unique natural transformation $\alpha: F \to \int_c T(-, c, c)$ in $X^P$ with $\omega^\# \circ \alpha = \beta$. Thus $\omega^\#$ is a universal wedge.
