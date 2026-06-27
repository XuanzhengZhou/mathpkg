---
role: proof
locale: en
of_concept: proposition-8-71
source_book: gtm040
source_chapter: "8"
source_section: "71"
---

**Proof:** State $i$ can be entered only on the $n$th step, as is clear from Definition 8-70. Hence the chain is in $i$ at most once, and $N_{0i} = H_{0i} = P_{0i}^{(n)}$. Along the path from 0 to $i$ there is a unique sequence of cells

$$U \subset U_{n-1} \subset U_{n-2} \subset \cdots \subset U_1 \subset \Omega \text{ with } U_k \in \mathcal{R}_k.$$

Then

$$P_{0i}^{(n)} = P_{0\langle U_1, 1 \rangle} P_{\langle U_1, 1 \rangle, \langle U_2, 2 \rangle} \cdots P_{\langle U_{n-1}, n-1 \rangle, \langle U, n \rangle}$$

$$= \frac{\mu(U_1)}{\mu(\Omega)} \frac{\mu(U_2)}{\mu(U_1)} \cdots \frac{\mu(U)}{\mu(U_{n-1})} = \mu(U).$$

For example, let $\Omega$ be a sequence space with some probability measure $\mu$, and let $\mathcal{R

every $n$, then the correspondence between all stochastic processes on $\{\mathcal{R}_n\}$ and all functions on the states of the space-time chain is one-one. We now restrict ourselves to the case where the $f_n$ are real-valued functions. Under the following definition the correspondence preserves inequalities, linear combinations, and limits.
