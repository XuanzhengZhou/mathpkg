---
role: proof
locale: en
of_concept: fittings-lemma
source_book: gtm030
source_chapter: "2"
source_section: "13"
---

Let $\beta_k$ denote the kernel of the endomorphism $\eta^k$, $k = 0, 1, 2, \cdots$, with $\eta^0 = 1$ so that $\beta_0 = 1$. Observe that $\beta_{k-1} \subseteq \beta_k$. Suppose $\beta_{r-1} = \beta_r$ and let $z \in \beta_{r-1}$. Write $z = y\eta$. Then $1 = z\eta^{r-1} = (y\eta)\eta^{r-1} = y\eta^r$. Hence $y\eta^{r-1} = 1$, and $z = y\eta$ satisfies $z\eta^{r-2} = 1$. Thus $z \in \beta_{r-2}$. This shows $\beta_{r-2} = \beta_{r-1}$, and by induction all $\beta_k = 1$. Consequently, either $\beta_1 = 1$ or

$$1 = \beta_0 \subset \beta_1 \subset \beta_2 \subset \cdots$$

is an infinite properly ascending chain of invariant $M$-subgroups, contradicting $II'$. Hence if $\mathfrak{G}\eta = \mathfrak{G}$, then $\beta_1 = 1$ and $\eta$ is 1-1 (and thus an automorphism by the chain conditions).

More generally, consider the descending chain $\mathfrak{G}\eta \supseteq \mathfrak{G}\eta^2 \supseteq \cdots$ and the ascending chain $\beta_1 \subseteq \beta_2 \subseteq \cdots$. By the chain conditions, there exists $m$ such that $\mathfrak{G}\eta^m = \mathfrak{G}\eta^{m+1}$ and $\beta_m = \beta_{m+1}$. Then $\eta$ restricted to $\mathfrak{G}\eta^m$ is onto, hence an automorphism, and $\eta$ restricted to $\beta_m$ satisfies $\eta^m = 0$ (nilpotent). Moreover $\beta_m \cap \mathfrak{G}\eta^m = 1$ and $\mathfrak{G} = \beta_m \cdot \mathfrak{G}\eta^m$, giving the direct product decomposition.
