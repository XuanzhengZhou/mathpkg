---
role: proof
locale: en
of_concept: lemma-10-32
source_book: gtm040
source_chapter: "10"
source_section: "32"
---

**Proof:** Conclusions (1) and (2) follow from the identities

$$\sum_{i \in S^h} \pi_i^h K^h(i, x) = \pi K(\cdot, x)$$

$$\sum_{j \in S^h} P^h_j K^h(j, x) = PK(\cdot, x),$$

both of which use the fact that $K(i, x) = 0$ if $i$ is not in $S^h$ (see the proof of Theorem 10-

where the sums over $S^h$ can be replaced by sums over $S$ because $i \in S - S^h$ implies $0 \leq h_i^{(1)} \leq K(i, x)/c_1 = 0$ or $h_i^{(1)} = 0$. Consequently we may assume that

$$\frac{h_i^{(1)}}{h_i} = \frac{h_i^{(2)}}{h_i}$$

for $i \in S^h$. That is, $h_i^{(1)} = h_i^{(2)}$ for $i \in S^h$. But $h_i^{(1)} = h_i^{(2)} = 0$ for $i \in S - S^h$. Hence $h^{(1)} = h^{(2)}$.

Conversely, if for $i \in S^h$

$$K^h(i, x) = c_3h_i^{(3)} + c_4h_i^{(4)},$$

then

$$K(i, x) = c_3h_i^{(3)}h_i + c_4h_i^{(4)}h_i$$

for $i \in S^h$. Extend $\{h_i^{(3)}h_i\}$ and $\{h_i^{(4)}h_i\}$ to be defined for all $i \in S$ by setting them equal to zero for $i \in S - S^h$. The convex sum of them is still $K(i, x)$, and they are both regular normalized functions, since

$$\sum_j P_{ij}h_j^{(3)}h_j = \sum_{j \in S^h} P_{ij}h_j^{(3)}h_j = h_i^{(3)}h_i$$

and

$$\sum_i \pi_i h_i^{(3)}h_i = \sum_{i \in S^h} \pi_i h_i^{(3)}h_i = \pi^h h^{(3)} = 1.$$

Consequently we may assume that $h_i^{(3)}h_i = h_i^{(4)}h_i$ for all $i \in S$. That is, $h_i^{(3)} = h_i^{(4)}$ for all $i \in S^h$.

We now begin to derive properties of the set $B_e$ of extreme points

and $h^A$ must both be regular and normalized. By Lemma 10-30, $h = h^A = h^A$. Thus, if $0 < \nu(A) < 1$,

$$\nu(A)h_i = \int_A K(i,x)d\nu(x)$$

for each fixed $i$. The same is trivially true if $\nu(A) = 0$, and it is true by hypothesis if $\nu(A) = 1$. Hence it is true of all Borel sets. Therefore for fixed $i$,

$$K(i,x) = h_i \quad \text{a.e.} [\nu].$$

Thus $K(i,x) = h_i$ for all $i$ almost everywhere $[\nu]$. Since $\nu(S^*) > 0$, there is at least one point $x_0$ where it is true. We have

$$K(i,x_0) = h_i$$

for all $i$. If there were another such point $x'$, then we would have $K(\cdot,x_0) = K(\cdot,x')$, and hence $x_0 = x'$ by Proposition 10-14. Therefore the complement of $\{x_0\}$ has measure zero, or $\nu$ is concentrated at $x_0$. Now, we know that $K(\cdot,x_0) = h$ and $h$ is normalized and minimal. Hence $x_0$ is extreme.
