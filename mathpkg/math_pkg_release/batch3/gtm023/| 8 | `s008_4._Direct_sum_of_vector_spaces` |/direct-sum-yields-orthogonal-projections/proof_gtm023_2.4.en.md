---
role: proof
locale: en
of_concept: direct-sum-yields-orthogonal-projections
source_book: gtm023
source_chapter: "2"
source_section: "4"
---

Define $\varrho_v = i_v \circ \pi_v$. Since $\pi_v \circ i_v = \iota_{E_v}$ (by the definition of canonical projections and injections), we have

$$
\varrho_v^2 = i_v \circ \pi_v \circ i_v \circ \pi_v = i_v \circ \iota_{E_v} \circ \pi_v = i_v \circ \pi_v = \varrho_v,
$$

so each $\varrho_v$ is a projection operator.

For $v \neq \mu$, the canonical projections satisfy $\pi_v \circ i_\mu = 0$ (since $i_\mu$ maps into $E_\mu$ and $\pi_v$ projects onto $E_v$, which are complementary summands). Hence

$$
\varrho_v \circ \varrho_\mu = i_v \circ \pi_v \circ i_\mu \circ \pi_\mu = i_v \circ 0 \circ \pi_\mu = 0.
$$

For the sum, by the definition of the canonical mappings for a direct sum decomposition, we have

$$
\sum_v \varrho_v = \sum_v i_v \circ \pi_v = \iota_E,
$$

as follows from the properties of canonical injections and projections (equations (2.25) and (2.26)). Moreover, $\operatorname{Im} \varrho_v = \operatorname{Im}(i_v \circ \pi_v) = \operatorname{Im} i_v = E_v$ since $\pi_v$ is surjective onto $E_v$ and $i_v$ is injective. Thus the decomposition of $E$ determined by the family $\{\varrho_v\}$ agrees with the original direct sum decomposition.
