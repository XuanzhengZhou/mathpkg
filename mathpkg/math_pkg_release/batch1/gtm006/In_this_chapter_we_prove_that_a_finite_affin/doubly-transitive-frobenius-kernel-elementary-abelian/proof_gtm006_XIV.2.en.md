---
role: proof
locale: en
of_concept: doubly-transitive-frobenius-kernel-elementary-abelian
source_book: gtm006
source_chapter: "XIV"
source_section: "2"
---

By Result 14.1, since $\Pi$ is doubly transitive on $\mathcal{S}$ and each $\Pi_a$ contains a Frobenius subgroup $\Gamma_a$ of even order on $\mathcal{S} \setminus \{a\}$, the stabilizer $\Pi_a$ is primitive on $\mathcal{S} \setminus \{a\}$.

By Result 14.3, since $\Sigma_a$ is a non-trivial normal subgroup of $\Pi_a$ (it is the kernel of the Frobenius group $\Gamma_a$ and is assumed normal in $\Pi_a$), $\Sigma_a$ is transitive on $\mathcal{S} \setminus \{a\}$.

Since $\Gamma_a$ is a Frobenius group, its kernel $\Sigma_a$ is nilpotent (this is a standard theorem of Frobenius groups). Moreover, $\Gamma_a$ contains an element of order $2$ not in $\Sigma_a$, so $\Sigma_a$ is abelian. 

By Result 14.2(ii), the subgroup $\Sigma_a$ has order related to its involutions. Since $\Sigma_a$ is a transitive abelian permutation group on $\mathcal{S} \setminus \{a\}$, which has $n$ points, $\Sigma_a$ must be regular on this set. A regular abelian permutation group is elementary abelian, so $\Sigma_a$ is elementary abelian. Consequently, $|\Sigma_a| = n$ and $n$ is a prime power (the order of any elementary abelian group is a prime power).
