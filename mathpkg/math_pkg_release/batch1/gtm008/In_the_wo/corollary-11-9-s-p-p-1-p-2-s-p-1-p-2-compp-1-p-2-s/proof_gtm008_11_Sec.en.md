---
role: proof
locale: en
of_concept: corollary-11-9-s-p-p-1-p-2-s-p-1-p-2-compp-1-p-2-s
source_book: gtm008
source_chapter: "11"
source_section: "11 The Independence of"
---
We first show that $\lambda$ is a cardinal in $M[G]$. Otherwise

$$(\exists f \in M[G]) (\exists \lambda_0 < \lambda) [f: \lambda_0 \xrightarrow{\text{onto}} \lambda].$$

Then, as in the previous proof, we obtain

$$\lambda \leq \bigcup_{\alpha < \lambda_0} S_\alpha$$

which contradicts the assumption that $\lambda$ is regular in $M$. Using the argument of Theorem 11.8 it follows that if $\mu \geq \lambda$ is a cardinal in $M[G]$ then $(\mu^+)^M$ is a cardinal in $M[G]$.

Remark. Next we will prove the independence of the $CH$ from the axioms of $ZF + AC$. The idea of the proof is the following. Choosing some suitable $P \in M$ which satisfies the countable chain condition in $M$ we adjoin $\alpha$-many subsets of $\omega$. If $\alpha$ is

If $\mathcal{D}(p_1)$ is $\{\langle \delta_1, m_1 \rangle, \ldots, \langle \delta_n, m_n \rangle\}$

$$S_{i0} \triangleq \{p \in S \mid \langle \delta_i, m_i \rangle \in \mathcal{D}(p) \land p(\delta_i, m_i) = 0\}, \quad i = 1, \ldots, n.$$

$$S_{i1} \triangleq \{p \in S \mid \langle \delta_i, m_i \rangle \in \mathcal{D}(p) \land p(\delta_i, m_i) = 1\}, \quad i = 1, \ldots, n.$$

Then $S = S_{10} \cup S_{11} \cup \cdots \cup S_{n0} \cup S_{n1}$. If

$$S'_{i0} \triangleq \{p - \{\langle \langle \delta_i, m_i \rangle, 0 \rangle\} \mid p \in S_{i0}\}, \quad i = 1, \ldots, n$$

$$S'_{i1} \triangleq \{p - \{\langle \langle \delta_i, m_i \rangle, 1 \rangle\} \mid p \in S_{i1}\}, \quad i = 1, \ldots, n.$$

Then $\bar{S}'_{i0} = \bar{S}'_{i1}$ and $\bar{S}'_{i1} = \bar{S}'_{i0}$. But, by the induction hypothesis for $n - 1$.

$$\bar{S}'_{i0} \leq \aleph_0 \land \bar{S}'_{i1} \leq \aleph_0.$$

Therefore $\bar{S}'^M \leq \aleph_0$.

Remark. If $G$ is $\mathbf{P}$-generic over $M$, then for each $\delta < \alpha$ we define

$$a_\delta(G) \triangleq \{n \in \omega \

Starting with some $\alpha > \omega_1^M$ we have $\alpha > \omega_1^{M[G]}$. This proves the following:

**Theorem 11.11.** If $G$ is $\mathbf{P}$-generic over $M$ (where $\mathbf{P}$ and $M$ are as specified above) then $M[G]$ is a standard transitive model of $ZF + AC + \neg CH$. Furthermore, for any given cardinal $\alpha \in M$ we can find a $G$ and a $\mathbf{P}$ such that

$$\overline{P(\omega)} \geq \alpha \quad \text{in} \quad M[G].$$
