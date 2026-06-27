---
role: proof
locale: en
of_concept: bius-function-lattice-d18
source_book: gtm054
source_chapter: "10"
source_section: "Section 52"
---

Let $\mathcal{R} = \{R_1, \ldots, R_k\} \in \mathbb{P}(X)$, and suppose $\mathcal{Q} \leq \mathcal{R}$. For each $i = 1, \ldots, k$, let $\mathcal{Q}_i = \mathcal{Q}(R_i)$. One easily sees that the segment $\mathbb{P}(X)_{[\mathcal{Q}, \mathcal{R}]}$ of $(\mathbb{P}(X), \leq)$ is isomorphic to the direct product

$$\mathbb{P}(R_1)_{[\mathcal{Q}_1, \{R_1\}]} \times \ldots \times \mathbb{P}(R_k)_{[\mathcal{Q}_k, \{R_k\}]}$$

of segments, which is in turn a segment of $(\mathbb{P}(R_1), \leq) \times \ldots \times (\mathbb{P}(R_k), \leq)$. Since each segment $\mathbb{P}(R_i)_{[\mathcal{Q}_i, \{R_i\}]}$ is isomorphic to the segment $\mathbb{P}(\mathcal{Q}_i)_{[\mathcal{P}_1(\mathcal{Q}_i

the second summation in D21 is 0. That summation clearly reduces to $|S| - 1$ if $|S + Q| = 1$. Hence the left-hand member of D21 reduces to

$$(-1)^{|S| - 1}(|S| - 1)! + (-1)^{|S| - 2}(|S| - 2)!(|S| - 1),$$

where the first term comes from the case $Q = S$. But this expression is identically 0.

Armed with the above proposition, we proceed to compute $\text{perm}(A)$, where $A = [a_{ij}]$ is an $n \times m$ matrix over $\mathbb{C}$. Let $N = \{1, \ldots, n\}$. For each $\mathcal{Q} \in \mathbb{P}(N)$, let

$$H(\mathcal{Q}) = \{h \in N^N : h(i) = h(j) \text{ if and only if } i, j \in Q \text{ for some } Q \in \mathcal{Q}\}.$$

and define

$$t(\mathcal{Q}) = \sum_{h \in H(\mathcal{Q})} \prod_{i=1}^{n} a_{i,h(i)}.$$

We observe that $H(\mathcal{P}_1(N)) = \Pi(N)$, and so $t(\mathcal{P}_1(N)) = \text{perm}(A)$ as defined in §VF.

Let $s: \mathbb{P}(N) \to \mathbb{C}$ be given by
