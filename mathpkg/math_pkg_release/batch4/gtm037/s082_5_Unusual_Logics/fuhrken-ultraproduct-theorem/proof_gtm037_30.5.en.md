---
role: proof
locale: en
of_concept: fuhrken-ultraproduct-theorem
source_book: gtm037
source_chapter: "30"
source_section: "5"
---

The proof is by induction on $\varphi$, and goes just as in Chapter 18 except for the step from $\varphi$ to $\mathbf{Q}v_j\varphi$.

Assume the result holds for $\varphi$. For any $i \in I$, define
$$T_i = \{a \in A_i : \mathfrak{A}_i \models_m \varphi[\operatorname{pr}_i \circ x_{v_j}^a]\}.$$

Now suppose $\{i \in I : \mathfrak{A}_i \models_m \mathbf{Q}v_j\varphi[\operatorname{pr}_i \circ x]\} \in F$. Then for $F$-almost all $i$, $|T_i| \geq m$. Since $|I| < \pi m$, we have $\prod_{i \in I} |T_i| \geq m$ (by definition of $\pi m$). This yields at least $m$ distinct elements in the reduced product witnessing $\mathbf{Q}v_j\varphi$, so $\prod \mathfrak{A}_i / \bar{F} \models_m \mathbf{Q}v_j\varphi[[] \circ x]$.

Conversely, suppose $\{i \in I : \mathfrak{A}_i \models_m \mathbf{Q}v_j\varphi[\operatorname{pr}_i \circ x]\} \notin F$. Let $J = \{i \in I : \mathfrak{A}_i \not\models_m \mathbf{Q}v_j\varphi[\operatorname{pr}_i \circ x]\} \in F$ (since $F$ is an ultrafilter). For $i \in J$, $|T_i| < m$. Since $|J| \leq |I| < \pi m$, by definition of $\pi m$, $\prod_{i \in J} |T_i| < m$. Hence there are fewer than $m$ witnesses in the reduced product, so $\prod \mathfrak{A}_i / \bar{F} \not\models_m \mathbf{Q}v_j\varphi[[] \circ x]$.
