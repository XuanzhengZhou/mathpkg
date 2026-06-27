---
role: proof
locale: en
of_concept: regular-function-gibbs-bijection
source_book: gtm040
source_chapter: "12"
source_section: "4"
---

**Proof.** Given $\mu \in \mathcal{G}_V$, define $h$ according to the first equation in the theorem. By Lemma 12-24,

$$
\begin{aligned}
\sum_{\kappa^{n+1}} P_{(n,\kappa^n)(n+1,\kappa^{n+1})} h_{(n+1,\kappa^{n+1})}
&= \sum_{\kappa^{n+1}} \frac{\nu([\kappa^n, \kappa^{n+1}])}{\nu([\kappa^n])} \cdot \frac{\mu([\kappa^n, \kappa^{n+1}])}{\nu([\kappa^n, \kappa^{n+1}])} \\
&= \sum_{\kappa^{n+1}} \frac{\mu([\kappa^n, \kappa^{n+1}])}{\nu([\kappa^n])} \\
&= \frac{\mu([\kappa^n])}{\nu([\kappa^n])} = h_{(n,\kappa^n)},
\end{aligned}
$$

so $h$ is $P$-regular. Clearly $h$ is also non-negative and normalized.

Conversely, let $h$ be any non-negative normalized $P$-regular function. We claim that the second equation prescribes cylinder probabilities for a unique measure $\mu \in \mathcal{G}_V$. Note first that $h$ must be strictly positive. To see this, write

$$
\sum_{\kappa^{n+1}} \nu([\kappa^{n+1}]) h_{(n+1,\kappa^{n+1})} = \pi P^{n+1} h = 1,
$$

and

$$
h_{(n,\kappa^n)} = (Ph)_{(n,\kappa^n)} = \sum_{\kappa^{n+1}} \frac{\nu([\kappa^n, \kappa^{n+1}])}{\nu([\kappa^n])} h_{(n+1,\kappa^{n+1})}.
$$

The first equation implies that $h_{(n+1,\kappa^{n+1})} > 0$ for some $\kappa^{n+1}$, and then the second equation, together with the strict positivity of all transition probabilities (since $\nu$ has the full support property), yields $h_{(n,\kappa^n)} > 0$ for all $(n,\kappa^n)$.

To show that the cylinder probabilities prescribed by the second equation satisfy the local characteristics condition for $\mathcal{G}_V$, take any finite $A \subset T$ and choose $n$ large enough that $A \subset \Lambda(n)$. Let $\iota = \{i_t : t \in T\} = (\kappa^0, \kappa^1, \ldots) \in \Omega$. Introduce the sets

$$
[\iota_A] = \{\omega \mid \omega_t = i_t \text{ for all } t \in A\},
$$
$$
[\iota_{\Lambda(n)-A}] = \{\omega \mid \omega_t = i_t \text{ for all } t \in \Lambda(n)-A\},
$$
$$
[\psi] = \{\omega \mid \omega_t = \psi_t \text{ for all } t \in \Lambda(n-1)-\Lambda(n)\},
\qquad \psi \in S^{\Lambda(n-1)-\Lambda(n)}.
$$

By construction,

$$
\mu([\iota_A]) = \sum_{\psi} \sum_{\kappa^n} \nu([\iota_A] \cap [\psi] \cap [\kappa^n]) \cdot h_{(n,\kappa^n)},
$$

and

$$
\mu([\iota_{\Lambda(n)-A}]) = \sum_{\psi} \sum_{\kappa^n} \nu([\iota_{\Lambda(n)-A}] \cap [\psi] \cap [\kappa^n]) \cdot h_{(n,\kappa^n)},
$$

where $\psi$ is summed over $S^{\Lambda(n-1)-\Lambda(n)}$ and $\kappa^n$ over $S^{K(n)}$. If $\iota^{\psi,\kappa^n}$ denotes the modification of $\iota$ obtained by replacing its values on $\Lambda(n-1)-\Lambda(n)$ with $\psi$ and its values on $K(n)$ with $\kappa^n$, then $\nu_A^{\Lambda(n)}(\iota^{\psi,\kappa^n}) = \nu_A^{\bar{A}}(\iota)$ for all $\psi$ and $\kappa^n$, since $\nu \in \mathcal{G}_V$. Thus

$$
\mu([\iota_A]) = \sum_{\psi} \sum_{\kappa^n} \nu_A^{\Lambda(n)}(\iota^{\psi,\kappa^n}) \cdot \nu([\iota_{\Lambda(n)-A}] \cap [\psi] \cap [\kappa^n]) \cdot h_{(n,\kappa^n)}.
$$

Computing $\mu([\iota_A]) / \mu([\iota_{\Lambda(n)-A}])$ yields $\nu_A^{\Lambda(n)}(\iota)$, which establishes $\mu \in \mathcal{G}_V$. The mapping is clearly bijective.
