---
role: proof
locale: en
of_concept: cylindric-set-algebra-is-cylindric-algebra
source_book: gtm037
source_chapter: "12. Cylindric Algebras"
source_section: "Part 2: Elements of Logic"
---

By routine checking one verifies that each axiom (C1)-(C7) of Definition 12.2 holds in any cylindric set algebra $\langle A, \cup, \cap, \sim, \varnothing, {}^\alpha U, C_\kappa, D_{\kappa\lambda} \rangle_{\kappa,\lambda < \alpha}$.

- (C1): $C_\kappa \varnothing = \varnothing$ since no $x \in {}^\alpha U$ can satisfy the condition with $y \in \varnothing$.
- (C2): $X \subseteq C_\kappa X$ because each $x \in X$ serves as its own witness ($y = x$).
- (C3): $C_\kappa(X \cap C_\kappa Y) = C_\kappa X \cap C_\kappa Y$ follows from the definition of $C_\kappa$: an element belongs to the left side iff its $\kappa$-th coordinate can be altered to land in $X \cap C_\kappa Y$, which is equivalent to belonging to both $C_\kappa X$ and $C_\kappa Y$.
- (C4): $C_\kappa C_\lambda X = C_\lambda C_\kappa X$ because altering coordinates $\kappa$ and $\lambda$ independently commutes.
- (C5): $D_{\kappa\kappa} = \{x \in {}^\alpha U : x_\kappa = x_\kappa\} = {}^\alpha U$, the unit of the Boolean algebra.
- (C6): If $\kappa \neq \lambda,\mu$, then $D_{\lambda\mu} = C_\kappa(D_{\lambda\kappa} \cap D_{\kappa\mu})$, since an $\alpha$-sequence whose $\lambda$-th and $\mu$-th coordinates are equal can be obtained from one whose $\lambda$-th and $\kappa$-th coordinates are equal and whose $\kappa$-th and $\mu$-th coordinates are equal by altering the $\kappa$-th coordinate appropriately.
- (C7): If $\kappa \neq \lambda$, then $C_\kappa(D_{\kappa\lambda} \cap X) \cap C_\kappa(D_{\kappa\lambda} \cap -X) = \varnothing$, since an $\alpha$-sequence cannot simultaneously satisfy $x_\kappa = x_\lambda$ with an element of $X$ and with an element of its complement after altering the $\kappa$-th coordinate.
