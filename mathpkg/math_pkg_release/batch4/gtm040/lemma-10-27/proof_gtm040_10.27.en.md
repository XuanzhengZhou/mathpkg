---
role: proof
locale: en
of_concept: lemma-10-27
source_book: gtm040
source_chapter: "10"
source_section: "27"
---

**Proof:** For each $i$, the function $K(i, x)$ is continuous. Hence the countable sum $\pi K(\cdot, x)$ is Borel measurable. Therefore the set where it equals one is a Borel set.

By Corollary 10-22,

$$\int_{S^*} K(i, x) d\mu(x) = 1.$$

Thus by Fubini's Theorem,

$$1 = \pi 1 = \pi \int_{S^*} K(\cdot, x) d\mu(x) = \int_{S^*} \pi K(\cdot, x) d\mu(x).$$

But $\int_{S^*} 1 d\mu(x) = 1$ also, and since $1 - \pi K(\cdot, x) \geq 0$, we conclude that

By Theorem 4-10 with the random time identically equal to one, we see that the column vector whose $i$th component is (see Proposition 10-21)

$$\int_B K(i, x)d\mu(x) = \Pr_i[x_v \in B]$$

is $P$-regular. By this observation and by Fubini's Theorem, we have

$$\int_B PK(\cdot, x)d\mu(x) = P \int_B K(\cdot, x)d\mu(x) = \int_B K(\cdot, x)d\mu(x).$$

Since $PK(\cdot, x) \leq K(\cdot, x)$, we must have $PK(\cdot, x) = K(\cdot, x)$ a.e. by Corollary 1-40.
