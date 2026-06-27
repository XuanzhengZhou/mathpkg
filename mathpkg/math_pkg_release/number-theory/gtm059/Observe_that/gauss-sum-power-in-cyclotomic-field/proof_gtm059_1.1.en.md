---
role: proof
locale: en
of_concept: gauss-sum-power-in-cyclotomic-field
source_book: gtm059
source_chapter: "1"
source_section: "1"
---

We prove that the expression $S(\chi)^m$ is fixed under all automorphisms of the compositum $\mathbb{Q}(\zeta_{q-1}, \zeta_p)$ over $\mathbb{Q}(\zeta_m)$. Let $\sigma_{i,j}$ be the automorphism sending $\zeta_p \mapsto \zeta_p^i$ and $\zeta_{q-1} \mapsto \zeta_{q-1}^j$, where $i \in (\mathbb{Z}/p\mathbb{Z})^*$ and $j \in (\mathbb{Z}/(q-1)\mathbb{Z})^*$.

For the Gauss sum $S(\chi) = \sum_{x \in F_q^*} \chi(x) \zeta_p^{\operatorname{Tr}(x)}$, the automorphism $\sigma_{i,j}$ acts as follows:
$$\sigma_{i,j}(S(\chi)) = \sum_{x \in F_q^*} \chi(x)^j \zeta_p^{i \operatorname{Tr}(x)} = \chi(j)^{-1} S(\chi^i).$$

Now consider $S(\chi)^m$. Applying $\sigma_{i,j}$:
$$\sigma_{i,j}(S(\chi)^m) = \chi(j)^{-m} S(\chi^i)^m.$$

Since $\chi$ has order $m$, we have $\chi(j)^m = 1$ for any $j$, hence $\chi(j)^{-m} = 1$. Moreover, $\sigma_{i,j}$ belongs to the Galois group of $\mathbb{Q}(\zeta_{q-1}, \zeta_p)$ over $\mathbb{Q}(\zeta_m)$ precisely when $j \equiv 1 \pmod{m/\gcd(m, \dots)}$. Under these automorphisms, both $\chi(j)^{-m} = 1$ and $\chi^i = \chi$ (since raising the character to a power coprime to its order and congruent to 1 mod $m$ fixes it).

Therefore $\sigma(S(\chi)^m) = S(\chi)^m$ for all $\sigma$ in $\operatorname{Gal}(\mathbb{Q}(\zeta_{q-1}, \zeta_p)/\mathbb{Q}(\zeta_m))$, which implies $S(\chi)^m \in \mathbb{Q}(\zeta_m)$. The second statement follows by considering the full field of definition.
