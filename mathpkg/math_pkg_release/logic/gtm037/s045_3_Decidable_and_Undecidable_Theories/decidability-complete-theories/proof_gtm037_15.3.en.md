---
role: proof
locale: en
of_concept: decidability-complete-theories
source_book: gtm037
source_chapter: "15"
source_section: "3. Decidable and Undecidable Theories"
---

$(i) \Rightarrow (ii)$. This is obvious, since $\Gamma$ axiomatizes $\Gamma$.

$(ii) \Rightarrow (i)$. Assume $(ii)$, say $\Delta$ axiomatizes $\Gamma$, where $g^{+*}\Delta$ is recursive. A decision procedure for $\Gamma$ can be described as follows. Assume that $\Gamma$ is consistent. (It is obvious, and trivial, that an inconsistent theory is both decidable and recursively axiomatizable.) Given any sentence $\varphi$, start listing all sentences derivable from $\Delta$ (recall from 10.29 that $g^{+*}(\Delta - \text{Thm})$ is r.e.). Since $\Gamma$ is complete, either $\varphi$ or $\neg\varphi$ will eventually appear on the list. If $\varphi$ appears, we of course give the output $\varphi \in \Gamma$. If $\neg\varphi$ appears, by the consistency of $\Gamma$ we give the output $\varphi \notin \Gamma$.

More formally, write $g^{+*}(\Delta - \text{Thm}) = \text{Rng}\, f$, where $f$ is recursive. Then

$$x \in g^{+*}\Gamma \;\text{iff}\; x \in g^{+*}\text{Sent} \;\text{and}\; f(\mu y(fy = x \;\text{or}\; fy = \neg' x)) = x.$$
