---
role: proof
locale: en
of_concept: associated-graded-of-quotient-module
source_book: gtm029
source_chapter: "VIII"
source_section: "1. The method of associated graded rings"
---

The $n$-th homogeneous component of $G(E/F)$ is $\mathfrak{m}^n(E/F)/\mathfrak{m}^{n+1}(E/F)$. Since $\mathfrak{m}^n(E/F) = (\mathfrak{m}^n E + F)/F$ and $\mathfrak{m}^{n+1}(E/F) = (\mathfrak{m}^{n+1} E + F)/F$, the $n$-th homogeneous component is

$$\frac{(\mathfrak{m}^n E + F)/F}{(\mathfrak{m}^{n+1} E + F)/F} \cong \frac{\mathfrak{m}^n E + F}{\mathfrak{m}^{n+1} E + F}.$$

By the second isomorphism theorem,

$$\frac{\mathfrak{m}^n E + F}{\mathfrak{m}^{n+1} E + F} \cong \frac{\mathfrak{m}^n E}{\mathfrak{m}^n E \cap (\mathfrak{m}^{n+1} E + F)}.$$

The canonical surjection $\mathfrak{m}^n E / \mathfrak{m}^{n+1} E \to \mathfrak{m}^n E / (\mathfrak{m}^n E \cap (\mathfrak{m}^{n+1} E + F))$, summed over all $n$, gives a surjection $G(E) \to G(E/F)$ whose kernel is precisely

$$\sum_{n=0}^{\infty} \frac{(\mathfrak{m}^n E) \cap (\mathfrak{m}^{n+1} E + F)}{\mathfrak{m}^{n+1} E},$$

which consists of the initial forms of elements of $F$, i.e., the leading submodule of $F$.