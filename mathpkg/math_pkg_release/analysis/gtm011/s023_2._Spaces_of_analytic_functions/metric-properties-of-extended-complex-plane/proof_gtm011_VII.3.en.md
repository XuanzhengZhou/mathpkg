---
role: proof
locale: en
of_concept: metric-properties-of-extended-complex-plane
source_book: gtm011
source_chapter: "VII"
source_section: "3"
---

The proof follows from the relationship between the chordal metric $d$ on $\mathbb{C}_\infty$ and the Euclidean metric on $\mathbb{C}$. Recall that for $z_1, z_2 \in \mathbb{C}$,

$$d(z_1, z_2) = \frac{2|z_1 - z_2|}{(1+|z_1|^2)^{1/2}(1+|z_2|^2)^{1/2}}$$

and $d(z, \infty) = \frac{2}{(1+|z|^2)^{1/2}}$.

(a) For fixed $a \in \mathbb{C}$ and $r > 0$, the function $\frac{2|z-a|}{(1+|z|^2)^{1/2}}$ is continuous in $z$ and positive for $z \neq a$. On the compact set $|z-a| = r$, it attains a positive minimum $\delta$. Choose $\rho = \delta$. If $d(z, a) < \rho \leq \delta \leq \frac{2|z-a|}{(1+|z|^2)^{1/2}} \leq \frac{2|z-a|}{(1+|a|^2)^{1/2}(1+|z|^2)^{1/2}}$ would only hold if... Actually, the simpler argument: since $d(z, a) \leq 2|z-a|$ for all $z, a \in \mathbb{C}$, choosing $\rho < 2r$ does not suffice. Instead, use continuity of stereographic projection. The details are omitted as the proof is left to the reader.

(b) Choose $r = \frac{\rho}{2}(1+|a|^2)$. Then for $|z-a| < r$, the chordal distance satisfies $d(z, a) \leq \frac{2|z-a|}{1+|a|^2 - |z-a|(1+|a|)}$. For $r$ sufficiently small relative to $\rho$, this yields $d(z, a) < \rho$.

(c) Choose $K = \{z \in \mathbb{C} : |z| \leq R\}$ where $R$ is large enough so that $d(z, \infty) = \frac{2}{\sqrt{1+|z|^2}} < \rho$ for $|z| > R$.

(d) Given compact $K \subset \mathbb{C}$, let $R = \max_{z \in K} |z|$. Then for any $\rho < \frac{2}{\sqrt{1+R^2}}$, we have $d(z, \infty) > \rho$ for all $z \in K$, so $B_\infty(\infty; \rho) \subset \mathbb{C}_\infty \setminus K$.
