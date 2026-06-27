---
role: proof
locale: en
of_concept: conjugate-natural-transformations-characterization
source_book: gtm005
source_chapter: "IV"
source_section: "7. Transformations of Adjoints"
---

First, the hom-set condition (5) implies each of the unit/counit diagrams (6) and (7). To see that (5) implies (6), put $x = G'a$ in (5), start with the identity arrow $1 : G'a 	o G'a$ in the upper right corner of the hom-set diagram, and use the description of $arphi$ and $arphi'$ by unit and counit to chase this element around:

$$arepsilon'_a \leftarrow 1 = 1_{G'a}$$

Through the upper isomorphism $arphi'^{-1}$, the identity corresponds to the counit $arepsilon'_a : F'G'a 	o a$. Applying $(\sigma_{G'a})^*$ precomposes with $\sigma_{G'a}$ to give an arrow $FG'a 	o a$. The lower isomorphism $arphi$ sends this to an arrow $G'a 	o Ga$. The commutativity of the diagram forces this to equal $	au_a$, giving the relation $arepsilon'_a \circ \sigma_{G'a} = arepsilon_a \circ F	au_a$, which is one of the four equivalent diagrams. The remaining implications among the four diagrams are similar.

Next, suppose $\sigma$ is given but $	au$ is not. The Yoneda Lemma applied to the composite transformation $arphi \circ (\sigma_x)^* \circ arphi'^{-1}$ (three legs of the hom-set diagram (5)) shows that there is a unique family of arrows $	au'_a$ for which (5) commutes, and this family is a natural transformation. Since each counit $arepsilon_a : FGa 	o a$ is universal from $F$ to $a$, there is also a unique family of arrows $	au''_a : G'a 	o Ga$ for which the first counit diagram commutes. Since (5) implies that counit diagram, $	au'_a = 	au''_a$. Conversely, if $	au = 	au''$ makes the counit diagram commute, it also makes (5) commute. Therefore the counit diagram implies (5).

Given $\sigma$, there is immediately a unique natural transformation $	au$ for which the first unit diagram commutes; since (5) implies that diagram, the solutions $	au'_a$ of (5) are necessarily natural; moreover the unit diagram implies (5). The dual argument with $	au$ given and $\sigma$ constructed follows by duality.
