---
role: proof
locale: en
of_concept: proposition-12-32
source_book: gtm040
source_chapter: "12"
source_section: "32"
---

**Proof:** Without loss of generality, assume that $V$ is normalized. It suffices to assume $T = \mathbb{N}$ and check the Markov property (the proof for $T = -\mathbb{N}$ being analogous). Fix $n > 0$, and set $A = \{1, 2, \ldots, n-1\}$. For any $\iota \in \Omega$, define

$$z_n(i_0, i_n) = \sum_{\kappa \in S^A} \exp \left\{ \sum_{B \subset

after cancellation. Hence

$$\Pr[x_0 = i_0 \wedge \dots \wedge x_n = i_n]$$

$$= \mu_A^{\bar{A}}(\iota) \Pr[x_0 = i_0 \wedge x_n = i_n]$$

$$= z_n(i_0, i_n)^{-1} \exp \left\{ \sum_{B \subset \bar{A}: B \cap A \neq \emptyset} V_B(\iota) \right\} \Pr[x_0 = i_0 \wedge x_n = i_n]$$

$$= z_n(0, i_n)^{-1} \exp \left\{ V_{\{0\}}(\iota) + \sum_{B \subset \bar{A}: B \cap A \neq \emptyset} V_B(\iota) \right\} \Pr[x_0 = 0 \wedge x_n = i_n]$$

Finally, after further cancellation, we obtain

$$\Pr[x_n = i_n \mid x_0 = i_0 \wedge \dots \wedge x_{n-1} = i_{n-1}]$$

$$= \frac{z_{n-1}(0, i_{n-1})}{z_n(0, i_n)} \left[ e^{V_{n-1}(\iota)} + V_{n-1,n}(\iota) \right] \frac{\Pr[x_0 = 0 \wedge x_n = i_n]}{\Pr[x_0 = 0 \wedge x_{n-1} = i_{n-1}]},$$

a conditional probability depending only on $n-1$, $i_{n-1}$ and $i_n$, which we may set equal to $P_{n-1,i_{n-1}i_n}$.
