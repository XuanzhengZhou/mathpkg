---
role: proof
locale: en
of_concept: group-fixing-all-1dim-subspaces
source_book: gtm006
source_chapter: "I"
source_section: "4. Vector Spaces"
---

Fix a basis $e_1, \dots, e_n$ of $V$. Let $\gamma \in N$ be a semi-linear transformation with associated automorphism $\sigma \in \operatorname{Aut}(K)$ that fixes every 1-dimensional subspace. This means for each $v \neq 0$ there exists $\lambda(v) \in K^*$ such that $v^\gamma = \lambda(v) v$.

In particular, for the basis vectors $e_i$, there exist $a_i \in K^*$ with $e_i^\gamma = a_i e_i$. For any $v = \sum_i x_i e_i$, we have

$$v^\gamma = \left(\sum_i x_i e_i\right)^\gamma = \sum_i (x_i e_i)^\gamma = \sum_i x_i^\sigma e_i^\gamma = \sum_i x_i^\sigma a_i e_i.$$

But we also require $v^\gamma = \lambda(v) \sum_i x_i e_i = \sum_i \lambda(v) x_i e_i$. Comparing coefficients, we must have $x_i^\sigma a_i = \lambda(v) x_i$ for all $i$ and all choices of $x_i$. This forces $a_1 = a_2 = \dots = a_n = a$ (say), and $\lambda(v) x_i = x_i^\sigma a$ for all $i$. Choosing $x_i = 1$ and $x_j = 0$ for $j \neq i$, we get $\lambda(v) = a \in K^*$. Thus $\gamma$ acts as $v^\gamma = a v^\sigma$ (i.e., apply $\sigma$ to coordinates and then multiply by $a$).

The map $\gamma \mapsto a \in K^*$ defines a homomorphism from $N$ to $K^*$. Conversely, for any $a \in K^*$, the map $v \mapsto a v$ (with $\sigma = \operatorname{id}$) lies in $N$. More generally, for any $\sigma \in \operatorname{Aut}(K)$ and $a \in K^*$, the map $v = \sum x_i e_i \mapsto \sum a x_i^\sigma e_i$ lies in $N$. This yields $N \cong K^*$.

For the second claim: $\gamma \in N \cap GL(V)$ means $\gamma$ is linear (so $\sigma = \operatorname{id}$) and fixes all 1-dimensional subspaces. As above, $\gamma$ must act as $v^\gamma = a v$ for some $a \in K^*$. For this to commute with all linear transformations, $a$ must lie in the centre $Z(K^*)$. Thus $N \cap GL(V) \cong Z(K^*)$ when $\dim V > 1$.
