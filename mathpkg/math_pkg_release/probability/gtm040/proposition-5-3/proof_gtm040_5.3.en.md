---
role: proof
locale: en
of_concept: proposition-5-3
source_book: gtm040
source_chapter: "5"
source_section: "3"
---

**Proof:** $N_{ij}$ in the $P$-process is finite when $j$ is transient; hence $N$ is finite-valued. Therefore $\lim_k (Q^k) = 0$ by Proposition 5-2.

We recall that $\bar{N}_{ij} = M_i[\bar{n}_j]$, and $N = I + \bar{N}$. Hence $\bar{N} = \sum_{k=1}^{\infty} Q^

Proof: The first two assertions are restatements of Proposition 4-13 for the case where $Q$ is our transition matrix. The last four results are a restatement of Proposition 4-15.

Note that the conclusions of Proposition 5-4 show how to compute $N$ from $H$ and $\bar{H}$. Our next result establishes a method of finding $N$ without using the $H$-matrix: For finite matrices the knowledge that $N$ is a (two-sided) inverse of $I - Q$ is sufficient to determine $N$ uniquely, but for infinite matrices it is not. For if $r$ is a $Q$-regular column vector and $\beta$ is a $Q$-regular row vector, then $N + r\beta$ is a second two-sided inverse of $I - Q$. We shall see that such regular vectors $r$ and $\beta$ often exist.

In Section 2 we shall obtain a refinement of Proposition 5-5 by proving that $N$ is the unique minimum non-negative inverse of $I - Q$ on each side.

Proposition 5-5: $N(I - Q) = (I - Q)N = I$ and $QN = NQ \leq N$. In particular, every row of $N$ is a $Q$-superregular measure, and every column of $N$ is a $Q$-superregular function.

Proof: The second and third assertions follow from the first, and $QN = N - I$ by Proposition 5-4. Also $NQ = N - I$ by Proposition 5-2 and monotone convergence. Since $N$ has finite entries, the first assertion follows.

If $P$ is a transient chain with a non-empty set $E$ of absorbing states, we define the absorption matrix $B$ to have index sets $\tilde{E}$ and $E$ and to have entries

$$B_{ij} = \Pr_i[\text{process is absorbed at } j].$$

The $B$-matrix is not square; it has the same index sets as the $R$-matrix.

Proposition 5-6: If $P$ is a transient chain with a non-empty set of absorbing states, then $B = NR$.

Proof: Let $

Summing on $n$, we find

$$B = \sum_{n=0}^{\infty} (Q^n R),$$

which by monotone convergence

$$= \left( \sum_{n=0}^{\infty} Q^n \right) R$$

$$= NR.$$

As a result, we see from the proof of Lemma 5-1 that if $P$ is a transient chain, then

$$\lim_{k} P^k = \begin{pmatrix} I & 0 \\ B & 0 \end{pmatrix}.$$

Let $P$ be an arbitrary Markov chain, let $E$ be a subset of the set of states, and let $s_E$ be the statement that the process is in states of $E$ infinitely often. Define $s^E$ by $s_i^E = \Pr_i[s_E]$.
