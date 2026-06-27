---
role: proof
locale: en
of_concept: dual-of-product-of-locally-convex-spaces
source_book: gtm003
source_chapter: "IV"
source_section: "4"
---

**Algebraic isomorphism.** Each $f = (f_\alpha) \in \bigoplus_\alpha E'_\alpha$ defines a linear form $x \mapsto f(x) = \sum_\alpha f_\alpha(x_\alpha)$ on $E$. Since only finitely many $f_\alpha$ are non-zero, this linear form is continuous on $E = \prod_\alpha E_\alpha$. Conversely, every continuous linear form $f$ on $\prod_\alpha E_\alpha$ has its kernel containing a product of neighborhoods of zero, which implies that $f$ factors through a finite product, hence is of the above form. This establishes the algebraic isomorphism $E' \cong \bigoplus_\alpha E'_\alpha$.

**1. Weak topology.** By Theorem 4.2, taking each $G_\alpha = E'_\alpha$ and each $\mathfrak{S}_\alpha$ as the family of finite subsets of $E'_\alpha$, the resulting $\mathfrak{S}$-topology on $E$ is the product of the weak topologies, establishing $\sigma(E, E') = \prod_\alpha \sigma(E_\alpha, E'_\alpha)$.

**2. Mackey topology on $E$.** Taking $\mathfrak{S}'_\alpha$ as the family of all convex, circled, $\sigma(E'_\alpha, E_\alpha)$-compact subsets of $E'_\alpha$, Theorem 4.2 shows that it suffices to verify that $\mathfrak{S}' = \bigoplus_\alpha \mathfrak{S}'_\alpha$ is a fundamental system of convex, circled, $\sigma(E', E)$-compact subsets of $E'$. Let $C$ be such a compact set; $C$ is bounded for $\sigma(E', E)$, hence bounded for $\tau(E', E)$. By part 3 of this theorem (proved below) and (II, 6.3), $C$ is contained in $\bigoplus_{\alpha \in H} \tilde{p}_\alpha(C)$ for a finite $H \subset A$, where $\tilde{p}_\alpha: E' \to E'_\alpha$ is the projection. Since $\tilde{p}_\alpha$ is continuous for $\sigma(E', E)$, each $\tilde{p}_\alpha(C) \in \mathfrak{S}'_\alpha$, proving the claim.

**3. Mackey topology on $E'$.** Apply the dual statement of Theorem 4.2 with the saturated families of all convex, circled, $\sigma(E_\alpha, E'_\alpha)$-compact subsets of $E_\alpha$. The corresponding topology on $G = \bigoplus_\alpha E'_\alpha$ is the locally convex direct sum of the $\tau(E'_\alpha, E_\alpha)$ topologies.
