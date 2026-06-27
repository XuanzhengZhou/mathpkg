---
role: proof
locale: en
of_concept: regular-open-via-lower-density
source_book: gtm002
source_chapter: "22"
source_section: "22. Category Measure Spaces"
---

($\Leftarrow$) Let $A \in S$. The set $\phi(A)$ is a basic open set in $\mathcal{T}$ (take $N_A = \emptyset$), so $\phi(A)$ is $\mathcal{T}$-open. By Theorem 22.6, the $\mathcal{T}$-closure of $\phi(A)$ is of the form $\overline{\phi(A)} = \phi(A) \cup N$ for some $N \in \mathcal{N}$. We must show $\phi(A)$ is regular open, i.e., $\phi(A) = \operatorname{int}_{\mathcal{T}}(\overline{\phi(A)})$.

Let $\phi(A_1) \setminus N_1$ be any basic open set contained in $\phi(A) \cup N$. Then applying the lower density $\phi$ and using its properties (4) and (5):
$$\phi(A_1) \setminus N_1 \subset \phi(A_1) = \phi(\phi(A_1) \setminus N_1) \subset \phi(\phi(A) \cup N) = \phi(A),$$
where the last equality uses $\phi(\phi(A) \cup N) = \phi(A)$ (since $\phi(A) \cup N \sim \phi(A)$ and property (2) of $\phi$). This shows that $\phi(A)$ contains every basic open subset of $\overline{\phi(A)} = \phi(A) \cup N$, so $\phi(A)$ is precisely the interior of its closure. Thus $\phi(A)$ is regular open.

($\Rightarrow$) Conversely, suppose $G$ is regular open in $\mathcal{T}$. By Theorem 22.7, $G$ has the property of Baire, so $G \in S$. Since $G$ is $\mathcal{T}$-open, it can be written as $G = \phi(B) \setminus N$ for some $B \in S$ and $N \in \mathcal{N}$. Now $\phi(B) \triangle (\phi(B) \setminus N) \subset N$, so $\phi(B) \sim \phi(B) \setminus N = G$. By property (2) of $\phi$, equivalent sets have the same image under $\phi$, so $\phi(B) = \phi(G)$.

But $\phi(B) = \phi(G)$ and $G$ differ by a subset of $N \in \mathcal{N}$, hence by a nowhere dense set (Theorem 22.6). Since both $G$ and $\phi(B)$ are regular open sets that differ by a nowhere dense set, they must be equal. Therefore $G = \phi(B) = \phi(G)$, so $G = \phi(A)$ with $A = G \in S$.
