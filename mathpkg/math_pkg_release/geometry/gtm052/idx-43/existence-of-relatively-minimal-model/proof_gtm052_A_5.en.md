---
role: proof
locale: en
of_concept: existence-of-relatively-minimal-model
source_book: gtm052
source_chapter: "A"
source_section: "§5"
---
Combining (5.4) and (5.7), it is clear that a surface is a relatively minimal model if and only if it contains no exceptional curves of the first kind. So given a surface $X$, if it is already a relatively minimal model, stop. If not, let $Y$ be an exceptional curve of the first kind. By (5.7) there is a morphism $X \rightarrow X_1$ contracting $Y$.

We continue in this manner, contracting exceptional curves of the first kind whenever one exists, and so we obtain a sequence of birational morphisms $X \rightarrow X_1 \rightarrow X_2 \rightarrow \ldots$. We must show that this process eventually stops.

The following proof is due to Matsumura [1]. Suppose that we have a sequence of $n$ contractions

$$X = X_0 \rightarrow X_1 \rightarrow \ldots \rightarrow X_n$$

as above. For each $i = 1, \ldots, n$, let $E_i' \subseteq X_{i-1}$ be the exceptional curve of the contraction $X_{i-1} \rightarrow X_i$, and let $E_i$ be its total transform on $X$.
