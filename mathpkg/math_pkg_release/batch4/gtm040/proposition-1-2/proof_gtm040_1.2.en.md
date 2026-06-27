---
role: proof
locale: en
of_concept: proposition-1-2
source_book: gtm040
source_chapter: "1"
source_section: "2"
---

**Proof:** We prove only the first assertion. We may assume that $A$ is a row vector $\pi$ and that $B$ and $C$ are column vectors $f$ and $g$. Then

$$\pi f + \pi g = \sum_{m \in M} \pi_m f_m + \sum_{m \in M} \pi_m g_m$$

$$= \sum_{m \in M} (\pi_m f_m + \pi_m g_m)$$

$$= \sum_{m \in M} \pi_m (f_m + g_m)$$

$$= \pi(f + g).$$

The fourth and fifth properties are related and nontrivial. Associativity does not always hold, but useful sufficient criteria for its validity are known. For an example of how associativity may fail, let $A$ be a matrix whose index sets are the non-negative integers and whose entries are given by

$$A = \begin{pmatrix}
1 & -1 & 0 & 0 & 0 & \ldots \\
0 & 1 & -1 & 0 & 0 & \ldots \\
0 & 0 & 1 & -1 & 0 & \ldots \\
0 & 0 & 0 & 1 & -1 & \ldots \\
0 & 0 & 0 & 0 & 1 & \ldots \\
\vdots
\end{pmatrix}$$

Then

$$1^T(A1) = 0,$$

whereas

$$(1^T A)1 = 1.$$

All the products involved are well defined, but the multiplications do not associate.

We shall not consider the problem of existence of inverses, but uniqueness rests upon associativity. For suppose $AB = BA = AC = CA = I$. Since $AC = I,$ we have $B

Lemma 1-3: Let $b_{ij}$ be a sequence of real numbers nondecreasing with $i$ and with $j$. Then $\lim_i \lim_j b_{ij} = \lim_j \lim_i b_{ij}$, both possibly infinite.

Proof: In the extended sense $\lim_i b_{ij} = L_j$ exists and so does $\lim_j b_{ij} = L_i^*$. Now $\{L_j\}$ is nondecreasing, for if $L_j > L_{j+k}$, then for $i$ sufficiently large $b_{ij} > L_{j+k} \geq b_{i,j+k}$, which is impossible. Similarly $\{L_i^*\}$ is nondecreasing, so that $\lim_j L_j = L$ and $\lim_i L_i^* = L^*$ exist in the extended sense. If $L \neq L^*$, we may assume $L^* > L$ and hence $L$ is finite. Then there exists an $i$ such that $L_i^* > L$. Hence

$$L_i^* > L$$
$$\geq L_j \quad \text{for all } j$$
$$\geq b_{ij} \quad \text{for all } j.$$

Thus $b_{ij}$ is bounded away from its limit on $j$, a contradiction.

Following the example of Lemma 1-3, we agree that all limits referred to in the future are on the extended real line.

Proposition 1-4: Non-negative matrices associate under multiplication.

Proof: Since we are interested in each entry separately of a triple product, we may assume that we are to show that $\pi(Af) = (\pi A)f$, where $\pi \geq 0, A \geq 0, f \geq 0, \pi$ is a row vector, $f$ is a column vector, and the index sets are subsets of the non-negative integers. Then

$$\pi(Af) = \sum_m \sum_n \pi_m A_{mn} f_n$$

and

$$(\pi A)f = \sum_n \sum_m \pi_m A_{mn} f_n.$$

Set $b_{ij} = \sum_{m=

absolute value of a matrix $A$ is $|A| = A^+ + A^-$. Proposition 1-4 now gives us five corollaries.
