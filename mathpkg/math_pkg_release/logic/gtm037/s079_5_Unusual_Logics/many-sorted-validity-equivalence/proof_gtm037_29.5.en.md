---
role: proof
locale: en
of_concept: many-sorted-validity-equivalence
source_book: gtm037
source_chapter: "29"
source_section: "5. Unusual Logics"
---

The proof follows directly from Proposition 29.28.

($\Rightarrow$) Suppose $\models \varphi$ in many-sorted logic. Let $\mathfrak{B}$ be any ordinary $\mathcal{L}^*$-structure that is a model of $\Gamma$. Then $\mathfrak{B}$ is of the form $\mathfrak{A}^*$ for some many-sorted $\mathcal{L}$-structure $\mathfrak{A}$ (since $\mathfrak{B} \models \Gamma$ ensures that each $\mathbf{P}_s^{\mathfrak{B}}$ is nonempty and the operations respect the sort conditions). By Proposition 29.28, $\mathfrak{A} \models \varphi$ iff $\mathfrak{B} \models \varphi^*$. Since $\models \varphi$, we have $\mathfrak{A} \models \varphi$, hence $\mathfrak{B} \models \varphi^*$. Thus $\Gamma \models \varphi^*$.

($\Leftarrow$) Suppose $\Gamma \models \varphi^*$. Let $\mathfrak{A}$ be any many-sorted $\mathcal{L}$-structure. By Proposition 29.28, $\mathfrak{A}^* \models \Gamma$, so by assumption $\mathfrak{A}^* \models \varphi^*$. By Proposition 29.28 again, $\mathfrak{A} \models \varphi$. Hence $\models \varphi$ in many-sorted logic.
