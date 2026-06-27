---
role: proof
locale: en
of_concept: boundary-removal-lemma
source_book: gtm035
source_chapter: "Chapter 9"
source_section: "9.2"
---
# Proof of the Boundary Removal Lemma

Fix $x \in X \setminus S$. Since $x \notin S$, there exists a boundary $S_0$ with $x \notin S_0$.

For each $y \in S_0$, choose $f_y \in \mathcal{F}$ with $f_y(x) = 0$ and $f_y(y) = 2$ (possible because $\mathcal{F}$ separates points; we may scale and translate). The set

$$\mathcal{N}_y = \{|f_y| > 1\}$$

is a neighborhood of $y$. By compactness of $S_0$, there exist $y_1, \ldots, y_k$ such that $\mathcal{N}_{y_1} \cup \cdots \cup \mathcal{N}_{y_k} \supset S_0$. Write $f_j$ for $f_{y_j}$.

Define

$$U = \{|f_1| < 1, \ldots, |f_k| < 1\}.$$

Then $U$ is a neighborhood of $x$ (since $f_j(x) = 0$ for all $j$) and $U \cap S_0 = \emptyset$ (since on $S_0$, at least one $|f_j| > 1$).

Now fix an arbitrary boundary $\beta$ and suppose, for contradiction, that $\beta \setminus U$ fails to be a boundary. Then there exists $f \in \mathcal{F}$ with $\max_X |f| = 1$ but $\max_{\beta \setminus U} |f| < 1$.

**Assertion.** There exists $n \in \mathbb{N}$ such that $\max_X |f^n f_i| < 1$ for $i = 1, \ldots, k$.

*Proof of the assertion.* Choose $M$ such that $\max_X |f_i| < M$ for $i = 1, \ldots, k$. Choose $n$ so large that

$$(\max_{\beta \setminus U} |f|)^n \cdot M < 1.$$

On $\beta \setminus U$, $|f^n f_i| \leq |f|^n \cdot M < 1$. On $U$, $|f^n f_i| \leq |f|^n |f_i| < 1$ by the definition of $U$ (where $|f_i| < 1$ and $|f| \leq 1$). This proves the assertion.

Now, since $S_0$ is a boundary, we can pick $\bar{x} \in S_0$ with $|f(\bar{x})| = 1$. By the assertion, $|f_i(\bar{x})| < 1$ for $i = 1, \ldots, k$. Hence $\bar{x} \in U$, contradicting $U \cap S_0 = \emptyset$.

Therefore $\beta \setminus U$ must be a boundary. $\square$
