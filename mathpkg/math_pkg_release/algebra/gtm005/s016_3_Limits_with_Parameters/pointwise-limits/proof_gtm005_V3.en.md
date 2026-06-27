---
role: proof
locale: en
of_concept: pointwise-limits
source_book: gtm005
source_chapter: "V"
source_section: "3. Limits with Parameters"
---

Given the bifunctor $T : J \times P \rightarrow X$, replace it by its adjunct $S : J \rightarrow X^P$ under the adjunction $\operatorname{Cat}(J \times P, X) \cong \operatorname{Cat}(J, X^P)$. For each object $p \in P$, the evaluation functor $E_p : X^P \rightarrow X$ satisfies $E_p S = T(-, p)$. By hypothesis, each $T(-, p)$ has a limit $L_p$ in $X$, with limiting cone $\lambda_p : L_p \rightarrow T(-, p)$.

These limits $L_p$ for all $p \in P$ define an object function of a functor $L : P \rightarrow X$: for each arrow $f : p \rightarrow p'$ in $P$, the universal property of the limit $L_{p'}$ applied to the cone $\lambda_{p} \circ T(-, f)^{-1}$ yields a unique arrow $L_f : L_p \rightarrow L_{p'}$, giving a functor $L = \operatorname{Lim}_j T(j, -) : P \rightarrow X$.

Equivalently, the functor $L$ corresponds under the adjunction to a functor $\widehat{L} : J \rightarrow X^P$ given by $\widehat{L}(j)(p) = T(j, p)$, with a limiting cone $\widehat{\lambda} : \widehat{L} \rightarrow \Delta(\text{something})$. The limit of $S$ in $X^P$ exists and its $p$-component is precisely $L_p$. For any other cone $\mu : M \rightarrow S$ in $X^P$, its components $\mu_p : M_p \rightarrow E_p S$ determine unique arrows $M_p \rightarrow L_p$, which combine into a natural transformation $M \rightarrow L$, proving $L$ is the limit in $X^P$. Hence $E_p(\operatorname{Lim} S) = \operatorname{Lim}(E_p S)$.
