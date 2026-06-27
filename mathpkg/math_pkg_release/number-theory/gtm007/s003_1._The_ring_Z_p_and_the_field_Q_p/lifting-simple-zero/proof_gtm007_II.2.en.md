---
role: proof
locale: en
of_concept: lifting-simple-zero
source_book: gtm007
source_chapter: "II. p-Adic Fields"
source_section: "2. p-adic equations"
---

*Proof.* This is the special case $n = 1, k = 0$ of the $p$-adic Newton method lemma. A zero $x$ modulo $p$ of the reduction of $f$ is called simple if at least one partial derivative $\partial f / \partial X_j$ is nonzero at $x$. In the case $m = 1$, this means $f(x) \equiv 0 \pmod{p}$ and $f'(x) \not\equiv 0 \pmod{p}$, i.e., $v_p(f'(x)) = 0 = k$. The condition $0 \leq 2k < n$ becomes $0 \leq 0 < 1$, which holds. By the $p$-adic Newton lemma, there exists $y \in \mathbb{Z}_p$ such that $f(y) \equiv 0 \pmod{p^2}$ and $y \equiv x \pmod{p}$. Iterating, we obtain a Cauchy sequence converging to a zero $y \in \mathbb{Z}_p$ of $f$ with $y \equiv x \pmod{p}$.

For $m > 1$, one reduces to the $m=1$ case by fixing all but one variable and applying the lemma to the single-variable polynomial obtained. Specifically, if $x = (x_1, \ldots, x_m)$ is a simple zero modulo $p$, then some $\partial f/\partial X_j$ is nonzero at $x$. Let $\tilde{f}(X_j)$ be the polynomial in one variable obtained by substituting $X_i = x_i$ for all $i \neq j$. Then $\tilde{f}(x_j) \equiv 0 \pmod{p}$ and $\tilde{f}'(x_j) = \partial f/\partial X_j(x) \not\equiv 0 \pmod{p}$, so the single-variable case applies, yielding $y_j \in \mathbb{Z}_p$ with $\tilde{f}(y_j) = 0$ and $y_j \equiv x_j \pmod{p}$. Setting $y_i = x_i$ for $i \neq j$ gives the desired zero $y$. $\square$
