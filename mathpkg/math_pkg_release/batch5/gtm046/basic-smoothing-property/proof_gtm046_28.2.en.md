---
role: proof
locale: en
of_concept: basic-smoothing-property
source_book: gtm046
source_chapter: "VIII"
source_section: "28.2"
---

The smoothing property follows from two previously established facts about conditional expectations:

**Fact 3.** If $X$ is $\mathcal{B}$-measurable, then $E^{\mathcal{B}}XY = XE^{\mathcal{B}}Y$ a.s. (conditional expectations commute with $\mathcal{B}$-measurable factors).

**Fact 4.** If $\mathcal{B} \subset \mathcal{B}'$, then $E^{\mathcal{B}}(E^{\mathcal{B}'}X) = E^{\mathcal{B}}X$ a.s. (iterated conditioning projects onto the coarser $\sigma$-field).

Together, Facts 3 and 4 yield the basic smoothing property. For $\mathcal{B} \subset \mathcal{B}'$ and $X'$ being $\mathcal{B}'$-measurable, we have

$$E^{\mathcal{B}}XX' = E^{\mathcal{B}}(X' E^{\mathcal{B}'}X) \text{ a.s.},$$

since $X'$ is $\mathcal{B}$-measurable (because $\mathcal{B} \subset \mathcal{B}'$) and can be pulled out of $E^{\mathcal{B}}$, while the inner expectation $E^{\mathcal{B}'}X$ is the result of smoothing $X$ by the finer $\sigma$-field $\mathcal{B}'$.
