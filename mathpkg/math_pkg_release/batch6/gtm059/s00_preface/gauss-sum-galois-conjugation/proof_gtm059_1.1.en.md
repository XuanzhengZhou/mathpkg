---
role: proof
locale: en
of_concept: gauss-sum-galois-conjugation
source_book: gtm059
source_chapter: "1"
source_section: "1"
---

**Proof.** By definition,

$$S(\chi^p) = \sum_{x \in F^*} \chi^p(x) \lambda(x) = \sum_{x \in F^*} \chi(x^p) \lambda(x).$$

Since $x \mapsto x^p$ is an automorphism of the finite field $F$ (the Frobenius automorphism), as $x$ runs over $F^*$, $x^p$ also runs over $F^*$, each element exactly once. Moreover, for the additive character $\lambda$ constructed from the trace, we have $\lambda(x) = \lambda(x^p)$ because $\operatorname{Tr}(x^p) = \operatorname{Tr}(x)$ (the trace to the prime field is invariant under Frobenius). Therefore, making the change of variables $y = x^p$,

$$S(\chi^p) = \sum_{y \in F^*} \chi(y) \lambda(y) = S(\chi).$$

This establishes the invariance of Gauss sums under the $p$-th power Frobenius automorphism. More generally, for an integer $c$ prime to the order of $\chi$, the automorphism $\sigma_c$ of the cyclotomic field $Q(\chi)$ sends $\chi(x)$ to $\chi(x)^c$, and the corresponding action on Gauss sums satisfies $\sigma_c(S(\chi)) = \chi(c)^{-1} S(\chi^c)$ (which reduces to equality when $c$ is a power of $p$ modulo the order of $\chi$).
