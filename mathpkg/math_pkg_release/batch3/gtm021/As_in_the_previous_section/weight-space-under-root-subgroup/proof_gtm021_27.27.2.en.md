---
role: proof
locale: en
of_concept: weight-space-under-root-subgroup
source_book: gtm021
source_chapter: "27"
source_section: "27.2"
---
Since $\operatorname{Ker} \rho \subset Z(G) \subset T$, there is no loss of generality in replacing $G$ by the linear group $\rho(G)$, which can be viewed as a matrix group if we choose a basis for $V$ consisting of weight vectors relative to $T$. Since $TU_\alpha$ lies in a Borel group, the Lie--Kolchin Theorem even allows us to take $U_\alpha$ in upper triangular (unipotent) form, while $T$ consists of diagonal matrices $t = \operatorname{diag}(t_1, \ldots, t_n)$. Notice that if $u \in U_\alpha$, $t \in T$, the matrix $t u t^{-1}$ has $(i, j)$ entry $t_i t_j^{-1} u_{ij}$.

Now we exploit the isomorphism $\varepsilon_\alpha: \mathbf{G}_a \rightarrow U_\alpha$ from Theorem 26.3(c). For $x \in \mathbf{G}_a$ and a weight vector $v \in V_\chi$, write $\rho(\varepsilon_\alpha(x))v = \sum_{\mu} v_\mu(x)$ where $v_\mu(x)$ lies in $V_\mu$. Applying the conjugation formula $t\varepsilon_\alpha(x)t^{-1} = \varepsilon_\alpha(\alpha(t)x)$ shows that the only weights $\mu$ that can appear satisfy $\mu - \chi = k\alpha$ for some $k \in \mathbb{Z}^+$.
