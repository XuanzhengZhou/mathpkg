---
role: proof
locale: en
of_concept: expectation-restriction-defined
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof that Expectation Over a Restricted Set is Defined

**Property D.** If $E\xi$ is defined, then so is the expectation $E(\xi I_A)$ for every $A \in \mathcal{F}$.

*Proof.* This follows from Property B and the observations

$$(\xi I_A)^+ = \xi^+ I_A \leq \xi^+, \quad (\xi I_A)^- = \xi^- I_A \leq \xi^-.$$

Since $E\xi$ is defined, at least one of $E\xi^+$ and $E\xi^-$ is finite. Because $(\xi I_A)^+ \leq \xi^+$ and $(\xi I_A)^- \leq \xi^-$, Property B implies that $E(\xi I_A)^+ \leq E\xi^+$ and $E(\xi I_A)^- \leq E\xi^-$. Therefore at least one of $E(\xi I_A)^+$ and $E(\xi I_A)^-$ is finite, so $E(\xi I_A)$ is well-defined. $\square$
