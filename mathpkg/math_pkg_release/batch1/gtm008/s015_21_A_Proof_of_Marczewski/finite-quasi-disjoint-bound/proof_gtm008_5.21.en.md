---
role: proof
locale: en
of_concept: finite-quasi-disjoint-bound
source_book: gtm008
source_chapter: "5"
source_section: "21. A Proof of Marczewski's Theorem"
---

[Proof reconstructed from OCR fragments. The original source text is corrupted; the following is a mathematical reconstruction that matches the usage in Corollary 21.4 and the visible proof fragments.]

Apply the Erdős–Rado theorem (Theorem 21.2) to the family $A = \{A_t \mid t \in T\}$. We verify the two hypotheses:

(1) By condition (i), each $A_t$ has cardinality $\leq \alpha$, so $(\forall x \in A)[\bar{x} \leq \alpha]$.

(2) Let $X \subseteq A$ be quasi-disjoint. We must show $\bar{X} \leq \gamma$. Suppose $X = \{A_t \mid t \in T_0\}$ for some $T_0 \subseteq T$, with $X$ quasi-disjoint. Fix $t_0 \in T_0$. For each $t \in T_0 - \{t_0\}$, condition (iii) gives $A_t \cap B_{t_0} \neq 0$, so we may pick

$$C_t = A_t \cap B_{t_0} \neq \emptyset$$

and select an element $x_t \in C_t$. We claim that for distinct $t, t' \in T_0 - \{t_0\}$, we have $x_t \neq x_{t'}$.

Suppose $x \in C_t \cap C_{t'}$ for some $t, t' \in T_0 - \{t_0\}$ with $t \neq t'$. Then

$$x \in A_t \cap A_{t'} = \bigcap_{t'' \in T_0} A_{t''}$$

since $\{A_{t''} \mid t'' \in T_0\}$ is quasi-disjoint. But also $x \in C_t \cap C_{t'} \subseteq B_{t_0}$, so

$$x \in B_{t_0} \cap \bigcap_{t'' \in T_0} A_{t''} \subseteq B_{t_0} \cap A_{t_0} = 0$$

by condition (ii). This is a contradiction.

Therefore the $x_t$ are all distinct elements of $B_{t_0}$, giving an injection $T_0 - \{t_0\} \hookrightarrow B_{t_0}$. Hence

$$\bar{T}_0 \leq \bar{B}_{t_0} + 1 \leq \gamma$$

(since $\gamma \geq \aleph_0$). Thus every quasi-disjoint subfamily of $A$ has cardinality $\leq \gamma$.

By the Erdős–Rado theorem, $\bar{A} = \bar{T} \leq \gamma^\alpha$. $\square$
