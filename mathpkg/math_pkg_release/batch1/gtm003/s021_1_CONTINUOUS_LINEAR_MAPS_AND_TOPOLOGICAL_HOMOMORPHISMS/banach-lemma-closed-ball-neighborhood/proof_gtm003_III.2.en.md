---
role: proof
locale: en
of_concept: banach-lemma-closed-ball-neighborhood
source_book: gtm003
source_chapter: "III"
source_section: "2"
---

Let $t = r/2$. Choose a null sequence $\{\rho_n\}$ of positive numbers such that $\sum_{n=1}^\infty \rho_n < t$. By hypothesis, the closure of $u(S_r)$ is a $0$-neighborhood in $\overline{u(L)}$. Hence there exists $\rho > 0$ such that $S_\rho \cap \overline{u(L)} \subset \overline{u(S_r)}$.

We claim that $S_\rho \cap \overline{u(L)} \subset u(S_{2r})$. Let $y \in S_\rho \cap \overline{u(L)}$. Since $y$ is in the closure of $u(S_r)$, we can find $x_1 \in S_r$ such that $|y - u(x_1)| \leq \rho_1$. Then $y - u(x_1) \in \overline{u(L)}$ and $|y - u(x_1)| \leq \rho_1$, so by a similar approximation with a scaled ball, we can find $x_2 \in S_{\rho_1}$ (rescaling) such that $|y - u(x_1) - u(x_2)| \leq \rho_2$. Continuing inductively, we construct a sequence $\{x_n\}$ with $|x_n| \leq \rho_{n-1}$ (with $\rho_0 = r$) such that $|y - u(x_1 + \cdots + x_n)| \leq \rho_n$.

Since $L$ is complete and $\sum |x_n| \leq r + \sum \rho_n < r + t$, the series $\sum x_n$ converges to some $z \in L$ with $|z| \leq r + \sum \rho_n \leq r + t \leq 2r$ (for a suitable choice of $t = r$ and $\{\rho_n\}$). By continuity of $u$, we have $u(z) = y$. Thus $S_\rho \cap \overline{u(L)} \subset u(S_{2r})$.

Since $S_\rho \cap \overline{u(L)}$ is a $0$-neighborhood in $\overline{u(L)}$, this shows that $u$ maps $0$-neighborhoods in $L$ to $0$-neighborhoods in $\overline{u(L)}$, hence $u$ is open onto $\overline{u(L)}$, i.e., a topological homomorphism.
