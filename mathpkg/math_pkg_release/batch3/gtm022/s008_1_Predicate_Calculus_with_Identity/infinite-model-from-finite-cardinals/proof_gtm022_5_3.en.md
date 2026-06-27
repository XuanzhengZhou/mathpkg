---
role: proof
locale: en
of_concept: infinite-model-from-finite-cardinals
source_book: gtm022
source_chapter: "V"
source_section: "3"
---

\textbf{Proof.} Let $\mathcal{T} = (\mathcal{R}, A, C)$, and put $\mathcal{T}' = (\mathcal{R}, A', C)$ where $A' = A \cup \{\text{al}(n) \mid n \in \mathbb{N}^+\}$. We show that $\mathcal{T}'$ is consistent. If $A' \vdash_{\mathcal{F}} F$ (where $F$ denotes a contradiction), then $A \cup N \vdash_{\mathcal{F}} F$ for some finite subset $N$ of $\{\text{al}(n) \mid n \in \mathbb{N}^+\}$. Let $m$ be the maximum index such that $\text{al}(m) \in N$. Since $\mathcal{T}$ has models of arbitrarily large finite cardinal, there is a model of $\mathcal{T}$ with at least $m$ elements, hence a model of $A \cup N$, contradicting $A \cup N \vdash F$. Therefore $\mathcal{T}'$ is consistent. By the completeness theorem, $\mathcal{T}'$ has a model $M$. Since $\text{al}(n)$ is true in $M$ for every $n \in \mathbb{N}^+$, the model $M$ has at least $n$ elements for every $n$, hence $M$ is infinite and is a model of $\mathcal{T}$.
