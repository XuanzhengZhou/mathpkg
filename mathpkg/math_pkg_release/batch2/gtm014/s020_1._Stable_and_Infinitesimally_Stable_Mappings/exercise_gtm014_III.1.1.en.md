---
role: exercise
locale: en
chapter: "III"
section: "§1. Stable and Infinitesimally Stable Mappings"
exercise_number: 1
---

Compute the derivative $\beta_f = (d\tilde{\beta})_{\operatorname{id}_Y}$ where $\tilde{\beta}: \operatorname{Diff}(Y) \to C^\infty(X, Y)$ is given by $k \mapsto k \circ f$, analogously to the computation of $\alpha_f$ in the text. Show that for $t \in C^\infty(TY)$ (identified with $T_{\operatorname{id}_Y}\operatorname{Diff}(Y)$), one has

$$
\beta_f(t) = t \circ f.
$$

*Hint:* Let $t \mapsto k_t$ be a curve in $\operatorname{Diff}(Y)$ based at $\operatorname{id}_Y$ representing $t$. Then $\beta_f(t)$ is represented by the curve $t \mapsto k_t \circ f$. Compute the derivative pointwise using Lemma 1.12 and note that no sign change occurs (unlike the $\alpha_f$ case where the inverse $h_t^{-1}$ contributed a minus sign).
