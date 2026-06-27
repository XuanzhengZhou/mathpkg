---
role: proof
locale: en
of_concept: m-complete-ultrafilter-from-generic
source_book: gtm008
source_chapter: "2"
source_section: "Generic Sets"
---

**Proof.** Let $B$ be an $M$-complete Boolean algebra and $P$ the associated partial order. Define $F = \{b \in |\mathbf{B}| \cap M \mid b = b^{-0} \land b \cap G \neq 0\}$.

Clearly $F \subseteq |B| \cap M$. Since $P$ is dense in $P$, $P \cap G \neq 0$, and $P$ is regular open with $P \in M$, so $P \in F$ and $F \neq 0$.

If $x, y \in F$, then $x \cap G \neq 0$ and $y \cap G \neq 0$, so there exist $c_1 \in x \cap G$ and $c_2 \in y \cap G$. Since $x, y$ are open, $[c_1] \subseteq x$ and $[c_2] \subseteq y$. By Theorem 2.4 (strong genericity), there exists $c \in G$ with $c \leq c_1, c_2$, so $c \in (x \cap y) \cap G$, hence $xy \in F$. If $x \in F$, $y \in |B| \cap M$, and $x \leq y$, then $x \cap G \neq 0$ implies $y \cap G \neq 0$, so $y \in F$. Since $0 \cap G = 0$, $0 \notin F$, so $F$ is proper.

For $M$-completeness: if $A \subseteq F$ and $A \in M$, then $\prod_{a \in A} a \in |B| \cap M$ (by $M$-completeness of $B^M$). To show $\prod_{a \in A} a \cap G \neq 0$, suppose it were empty. Then $G \subseteq \bigcup_{a \in A} -a$. The set $S = \bigcup_{a \in A} -a$ is dense in $P$ and belongs to $M$. By genericity, $G \cap S \neq 0$, so some $q \in G$ belongs to $-a$ for some $a \in A$. Then $-a \in F$, contradicting $a \in F$ and $F$ being a proper filter. Hence $\prod_{a \in A} a \in F$.

Finally, for any $a \in |B| \cap M$, $a \cup -a$ is dense in $P$ and belongs to $M$, so $(a \cup -a) \cap G \neq 0$, giving $a \in F \lor -a \in F$. Since $a(-a) = 0 \notin F$, we have $a \in F \leftrightarrow -a \notin F$, so $F$ is an ultrafilter.
