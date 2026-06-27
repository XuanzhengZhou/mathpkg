---
role: proof
locale: en
of_concept: theorem-19-6
source_book: gtm008
source_chapter: "19"
source_section: "19 Independence Results Using the Models"
---
Let $S \subseteq B$ be a set of mutually disjoint elements. We have to show that $\bar{S} \leq \omega$. Therefore we can assume that $0 \notin S$. Let $S_n =

since the Boolean operations in $B$ are the corresponding set theoretical operations. Let

$$S_{ij} = \{p \in X \mid (\forall n \in \omega)[p(n, i) = p(n, j)]\}.$$

We have to show that $S_{ij} \in N$, i.e., $S_{ij}$ has measure 0. For arbitrary $k \in \omega$ let

$$n_1, \ldots, n_k \in \omega \quad \text{be different natural numbers and}$$
$$p_1, \ldots, p_2^k \quad \text{be an enumeration of all functions in } 2^{(n_1, \ldots, n_k)}.$$

Define, for $1 \leq l \leq 2^k$,

$$u_l = \{p \in X \mid p(n_1, i) = p_l(n_1) \wedge \cdots \wedge p(n_k, i) = p_l(n_k)$$
$$\wedge p(n_1, j) = p_l(n_1) \wedge \cdots \wedge p(n_k, j) = p_l(n_k)\}.$$

Then $S_{ij} \subseteq u_1 \cup \cdots \cup u_2^k$ and $m(u_l) = 1/2^{2k}$, hence $m(S_{ij}) \leq 2^k \cdot 1/2^{2k} = 1/2^k$. Since $k$ was arbitrary, $m(S_{ij}) = 0$. Thus

2. $(\forall i, j \in I)[i \neq j \rightarrow [u_i = u_j] = 0]$.

Similarly, $s \subseteq \omega \rightarrow [u_i = \check{s}] = 0$.

Therefore

3. $(\forall i \in I)[\llbracket u_i \in (\mathcal{P}(\omega))^* \rrbracket = 0]$.

Since $B$ satisfies the c.c.c., $\omega_1$, in $V^{(B)}$, is $\check{u}_1$. Therefore

$$[\neg CH] = [\neg (\exists f
