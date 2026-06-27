---
role: proof
locale: en
of_concept: mathcalma-times-b
source_book: gtm001
source_chapter: "6"
source_section: ""
---

$c \in a \times b \rightarrow (\exists x, y)[x \in a \land y \in b \land c = \langle x, y \rangle]$.

$\rightarrow (\exists x, y)[\{x\} \subseteq a \cup b \land \{x, y\} \subseteq a \cup b \land c = \langle x, y \rangle]$.

$\rightarrow (\exists x, y)[\{x\}, \{x, y\} \in \mathcal{P}(a \cup b) \land c = \langle x, y \rangle]$.

$\rightarrow (\exists x, y)[\langle x, y \rangle \in \mathcal{P}(\mathcal{P}(a \cup b)) \land c = \langle x, y \rangle]$.

$\rightarrow c \in \mathcal{P}(\mathcal{P}(a \cup b))$.

Therefore $a \times b \subseteq \mathcal{P}(\mathcal{P}(a \cup b))$; hence $\mathcal{M}(a \times b)$.
