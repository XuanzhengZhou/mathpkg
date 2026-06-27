---
role: proof
locale: en
of_concept: theorem-zeta-factorization
source_book: gtm052
source_chapter: "Appendix C"
source_section: "4"
---

The Lefschetz trace formula in $l$-adic cohomology states that for the $r$-th power of the Frobenius morphism $f$,

$$N_r = \sum_{i=0}^{2n} (-1)^i \operatorname{Tr}(f^{*r}; H^i(\bar{X}, \mathbf{Q}_l)).$$

Substituting this into the definition of the zeta function:

$$Z(X,t) = \exp\left(\sum_{r=1}^{\infty} N_r \frac{t^r}{r}\right) = \exp\left(\sum_{r=1}^{\infty} \sum_{i=0}^{2n} (-1)^i \operatorname{Tr}(f^{*r}; H^i) \frac{t^r}{r}\right)$$

$$= \prod_{i=0}^{2n} \left[ \exp\left( \sum_{r=1}^{\infty} \operatorname{Tr}(f^{*r}; H^i) \frac{t^r}{r} \right) \right]^{(-1)^i}$$

Applying Lemma 4.1 to each factor yields $Z(X,t) = \prod_{i=0}^{2n} \det(1 - f^* t; H^i)^{(-1)^{i+1}}$, which gives the stated factorization with $P_i(t) = \det(1 - f^* t; H^i(\bar{X}, \mathbf{Q}_l))$. The Frobenius $f$ is a finite morphism of degree $q^n$, so $f^*$ acts as multiplication by $q^n$ on $H^{2n}$, giving $P_{2n}(t) = 1 - q^n t$, and as the identity on $H^0$, giving $P_0(t) = 1-t$.
