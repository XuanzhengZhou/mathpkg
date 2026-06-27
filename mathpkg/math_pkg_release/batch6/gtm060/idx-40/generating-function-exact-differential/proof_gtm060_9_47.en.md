---
role: proof
locale: en
of_concept: generating-function-exact-differential
source_book: gtm060
source_chapter: "9"
source_section: "47"
---

This property follows directly from the definition of a canonical transformation (Section 45A). By definition, a transformation $g: (\mathbf{p}, \mathbf{q}) \mapsto (\mathbf{P}, \mathbf{Q})$ is canonical if and only if it preserves the canonical 1-form up to an exact differential, i.e., the integral $\oint \mathbf{p} \, d\mathbf{q}$ is invariant. Equivalently, the 1-form $\mathbf{p} \, d\mathbf{q} - \mathbf{P} \, d\mathbf{Q}$ is closed. By the Poincare lemma, on a simply connected domain, a closed 1-form is exact, hence there exists a function $S(\mathbf{p}, \mathbf{q})$ such that $\mathbf{p} \, d\mathbf{q} - \mathbf{P} \, d\mathbf{Q} = dS(\mathbf{p}, \mathbf{q})$.

Conversely, if $\mathbf{p} \, d\mathbf{q} - \mathbf{P} \, d\mathbf{Q}$ is an exact differential, then its exterior derivative vanishes, and by Stokes' theorem the integral of $\mathbf{p} \, d\mathbf{q}$ over any closed curve is preserved, which is precisely the condition for a canonical transformation. $\square$
