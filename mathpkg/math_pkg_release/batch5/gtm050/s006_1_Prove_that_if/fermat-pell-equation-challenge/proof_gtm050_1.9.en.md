---
role: proof
locale: en
of_concept: fermat-pell-equation-challenge
source_book: gtm050
source_chapter: "1"
source_section: "1.9"
---

The problem -- to prove that for every non-square $A$, $y^2 - Ax^2 = 1$ has infinitely many integer solutions -- was Fermat's challenge to the English mathematicians in 1657.

Wallis and Brouncker gave a computational method (the "English method") that produces solutions in particular cases, but they did not prove it always succeeds. Even Euler could not provide a general proof. The first rigorous proof that solutions always exist was given by Lagrange approximately 110 years later. Lagrange's proof is outlined in the exercises following this section. It is unclear whether Fermat himself possessed a fully satisfactory proof, though he claimed the method of infinite descent "duly and properly applied" would supply one.

Once one solution $(x_1, y_1)$ is found, infinitely many solutions are obtained by:
$$y_k + x_k\sqrt{A} = (y_1 + x_1\sqrt{A})^k$$
for $k = 1, 2, 3, \ldots$
