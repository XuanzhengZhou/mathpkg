---
role: proof
locale: en
of_concept: phi-group-regular-on-affine-points
source_book: gtm006
source_chapter: "2"
source_section: "8"
---

*Proof.* The composition of two such mappings is $\phi_{a,b} \phi_{a',b'} = \phi_{a+a', b+b'}$, which is again of the same form, so the set is closed under composition. The inverse is given by $\phi_{a,b}^{-1} = \phi_{-a,-b}$, so we have a subgroup of $\text{Aut}\,\mathcal{A}$.

To show transitivity, note that the point $E_3 = \langle e_3 \rangle$ is sent to $\langle a e_1 + b e_2 + e_3 \rangle$ by $\phi_{a,b}$, and thus $E_3$ can be mapped to any point of $\mathcal{A}$. The only element fixing $E_3$ is $\phi_{0,0}$, which is the identity. Hence the group action is regular (both transitive and semi-regular) on the points of $\mathcal{A}$. $\square$