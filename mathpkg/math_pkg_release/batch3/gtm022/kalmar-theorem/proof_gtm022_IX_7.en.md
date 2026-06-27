---
role: proof
locale: en
of_concept: "kalmar-theorem"
source_book: gtm022
source_chapter: "IX"
source_section: "7"
---
Proof. The theorem is proved by constructing a function $f: P(V, \{\rho\}) \to P(V, \{r\})$ where $\rho$ is a 4-ary relation symbol, such that $p$ is a theorem of $\operatorname{Pred}(V, \{\rho\})$ iff $f(p)$ is a theorem of $\operatorname{Pred}(V, \{r\})$. Lemma 7.6 shows how to encode a 4-ary relation on a set $S$ in terms of a binary relation on an extended set $S' = \{K\} \cup S^2 \cup S^4$. The reduction preserves provability and maps sentences to sentences. Since $\operatorname{Pred}(V, \{\rho\})$ is undecidable (it can encode arithmetic), $\operatorname{Pred}(V, \{r\})$ is undecidable. $\square$
