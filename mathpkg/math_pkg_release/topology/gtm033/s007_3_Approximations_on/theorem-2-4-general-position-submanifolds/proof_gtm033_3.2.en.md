---
role: proof
locale: en
of_concept: theorem-2-4-general-position-submanifolds
source_book: gtm033
source_chapter: "3"
source_section: "2. Transversality"
---

# Proof of Theorem 2.4: General Position of Submanifolds

**Theorem 2.4.** Let $A, B$ be $C^r$ submanifolds of $N$, $1 \leqslant r \leqslant \infty$. Every neighborhood of the inclusion $i_B: B \to N$ in $C^r_S(B,N)$ contains an embedding which is transverse to $A$.

*Proof.* From the approximation results of Chapter 2 (specifically the smoothing and approximation theorems), we may assume $r = \infty$ without loss of generality.

Consider the transversality condition: a map $f: B \to N$ is transverse to $A$ if for every $x \in B$ with $f(x) \in A$,

$$T_{f(x)}N = T_{f(x)}A + Df_x(T_x B).$$

By the Transversality Theorem 2.1 (applied with $M = B$, $L = B$, and $A \subset N$ as the target submanifold), the set $\bigcap^{\,r}(B, N; A)$ is dense and open in $C^r_S(B,N)$. In particular, every strong neighborhood of $i_B$ contains maps $f: B \to N$ that are transverse to $A$.

Simultaneously, embeddings form an open subset of $C^r_S(B,N)$ (by the openness of immersions and the fact that proper injective immersions are embeddings). Moreover, embeddings are dense (Chapter 2 approximation theorems). Therefore, the intersection of the open dense set of embeddings with the open dense set of maps transverse to $A$ is nonempty and lies in any given strong neighborhood of $i_B$.

Thus we can choose $f \in C^r_S(B,N)$ which is both an embedding and transverse to $A$, and arbitrarily close to the inclusion $i_B$ in the strong topology.

QED
