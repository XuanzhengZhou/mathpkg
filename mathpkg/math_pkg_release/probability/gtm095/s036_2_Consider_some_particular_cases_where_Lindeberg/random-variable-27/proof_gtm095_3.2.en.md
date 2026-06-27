---
role: proof
locale: en
of_concept: random-variable-27
source_book: gtm095
source_chapter: "3"
source_section: "2"
---

# Proof of Central Limit Theorem for Triangle Arrays (Theorem 2)

**Theorem 2.** Let for each $n \geq 1$

$$\xi_{n1}, \xi_{n2}, \ldots, \xi_{nn}$$

be independent random variables such that $E \xi_{nk} = 0$ and $\operatorname{Var} S_n = 1$, where $S_n = \xi_{n1} + \cdots + \xi_{nn}$.

Then Lindeberg's condition

$$\sum_{k=1}^{n} E[\xi_{nk}^2 I(|\xi_{nk}| \geq \varepsilon)] \to 0, \quad n \to \infty, \tag{16}$$

is sufficient for convergence $S_n \xrightarrow{d} \mathcal{N}(0, 1)$.

*Proof.* The proof proceeds by repeating word by word the proof of Theorem 1 (the Lindeberg Central Limit Theorem for sums of independent random variables normalized by their standard deviation $D_n$).

The essential observation is that Theorem 1's proof never relies on the special form $\xi_{nk} = (\xi_k - m_k)/D_n$, but only on the following facts:

1. $E \xi_{nk} = 0$ for all $n, k$,
2. $\operatorname{Var} S_n = \sum_{k=1}^{n} \operatorname{Var} \xi_{nk} = 1$,
3. Lindeberg's condition (16) holds.

In Theorem 1, these properties are satisfied by the normalized variables $\xi_{nk} = (\xi_k - m_k)/D_n$, where $D_n^2 = \sum_{k=1}^{n} \operatorname{Var} \xi_k$. The proof of Theorem 1 bounds the difference between the characteristic functions

$$\varphi_{S_n}(t) = \prod_{k=1}^{n} f_{nk}(t) \quad \text{and} \quad e^{-t^2/2}$$

using a Taylor expansion of $\log f_{nk}(t)$ and the estimate

$$|f_{nk}(t) - 1| \leq \frac{1}{2} t^2 \sigma_{nk}^2, \quad \sigma_{nk}^2 = \operatorname{Var} \xi_{nk},$$

together with the Lindeberg condition to control the tail contributions. None of these steps require anything beyond conditions (1)-(3) above.

Therefore, Theorem 2 follows as an immediate consequence of the same argument, with the only difference being that the triangular array $\{\xi_{nk}\}$ is not required to arise from a single sequence via $\xi_{nk} = (\xi_k - m_k)/D_n$. $\square$

**Remark.** This formulation is especially useful in the "triangle array" setting of the Central Limit Theorem, where the row-by-row independence structure is the fundamental assumption, without reference to an underlying single sequence.
