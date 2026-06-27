---
role: proof
locale: en
of_concept: adjoint-bounded-below-lemma
source_book: gtm015
source_chapter: "57"
source_section: "57.15"
---

# Proof of Adjoint bounded below implies range contains a ball

**Proof.** Let $M > 0$ be such that $\|T'f\| \ge M\|f\|$ for all $f \in E'$. We show $\overline{T(E_1)}$ contains the ball $\{y : \|y\| \le M\}$, where $E_1 = \{x : \|x\| \le 1\}$.

Assuming $y \notin \overline{T(E_1)}$, we prove $\|y\| > M$. Since $\overline{T(E_1)}$ is closed and convex, by Hahn-Banach there exist $f \in E'$ and $\beta \in \mathbb{R}$ with $\operatorname{Re} f(y) > \beta$ and $\operatorname{Re} f(z) < \beta$ for all $z \in \overline{T(E_1)}$. It follows that $|(T'f)(x)| < \beta$ for all $x \in E_1$, so $\|T'f\| \le \beta$. Then
$$M\|f\| \le \|T'f\| \le \beta < \operatorname{Re} f(y) \le |f(y)| \le \|f\|\|y\|,$$
hence $M < \|y\|$.
