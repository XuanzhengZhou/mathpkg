---
role: proof
locale: en
of_concept: lebesgue-integral-measure-correspondence
source_book: gtm055
source_chapter: "7"
source_section: "8"
---

**Part 1 (Integral determines measure)**: Define $\mu$ as in (6). We verify that $\mu$ is a measure:
- $\mu(\emptyset) = L(\chi_\emptyset) = L(0) = 0$.
- Finite additivity: If $E_1, E_2$ are disjoint measurable sets and both characteristic functions are integrable, then $\chi_{E_1 \cup E_2} = \chi_{E_1} + \chi_{E_2}$ (a.e.), so $\mu(E_1 \cup E_2) = L(\chi_{E_1} + \chi_{E_2}) = L(\chi_{E_1}) + L(\chi_{E_2}) = \mu(E_1) + \mu(E_2)$.
- Countable additivity follows from axiom $(L_2)$ and the monotone convergence property (Proposition 7.2).

**Part 2 (Uniqueness)**: If $L$ satisfies (6) with respect to a given measure $\mu$, then (6) determines which characteristic functions are integrable and forces $L(\chi_E) = \mu(E)$ when $\mu(E) < +\infty$. By linearity, $L$ is determined on all simple functions. By Proposition 6.6, every integrable function is the pointwise limit of simple functions, and axiom $(L_2)$ forces $L$ on such limits. Thus $L$ is uniquely determined by $\mu$.

**Part 3 (Existence)**: The construction of the Lebesgue integral from a measure is standard and can be found in any integration theory textbook. The procedure begins with simple functions, extends to nonnegative measurable functions via monotone limits, and then to general functions by linear decomposition.
