---
role: proof
locale: en
of_concept: structure-of-k-mod-k-star-2
source_book: gtm007
source_chapter: "IV"
source_section: "§2.2.2"
---

The proof is given in Chapter III, where the structure of $k^*/k^{*2}$ is studied via local class field theory and the properties of the Hilbert symbol.

For part (a): the dimension $r$ of $k^*/k^{*2}$ as an $\mathbf{F}_2$-vector space is $2$ for $p \neq 2$ (the classes are represented by $1, u, p, up$ where $u$ is a non-square unit) and $3$ for $p = 2$ (there are additional classes from the units congruent to $1$ modulo $8$).

For part (b): the Hilbert symbol $(x,a)$ is a nondegenerate bilinear form on $k^*/k^{*2} \times k^*/k^{*2}$ with values in $\{\pm 1\}$. For $a = 1$, $(x,1) = 1$ for all $x$, so $H_1^1 = k^*/k^{*2}$ (all $2^r$ elements) and $H_1^{-1} = \varnothing$. For $a \neq 1$, the map $x \mapsto (x,a)$ is a nontrivial homomorphism from the $\mathbf{F}_2$-vector space to $\{\pm 1\}$, hence its kernel $H_a^1$ and non-kernel $H_a^{-1}$ each have exactly $2^{r-1}$ elements.

For part (c): the intersection $H_a^\varepsilon \cap H_{a'}^{\varepsilon'}$ is the set of $x$ with $(x,a) = \varepsilon$ and $(x, a') = \varepsilon'$. This is an affine subspace of $k^*/k^{*2}$. If the two linear conditions are dependent, meaning $(a, a') = \varepsilon \varepsilon'$, then the two equations are equivalent and the intersection equals $H_a^\varepsilon$, which has $2^{r-1}$ elements. Otherwise the two conditions are independent, defining a subspace of codimension $2$, hence the intersection has $2^{r-2}$ elements.
