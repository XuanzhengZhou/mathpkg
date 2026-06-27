---
role: proof
locale: en
of_concept: metric-vs-uniform-completeness
source_book: gtm015
source_chapter: "7"
source_section: "Complete topological groups"
---

# Proof of Metric completeness equals uniform completeness

Let $(X, d)$ be a metric space and let $(X, \mathcal{U}_d)$ be the uniform structure derived from $d$. The basic entourages are $U_n = \{(x, y) : d(x, y) < 1/n\}$ for $n = 1, 2, 3, \ldots$.

**($\Rightarrow$)** Suppose $(X, d)$ is a complete metric space. Let $\mathcal{F}$ be a Cauchy filter on $(X, \mathcal{U}_d)$. We need to produce a point $x$ to which $\mathcal{F}$ converges.

For each $n$, there exists $A_n \in \mathcal{F}$ that is small of order $U_{2n}$, i.e., $d(x, y) < 1/(2n)$ for all $x, y \in A_n$. Then for all $x, y \in \overline{A}_n$, continuity of $d$ gives $d(x, y) \leq 1/(2n) < 1/n$, so $\overline{A}_n$ is small of order $U_n$.

Define $B_n = \overline{A}_1 \cap \cdots \cap \overline{A}_n$. Since $\overline{A}_k \supset A_k \in \mathcal{F}$ and $\mathcal{F}$ is closed under finite intersection, $B_n \in \mathcal{F}$ and in particular $B_n \neq \emptyset$. Moreover, $B_n$ is closed, $B_1 \supset B_2 \supset B_3 \supset \cdots$, and $\operatorname{diam} B_n \leq 1/n$ because $B_n \subset \overline{A}_n$. By completeness of $(X, d)$, $\bigcap_n B_n = \{x\}$ for some $x \in X$.

To show $\mathcal{F} \to x$, let $N = \{y : d(x, y) < \varepsilon\}$ be a basic neighborhood of $x$. Choose $n$ with $1/n < \varepsilon$. For any $y \in B_n$, since $x \in B_n$, we have $(x, y) \in B_n \times B_n \subset \overline{A}_n \times \overline{A}_n \subset U_n$, so $d(x, y) < 1/n < \varepsilon$. Hence $B_n \subset N$, and since $B_n \in \mathcal{F}$, the filter $\mathcal{F}$ contains $N$. Thus $\mathcal{F} \to x$.

**($\Leftarrow$)** Conversely, suppose $(X, \mathcal{U}_d)$ is complete. Every Cauchy sequence $(x_n)$ generates a Cauchy filter, which converges by hypothesis, and the limit of the filter is also the limit of the sequence in the metric sense. Hence $(X, d)$ is complete.
