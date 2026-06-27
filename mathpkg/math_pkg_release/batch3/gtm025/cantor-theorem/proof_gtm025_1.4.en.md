---
role: proof
locale: en
of_concept: cantor-theorem
source_book: gtm025
source_chapter: "1"
source_section: "4"
---
The function \(x \mapsto \{x\}\) is injective, so \(\overline{U} \leq \overline{\mathcal{P}(U)}\). If equality held, there would be a bijection \(h: U \to \mathcal{P}(U)\). Define \(S = \{x \in U : x \notin h(x)\}\). Then \(S = h(y)\) for some \(y \in U\). But \(y \in S \iff y \notin h(y) = S\), a contradiction.