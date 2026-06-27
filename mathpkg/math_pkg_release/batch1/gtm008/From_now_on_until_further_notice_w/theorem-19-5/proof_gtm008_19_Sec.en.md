---
role: proof
locale: en
of_concept: theorem-19-5
source_book: gtm008
source_chapter: "19"
source_section: "19 Independence Results Using the Models"
---
Let $B$ be as in Theorem 19.4. Then $\bar{B} \leq 2^{N_

Suppose $[u = \check{s}] \neq 0$ and let $\langle p_1, p_2 \rangle \in \prod_{n \in \omega} (u(\check{n}) \iff \check{s}(\check{n}))$. Then

$$[\langle p_1, p_2 \rangle] \subseteq \left( \bigcap_{n \in \omega} (u(\check{n}) \iff \check{s}(\check{n})) \right)$$

and hence

$(\forall q_1 q_2) \left[ \langle q_1, q_2 \rangle \in P \land \langle q_1, q_2 \rangle \leq \langle p_1, p_2 \rangle \rightarrow [\langle q_1, q_2 \rangle] \cap \bigcap_{n \in \omega} (u(\check{n}) \iff \check{s}(\check{n})) \neq 0$$

Choose some $n \in \omega$ such that $n \notin p_1 \cup p_2$ and define $q = \langle q_1, q_2 \rangle$ by

$$q_1 = p_1 \quad \text{if } \check{s}(\check{n}) = 1$$
$$q_2 = p_2 \cup \{n\} \quad \text{if } \check{s}(\check{n}) = 0$$

Since

$(u(\check{n}) \iff s(\check{n})) = u(\check{n}) \quad \text{if } \check{s}(\check{n}) = 1$
$$= -u(\check{n}) \quad \text{if } \check{s}(\check{n}) = 0$$

and $-u(\check{n}) = [\langle 0, \{n\} \rangle]^{-0}$, (by the exercise following Corollary 11.4) we have $\langle q_1, q_2 \rangle \leq \langle p_1, p_2 \rangle$ and $[\langle q_1, q_

Therefore $[v \in (\mathcal{P}(\omega))^\vee] = 1$.

Since $v \in \mathcal{D}(S)$ this implies that

$$1 = [v \in S] = \sum_{x \in \mathcal{D}(S)} [x = v] \leq \sum_{x \in \mathcal{L}(S)} [x \in (\mathcal{P}(\omega))^\vee] = 0.$$

This is a contradiction which proves ii).

Remark. Next we give a new proof of the independence of the Continuum Hypothesis, however this time we use a measure algebra $B$. Let $I$ be an index set of cardinality $> 2^{N_0}$, let $X = 2^{\omega \times I}$ be a generalized Cantor space, $B$ the $\sigma$-algebra of all Borel sets of $X$, $N$ the $\sigma$-ideal in $B$ consisting of all the null sets for the usual product measure, and finally let $B = \mathcal{B}/N$. Basic open sets of $X$ are of the form

$$U(p_0) = \{p \mid p \in 2^{\omega \times I} \land p(j_1) = p_0(j_1) \land \cdots \land p(j_n) = p_0(j_n)\}$$

where $p_0: \{j_1, \ldots, j_n\} \to 2$ and $j_1, \ldots, j_n \in \omega \times I$. Without proof we shall use the fact that there is a (unique) measure $m$ for subsets of $X$ such that

$$m(U(p_0)) = (\frac{1}{2})^n \quad \text{and} \quad m(X) = 1.$$

With this notation we are prepared to prove the following.
