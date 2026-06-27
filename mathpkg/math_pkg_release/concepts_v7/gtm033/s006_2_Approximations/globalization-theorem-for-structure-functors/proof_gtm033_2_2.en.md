---
role: proof
locale: en
of_concept: globalization-theorem-for-structure-functors
source_book: gtm033
source_chapter: "2"
source_section: "2"
---

# Proof of Theorem 2.11 (Globalization theorem for structure functors)

Let $(\mathcal{F}, \mathfrak{Y})$ be a nontrivial structure functor on $X$ which is continuous and locally extendable. We must show that $\mathcal{F}(X) \neq \emptyset$, and in fact if $\mathcal{F}(Y_0) \neq \emptyset$ then $\mathcal{F}(X) \to \mathcal{F}(Y_0)$ is surjective.

Let $a_0 \in \mathcal{F}(Y_0)$. Let $S$ be the set of pairs $(Y, a)$ with $Y_0 \subset Y \in \mathfrak{Y}$ and $a \in \mathcal{F}(Y)$, $a|Y_0 = a_0$. Partially order $S$ by $(Y', a') \leqslant (Y, a)$ if $Y' \subset Y$ and $a|Y' = a'$.

By the closure property of $\mathfrak{Y}$ (the union of any collection of elements of $\mathfrak{Y}$ is again in $\mathfrak{Y}$) and the continuity of the structure functor, every chain in $S$ has an upper bound. Indeed, if $\{(Y_i, a_i)\}$ is a chain, let $Y = \bigcup_i Y_i \in \mathfrak{Y}$. By continuity of $(\mathcal{F}, \mathfrak{Y})$, there is a unique $a \in \mathcal{F}(Y)$ such that $a|Y_i = a_i$ for all $i$. Then $(Y, a) \in S$ and is an upper bound for the chain.

By Zorn's Lemma, $S$ has a maximal element $(Y_{\max}, a_{\max})$. Suppose $Y_{\max} \neq X$. Since the structure functor is locally extendable, there exists $Z \in \mathfrak{Y}$ strictly containing $Y_{\max}$ and $b \in \mathcal{F}(Z)$ such that $b|Y_{\max} = a_{\max}$. But then $(Z, b) \in S$ and $(Y_{\max}, a_{\max}) < (Z, b)$, contradicting maximality.

Therefore $Y_{\max} = X$, so $\mathcal{F}(X) \neq \emptyset$, and the element $a_{\max}$ maps to $a_0$ under the restriction $\mathcal{F}(X) \to \mathcal{F}(Y_0)$, proving surjectivity.

QED
