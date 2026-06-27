---
role: proof
locale: en
of_concept: completeness-theorem-second-form
source_book: gtm037
source_chapter: "11"
source_section: "Elements of Logic"
---

($\Rightarrow$) This is Lemma 11.8 (Soundness): $\Gamma \vdash \varphi$ implies $\Gamma \models \varphi$.

($\Leftarrow$) We prove the contrapositive. Assume $\Gamma \not\vdash \varphi$. Then by the properties of formal deducibility, $\Gamma \cup \{\neg\varphi\}$ is consistent (if it were inconsistent, $\Gamma$ would prove $\varphi$ by reductio ad absurdum).

By the Completeness Theorem, first form (Theorem 11.19), the consistent set $\Gamma \cup \{\neg\varphi\}$ has a model $\mathfrak{A}$. Then $\mathfrak{A} \models \Gamma$ and $\mathfrak{A} \models \neg\varphi$, so $\mathfrak{A} \not\models \varphi$. Therefore $\Gamma \not\models \varphi$, completing the contrapositive.

Thus $\Gamma \models \varphi$ implies $\Gamma \vdash \varphi$.
