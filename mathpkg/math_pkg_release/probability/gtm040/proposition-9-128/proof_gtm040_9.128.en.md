---
role: proof
locale: en
of_concept: proposition-9-128
source_book: gtm040
source_chapter: "9"
source_section: "128"
---

**Proof:** If $P$ represents a circuit, then it has a regular measure $\alpha$ and is $\alpha$-reversible by Proposition 9-127. Its states communicate since the circuit is connected.

Conversely, suppose that $P$ is a transition matrix with the stated properties. Introduce the electric circuit with the states of $P$ as terminals and with $c_{ij} = \alpha_i P_{ij}$. The circuit is well defined since

$$c_{ii} = \alpha_i P_{ii} = 0$$

and since

$$c_{ij} = \alpha_i P_{ij} = \alpha_j P_{ji} = c_{ji}.$$

Since the states communicate, the circuit is connected. To see that $P$ represents the circuit, we note that

$$\alpha_i = \sum_k \alpha_i P_{ik} = \sum_k c_{ik}.$$

Thus

$$P_{ij} = \frac{c_{ij}}{\alpha_i} = \frac{c_{ij}}{\sum

PROOF:

$$0 \bar{H}_{0\bar{F}} = \sum_{k} P_{0k} 0 H_{k\bar{F}}$$
$$= \sum_{k} P_{0k} (1 - \bar{F} H_{k0}) \quad \text{since } \bar{F} P \text{ is absorbing}$$
$$= \sum_{k} P_{0k} (1 - B_{k0}^{(0)} \cup \bar{F})$$
$$= \sum_{k} P_{0k} (v_0 - v_k)$$
$$= \frac{1}{\alpha_0} \sum_{k} c_{0k} (v_0 - v_k)$$
$$= \frac{\mu_0}{\alpha_0}.$$

Lemma 9-130: In any Markov chain a state 0 is recurrent if and only if $0 \bar{H}_{0\bar{F}} \rightarrow 0$ for some (or every) increasing sequence of finite sets $F$ with union the set of all states.

PROOF: If 0 is transient, then there is a positive probability $1 - \bar{H}_{00}$ that the chain never returns to 0. Hence

$$0 \bar{H}_{0\bar{F}} \geq 1 - \bar{H}_{00} > 0$$

for every finite set $F$, and $0 \bar{H}_{0\bar{F}}$ cannot approach 0.

Conversely, let 0 be recurrent. Choose $N$ sufficiently large that $\bar{H}_{00}^{(N)} > 1 - \epsilon$. Choose $\delta$ close enough to 1 so that

$$1 - \epsilon < \delta^N < 1.$$

Then construct an increasing sequence of finite sets $A_0, A_1, \ldots, A_N$ such that $A_0 = \{0\}$ and such that the probability of stepping from any state of $A_k$ to a state of $A_{k+1}$ is greater than $\delta$. Let $F$ be any finite set containing $A_N$. The probability that the process started at 0 is, for every $n \

so that

$$0 \bar{H}_{0F} < 2\epsilon$$

for all $F$ containing $A_N$.
