---
role: proof
locale: en
of_concept: the-l-machine-m-has-the-collapsing-property
source_book: gtm001
source_chapter: "15"
source_section: ""
---

Let $\eta$ be an ordinal, let $X$ be a subalgebra of $M^\eta$; and let $\pi: \bar{\eta} \rightarrow X$ be the collapsing map of $X$. We shall prove that $\pi: \bar{\eta} \rightarrow \eta$ is a strong $M$-map. Since $\mathcal{P}_<$ has the collapsing property, $\pi: \bar{\eta} \rightarrow \eta$ is a strong $\mathcal{P}_<$-map.

First we show, by induction on $\bar{\varphi}$, that for any sentence $\bar{\varphi} < \bar{\eta}$ of $\mathcal{L}$, $L \models \bar{\varphi}$ iff $L \models \pi(\bar{\varphi})$. We consider only the case where $\bar{\varphi}$ is $\exists^\alpha x_i \bar{\theta}(x_i)$. Other cases can be treated similarly. Let $\alpha = \pi(\bar{\alpha})$ and $\theta = \pi(\bar{\theta})$. Then $\pi(\bar{\varphi}) = \exists^\alpha x_i \theta(x_i)$ and

$$L \models \bar{\varphi} \rightarrow (\exists \bar{t} \in T_\alpha)[L \models \bar{\theta}(\bar{t})]$$

$$\rightarrow (\exists t \in T_\alpha)[L \models \theta(t)] \quad (\text{by the induction hypothesis})$$

$$\rightarrow L \models \exists^\alpha x_i \theta(x_i)$$

$$\rightarrow L \models \varphi.$$

Conversely, suppose $L \models \varphi$ and let $t = K(\langle \varphi \rangle) \in T_\alpha$. Since $t < \varphi$, $t = K^\eta(\langle \varphi \rangle)$ and hence $t \in X$. Let $\bar{t} < \bar{\eta}$ be such that $\pi(\bar{t}) = t$. Then $\bar{t} \in T_\bar{\alpha}$, and by the induction hypothesis, $L \models \bar{\theta}(\bar{t})$. Therefore $L \

If $\varphi$ is $\exists^\alpha x\theta(x)$, then $\pi_{i\infty}(\varphi) = \exists^{\pi_{i\infty}(\alpha)}x\pi_{i\infty}(\theta)(x)$. Suppose $L \models \varphi$. Then there exists a $t \in T_\alpha$ such that $L \models \theta(t)$, and hence, by the induction hypothesis, $L \models \pi_{i\infty}(\theta)(\pi_{i\infty}(t))$ with $\pi_{i\infty}(t) \in T_{\pi_{i\infty}(\alpha)}$. Thus we have $L \models \pi_{i\infty}(\varphi)$. Now suppose $L \models \pi_{i\infty}(\varphi)$. Then there exists a $t' \in T_{\pi_{i\infty}(\alpha)}$ such that $L \models \pi_{i\infty}(\theta)(t')$. Let $j \geq i$ and $t \in T_{\pi_{ij}(\alpha)}$ be such that $\pi_{j\infty}(t) = t'$. By the induction hypothesis, $L \models \pi_{ij}(\theta)(t)$, and hence $L \models \pi_{ij}(\varphi)$. Since $\pi_{ij} : \eta_i \rightarrow \eta_j$ is a strong $M$-map, we see that $L \models \varphi$.

From (1) it is easy to see that

(2) $\pi_{i\infty}(T^{\eta_i}(\alpha)) \simeq T^{\eta\infty}(\hat{\pi}_{i\infty}(\alpha))$ for all $\alpha \in \eta_i^\circ$.

It remains to verify that

(3) $\pi_{i\infty}(K^{\eta_i}(\alpha)) \simeq K^{\eta\infty}(\hat{\pi}_{i\infty}(\alpha))$ for all $\alpha \in \eta_i^\circ$.

Let $\varphi = \exists^\alpha x\theta(x)$ be a sentence that is less than $\eta_i$. Then by (1), $K^{\eta_i}(\langle \varphi \rangle)$ is defined iff $K^{\eta\infty}(\langle \pi_{i\infty}(\varphi) \rangle)$ is defined. Suppose
