---
role: proof
locale: en
of_concept: root-space-bracket-properties
source_book: gtm009
source_chapter: "8"
source_section: "8.1 Maximal toral subalgebras and roots"
---

**First assertion.** Let $x \in L_\alpha$, $y \in L_\beta$, $h \in H$. By the Jacobi identity,
$$\mathrm{ad} h([x y]) = [[h x] y] + [x [h y]] = \alpha(h) [x y] + \beta(h) [x y] = (\alpha+\beta)(h) [x y].$$
Thus $[x y] \in L_{\alpha+\beta}$, so $[L_\alpha L_\beta] \subset L_{\alpha+\beta}$.

**Second assertion.** If $\alpha \neq 0$, then for any $\beta \in H^*$, only finitely many $\beta + i\alpha$ can be roots (since $\Phi$ is finite). Thus $\mathrm{ad} x$ acts nilpotently on each $L_\beta$, and $L$ is the direct sum of $H$ and all root spaces. Since $\mathrm{ad} x(H) \subset L_\alpha$ and $\mathrm{ad} x$ maps $L_\alpha$ into $L_{2\alpha}$, etc., the finiteness of $\Phi$ forces $\mathrm{ad} x$ to be nilpotent on all of $L$.

**Third assertion.** Choose $h \in H$ such that $(\alpha+\beta)(h) \neq 0$. For $x \in L_\alpha$, $y \in L_\beta$, using associativity of the Killing form:
$$\kappa([h x], y) = -\kappa([x h], y) = -\kappa(x, [h y]),$$
so $\alpha(h) \kappa(x, y) = -\beta(h) \kappa(x, y)$, or $(\alpha+\beta)(h) \kappa(x, y) = 0$. Since $(\alpha+\beta)(h) \neq 0$, we get $\kappa(x, y) = 0$.
