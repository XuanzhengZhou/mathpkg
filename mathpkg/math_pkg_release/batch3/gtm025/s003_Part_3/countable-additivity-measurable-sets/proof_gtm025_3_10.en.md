---
role: proof
locale: en
of_concept: countable-additivity-measurable-sets
source_book: gtm025
source_chapter: "3"
source_section: "10"
---

**Proof.** First prove by induction that for all $p \in \mathbb{N}$,
$$\mu(T) = \sum_{n=1}^{p} \mu(T \cap A_n) + \mu\left(T \cap \bigcap_{n=1}^{p} A_n'\right). \tag{1}$$
For $p = 1$, this is the definition of measurability of $A_1$. Assuming (1) for $p$, apply measurability of $A_{p+1}$ to $T \cap \bigcap_{n=1}^{p} A_n'$ (which is measurable by 10.8 and 10.10). Since $A_n \cap A_{p+1} = \emptyset$ for $n \leq p$, we get (1) for $p+1$.

The sequence $\mu(T \cap \bigcap_{n=1}^{p} A_n')$ is nonincreasing and bounded below by $\mu(T \cap \bigcap_{n=1}^{\infty} A_n')$. Taking limits in (1):
$$\mu(T) = \lim_{p \to \infty} \sum_{n=1}^{p} \mu(T \cap A_n) + \lim_{p \to \infty} \mu\left(T \cap \bigcap_{n=1}^{p} A_n'\right)$$
$$\geq \sum_{n=1}^{\infty} \mu(T \cap A_n) + \mu\left(T \cap \bigcap_{n=1}^{\infty} A_n'\right).$$

The reverse inequality holds by countable subadditivity. Setting $T = \bigcup A_n$ yields $\mu(\bigcup A_n) = \sum \mu(A_n)$. $\square$
