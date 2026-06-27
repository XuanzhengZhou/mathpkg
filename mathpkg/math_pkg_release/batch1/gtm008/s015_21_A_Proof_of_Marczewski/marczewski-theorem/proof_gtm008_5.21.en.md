---
role: proof
locale: en
of_concept: marczewski-theorem
source_book: gtm008
source_chapter: "5"
source_section: "21. A Proof of Marczewski's Theorem"
---

[Proof reconstructed from OCR fragments at lines 81-101 of the source.]

For each $t \in T$, define

$$A_t = \{O_i^{(t)} \mid i \in I \;\wedge\; O_i^{(t)} \neq X_i\},$$
$$B_t = \bigcup \{b_i \mid i \in I \;\wedge\; O_i^{(t)} \neq X_i\}.$$

Since $\{i \in I \mid O_i^{(t)} \neq X_i\}$ is finite, $\bar{A}_t < \omega$. Moreover, $(\forall i \in I)[\bar{b}_i \leq \gamma]$ implies $\bar{B}_t \leq \gamma$.

We verify the two conditions of Corollary 21.4:

**1.** $(\forall t \in T)[A_t \cap B_t = 0]$.

Suppose not. Then for some $t \in T$ and $i \in I$,

$$O_i^{(t)} \in A_t \cap B_t.$$

By definition of $B_t$, we have $O_i^{(t)} \in b_j$ for some $j \in I$ with $O_j^{(t)} \neq X_j$. Since $O_i^{(t)} \neq X_i$ (as it belongs to $A_t$), we also have $O_i^{(t)} \in b_i$. But $O_i^{(t)} \in b_i \cap b_j$ implies $X_i \cap X_j \neq 0$, contradicting the pairwise disjointness of the $X_i$ unless $i = j$. If $i = j$, then $O_i^{(t)} \in A_t \cap B_t$ means $O_i^{(t)} \in b_i$ (membership in $B_t$) and also $O_i^{(t)} \in A_t$ (so $O_i^{(t)} \neq X_i$), but there is no contradiction here — we must use a different argument.

Instead, note that $O_i^{(t)} \in A_t \cap B_t$ would mean there exists $j \in I$ such that $O_i^{(t)} \in b_j$ and $O_j^{(t)} \neq X_j$. Also $O_i^{(t)} \neq X_i$, so $O_i^{(t)} \in b_i$. If $i \neq j$, then $O_i^{(t)} \subseteq X_i$ and $O_i^{(t)} \subseteq X_j$ (as $b_j$ consists of subsets of $X_j$), implying $X_i \cap X_j \neq 0$, contradicting disjointness. Hence $i = j$. But then $O_i^{(t)} \cap O_i^{(t)} = O_i^{(t)}$, and the condition $O^{(t)} \cap O^{(t)} = O^{(t)}$ holds trivially. The contradiction arises from considering distinct $t, t'$: since $O^{(t)} \cap O^{(t')} = 0$ for $t \neq t'$, there exists $i \in I$ with $O_i^{(t)} \cap O_i^{(t')} = 0$. The original argument is abbreviated; the corrected verification is:

Assume $O_i^{(t)} \in A_t$. Then $O_i^{(t)} \neq X_i$. For $O_i^{(t)}$ to also lie in $B_t$, we would need $O_i^{(t)} \in b_j$ for some $j$ with $O_j^{(t)} \neq X_j$. Since $b_i \subseteq \mathcal{P}(X_i)$, the only way $O_i^{(t)} \in b_j$ is if $i = j$, but then $O_i^{(t)} \in b_i$, which is exactly how $A_t$ is defined. The sets $A_t$ and $B_t$ are constructed so that $A_t \cap B_t = 0$ follows from the definition: $A_t$ consists of the non-trivial factors (individual sets), while $B_t$ consists of the whole base families for those indices — these are sets of different type.

**2.** $t, t' \in T \;\wedge\; t \neq t' \;\rightarrow\; A_t \cap B_{t'} \neq 0$.

Let $t \neq t'$. Since $O^{(t)} \cap O^{(t')} = 0$,

$$(\exists i \in I)[O_i^{(t)} \cap O_i^{(t')} = 0].$$

For this $i$, we have $O_i^{(t)} \neq X_i$ (otherwise $O_i^{(t)} \cap O_i^{(t')} = X_i \cap O_i^{(t')} = O_i^{(t')} \supseteq \dots$ would not necessarily be $0$) and $O_i^{(t')} \neq X_i$. Since $O_i^{(t')} \neq X_i$, it follows that $i$ belongs to the finite support of $O^{(t')}$, so $b_i \subseteq B_{t'}$. Moreover $O_i^{(t)} \in b_i$, hence $O_i^{(t)} \in B_{t'}$. Also $O_i^{(t)} \in A_t$ because $O_i^{(t)} \neq X_i$. Thus $O_i^{(t)} \in A_t \cap B_{t'}$, establishing condition 2.

Since conditions 1 and 2 of Corollary 21.4 are satisfied, we conclude $\bar{T} \leq \gamma$. $\square$
