---
role: proof
locale: en
of_concept: lemma-lemma-12
source_book: gtm042
source_chapter: "12.1"
source_section: "The rings"
---

First, let $V$ be a linear representation of $G$ over $L$ with character $\chi$; by restricting scalars we can consider $V$ as a $K$-vector space (of dimension $d$ times as large) and even as a linear representation of $G$ over $K$. We see immediately that the character of this representation is equal to $\text{Tr}_{L/K}(\chi)$, where $\text{Tr}_{L/K}$ denotes the trace associated with the extension $L/K$. It follows by linearity that $\text{Tr}_{L/K}(\chi) \in R_K(G)$, for each element $\chi$ of $R_L(G)$.

In particular, take $\chi \in \overline{R}_K(G)$, i.e. suppose that the values of $\chi$ belong to $K$. Then $\text{Tr}_{L/K}(\chi) = d \cdot \chi$; hence $d \cdot \chi \in R_K(G)$, and the proof is complete.

12.2 Schur indices

The results of the preceding section can also be obtained, and even refined, by using the theory of semisimple algebras. We sketch this briefly:

The algebra $K[G]$ is a product of simple algebras $A_i$, corresponding to the distinct irreducible representations $V_i$ of $G$ over $K$. If $D_i = \text{Hom}^G(V_i, V_i)$ is the commuting algebra of $G$ in $\text{End}(V_i)$, then $D_i$ is a field (noncommutative, in general), and $A_i

Now let $\Sigma_i$ be the set of K-homomorphisms of the field $K_i$ into the algebraically closed field $C$. If $\sigma \in \Sigma_i$, scalar extension from $K$ to $C$ by means of $\sigma$ makes $D_i$ into a matrix algebra $M_{m_i}(C)$, and $A_i$ becomes $M_{n_i m_i}(C)$. Composing $G \rightarrow A_i \rightarrow M_{n_i m_i}(C)$, we obtain an irreducible representation of $G$ over $C$, of degree $n_i m_i$, and with character $\psi_{i,\sigma} = \sigma(\psi_i)$. For fixed $i$, the characters $\psi_{i,\sigma}$ are conjugate: the Galois group of $C$ over $K$ permutes them transitively. Moreover, each irreducible character of $G$ over $C$ is equal to one of the $\psi_{i,\sigma}$. We have

$$\chi_i = \text{Tr}_{K_i/K}(\varphi_i) = \sum_{\sigma \in \Sigma_i} \sigma(\varphi_i) = m_i \sum_{\sigma \in \Sigma_i} \psi_{i,\sigma},$$

which gives the decomposition of $\chi_i$ as a sum of irreducible characters over $C$.

Now let $\chi = \sum_{i,\sigma} d_{i,\sigma} \psi_{i,\sigma}$ be an element of $R(G)$, where the $d_{i,\sigma}$ are integers. In order that $\chi$ have values in $K$, it is necessary and sufficient that it be invariant under the Galois group of $C$ over $K$, i.e., that the $d_{i,\sigma}$ depend only on $i$. If this is indeed the case, and we let $d_i$ denote their common value, we have

$$\chi = \sum_i d_i \psi_i = \sum_i d_i \chi_i/m_i.$$

Hence we have the following proposition, which refines prop. 34:

**Proposition 35.** The characters $\psi_i = \chi_i/m_i$ form a basis of $\overline{R}_K(G)$.

Let us say that $K[

Chapter 12: Rationality questions

12.3. Take for $G$ the quaternion group $\{\pm 1, \pm i, \pm j, \pm k\}$. The group $G$ has 4 characters of degree 1, with values in $\{\pm 1\}$. On the other hand, the natural embedding of $G$ in the division ring $H_Q$ of quaternions over $Q$ defines a surjective homomorphism $Q[G] \rightarrow H_Q$. Show that the decomposition of $Q[G]$ into simple components is

$$Q[G] = Q \times Q \times Q \times Q \times H_Q.$$

The Schur index of the last component is equal to 2. The corresponding character $\psi$ is given by

$$\psi(1) = 2, \quad \psi(-1) = -2, \quad \psi(s) = 0 \quad \text{for } s \neq \pm 1.$$

Hence $K[G]$ is quasisplit if and only if $K \otimes H_Q$ is isomorphic to $M_2(K)$; show that this is equivalent to saying that $-1$ is a sum of two squares in $K$.

12.4. Show that the Schur indices $m_i$ divide the index $a$ of the center of $G$. [Observe that the degree of the irreducible representation with character $\psi_{i,\sigma}$ is $n_i m_i$ and apply prop. 17.] Deduce that $a \cdot \overline{R}_K(G)$ is contained in $R_K(G)$.

12.5. Let $L$ be a finite extension of $K$. Show that, if $L[G]$ is quasisplit, then $[L: K]$ is divisible by each of the Schur indices $m_i$.

12.3 Realizability over cyclotomic fields

We keep the notation of the preceding sections, and denote by $m$ the least common multiple of the orders of the elements of $G$; it is a divisor of $g$.

Theorem 24 (Brauer). If $K$ contains the $m$th roots of unity, then $R
