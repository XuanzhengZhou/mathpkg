---
role: proof
locale: en
of_concept: lkf-equals-denotation-terms
source_book: gtm008
source_chapter: "8"
source_section: "Relative Constructibility and Ramified Languages"
---
We prove the equality $L[K;F] = \{D(t) \mid t \in T\}$ where $F \subseteq K$ and $K$ is transitive.

Recall $L[K;F] = \bigcup_{\alpha \in On} \mathbf{B}_\alpha$ where $\mathbf{B}_0 = 0$, $\mathbf{B}_{\alpha+1} = Df(\mathbf{B}_\alpha) \cup \bar{K}_{\alpha+1}$, and $\mathbf{B}_\lambda = \bigcup_{\alpha<\lambda} \mathbf{B}_\alpha$ for limit $\lambda$. Let $B'_\beta = \{D(t) \mid t \in T_\beta\}$.

We prove by induction on $\beta$:
\begin{enumerate}
\item[(i)] $\mathbf{B}_\beta = B'_\beta$,
\item[(ii)] for all closed limited formulas $\varphi$ of rank $\leq \beta$, $D(\varphi) \leftrightarrow \mathbf{B}_\beta \models D_\beta(\varphi)$.
\end{enumerate}

Assume (i) and (ii) hold for all $\alpha < \beta$. The induction step uses the operator $D_\alpha$ from Definition 8.18. We prove (ii) for $\alpha = \beta$ by induction on $\text{Ord}^3(\varphi)$. The key cases are:

For universal quantification:
$$D((\forall x^\beta)\varphi(x^\beta)) \leftrightarrow (\forall t \in T_\beta) D(\varphi(t))$$
$$\leftrightarrow (\forall t \in T_\beta) [\mathbf{B}_\beta \models D_\beta(\varphi(D(t)))] \quad \text{(by induction hypothesis)}$$
$$\leftrightarrow (\forall a \in B'_\beta) [\mathbf{B}_\beta \models D_\beta(\varphi(a))]$$
$$\leftrightarrow (\forall a \in \mathbf{B}_\beta) [\mathbf{B}_\beta \models D_\beta(\varphi(a))] \quad \text{(by (i))}$$
$$\leftrightarrow \mathbf{B}_\beta \models D_\beta((\forall x^\beta)\varphi(x^\beta)).$$

The case for ranked variables $\gamma < \beta$ is proved similarly.

Now we show $\mathbf{B}_{\beta+1} = B'_{\beta+1}$:

$$D(\hat{x}^\beta \varphi(x^\beta)) = \{D(t) \mid t \in T_\beta \land D(\varphi(t))\}$$
$$= \{D(t) \mid t \in T_\beta \land \mathbf{B}_\beta \models D_\beta(\varphi(D(t)))\}$$
$$= \{a \in \mathbf{B}_\beta \mid \mathbf{B}_\beta \models D_\beta(\varphi(a))\}$$
$$= Df(\mathbf{B}_\beta).$$

Since $\bar{K}_{\beta+1} = \{D(k) \mid k \in K, \text{rank}(k) \leq \beta\}$ is also captured by terms of rank $\leq \beta$, we have $\mathbf{B}_{\beta+1} = B'_{\beta+1}$.

By transfinite induction, $\mathbf{B}_\alpha = B'_\alpha$ for all $\alpha$, hence $L[K;F] = \bigcup_\alpha \mathbf{B}_\alpha = \bigcup_\alpha B'_\alpha = \{D(t) \mid t \in T\}$.
