---
role: proof
locale: en
of_concept: convergence-in-measure-properties
source_book: gtm018
source_chapter: "IV"
source_section: "21"
---
**Proof.** The first assertion follows from
$$\{x: |f_n(x)-f_m(x)| \geq \epsilon\} \subset \{x: |f_n(x)-f(x)| \geq \epsilon/2\} \cup \{x: |f_m(x)-f(x)| \geq \epsilon/2\}.$$
For the second,
$$\{x: |f(x)-g(x)| \geq \epsilon\} \subset \{x: |f_n(x)-f(x)| \geq \epsilon/2\} \cup \{x: |f_n(x)-g(x)| \geq \epsilon/2\}.$$
Choosing $n$ large makes both right-hand measures arbitrarily small, so $\mu(\{x: |f(x)-g(x)| \geq \epsilon\}) = 0$ for all $\epsilon > 0$, hence $f = g$ a.e.
