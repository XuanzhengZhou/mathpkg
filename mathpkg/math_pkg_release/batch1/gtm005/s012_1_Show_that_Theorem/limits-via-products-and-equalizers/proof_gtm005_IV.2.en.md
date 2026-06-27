---
role: proof
locale: en
of_concept: limits-via-products-and-equalizers
source_book: gtm005
source_chapter: "IV"
source_section: "2"
---

Theorem: $C$ has all small limits iff $C$ has all small products and equalizers.

($\Leftarrow$) Given $F: J \to C$, construct $\varprojlim F$:

1. Form $P = \prod_{j \in J_0} F(j)$ (product over objects of $J$) with projections $\pi_j: P \to F(j)$.
2. Form $Q = \prod_{\alpha: j \to k} F(k)$ (product over arrows of $J$) with projections $\rho_\alpha: Q \to F(k)$.
3. Define $f, g: P \to Q$ by $\rho_\alpha \circ f = \pi_k$ and $\rho_\alpha \circ g = F(\alpha) \circ \pi_j$ for each $\alpha: j \to k$.
4. The equalizer $e: L \to P$ of $f, g$ is $\varprojlim F$, with cone $\lambda_j = \pi_j \circ e$.

The equalizer condition $f \circ e = g \circ e$ ensures $F(\alpha) \circ \lambda_j = \lambda_k$, i.e., the $\lambda_j$ form a cone. Universality: any cone $\{\mu_j: X \to F(j)\}$ induces $h: X \to P$ with $\pi_j \circ h = \mu_j$, and the cone condition ensures $f \circ h = g \circ h$, so $h$ factors uniquely through $e$, giving the unique map $X \to L$.

($\Rightarrow$) Products and equalizers are special limits (limits over discrete categories and over $\bullet \rightrightarrows \bullet$).
