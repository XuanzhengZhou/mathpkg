---
role: proof
locale: en
of_concept: lemma-c29-closed-sets-successor
source_book: gtm054
source_chapter: "X"
source_section: "49"
---

**Proof.** Suppose that $U_2$ is a successor of $U_1$ and choose $x \in U_2 \setminus U_1$. Since $U_1 \cup \{x\} \subseteq U_2$, we have

$$U_1 \subset c(U_1 \cup \{x\}) \subseteq c(U_2) = U_2.$$

Since $U_2$ is a successor of $U_1$, we cannot have $c(U_1 \cup \{x\}) \subset U_2$. Hence $c(U_1 \cup \{x\}) = U_2$.

Conversely, suppose that $U_2 = c(U_1 \cup \{x_1\})$ for some $x_1 \in U_2 \setminus U_1$. We must show that $U_2$ is a successor of $U_1$. Let $W$ be a closed set such that $U_1 \subset W \subseteq U_2$. Choose $y \in W \setminus U_1$. Then $U_1 \cup \{y\} \subseteq W$, so $c(U_1 \cup \{y\}) \subseteq c(W) = W$. By the exchange property (C11) of the closure operator, since $y \in c(U_1 \cup \{x_1\}) \setminus c(U_1)$, we have $x_1 \in c(U_1 \cup \{y\})$. Therefore $U_2 = c(U_1 \cup \{x_1\}) \subseteq c(U_1 \cup \{y\}) \subseteq W$, which implies $W = U_2$. Thus $U_2$ is a successor of $U_1$.
