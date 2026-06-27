---
role: proof
locale: en
of_concept: law-countable-family-cdf
source_book: gtm046
source_chapter: "VIII"
source_section: "30.3"
---

**Proof.** By definition, the law of the countable family $(X_1, X_2, \ldots)$ is determined by the joint distribution of this family. The joint distribution determines, and is determined by, the consistent family of finite-dimensional distributions $P S_1, P S_{12}, \ldots$, where $S_{k_1\cdots k_m}$ denotes a Borel set in the product space of $(X_{k_1}, \ldots, X_{k_m})$.

Because of the consistency requirement (Kolmogorov's extension theorem), this family is superabundant—not every choice of finite-dimensional distributions yields a valid joint law. Conditioning permits us to determine the law by a non-superabundant family: apply repeatedly the definition of conditional distributions.

Let $P(S_1)$ be the marginal distribution of $X_1$. Let $P(x_1; S_2)$ be a regular conditional distribution of $X_2$ given $X_1 = x_1$. Let $P(x_1, x_2; S_3)$ be a regular conditional distribution of $X_3$ given $X_1 = x_1, X_2 = x_2$, and so on. Then the joint distribution of $(X_1, \ldots, X_n)$ is determined iteratively by

$$P(S_{1\cdots n}) = \int_{S_1} P(dx_1) \int_{S_2} P(x_1; dx_2) \cdots \int_{S_n} P(x_1, \ldots, x_{n-1}; dx_n).$$

Thus the law of $(X_1, X_2, \ldots)$ determines and is determined by the family

$$P(S_1), \quad P(x_1; S_2), \quad P(x_1, x_2; S_3), \ldots$$

of conditional distribution functions, with no consistency relations required among them—each can be chosen arbitrarily (subject to measurability). This is the essential simplification provided by conditioning: the law is parameterized by a sequence of Markov kernels rather than a superabundant system of compatible finite-dimensional distributions.
