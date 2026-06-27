---
role: proof
locale: en
of_concept: faithful-module-characterization
source_book: gtm013
source_chapter: "1"
source_section: "8"
---

Using Proposition 4.5, we have

$$\mathrm{Rej}_R M = \bigcap \{ \mathrm{Ker}\, f \mid f \in \mathrm{Hom}(R, M) \}$$

$$= \bigcap \{ \mathrm{Ker}\, \rho(x) \mid x \in M \}$$

$$= \bigcap_{x \in M} l_R(x) = l_R(M).$$

Now $M$ is faithful iff $l_R(M) = 0$ iff $\mathrm{Rej}_R M = 0$. By definition, this means $M$ cogenerates $R$: every non-zero element of $R$ is separated from zero by some homomorphism into $M$.
