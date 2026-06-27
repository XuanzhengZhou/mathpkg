---
role: proof
locale: en
of_concept: theorem-18-4
source_book: gtm008
source_chapter: "18"
source_section: "18 Model Theoretic Consequences of the Distributive Laws

There"
---
We can assume that $\alpha$ is an infinite cardinal. Suppose

$$\{a_{ij} \mid i \in I \land j < 2\} \subseteq B$$

where $\bar{I} = \alpha$. Define $T = (I \times \{0\}) \cup (I \times \{1\})$. Then $\bar{T} = \alpha$. For $f \in 2^T$ define $f_0, f_1 \in 2^i$ by

$$f_0(i) = f(i, 0)$$
$$f_1(i) = f(i, 1) \quad \text{for } i \in I.$$

Because of Theorem 4.2 it suffices to show that

$$\prod_{i \in I} (a_{i0} + a_{i1}) \leq \sum_{f \in 2^I} \prod_{i \in I} a_{if(i)}.$$

Let $J = \{j \mid j = \langle i, n \rangle \text{ where } i \in I \land n < 2\}$. For $j = \langle i, n \rangle \in J$ define

$$b_{j0} = a_{i,n}, \quad b_{j1} = -a_{i,n},$$

and let

$$b = \prod_{i \in I} (a_{i0} + a_{i1}).$$

Then $(\forall j \in J)[b_{j0} = -b_{j1}],$ and since $b \leq (a_{i0} + a_{i1})$,

i) $b \cdot b_{\langle i, 0 \rangle n} \leq a_{i,n}$.
ii) $b \cdot b_{\langle i, 1 \rangle n} \leq a_{i,1-n}$ for $i \in I, n < 2$.

Since $\prod_{j \in J} (b_{j0} + b_{j1}) =

2. For all families $\{b_{ij} \mid i \in I \land j \in J\} \in B,$

$$(\forall f \in J^1) \left[ \prod_{i \in I} b_{if(i)} = 0 \rightarrow \prod_{i \in I} \sum_{j \in J} b_{ij} = 0 \right]$$

(i.e., in order to prove the $(I, J)$-DL we need only show that the left-hand side is 0 if the right-hand side is 0).

3. For all families $\{b_{ij} \mid i \in I \land j \in J\} \subseteq B$ and any $b \in B,$

$$(\forall f \in J^1) \left[ \prod_{i \in I} b_{if(i)} = 0 \right] \wedge (\forall i \in I) \left[ \sum_{j \in J} b_{ij} = b \right] \rightarrow b = 0.$$

Proof. We need only show that 3 implies 1. Therefore let

$$\{b_{ij} \mid i \in I \land j \in J\} \subseteq B.$$

Let

$$b = \prod_{i \in I} \sum_{j \in J} b_{ij} - \sum_{f \in 2^I} \prod_{i \in J} b_{if(i)},$$

$$a_{ij} = b \cdot b_{ij} \quad \text{for } i \in I, j \in J.$$

Because of Theorem 4.2, we have to prove that $b = 0.$

$$\sum_{j \in J} a_{ij} = b \sum_{j \in J} b_{ij} = \sum_{j \in J} b_{ij} \left( \prod_{i' \in I} \sum_{j' \in J} b_{i'j'} - \sum_{f \in JI} \prod_{i' \in I} b_{i'f(i')} \right)$$

$$= b$$

and for $f \in J^1$:

$$\prod_{
