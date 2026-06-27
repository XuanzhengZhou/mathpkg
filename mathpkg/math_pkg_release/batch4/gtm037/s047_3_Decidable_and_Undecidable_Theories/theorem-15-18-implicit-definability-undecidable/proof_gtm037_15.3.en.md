---
role: proof
locale: en
of_concept: theorem-15-18-implicit-definability-undecidable
source_book: gtm037
source_chapter: "15"
source_section: "3"
---

Suppose $\Gamma$ is decidable. Let

$$A = \{ e : e \text{ is the Gödel number of a formula } \psi \text{ having at most } v_0 \text{ free, and } \psi(e) \notin \Gamma \}.$$

Clearly $A$ is recursive, by the hypothesis that $\Gamma$ is decidable (membership in $\Gamma$ is decidable, and the condition on $e$ being the Gödel number of a formula with at most $v_0$ free is recursive).

Let $\varphi$ weakly syntactically define $A$ in $\Gamma$, and set $e = g^{+} \varphi$. Then

$$\varphi(e) \in \Gamma \quad \text{iff} \quad e \in A \quad (\text{since } \varphi \text{ weakly syntactically defines } A)$$

$$\text{iff} \quad \varphi(e) \notin \Gamma \quad (\text{by definition of } A).$$

This is a contradiction. Therefore $\Gamma$ is undecidable.

The above proof constitutes a typical application of the diagonal method.
