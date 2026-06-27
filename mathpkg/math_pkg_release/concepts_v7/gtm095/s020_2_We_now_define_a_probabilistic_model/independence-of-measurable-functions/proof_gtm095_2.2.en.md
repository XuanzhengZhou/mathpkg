---
role: proof
locale: en
of_concept: independence-of-measurable-functions
source_book: gtm095
source_chapter: "2"
source_section: "2"
---

# Proof of Lemma 4 (Independence of Generated $\sigma$-Algebras)

**Lemma 4.** Let $\mathcal{A}_1, \mathcal{A}_2, \ldots, \mathcal{A}_n$ be algebras of events that are independent with respect to the probability measure $P$. Then the $\sigma$-algebras $\sigma(\mathcal{A}_1), \sigma(\mathcal{A}_2), \ldots, \sigma(\mathcal{A}_n)$ are also independent with respect to $P$.

*Proof.* Note first that independence of sets and systems of sets (algebras, $\sigma$-algebras, etc.) in general probabilistic models is defined in exactly the same way as in elementary probability theory (see Definitions 2-5 in Sect. 3, Chap. 1).

Fix $A_2 \in \mathcal{A}_2, \ldots, A_n \in \mathcal{A}_n$ and consider the collection

$$\mathcal{L}_1 = \left\{ A \in \sigma(\mathcal{A}_1) : P(A \cap A_2 \cap \cdots \cap A_n) = P(A) \prod_{k=2}^{n} P(A_k) \right\}. \tag{3}$$

We show that $\mathcal{L}_1$ is a $\lambda$-system.

- $(\lambda_a)$: Clearly $\Omega \in \mathcal{L}_1$, since $P(\Omega \cap A_2 \cap \cdots \cap A_n) = P(A_2 \cap \cdots \cap A_n) = P(\Omega) \prod_{k=2}^{n} P(A_k)$.

- $(\lambda_b)$: Let $A, B \in \mathcal{L}_1$ with $A \subseteq B$. Then

$$P(A \cap A_2 \cap \cdots \cap A_n) = P(A) \prod_{k=2}^{n} P(A_k),$$

$$P(B \cap A_2 \cap \cdots \cap A_n) = P(B) \prod_{k=2}^{n} P(A_k).$$

Subtracting the first equality from the second and using finite additivity, we obtain

$$P\bigl((B \setminus A) \cap A_2 \cap \cdots \cap A_n\bigr) = P(B \setminus A) \prod_{k=2}^{n} P(A_k).$$

Hence $B \setminus A \in \mathcal{L}_1$, satisfying $(\lambda_b)$.

- $(\lambda_c)$: If $B_k \in \mathcal{L}_1$ with $B_k \uparrow B$, then by continuity of probability,

$$P(B \cap A_2 \cap \cdots \cap A_n) = \lim_{k} P(B_k \cap A_2 \cap \cdots \cap A_n)$$

$$= \lim_{k} \left( P(B_k) \prod_{j=2}^{n} P(A_j) \right) = P(B) \prod_{j=2}^{n} P(A_j).$$

Thus $B \in \mathcal{L}_1$, satisfying $(\lambda_c)$.

Therefore $\mathcal{L}_1$ is a $\lambda$-system. Moreover, by the independence hypothesis on the algebras $\mathcal{A}_i$, we have $\mathcal{A}_1 \subseteq \mathcal{L}_1$. Since $\mathcal{L}_1$ is a $\lambda$-system containing $\mathcal{A}_1$, and $\sigma(\mathcal{A}_1) = \lambda(\mathcal{A}_1)$ (by the $\pi$-$\lambda$ theorem, since $\mathcal{A}_1$ is a $\pi$-system), it follows that $\sigma(\mathcal{A}_1) \subseteq \mathcal{L}_1$. Thus for every $A_1 \in \sigma(\mathcal{A}_1)$ and for every choice $A_2 \in \mathcal{A}_2, \ldots, A_n \in \mathcal{A}_n$,

$$P(A_1 \cap A_2 \cap \cdots \cap A_n) = P(A_1) \prod_{k=2}^{n} P(A_k).$$

This shows that $\sigma(\mathcal{A}_1)$ is independent of the algebra $\mathcal{A}_2$ in the presence of $\mathcal{A}_3, \ldots, \mathcal{A}_n$. Repeating the same argument for $\mathcal{A}_2$ (now with $\sigma(\mathcal{A}_1)$ in place of $\mathcal{A}_1$), and proceeding inductively, we obtain that the $\sigma$-algebras $\sigma(\mathcal{A}_1), \sigma(\mathcal{A}_2), \ldots, \sigma(\mathcal{A}_n)$ are independent. $\square$
