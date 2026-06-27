---
role: proof
locale: en
of_concept: theorem-9-6-radon-nikodym
source_book: gtm055
source_chapter: "9"
source_section: "2"
---

The proof proceeds in several steps. First, by decomposing $X$ into a disjoint union of sets of finite $\mu$-measure, the problem reduces to the case where $\mu$ is finite. Uniqueness follows from the fact that if $\int_E f \, d\mu = \int_E f_0 \, d\mu$ for all $E \in \mathbf{S}$, then $f = f_0$ a.e. $[\mu]$.

For existence, for each positive rational $r$, let $\{A_r, X \setminus A_r\}$ be a Hahn decomposition of $X$ with respect to the signed measure $r\mu - 
u$, so that $
u(E) \leq r\mu(E)$ for measurable $E \subseteq A_r$, and $
u(E) \geq r\mu(E)$ for $E \subseteq X \setminus A_r$. For rationals $0 < r < s$, one shows $\mu(A_r \setminus A_s) = 0$ and hence $
u(A_r \setminus A_s) = 0$. Define $B_t = igcup_{0 < r < t} A_r$ for each real $t > 0$, where the union is over rational $r$. The family $\{B_t\}$ satisfies that $\{B_t, X \setminus B_t\}$ is a Hahn decomposition for $t\mu - 
u$ and is nested: $B_u = igcup_{0 < t < u} B_t$.

The Radon--Nikodym derivative is then defined by

$$f(x) = egin{cases} \inf\{t : x \in B_t\}, & x \in B_\infty, \ +\infty, & x \in X \setminus B_\infty. \end{cases}$$

One verifies that $f$ is measurable and that for any measurable $E$, the measures $
u$ and $
u_f$ agree. The key estimates use the Hahn decomposition property: for $E \subseteq B_\infty$ with finite measure, $
u(E)$ is approximated by $
u(E \cap B_{t_n})$ for increasing $t_n$, and the semicontinuity of measures yields equality. For $E \subseteq X \setminus B_\infty$, either $\mu(E) = 0$ (so both are zero by absolute continuity) or $
u(E) = +\infty = 
u_f(E)$.
