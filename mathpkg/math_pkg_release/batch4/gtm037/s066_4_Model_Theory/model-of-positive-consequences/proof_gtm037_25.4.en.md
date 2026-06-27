---
role: proof
locale: en
of_concept: model-of-positive-consequences
source_book: gtm037
source_chapter: "25"
source_section: "4"
---

Consider the set $\Gamma \cup \{\neg \varphi : \varphi \text{ is a positive sentence and } \Gamma \models \neg \varphi\}$. We claim this set is consistent. If not, by compactness there are finitely many positive sentences $\varphi_0, \ldots, \varphi_{k-1}$ such that $\Gamma \models \neg \varphi_i$ for each $i < k$, and $\Gamma \cup \{\neg \varphi_0, \ldots, \neg \varphi_{k-1}\}$ is inconsistent. Then $\Gamma \models \varphi_0 \vee \cdots \vee \varphi_{k-1}$. But a disjunction of positive sentences is logically equivalent to a positive sentence (by distributing quantifiers), contradicting the assumption that $\mathfrak{B}$ satisfies $\varphi_0 \vee \cdots \vee \varphi_{k-1}$ while each $\neg \varphi_i$ holds in $\mathfrak{B}$. Therefore the set is consistent, and any model $\mathfrak{A}$ of this set satisfies the required condition: $\mathfrak{A} \models \Gamma$ and for every positive sentence $\varphi$, if $\mathfrak{A} \models \varphi$ then $\mathfrak{B} \models \varphi$, i.e., $\mathfrak{A} \preceq_{\mathrm{pos}} \mathfrak{B}$.
