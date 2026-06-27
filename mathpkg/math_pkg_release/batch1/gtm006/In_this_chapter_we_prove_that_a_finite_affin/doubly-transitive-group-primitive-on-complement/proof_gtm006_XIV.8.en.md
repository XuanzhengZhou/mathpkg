---
role: proof
locale: en
of_concept: doubly-transitive-group-primitive-on-complement
source_book: gtm006
source_chapter: "XIV"
source_section: "8"
---

Since $\Pi$ is transitive on $\mathcal{S}$, it follows at once by taking conjugates of $\Pi_a$ that for every $s \in \mathcal{S}$ there is a subgroup $\Gamma_s$ which fixes $s$ and is a Frobenius group of even order on $\mathcal{S} \setminus \{s\}$.

Suppose $\Pi_a$ is not primitive on $\mathcal{S} \setminus \{a\}$. Then there is a non-trivial partition of $\mathcal{S} \setminus \{a\}$ into blocks of imprimitivity. Let $\mathcal{B}$ be a block of this partition containing $b$. Since $\Gamma_a$ is a Frobenius group on $\mathcal{S} \setminus \{a\}$, the stabilizer of $b$ in $\Gamma_a$ is non-trivial. By properties of Frobenius groups, this stabilizer fixes only $b$ among the points of $\mathcal{S} \setminus \{a\}$.

However, since $\mathcal{B}$ is a block of imprimitivity, the stabilizer of $b$ must also fix the block $\mathcal{B}$ setwise. Because the Frobenius group $\Gamma_a$ acts regularly on the non-identity orbits, this leads to a contradiction with the structure of Frobenius groups, forcing $\Pi_a$ to be primitive on $\mathcal{S} \setminus \{a\}$.
