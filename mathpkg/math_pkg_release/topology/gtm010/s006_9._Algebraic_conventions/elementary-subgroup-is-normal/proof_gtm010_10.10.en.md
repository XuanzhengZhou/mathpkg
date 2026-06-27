---
role: proof
locale: en
of_concept: elementary-subgroup-is-normal
source_book: gtm010
source_chapter: "10"
source_section: "10"
---

For any $X \in GL(R)$ and generator $E$ of $E(R)$, $XEX^{-1}$ can be written as a product of elementary matrices. Specifically, if $X = \prod E_i$, then $XEX^{-1} = E_1 E_2 \cdots E_k E E_k^{-1} \cdots E_1^{-1}$, each conjugate of an elementary matrix being elementary. For a commutator $ABA^{-1}B^{-1}$, using (10.1), $(AB)(A^{-1}B^{-1}) = [E_1(BA)E_2](BA)^{-1} = E_1[(BA)E_2(BA)^{-1}] \in E(R)$. Hence the commutator subgroup is contained in $E(R)$. Conversely, each generator $(I_n + aE_{i,k}^n)$ of $E(R)$ is a commutator because $(I_n + aE_{i,k}^n) = (I_n + aE_{i,j}^n)(I_n + E_{j,k}^n)(I_n - aE_{i,j}^n)(I_n - E_{j,k}^n)$. Thus $E(R) = [GL(R), GL(R)]$, establishing normality and that the quotient is abelian.
