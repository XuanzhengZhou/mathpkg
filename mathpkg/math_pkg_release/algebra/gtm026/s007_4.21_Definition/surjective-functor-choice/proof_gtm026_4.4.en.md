---
role: proof
locale: en
of_concept: surjective-functor-under-axiom-of-choice
source_book: gtm026
source_chapter: "4"
source_section: "4"
---

**Proof of (4.29).** Let $f: X \longrightarrow Y$ be surjective. By the axiom of choice, there exists a choice function $d: Y \longrightarrow X$ such that $d \cdot f = \mathrm{id}_Y$. Applying the functor $H$ to this equation yields:

$$dH \cdot fH = (d \cdot f)H = (\mathrm{id}_Y)H = \mathrm{id}_{YH}$$

Since $fH$ has a right inverse (namely $dH$), it follows that $fH$ is surjective. $\square$
