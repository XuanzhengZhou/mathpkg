---
role: proof
locale: en
of_concept: extension-of-homomorphisms-to-rings-of-fractions
source_book: gtm032
source_chapter: "Introduction"
source_section: "1"
---

Let $\alpha_1\beta_1^{-1} = \alpha_2\beta_2^{-1}$, with $\alpha_i \in \mathfrak{o}$, $\beta_i \in M$. Then $\alpha_1\beta_2 = \alpha_2\beta_1$ in $\mathfrak{o}$, and applying $s$ gives $\alpha_1^s\beta_2^s = \alpha_2^s\beta_1^s$ in $P'$. Since $\beta_i^s \neq 0$ by hypothesis, this yields $\alpha_1^s(\beta_1^s)^{-1} = \alpha_2^s(\beta_2^s)^{-1}$. Hence the mapping

$$S: \alpha\beta^{-1} \mapsto \alpha^s(\beta^s)^{-1}, \qquad \alpha \in \mathfrak{o}, \beta \in M$$

is well-defined on $\mathfrak{o}_M = \{\alpha\beta^{-1}\}$. One verifies directly that $S$ is a homomorphism: for $\alpha\beta^{-1}, \gamma\delta^{-1} \in \mathfrak{o}_M$,

$$(\alpha\beta^{-1} + \gamma\delta^{-1})^S = (\alpha\delta + \gamma\beta)(\beta\delta)^{-1} \mapsto (\alpha^s\delta^s + \gamma^s\beta^s)(\beta^s\delta^s)^{-1} = \alpha^s(\beta^s)^{-1} + \gamma^s(\delta^s)^{-1},$$
$$(\alpha\beta^{-1} \cdot \gamma\delta^{-1})^S = (\alpha\gamma)(\beta\delta)^{-1} \mapsto (\alpha^s\gamma^s)(\beta^s\delta^s)^{-1} = \alpha^s(\beta^s)^{-1} \cdot \gamma^s(\delta^s)^{-1}.$$

For $\alpha \in \mathfrak{o}$, $\alpha^S = (\alpha 1^{-1})^S = \alpha^s(1^s)^{-1} = \alpha^s$, so $S$ extends $s$.

For uniqueness, let $S'$ be any extension of $s$ to $\mathfrak{o}_M$. For $\beta \in M$, the relation $\beta\beta^{-1} = 1$ gives $\beta^{S'}(\beta^{-1})^{S'} = 1$, hence $(\beta^{-1})^{S'} = (\beta^{S'})^{-1} = (\beta^s)^{-1}$. Then for $\alpha \in \mathfrak{o}$,
$$(\alpha\beta^{-1})^{S'} = \alpha^{S'}(\beta^{-1})^{S'} = \alpha^s(\beta^s)^{-1} = (\alpha\beta^{-1})^S,$$
so $S' = S$.

If $s$ is an isomorphism, then $\alpha^s = 0$ implies $\alpha = 0$, so $\alpha^s(\beta^s)^{-1} = 0$ implies $\alpha^s = 0$ implies $\alpha = 0$, and $S$ is injective, hence an isomorphism. Conversely, if $S$ is an isomorphism, its restriction $s$ to $\mathfrak{o}$ is also injective, hence an isomorphism onto its image.
