---
role: proof
locale: en
of_concept: discriminant-invariance-unimodular-transformation
source_book: gtm041
source_chapter: ""
source_section: "Quadratic Forms and the Modular Group"
---

Under the unimodular transformation
$$x = \alpha x' + \beta y', \quad y = \gamma x' + \delta y',$$
with $\alpha\delta - \beta\gamma = 1$, we compute
$$Q(x, y) = a(\alpha x' + \beta y')^2 + b(\alpha x' + \beta y')(\gamma x' + \delta y') + c(\gamma x' + \delta y')^2.$$

Expanding and collecting terms in $x'^2$, $x'y'$, $y'^2$, we obtain
$$Q(x, y) = a'x'^2 + b'x'y' + c'y'^2 = Q_1(x', y')$$
where
\begin{align*}
a' &= a\alpha^2 + b\alpha\gamma + c\gamma^2,\\
b' &= 2a\alpha\beta + b(\alpha\delta + \beta\gamma) + 2c\gamma\delta,\\
c' &= a\beta^2 + b\beta\delta + c\delta^2.
\end{align*}

The discriminant of $Q_1$ is $d' = 4a'c' - b'^2$. Substituting the expressions for $a', b', c'$ and simplifying using $\alpha\delta - \beta\gamma = 1$, we find
$$d' = 4a'c' - b'^2 = (\alpha\delta - \beta\gamma)^2(4ac - b^2) = 1 \cdot d = d.$$

Thus the discriminant is invariant under unimodular transformations. Moreover, equivalent forms represent the same integers: if $Q(x, y) = n$ for integers $x, y$, then the inverse unimodular transformation yields integers $x', y'$ with $Q_1(x', y') = n$.
