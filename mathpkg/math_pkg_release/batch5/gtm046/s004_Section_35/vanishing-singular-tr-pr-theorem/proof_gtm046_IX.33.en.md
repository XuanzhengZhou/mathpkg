---
role: proof
locale: en
of_concept: vanishing-singular-tr-pr-theorem
source_book: gtm046
source_chapter: "IX"
source_section: "33"
---

Fix $x\in[\bar{P}_s(x,R)=0]$. For $m<n$, split the Cesaro sum. As $m\to\infty$, the limit follows. For a $\bar{P}$-null $S_0$: $\bar{P}(x,S_0)=\lim\frac{1}{n}\sum P^k(x,S_0)\leq\lim\frac{1}{n}\sum P_s^k(x,R)=0$, so $\bar{P}(x,\cdot)$ is $\bar{P}$-continuous. From $\frac{1}{n}\sum_{k=m+1}^{m+n}P^k(x,S)=\int\{\frac{1}{n}\sum P^k(x,dy)P^m(y,S)\}$, letting $n\to\infty$ gives $\bar{P}(x,S)=\int\bar{P}(x,dy)P^m(y,S)$. Hence $\bar{P}(x,S)=\int\bar{P}(x,dy)\{\frac{1}{n}\sum P^k(y,S)\}$. If the exceptional set is $\bar{P}$-null, dominated convergence yields idempotency.
