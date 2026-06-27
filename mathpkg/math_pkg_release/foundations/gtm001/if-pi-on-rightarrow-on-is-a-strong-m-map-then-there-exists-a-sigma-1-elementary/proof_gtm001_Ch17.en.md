---
role: proof
locale: en
of_concept: if-pi-on-rightarrow-on-is-a-strong-m-map-then-there-exists-a-sigma-1-elementary
source_book: gtm001
source_chapter: "17"
source_section: ""
---

For any term $t$ of $\mathcal{L}$, we let $h(D(t)) = D(\pi(t))$. Then $h$ is well defined and for all $\alpha \in \text{On}$, $h(\alpha) = h(D(\check{\alpha})) = D(\pi(\check{\alpha})) = D(\pi(\alpha)) = \pi(\alpha)$.

Let $\psi(x_0, \ldots, x_n)$ be a bounded formula and let $t_0, \ldots, t_n \in T_\alpha$. Let $\psi^\alpha(x_0, \ldots, x_n)$ be the formula of $\mathcal{L}$ obtained from $\psi$ by replacing each quantifier $\exists x \in y(\ldots)$ in $\psi$ by $\exists^\alpha x(x \in y \wedge \ldots)$. Then

$$L \models \psi(D(t_0), \ldots, D(t_n)) \leftrightarrow T(\langle \psi^\alpha(t_0, \ldots, t_n) \rangle) = 1$$

$$\leftrightarrow T(\langle \psi^{\pi(\alpha)}(\pi(t_0), \ldots, \pi(t_n)) \rangle) = 1$$

$$\leftrightarrow L \models \psi(D(\pi(t_0)), \ldots, D(\pi(t_n))).$$

Let $\varphi(x_1, \ldots, x_n)$ be $(\exists x_0)\psi(x_0, x_1, \ldots, x_n)$ and let $t_1, \ldots, t_n$ be terms of $\mathcal{L}$. Then,

$$L \models \varphi(D(t_1), \ldots, D(t_n))$$

$$\rightarrow (\exists \alpha)(\exists t_0)(t_0, t_1, \ldots, t_n \in T_\alpha \wedge L \models

$o(M^{\bar{\eta}}(\bar{\alpha} \cup \bar{Q})) < \bar{\kappa}$. If $i = \langle \bar{\eta}, \bar{\alpha}, \bar{Q} \rangle$, then we set $\bar{\eta}_i = \bar{\eta}$, $\bar{\alpha}_i = \bar{\alpha}$ and $\bar{Q}_i = \bar{Q}$. For any, $i, j \in I$, we define $i < j$ and $i \leq j$ by

$$i < j \xleftrightarrow{\Delta} \bar{\eta}_i \leq \bar{\eta}_j \wedge \bar{\alpha}_i \leq \bar{\alpha}_j \wedge \bar{Q}_i \subseteq \bar{Q}_j \wedge \eta_i \in Q_j,$$

$$i \leq j \xleftrightarrow{\Delta} i < j \vee i = j.$$

Then $\langle I, \leq \rangle$ is directed, but note that $I$ is a proper class in the present situation. For each $i \in I$, let $X_i = M^{\bar{\eta}_i}(\bar{\alpha}_i \cup \bar{Q}_i)$ and $\bar{\rho}_i: \bar{\delta}_i \rightarrow X_i$ be the collapsing map of $X_i$. Also let $\bar{P}_i = (\bar{\rho}_i^{-1})^* \bar{Q}_i$. When $i \leq j$, we set $\bar{\pi}_{ij} = \bar{\rho}_j^{-1} \circ \bar{\rho}_i$. Then $\bar{\pi} = \langle \langle \bar{\delta}_i, \bar{\alpha}_i, \bar{P}_i \rangle, \bar{\pi}_{ij} \rangle_{i,j \in I}$ is a $\kappa$-direct limit system whose limit is On.

If we put $\Pi = h(\bar{\Pi})$, then $\Pi$ is a $\kappa$-direct limit system such that $\lim_{\to} \Pi$ is linearly ordered and has no infinite descending sequence. We define $h^*: \text{

Introduction to Forcing

In proving that AC and GCH are consistent with ZF, Gödel used the so-called method of internal models. From the assumption that the universe $V$ is a model of ZF Gödel prescribed a method for producing a submodel $L$ that is also a model of $V = L$, AC and GCH. This submodel is defined as the class of all sets having a certain property, i.e.,

$$L = \{x | (\exists \alpha) [x = F' \alpha]\}.$$

Indeed since $x = F' \alpha$ is absolute w.r.t. every standard transitive model $M$ it follows that if

$$L^M = \{x | (\exists \alpha \in M) [x = F' \alpha]\}$$

then $L^M$ is a submodel of $M$ that is also a model of $V = L$.

If $V = L$ is valid in every model then $V = L$ must be provable in ZF and conversely if $V = L$ is not provable in ZF then $V = L$ is not valid in some model. Can we hope to find such a model by the method of internal models? That is, can we hope to produce a property $\varphi(q)$ such that

$$\{x | \varphi(x)\}$$

is a model of ZF + $V \neq L$? There are compelling reasons for believing that this method cannot succeed. The arguments turn upon the assumption that there is a set that is a standard model of ZF.
