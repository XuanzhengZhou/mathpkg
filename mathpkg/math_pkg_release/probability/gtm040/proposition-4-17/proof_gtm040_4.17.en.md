---
role: proof
locale: en
of_concept: proposition-4-17
source_book: gtm040
source_chapter: "4"
source_section: "17"
---

**Proof:** Suppose $n \geq 0$ is the smallest exponent for which $(P^n)_{ij} > 0$. Then $F^{(n)}_{ij} = (P^n)_{ij} > 0$, and since $H_{ij} = \sum_n F^{(n)}_{ij}$, we have $R(i,j)$. Conversely, if $R(i,j)$, then $

Definition 4-18: A state $i$ is said to be recurrent if $\bar{H}_{ii} = 1$; it is said to be transient if $\bar{H}_{ii} < 1$.

The lemma to follow contains some identities connecting $H$ and $\bar{H}$ which will be used in the next few propositions. The reader should study these examples of the use of the strong Markov property in order to develop his intuition.

Lemma 4-19: The following statements hold:

(1) The probability starting in $i$ of returning to state $i$ at least $k$ times is $(\bar{H}_{ii})^k$. (Use the convention $0^0 = 1$.)

(2) The probability starting in $i$ of returning at least $k$ times to $i$ before hitting $j$ is $(j\bar{H}_{ii})^k$, provided $i \neq j$.

(3) The probability starting in $i$ of returning to $i$ via $j$ is $i\bar{H}_{ij}H_{ji}$, provided $i \neq j$.

(4) The probability starting in $i$ of reaching $j$ for the first time after $n$ returns to $i$ is $(j\bar{H}_{ii})^n i\bar{H}_{ij}$, provided $i \neq j$.

(5) The probability starting in $i$ of being in state $j$ at least $n$ times is $H_{ij}(\bar{H}_{jj})^{n-1}$.

Proof: The proofs are all by Theorem 4-10.

(1) Use induction on $k$. For $k = 0$ the result is trivial; assume that it holds for $k - 1$. Let $p$ be the statement that the process returns to $i$ at least $k$ times, and let $t = \bar{t}_i$. Then $p'$ is the statement that the process returns to $i$ at least $k - 1$ times.

$$\Pr_i[p] = \sum_j \Pr_i[x_{i_i} = j] \Pr_j[p']$$

$$= \Pr_i[x_{i_i} = i] \Pr

(4) The argument is the same as in (3). Use the systems theorem with $t$ equal to the time of the $n$th return to $i$ if the return occurs before $j$ is reached, or $+\infty$ otherwise.

(5) The proof is by induction on $n$ and is the same as in (1) except that the random time becomes $t = \bar{t}_j$.
