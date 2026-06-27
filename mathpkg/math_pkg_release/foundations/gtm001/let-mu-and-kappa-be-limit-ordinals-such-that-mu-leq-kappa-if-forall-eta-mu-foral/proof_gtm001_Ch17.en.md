---
role: proof
locale: en
of_concept: let-mu-and-kappa-be-limit-ordinals-such-that-mu-leq-kappa-if-forall-eta-mu-foral
source_book: gtm001
source_chapter: "17"
source_section: ""
---

Let $I = \{\langle \eta, \alpha, Q \rangle | \eta < \mu \wedge \alpha < \kappa \wedge \alpha \leq \eta \wedge Q$ is a finite subset of $\eta\}$. For each $i = \langle \eta, \alpha, Q \rangle \in I$, we set $\eta_i = \eta, \alpha_i = \alpha$ and $Q_i = Q$. For any $i, j \in I$, we define $i < j$ by

$$i < j \xrightarrow{\Delta} \eta_i \leq \eta_j \wedge \alpha_i \

(2) $i, j \in I \wedge i \leq j \rightarrow (i, j \in I_1 \wedge i \leq_1 j) \vee (i, j \in I_2 \wedge i \leq_2 j)$
$\vee (i \in I_1 \wedge j \in I_2)$,

(3) $\langle \zeta_i, \gamma_i, R_i \rangle = \begin{cases} \langle \xi_i, \alpha_i, P_i \rangle & \text{if } i \in I_1, \\ \langle \eta_i, \beta_i, Q_i \rangle & \text{if } i \in I_2, \end{cases}$

(4) $\pi_{ij} = \begin{cases} \rho_{ij} & \text{if } i, j \in I_1, \\ \theta_{ij} & \text{if } i, j \in I_2. \end{cases}$

We need to define $i < j$ and $\pi_{ij}$ when $i \in I_1$ and $j \in I_2$: If $i \in I_1$ and $j \in I_2$, then

$$i < j \iff \xi_i \leq \eta_j \wedge \alpha_i \leq \beta_j \wedge \rho_{i\infty}^* P_i \subseteq \mathcal{W}(\theta_{j\infty}) \wedge$$
$$\sup \{ \rho_{i\infty}(v) + 1 | v < \xi_i \} \in \mathcal{W}(\theta_{j\infty}).$$

It is easily seen that

$$\mathcal{W}(\rho_{i\infty}) = \rho_{i\infty}^* \xi_i = \rho_{i\infty}^* M^{\xi_i}(\alpha_i \cup P_i) \subseteq \mathcal{W}(\varphi_{j\infty}).$$

