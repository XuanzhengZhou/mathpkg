---
role: proof
locale: en
of_concept: "notation-is-as-in-1911-the-set-function-is"
source_book: gtm025
source_chapter: "Complex Analysis"
source_section: "19.12"
---

It is obvious that $|v|(\emptyset) = 0$. Thus we need only show that $|v|$ is countably additive. Let $(A_j)_{j=1}^{\infty}$ be a pairwise disjoint sequence of sets in $\mathcal{A}$ and let $A = \bigcup_{j=1}^{\infty} A_j$. Let $\beta$ be an arbitrary real number such that $\beta < |v|(A)$. Choose a measurable dissection $\{E_1, \ldots, E_n\}$

reverse of this inequality is obvious. Thus suppose that $|v|(A) < \infty$. For any $j_0 \in N$ and any measurable dissection $\{B_1, \ldots, B_m\}$ of $A_{j_0}$, we have

$$\sum_{k=1}^{m} |v(B_k)| \leq |v\left(\bigcup_{j \neq j_0} A_j\right)| + \sum_{k=1}^{m} |v(B_k)| \leq |v|(A),$$

and so $|v|(A_j) < \infty$ for all $j \in N$. Let $\varepsilon > 0$ be arbitrary. For each $j$, choose a measurable dissection $\{E_{j,1}, \ldots, E_{j,n_j}\}$ of $A_j$ such that

$$\sum_{k=1}^{n_j} |v(E_{j,k})| > |v|(A_j) - \frac{\varepsilon}{2^j}.$$

Then for all $m \in N$, we have

$$\sum_{j=1}^{m} |v|(A_j) < \sum_{j=1}^{m} \left(\frac{\varepsilon}{2^j} + \sum_{k=1}^{n_j} |v(E_{j,k})|\right)$$

$$< \varepsilon + |v\left(\bigcup_{j=m+1}^{\infty} A_j\right)| + \sum_{j=1}^{m} \sum_{k=1}^{n_j} |v(E_{j,k})|$$

$$\leq \varepsilon + |v|(A).$$

Since $\varepsilon$ is arbitrary, we have

$$\sum_{j=1}^{m} |v|(A_j) \leq |v|(A)$$

for every $m \in N$, and so

$$\sum_{j=1}^{\infty} |v|(A_j) \leq |v|(A).$$

(2)

Combining (1) and (2), we see that $|v|$ is countably additive. $\square$
