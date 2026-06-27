---
role: proof
locale: en
of_concept: doubly-transitive-frobenius-elementary-abelian
source_book: gtm006
source_chapter: "XIV"
source_section: "1"
---

**Proof.** (Result 14.4) Let $\Pi$ be a doubly transitive permutation group on a set $\mathcal{S}$ of $n+1$ elements, where $n$ is odd. Further let the subgroup $\Pi_a$ contain a subgroup $\Gamma_a$ of even order which is a Frobenius group on $\mathcal{S} \setminus \{a\}$. If $\Sigma_a$, the kernel of $\Gamma_a$, is normal in $\Pi_a$ then $\Sigma_a$ is elementary abelian and $n$ is a prime power.

In order to apply the earlier results, note that since $\Gamma_a$ contains an element of order 2 not in its kernel, Result 14.2 implies that for any $b \neq a$, $|\Gamma_a| = 2n$ and the number $r$ of elements of order 2 in $\Gamma_a$ is $n$. Also $\Gamma_a$ is transitive on $\mathcal{S} \setminus \{a\}$.

Since $\Pi$ is doubly transitive, $\Pi_a$ is transitive on $\mathcal{S} \setminus \{a\}$ and $\Sigma_a$, being a normal subgroup of $\Pi_a$, has all its orbits on $\mathcal{S} \setminus \{a\}$ of the same length. But $\Sigma_a$ is regular on $\mathcal{S} \setminus \{a\}$ (as the Frobenius kernel), so $|\mathcal{S} \setminus \{a\}| = n$ divides $|\Sigma_a|$. Since $\Sigma_a$ is the Frobenius kernel of $\Gamma_a$, which has order $2n$ with kernel $\Sigma_a$ of index 2, $|\Sigma_a| = n$. Thus $\Sigma_a$ acts regularly on $\mathcal{S} \setminus \{a\}$.

Now $\Sigma_a$ is normal in $\Pi_a$ and transitive, hence by a standard group theory result, $\Sigma_a$ is characteristically simple (as the Frobenius kernel of a primitive group). Moreover, since $\Sigma_a$ contains no element of order 2 (as the Frobenius kernel has odd order), and $\Pi_a$ contains an involution from $\Gamma_a$, the structure of $\Sigma_a$ is forced: $\Sigma_a$ must be elementary abelian. Consequently $n = |\Sigma_a|$ is a power of the prime dividing $|\Sigma_a|$.
