---
role: proof
locale: en
of_concept: lebesgue-measure-transformation-invariance
source_book: gtm018
source_chapter: "III. Extension of Measures"
source_section: "§15. Lebesgue Measure"
---

For $\alpha > 0$: $T(\mathbf{S}) = \mathbf{S}$ follows from the inverse transformation $T^{-1}(x) = (x-\beta)/\alpha$. Define $\mu_1(E) = \mu(T(E))$, $\mu_2(E) = \alpha\mu(E)$ on $\mathbf{S}$. For $E = [a,b)$, $T(E) = [\alpha a + \beta, \alpha b + \beta)$ gives $\mu_1(E) = \alpha(b-a) = \alpha\mu(E) = \mu_2(E)$. By 8.E and 13.A, $\mu(T(E)) = \alpha\mu(E)$ for all $E \in \mathbf{S}$.

For outer measure: $\mu^*(T(E)) = \inf\{\mu(F): T(E) \subset F \in \mathbf{S}\} = \inf\{\alpha\mu(T^{-1}(F)): E \subset T^{-1}(F) \in \mathbf{S}\} = \alpha \inf\{\mu(G): E \subset G \in \mathbf{S}\} = \alpha\mu^*(E)$. Replacing $\inf$ by $\sup$, $\subset$ by $\supset$ gives the inner measure formula. For $\alpha < 0$, compose $x \mapsto |\alpha|x + \beta$ with $x \mapsto -x$.
