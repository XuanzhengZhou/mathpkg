---
role: proof
locale: en
of_concept: interpretation-implies-consequence
source_book: gtm037
source_chapter: ""
source_section: ""
---
Assume $\Gamma \models \varphi$. Let $\mathfrak{B}$ be any model of $\Gamma'$. By definition of an interpretation, $\mathfrak{A}$ is an interpretation of $\Gamma$ in $\Gamma'$, which means that for every model $\mathfrak{B} \models \Gamma'$, the interpreted structure $\mathfrak{B}^{\Gamma'\mathfrak{A}}$ is a model of $\Gamma$. Thus $\mathfrak{B}^{\Gamma'\mathfrak{A}} \models \Gamma$.

Since $\Gamma \models \varphi$, it follows that $\mathfrak{B}^{\Gamma'\mathfrak{A}} \models \varphi$. Taking the empty assignment (or any assignment $x$), Proposition 11.45 yields $\mathfrak{B}^{\Gamma'\mathfrak{A}} \models \varphi$ iff $\mathfrak{B} \models \varphi^{2\mathfrak{A}}$. Hence $\mathfrak{B} \models \varphi^{2\mathfrak{A}}$.

Since $\mathfrak{B}$ was an arbitrary model of $\Gamma'$, we conclude $\Gamma' \models \varphi^{2\mathfrak{A}}$.