Hence $\theta_{j\infty}^{-1} \circ \rho_{i\infty}$ is a medium $M$-map, by Proposition 16.18, and so we set $\pi_{ij} = \theta_{j

Let $\mu' = \sup\{h^*(\bar{\sigma}) + 1 | \bar{\sigma} < \bar{\mu}\}$. We want to show that $h^*: \bar{\mu} \to \mu'$ is a strong $M$-map. Let $F$ be one of $F_0, J, C_i, T$ and $K$, and $\bar{\sigma}, \bar{\tau} < \bar{\mu}$ be such that $F(\bar{\sigma}) = \bar{\tau}$. Then

$$(\exists i \in I)(\exists \bar{\sigma}', \bar{\tau}' < \bar{\delta}_i)[\bar{\pi}_{i\infty}(\bar{\sigma}') = \bar{\sigma} \wedge \bar{\pi}_{i\infty}(\bar{\tau}') = \bar{\tau}].$$

Since $\bar{\pi}_{i\infty}: \bar{\delta}_i \to \bar{\mu}$ is a medium $M$-map,

$$F(\bar{\sigma}') = \bar{\tau}'.$$

But since $h$ is elementary,

$$F(h(\bar{\sigma}')) = h(\bar{\tau}').$$

Hence

$$\pi_{i\infty}(F(h(\bar{\sigma}'))) = \pi_{i\infty}(h(\bar{\tau}')).$$

Since $\pi_{i\infty}: \delta_i \to \mu$ is a medium $M$-map,

$$F(\pi_{i\infty}(h(\bar{\sigma}'))) = \pi_{i\infty}(h(\bar{\tau}')).$$

And hence,

$$F(h^*(\bar{\sigma})) = h^*(\bar{\tau}).$$

Thus we have

$$F^{\bar{\mu}}(\bar{\sigma}) \simeq \bar{\tau} \to F^{\mu'}(h^*(\bar{\sigma})) \simeq h^*(\bar{\tau}).$$

Let $\bar{\sigma}$ and $\tau$ be such that $\bar{\sigma} < \bar{\mu}$, $\tau < \mu'$ and $F(h^*(\bar{\sigma})) = \tau$. Then

$$(\exists i \in I)(\exists \bar{\sigma}',

(5) For each singular cardinal $\lambda$,

$$\overline{2^{\lambda}} = \begin{cases} 2^{\lambda} & \text{if } (\exists \tau < \lambda) (\overline{2^{\tau}} = 2^{\lambda}), \\ (2^{\lambda})^+ & \text{otherwise.} \end{cases}$$

(1) Let $x \subseteq \lambda$ be such that $\bar{x} = \text{cf}(\lambda)$ and $\cup x = \lambda$. Then by $S$ there exists a $y \in L$ such that $x \subseteq y \subseteq \lambda$ and $\bar{y} = \max(\bar{x}, \aleph_1)$. Since $\cup y = \lambda$ and $\lambda$ is regular in $L$, we see that $\bar{y}^L = \lambda$. Hence we have $\bar{y} = \bar{\lambda} \geq \aleph_2$. Thus, $\text{cf}(\lambda) = \bar{x} = \bar{y} = \bar{\lambda}$.

(2) Note that $\lambda \geq \aleph_\omega > \aleph_2$. By (1), $\lambda$ is singular in $L$.

(3) Obviously $(\lambda^+)^L \leq \lambda^+$. Suppose $(\lambda^+)^L < \lambda^+$. From (1) $\text{cf}((\lambda^+)^L) = (\lambda^+)^L = \lambda$. Hence $\lambda$ is a regular cardinal.

(4) By the König lemma,

$(\forall \tau) [\text{cf}(\lambda) \leq \tau < \lambda \rightarrow \lambda < \overline{\lambda^{\text{cf}(\lambda)}} \leq \overline{\lambda^{\tau}}]$.

Therefore,

$(\forall \tau) [\text{cf}(\lambda) \leq \tau < \lambda \rightarrow \overline{\lambda^{\tau}} \geq \max(\overline{2^{\tau}}, \lambda^+)]$.

Let $\tau$ be an arbitrary cardinal such that $\text{cf}(\lambda) \leq \tau < \lambda$. Since

$$\lambda^\tau = \cup \{

(5) Let $\kappa = \text{cf}(\lambda)$ and let $\lambda_v$ for $v < \kappa$ be such that $\lambda_v < \lambda$ and $\lambda = \bigcup_{v < \kappa} \lambda_v$. Then

$$\overline{2^\lambda} = \overline{2^{\bigcup_{v < \kappa} \lambda_v}} = \prod_{v < \kappa} 2^{\lambda_v} \leq \prod_{v < \kappa} 2^{\lambda} = (2^{\lambda})^\kappa.$$

If $\overline{2^\tau} = 2^{\lambda}$ for some $\tau < \lambda$, such that $\kappa \leq \tau$, then

$$\overline{2^\lambda} \leq \overline{(2^\lambda)}^\kappa = \overline{2^{\tau \times \kappa}} \leq 2^{\lambda}.$$

and hence $\overline{2^\lambda} = 2^{\lambda}$. Suppose $(\forall \tau < \lambda)(\overline{2^\tau} < 2^{\lambda})$. Then by (4) we have

$$\overline{(2^\lambda)}^\kappa = \max(\overline{2^\kappa}, (2^\lambda)^+) = (2^\lambda)^+.$$

Therefore, $\overline{2^\lambda} \leq (2^\lambda)^+$. On the other hand, $\overline{(2^\lambda)}^\kappa \leq \overline{(2^\lambda)}^\kappa \leq \overline{2^\lambda}$.
