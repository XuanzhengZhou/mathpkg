---
role: proof
locale: en
of_concept: "quotient-is-cstar-algebra"
source_book: gtm039
source_chapter: "1"
source_section: "1.3"
---
Let $E = \{u = u^* \in J : \text{sp}(u) \subseteq [0,1]\}$. Using the approximate unit from 1.3.1, one shows $\|\dot{x}\| = \inf_{u \in E} \|x(e-u)\|$. Then $\|\dot{x}\|^2 = \inf_u \|x(e-u)\|^2 = \inf_u \|(e-u)x^*x(e-u)\| \leqslant \inf_u \|x^*x(e-u)\| = \|\dot{x}^*\dot{x}\|$. The reverse inequality $\|\dot{x}^*\dot{x}\| \leqslant \|\dot{x}^*\|\|\dot{x}\| = \|\dot{x}\|^2$ always holds, giving equality and hence the $C^*$-condition for the quotient. $\square$
