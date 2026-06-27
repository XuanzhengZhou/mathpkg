---
role: proof
locale: en
of_concept: syntactic-implies-recursive-for-cons-r-a-theory
source_book: gtm037
source_chapter: "14"
source_section: "Decidable and Undecidable Theories"
---

Say $\Gamma$ is recursively axiomatized by $\Delta$. Let

$$\mathbf{T}_m^{\Delta} = \{(e, x_0, \ldots, x_{m-1}, z, y) : e \text{ is the Gödel number of a formula } \varphi \text{ with free variables among } v_0, \ldots, v_m, \text{ and } y \text{ is the Gödel number of a proof in } \Gamma \text{ of } \varphi(\mathbf{x}_0, \ldots, \mathbf{x}_{m-1}, \mathbf{z}) \text{ from } \Delta\}.$$

Then $T_m^{\Delta}$ is recursive. Let $f$ be syntactically defined in $\Gamma$ by $\varphi$, and let $e = g^{+} \varphi$. Then for all $x_0, \ldots, x_{m-1} \in \omega$ we have

$$f(x_0, \ldots, x_{m-1}) = y \quad \text{iff} \quad \exists z ((e, x_0, \ldots, x_{m-1}, z, y) \in T_m^{\Delta}),$$

so $f$ is r.e. Let $g$ be the unary function defined by: $g(y) = y$ if $\exists z ((e, x_0, \ldots, x_{m-1}, z, y) \in T_m^{\Delta})$, and $g(y) = \text{undefined}$ otherwise. Then $g$ is partial recursive and $f(x_0, \ldots, x_{m-1})$ is the unique value for which $g$ is defined. By standard recursion theory, since $f$ is total and $g$ is partial recursive with unique output, $f$ is recursive.

For a relation $R \subseteq {}^m\omega$, the proof is similar: let $\varphi$ syntactically define $R$ in $\Gamma$ with $e = g^{+} \varphi$. Then

$$\langle x_0, \ldots, x_{m-1} \rangle \in R \quad \text{iff} \quad \exists z ((e, x_0, \ldots, x_{m-1}, z) \in T_m^{\Delta} \text{ with the last coordinate being the Gödel number of } v_0 = v_0),$$

so $R$ is r.e.
