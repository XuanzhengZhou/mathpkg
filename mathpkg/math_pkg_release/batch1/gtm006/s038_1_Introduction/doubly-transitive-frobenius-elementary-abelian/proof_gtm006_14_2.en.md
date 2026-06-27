---
role: proof
locale: en
of_concept: doubly-transitive-frobenius-elementary-abelian
source_book: gtm006
source_chapter: "XIV"
source_section: "2"
---
**Proof of Result 14.4.** This result combines Results 14.1, 14.2, and 14.3.

By Result 14.1, $\Pi_a$ is primitive on $\mathcal{S} \setminus \{a\}$. Since $\Gamma_a$ is a Frobenius group of even order on $\mathcal{S} \setminus \{a\}$ and its kernel $\Sigma_a$ is normal in $\Pi_a$, the primitivity of $\Pi_a$ forces certain constraints.

Since $\Gamma_a$ contains an element of order $2$ not in its kernel $\Sigma_a$, the Frobenius kernel $\Sigma_a$ is abelian (and therefore soluble; see Burnside [1]). 

By Result 14.2, the structure of the Frobenius group $\Gamma_a$ (order $2n$ on $n$ points, $n$ odd) provides a one-to-one correspondence between involutions and points of $\mathcal{S}\setminus\{a\}$. The normality of $\Sigma_a$ in $\Pi_a$ together with the primitivity of $\Pi_a$ forces $\Sigma_a$ to be an elementary abelian $p$-group for some prime $p$.

Finally, since $|\mathcal{S} \setminus \{a\}| = n$ and $\Sigma_a$ acts regularly on this set, we have $|\Sigma_a| = n$, which implies $n = p^r$ for some $r \geq 1$. $\square$
