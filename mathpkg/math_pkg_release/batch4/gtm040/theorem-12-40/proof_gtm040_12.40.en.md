---
role: proof
locale: en
of_concept: theorem-12-40
source_book: gtm040
source_chapter: "12"
source_section: "5"
---

Suppose $\mu \in \mathcal{E}_Q$, and let $k_n$, $n \in \mathbb{Z}$, be the sequence of states appearing in the ratio limit representation of Theorem 12-37 for the functions $g_{(m,i)}$ and $h_{(m,i)}$. Since $S$ is finite, there exists some state $j'' \in S$ and an infinite sequence $n'' \to \infty$ such that $k_{n''} \equiv j''$ for all terms in the subsequence. By the ratio limit representation,
$$
h_{(m,i_m)} = c'' \frac{\lim_{n'' \to \infty} (Q^{n'' - m})_{i_m j''}}{\lim_{n'' \to \infty} (Q^{n''})_{0 j''}}.
$$
By the convergence theorem for noncyclic ergodic chains (or the Perron-Frobenius theorem for the stochastic matrix $Q$), both limits equal the stationary measure $\alpha_{j''}$, hence
$$
h_{(m,i_m)} = c'' \frac{\alpha_{j''}}{\alpha_{j''}} = c'',
$$
so $h$ is constant in both $m$ and $i$. Similarly, there exists $j' \in S$ and a sequence $n' \to -\infty$ with $k_{n'} \equiv j'$, giving
$$
g_{(m,i_m)} = c' \frac{\lim_{n' \to -\infty} (Q^{m-n'})_{j' i_m}}{\lim_{n' \to -\infty} (Q^{-n'})_{j' 0}} = c' \frac{\alpha_{i_m}}{\alpha_0} = c_0 \alpha_{i_m}.
$$
From the representation in Theorem 12-37, it follows that the one-dimensional marginals satisfy $\pi_{n,j} = \alpha_j$ for all $n \in \mathbb{Z}$ (the stationary measure), and the transition probabilities satisfy $P_{n,jk} = Q_{jk}$ for all $n \in \mathbb{Z}$. Thus the Gibbs field $\mu$ is uniquely determined as the stationary Markov chain with transition matrix $Q$ and stationary measure $\alpha$. Since every $\mu \in \mathcal{E}_Q$ yields the same $Q$ and $\alpha$, and by Theorem 12-28 $\mathcal{G}_Q$ is the closed convex hull of $\mathcal{E}_Q$, it follows that $|\mathcal{G}_Q| = 1$.
