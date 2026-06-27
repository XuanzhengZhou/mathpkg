---
role: proof
locale: en
of_concept: lindenbaum-tarski-algebra-is-cylindric
source_book: gtm037
source_chapter: "12"
source_section: "2"
---

The proof is indicated as "routine checking" and references Sections 9.54-9.56 of the original text. The verification consists of checking that the operations defined on equivalence classes $[\varphi]$ of formulas modulo $\equiv_\Gamma^\mathcal{L}$ satisfy all $\mathrm{CA}_\omega$ axioms. Specifically:

- The Boolean reduct $\langle \mathrm{Fmla}_\mathcal{L}/{\equiv}, +, \cdot, -, 0, 1 \rangle$ is the Lindenbaum-Tarski Boolean algebra, which is well-known to be a Boolean algebra.
- $c_\kappa$ corresponds to $\exists v_\kappa$ and satisfies the cylindrification axioms: $c_\kappa 0 = 0$, $x \leq c_\kappa x$, $c_\kappa(x \cdot c_\kappa y) = c_\kappa x \cdot c_\kappa y$, and $c_\kappa c_\lambda x = c_\lambda c_\kappa x$.
- $d_{\kappa\lambda}$ corresponds to $v_\kappa = v_\lambda$ and satisfies the diagonal axioms: $d_{\kappa\kappa} = 1$, $c_\kappa(d_{\kappa\lambda} \cdot d_{\kappa\mu}) = d_{\lambda\mu}$ for $\kappa \notin \{\lambda, \mu\}$, and $d_{\kappa\lambda} \cdot x \leq c_\kappa(d_{\kappa\lambda} \cdot x)$.

The justification of these operations as well-defined on equivalence classes follows from the definition of $\equiv_\Gamma^\mathcal{L}$ as logical equivalence modulo $\Gamma$.
