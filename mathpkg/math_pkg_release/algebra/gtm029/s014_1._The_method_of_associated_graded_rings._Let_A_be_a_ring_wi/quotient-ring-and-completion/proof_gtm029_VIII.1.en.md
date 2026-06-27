---
role: proof
locale: en
of_concept: quotient-ring-and-completion
source_book: gtm029
source_chapter: "VIII"
source_section: "1. The method of associated graded rings"
---

The kernel of $\varphi: A \to A_S$ consists of all $b \in A$ for which there exists $s = 1-m \in S$ such that $bs = 0$. This implies $b = bm = bm^2 = \cdots$, so $b \in \bigcap \mathfrak{m}^n$. Conversely, if $b \in \bigcap \mathfrak{m}^n$, then by Lemma 1 of Vol. I, Ch. IV, $\S$7, there exists $q$ with $\mathfrak{m}b \supset \mathfrak{m}^q \cap Ab$, so $\mathfrak{m}b = Ab$ and $b = mb$ for some $m \in \mathfrak{m}$, giving $b(1-m) = 0$. Thus $\ker\varphi = \bigcap \mathfrak{m}^n$. The identification of $A_S$ with a subring of $\hat{A}$ follows since $\hat{A}$ is the completion, and elements of $S$ become units in $\hat{A}$.