---
role: proof
locale: en
of_concept: "substitution-theorem-propositional-calculus"
source_book: gtm022
source_chapter: "II"
source_section: "4"
---
Proof. (a) Let $p_1, \ldots, p_n$ be a proof of $w$ from $A$. We show by induction on $n$ that $\varphi(p_1), \ldots, \varphi(p_n)$ is a proof of $\varphi(w)$ from $\varphi(A)$. If $p_i \in \mathcal{A} \cup A$, then $\varphi(p_i) \in \mathcal{A} \cup \varphi(A)$ since homomorphisms preserve axioms (the images of $\mathcal{A}_1, \mathcal{A}_2, \mathcal{A}_3$ are again axioms). If $p_k = p_j \Rightarrow p_i$, then $\varphi(p_k) = \varphi(p_j) \Rightarrow \varphi(p_i)$, so Modus Ponens applies.

(b) Let $v: P(Y) \rightarrow \mathbb{Z}_2$ be a valuation with $v(\varphi(A)) \subseteq \{1\}$. Then $v \circ \varphi: P(X) \rightarrow \mathbb{Z}_2$ is a valuation of $P(X)$ with $(v \circ \varphi)(A) \subseteq \{1\}$. Since $A \models w$, we have $(v \circ \varphi)(w) = 1$, so $v(\varphi(w)) = 1$. $\square$
