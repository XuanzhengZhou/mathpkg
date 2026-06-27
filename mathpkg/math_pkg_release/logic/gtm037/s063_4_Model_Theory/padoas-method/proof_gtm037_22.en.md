---
role: proof
locale: en
of_concept: padoas-method
source_book: gtm037
source_chapter: "22"
source_section: "4"
---

The method follows directly from the definition of definability: if $\pi$ were definable in $\Gamma$, there would be an explicit definition of $\pi$ in terms of the other nonlogical constants. Any two models agreeing on those other constants would then necessarily agree on $\pi$. The contrapositive gives Padoa's method.

As an application, let $\Gamma$ be the theory of the structure $\langle \mathbb{Z}, + \rangle$, i.e., $\Gamma = \{\varphi : \varphi \text{ is a sentence and } \varphi \text{ holds in } \langle \mathbb{Z}, + \rangle\}$. Then $<$ is not definable in $\Gamma$. To prove this, let $\Gamma'$ be the theory of $\langle \mathbb{Z}, +, < \rangle$. Then $\langle \mathbb{Z}, +, > \rangle$ is also a model of $\Gamma'$, since $\langle -x : x \in \mathbb{Z} \rangle$ is an isomorphism from $\langle \mathbb{Z}, +, < \rangle$ onto $\langle \mathbb{Z}, +, > \rangle$. The two models agree on $+$ but disagree on $<$, so by Padoa's method, $<$ is not definable in $\Gamma'$.
