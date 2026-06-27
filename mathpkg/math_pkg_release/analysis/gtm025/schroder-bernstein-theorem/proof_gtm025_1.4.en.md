---
role: proof
locale: en
of_concept: schroder-bernstein-theorem
source_book: gtm025
source_chapter: "1"
source_section: "4"
---
Let \(U, V\) be sets with \(\overline{U} = u, \overline{V} = v\). There exist one-to-one functions \(f: U \to V\) and \(g: V \to U\). Define \(\varphi(E) = U \setminus g(V \setminus f(E))\) for \(E \subset U\). If \(E \subset F\) then \(\varphi(E) \subset \varphi(F)\). Let \(\mathcal{D} = \{E \in \mathcal{P}(U) : E \subset \varphi(E)\}\) and \(D = \bigcup \mathcal{D}\). Then \(D \in \mathcal{D}\) and \(\varphi(D) = D\), giving a bijection between \(U\) and \(V\).