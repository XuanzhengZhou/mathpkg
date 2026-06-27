---
role: proof
locale: en
of_concept: projective-covers-over-semiperfect
source_book: gtm013
source_chapter: "7"
source_section: "27. Semiperfect Rings"
---

By (27.10.c), the simple modules are exactly the $R e_i / J e_i$. Since $M$ is finitely generated, $M/J M$ is a finitely generated semisimple module, so it decomposes uniquely as

$$M/J M \cong (R e_1/J e_1)^{(k_1)} \oplus \ldots \oplus (R e_m/J e_m)^{(k_m)}.$$

Set $P = R e_1^{(k_1)} \oplus \ldots \oplus R e_m^{(k_m)}$. Then $P$ is a finitely generated projective module, and

$$P/J P \cong (R e_1/J e_1)^{(k_1)} \oplus \ldots \oplus (R e_m/J e_m)^{(k_m)} \cong M/J M.$$

By (15.13), $J P \ll P$, so the natural epimorphism $P \rightarrow P/J P \rightarrow 0$ is a projective cover. Also $J M \ll M$ by (15.13). Hence, using the isomorphism $P/J P \cong M/J M$, we can apply (27.5) to deduce the existence of a projective cover $P \rightarrow M \rightarrow 0$. Projective covers are unique up to isomorphism by (17.17).
