---
role: proof
locale: en
of_concept: existence-of-light-signals-through-intermediate-events
source_book: gtm048
source_chapter: "5"
source_section: "5.2"
---

\begin{proof}[Proof of Proposition 5.2.3]

Let $\mathcal{U}$ be a simply convex open neighborhood of $\beta(u_1)$. Let $[a, c]$ be an interval in $\mathcal{E}$ containing $u_1$ as an interior point such that $\beta([a, c]) \subset \mathcal{U}$.

Regard $(\mathcal{U}, \mathbf{g})$ as a spacetime as in Sections 5.0.5 and 5.0.6, and adopt the notation of those subsections.

Let $\mathcal{W} = (I_{\beta(c)}^{-}) \cap (I_{\beta(a)}^{+})$. Thus $\mathcal{W}$ is an open neighborhood of $\beta((a, c))$, in particular of $\beta(u_1)$ (Exercise 5.0.10). Define $\mathcal{F} = (a, c)$. We claim that $\mathcal{W}$ and $\mathcal{F}$ have the required property.

Suppose $x \in \mathcal{W} \setminus \beta(\mathcal{F})$. Then $\beta(c) \in I_x^{+}$ since $x \in I_{\beta(c)}^{-}$. Similarly $\beta(a) \in I_x^{-}$, and in particular $\beta(a) \notin \operatorname{cl}(I_x^{+})$. Since $\beta$ is continuous, the lemma in Section 5.0.6 shows that there exists a unique $u_2 \in (a, c)$ such that the geodesic $\lambda: [0, 1] \to \mathcal{U}$ from $x$ to $\beta(u_2)$ is future-directed and null, i.e., $[\lambda]$ is a light signal from $x$ to $\beta(u_2)$.

By a symmetric argument (reversing the time orientation), there exists a unique $u_0 \in (a, c)$ and a unique light signal $[\lambda']$ from $\beta(u_0)$ to $x$.

\end{proof}
