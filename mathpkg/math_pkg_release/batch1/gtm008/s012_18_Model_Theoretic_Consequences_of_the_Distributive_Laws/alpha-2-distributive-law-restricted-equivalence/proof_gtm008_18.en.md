---
role: proof
locale: en
of_concept: alpha-2-distributive-law-restricted-equivalence
source_book: gtm008
source_chapter: "18"
source_section: "18. Model Theoretic Consequences of the Distributive Laws"
---

We can assume that $\alpha$ is an infinite cardinal. Suppose

$$\{a_{ij} \mid i \in I \land j < 2\} \subseteq B$$

where $\bar{I} = \alpha$. Define $T = (I \times \{0\}) \cup (I \times \{1\})$. Then $\bar{T} = \alpha$. For $f \in 2^T$ define $f_0, f_1 \in 2^I$ by

$$f_0(i) = f(i, 0), \quad f_1(i) = f(i, 1) \quad \text{for } i \in I.$$

Because of Theorem 4.2 it suffices to show that

$$\prod_{i \in I} (a_{i0} + a_{i1}) \leq \sum_{f \in 2^I} \prod_{i \in I} a_{i f(i)}.$$

Let $J = \{j \mid j = \langle i, n \rangle \text{ where } i \in I \land n < 2\}$. For $j = \langle i, n \rangle \in J$ define

$$b_{j0} = a_{i,n}, \quad b_{j1} = -a_{i,n},$$

and let

$$b = \prod_{i \in I} (a_{i0} + a_{i1}).$$

Then $(\forall j \in J)[b_{j0} = -b_{j1}]$, and since $b \leq (a_{i0} + a_{i1})$,

$$\begin{aligned}
\text{(i)} &\quad b \cdot b_{\langle i, 0 \rangle, n} \leq a_{i,n},\\
\text{(ii)} &\quad b \cdot b_{\langle i, 1 \rangle, n} \leq a_{i,1-n} \quad \text{for } i \in I,\; n < 2.
\end{aligned}$$

Since $\prod_{j \in J} (b_{j0} + b_{j1}) = 1$, the restricted $(\alpha, 2)$-DL yields

$$b = b \cdot 1 = b \cdot \sum_{f \in 2^J} \prod_{j \in J} b_{j, f(j)}.$$

Using the inequalities (i) and (ii) together with the definition of $b$, one obtains $b = 0$, which by Theorem 4.2 implies the unrestricted $(\alpha, 2)$-DL holds.
