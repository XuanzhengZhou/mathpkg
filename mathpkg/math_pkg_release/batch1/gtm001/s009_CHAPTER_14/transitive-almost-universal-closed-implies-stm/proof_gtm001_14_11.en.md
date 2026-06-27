---
role: proof
locale: en
of_concept: transitive-almost-universal-closed-implies-stm
source_book: gtm001
source_chapter: "14"
source_section: "The Fundamental Operations"
---
We verify each axiom of ZF:

**Axiom 1 (Extensionality):** Since $M$ is transitive, $a \in M$ implies $a \subseteq M$. Hence $[a = b]^M \leftrightarrow a = b$, so $M$ satisfies Extensionality.

**Axiom 6 (Regularity):** $M$ is a transitive subclass of $V$; the $\in$-relation restricted to $M$ is well-founded, so Regularity holds.

**Axiom 2 (Pairing):** By Proposition 14.5, $(\forall x, y \in M)[\{x, y\} \in M]$.

**Axiom 3 (Unions):** Since $M$ is transitive, $\cup(a) \subseteq M$ for $a \in M$. Hence $(\exists y \in M)[\cup(a) \subseteq y]$. Using Proposition 14.5, $b \times a \in M$, and closure under $\mathcal{F}_2$ gives $(b \times a) \cap E \in M$. Then by Proposition 14.7, $\cup(a) = \mathcal{D}((b \times a) \cap E) \in M$.

**Axiom 4 (Powers):** Since $\mathcal{P}(a) \cap M \subseteq M$, there exists $y \in M$ with $\mathcal{P}(a) \cap M \subseteq y$. By Proposition 14.10, $\mathcal{P}(a) \cap M = \{x \mid x \in y \land [x \subseteq a]^M\} \in M$.

**Axiom 5 (Replacement):** If $(\forall x, y, z \in M)[\varphi^M(x, y) \land \varphi^M(x, z) \rightarrow y = z]$ and $a \in M$, then $F \triangleq \{\langle x, y \rangle \in M^2 \mid x \in a \land \varphi^M(x, y)\}$ is a function. Since $\mathcal{D}(F) \subseteq a$, both $\mathcal{D}(F)$ and $\mathcal{W}(F)$ are sets. Since $F''a \subseteq M$, there exists $z \in M$ with $F''a \subseteq z$. Then $\{y \in M \mid (\exists x \in a)\varphi^M(x, y)\} \in M$ by Proposition 14.10.

**Axiom of Infinity:** The union of all ordinals in $M$ is an ordinal $\beta \in M$. For any ordinal $\alpha \subseteq a$, we have $\alpha \leq \beta + 1$ and $\beta + 1 = \beta \cup \{\beta\} \in M$, hence $\alpha \in M$. Thus $\omega \subseteq M$ and therefore $\omega \in M$.
