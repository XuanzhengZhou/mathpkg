---
role: proof
locale: en
of_concept: mu-categoricity-implies-completeness
source_book: gtm053
source_chapter: "5"
source_section: "5.1"
---

Let $T$ be a theory with no finite models that is $\mu$-categorical for some infinite cardinal $\mu$. Suppose, for contradiction, that $T$ is not complete. Then there exists a sentence $\varphi$ in the language of $T$ such that neither $T \vdash \varphi$ nor $T \vdash \neg\varphi$. Hence both $T \cup \{\varphi\}$ and $T \cup \{\neg\varphi\}$ are consistent. By the Löwenheim-Skolem theorem, each has a model of cardinality $\mu$. Since $T$ has no finite models, these models are infinite of cardinality $\mu$. They are both models of $T$ but are not elementarily equivalent (one satisfies $\varphi$, the other $\neg\varphi$), hence not isomorphic. This contradicts the $\mu$-categoricity of $T$. Therefore $T$ must be complete.
