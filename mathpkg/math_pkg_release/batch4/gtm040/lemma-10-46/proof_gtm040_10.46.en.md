---
role: proof
locale: en
of_concept: lemma-10-46
source_book: gtm040
source_chapter: "10"
source_section: "46"
---

**Proof:** If $h$ is minimal, then the regularity of $h$ implies that 1 is regular for $P^h$ restricted to $S^h$. By adding a suitable multiple of 1 to a given bounded regular function for $P^h$, we may assume that it is a non-negative bounded regular function for $P^h$. Thus let $\bar{h}$ with $0 \leq \bar{h} \leq c1$ be a regular function for $P^h$ restricted to $S^h$. Set

$$k_i = \begin{cases} \bar{h}_i h_i & \text{if } i \in S^h \\ 0 & \text{otherwise.} \end{cases}$$

Then $k$ is $P$-

PROOF: The $h$-process for $h = K(\cdot, x)$ disappears with probability zero, and thus

$$\Pr^{K(\cdot, x)}[x_n \in S] = 1.$$

Therefore

$$\Pr^{K(\cdot, x)}[x_n \in A \text{ from some time on}]$$

$$= \Pr^{K(\cdot, x)}[x_n \in S - A \text{ only finitely often}]$$

$$= 1 - \Pr^{K(\cdot, x)}[x_n \in S - A \text{ infinitely often}].$$

By Lemma 10-46, the only bounded regular functions for this process are the constants, and thus, by Proposition 5-19, this last expression must equal zero or one.

Proposition 10-47 shows that fine neighborhoods of $x$ in $B_e$ are those sets $A$ in $S^*$ for which $x$ is in $A$ and

$$\Pr^{K(\cdot, x)}[x_n \in A \text{ from some time on}] > 0.$$

The complement of a fine neighborhood of $x$ is called thin at $x$. Such sets $A$ are characterized by the property

$$\Pr^{K(\cdot, x)}[x_n \in A \text{ infinitely often}] = 0.$$

By Proposition 10-47 this probability must again be zero or one.

Let $h \geq 0$ be a $\pi$-integrable regular function with fine boundary function $f$. The fine topology for $S^*$ has the property that the function $h \cup f$ obtained by extending $h$ to $S^*$ by $f$ is continuous at almost every $[\mu]$ point $x$ in $S^*$. In fact, the statement is trivial for $x$ not in $B_e$, and it therefore suffices by Corollary 10-44 to prove the result for every $x$ in $B_e$ for which

$$\Pr^{K(\cdot, x)}[\lim h(x_n) = f(x)] = 1.$$
