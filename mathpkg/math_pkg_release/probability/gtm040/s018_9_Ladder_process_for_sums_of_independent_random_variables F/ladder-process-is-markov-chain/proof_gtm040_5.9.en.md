---
role: proof
locale: en
of_concept: ladder-process-is-markov-chain
source_book: gtm040
source_chapter: "5"
source_section: "9"
---

The times $s_n$ are stopping times with respect to the natural filtration of the original chain. Applying the strong Markov property (Theorem 4-9) to the stopping time $s_n$ and the statement $r \equiv (x_{s_{n+1}} = c_{n+1})$, we find that, whenever
$$\Pr_\pi[x_{s_0} = c_0 \wedge \dots \wedge x_{s_n} = c_n] > 0,$$
the conditional probability factors as
$$\Pr_\pi[x_{s_{n+1}} = c_{n+1} \mid x_{s_0} = c_0 \wedge \dots \wedge x_{s_n} = c_n] = \Pr_{c_n}[x_{s_1} = c_{n+1}].$$

The right-hand side depends only on the current state $c_n$ and the target state $c_{n+1}$, which establishes the Markov property for the ladder process $P^+$.

Since the original chain $P$ is a sums of independent random variables Markov chain, its transition probabilities are spatially homogeneous: $P_{i,j} = P_{0,j-i}$ for all $i,j$. The ladder process inherits this spatial homogeneity. Indeed,
$$P^+_{ij} = \Pr_i[x_{s_1} = j] = \Pr_0[x_{s_1} = j-i] = P^+_{0,\,j-i},$$
which completes the proof.
