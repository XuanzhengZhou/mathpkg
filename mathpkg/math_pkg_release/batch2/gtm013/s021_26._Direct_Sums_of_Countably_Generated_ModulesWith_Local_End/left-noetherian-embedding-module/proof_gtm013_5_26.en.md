---
role: proof
locale: en
of_concept: left-noetherian-embedding-module
source_book: gtm013
source_chapter: "5"
source_section: "26"
---

($\Rightarrow$) Suppose $R$ is left noetherian. By (25.8), every injective left $R$-module is a direct sum of indecomposable injective modules. Since a module can be embedded in an injective module, every left $R$-module embeds in a direct sum of indecomposable injectives. Moreover, every $c$-generated module is isomorphic to a submodule of the direct sum of the modules in the set $\{R^{(C)}/K \mid K \leq R^{(C)}\}$ when $\operatorname{card} C = c$. Let $H$ be the direct sum of a complete set of representatives of isomorphism classes of such quotient modules. Then every left $R$-module can be embedded in a direct sum of copies of $H$.

($\Leftarrow$) If $H$ satisfies the stated condition, then every injective left $R$-module is isomorphic to a direct summand of a direct sum of copies of $H$ (since an injective module, being embedded in $\oplus H$, splits off as a direct summand). In particular, each injective module is a direct summand of a direct sum of copies of $H$. By (26.1), each such direct summand is a direct sum of countably generated modules. Hence every injective left $R$-module is a direct sum of countably generated modules. By (25.8) this implies $R$ is left noetherian.
