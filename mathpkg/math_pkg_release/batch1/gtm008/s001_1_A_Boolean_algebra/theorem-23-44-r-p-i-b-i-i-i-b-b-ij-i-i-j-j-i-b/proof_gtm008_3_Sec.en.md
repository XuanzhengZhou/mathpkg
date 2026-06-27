---
role: proof
locale: en
of_concept: theorem-23-44-r-p-i-b-i-i-i-b-b-ij-i-i-j-j-i-b
source_book: gtm008
source_chapter: "3"
source_section: "3 A consequence of"
---
Without loss of generality, we may take $I = \aleph_\alpha$. First of all, we assume that $\aleph_\alpha$ is

Then $\mu' < \mu < \aleph_\alpha \rightarrow q_\mu \leq q'_\mu$. Therefore by 2 of Definition 23.40 we can pick a $\bar{q} \in \Delta$ such that $(\forall \mu < \aleph_\alpha)[\bar{q} \leq q_\mu]$. Define $\Lambda = \bigcup_{\mu < \aleph_\alpha} \Lambda_\mu$ and take $\bar{r} = \bar{q}$. Then $\bar{r}$ and $\Lambda$ satisfy 2 and 3.

Next we consider an arbitrary $r \in P$ but still assume that $\aleph_\alpha$ is regular. Let $r = p \cdot q$ and for this $q$ let $\bar{q}$ and $\Lambda$ be constructed as above. Define $\bar{r} = p \cdot \bar{q}$. Then $\bar{r}$ and $\Lambda$ satisfy 2 and 3.

Finally, we consider the case where $\aleph_\alpha$ is singular. Then $\aleph_\alpha = \sup_{\mu < \alpha'} \aleph_{\alpha+1}$ for some sequence $\langle \alpha_\mu | \mu < \alpha' \rangle$ where $\alpha' = cf(\aleph_\alpha) < \aleph_\alpha$. Since $\aleph_{\alpha+1}$ is regular we can apply the preceding proof for each $\aleph_{\alpha+1}$ (inductively on $\mu$). Thus for each $\mu < \alpha'$ we can pick $r_\mu \in P$ and $\Lambda_\mu \subseteq \Gamma$ in the following way. We can assume that for previously defined $r_v$'s $(\nu < \mu) r_v \leq r_v'$ holds if $\nu' < \nu$. There is an $r \in P$ such that $r \leq r_v$ for all $\nu < \mu$. Then $r_\mu \leq r$, $\bar{\Lambda}_\mu \leq \aleph_{\alpha+1}$, and for each $r' \leq r_\mu$ and each $\xi < \aleph_{\alpha+1}$

$$(\exists p \in \Lambda_\mu)[p \cdot r' > 0 \wedge [p \

Then by Theorem 23.44, there exists an $\bar{r} \in P$ and a $\Lambda \subseteq \Gamma$ such that $\bar{r} \leq r$, $\bar{\Lambda} \leq \aleph_\alpha$ and

$(\forall r' \leq \bar{r})(\forall i \in I)(\exists p \in \Lambda)(\exists j < \aleph_\beta)[p \cdot r' > 0 \wedge [p \cdot \bar{r} \leq b_{ij} \vee p \cdot \bar{r} \leq -b].$

Since $0 < p \cdot \bar{r} \leq b$, we cannot have $p \cdot \bar{r} \leq -b.$

Therefore there exists an $\bar{r} \in P$ and a $\Lambda \subseteq \Gamma$ such that $\bar{r} \leq b$, $\bar{\Lambda} \leq \aleph_\alpha$, and

$(\forall r' \leq \bar{r})(\forall i \in I)(\exists p \in \Lambda)(\exists j < \aleph_\beta)[p \cdot r' > 0 \wedge p \cdot \bar{r} \leq b_{ij}].$

Hence $B$ is $(\aleph_\alpha, \aleph_\beta)$-splitable.

24. Easton’s Model

In this section we will consider the question of alternatives to the GCH. If $G: On \rightarrow On$ we wish to know for what choices of $G$

$$GCH_G \quad (\forall \alpha)[\overline{2^{\aleph_\alpha}} = \aleph_{G(\alpha)}]$$

will be consistent with the axioms of $ZF + AC$.

There are two results, provable in $ZF + AC$, that restrict the choice of $G$:

$$\alpha \leq \beta \rightarrow \overline{2^{\aleph_\alpha}} \leq \overline{2^{\aleph_\beta}}$$

and

$$(\forall \alpha)[cf(\overline{2^{\aleph_\alpha}}) > \aleph_\alpha] \quad (\text{König’s Theorem})$$

From these results we see that it is necessary that $G$ have the following properties.

1. $(\forall \alpha)(\forall \beta)[\alpha \leq \beta \rightarrow G(\alpha) \leq G(\beta)]$
2. $(\forall \alpha)[cf(\aleph_{G(\alpha)}) > \aleph_\alpha]$

Solovay conjectured that 1 and 2 are also sufficient. Solovay’s conjecture is at this time still an open question. Strong supporting evidence for the conjecture was established in 1964 by Easton who, using forcing techniques, proved that for any $G$ satisfying 1 and 2 there is a model of $ZF + AC$ in which the $GCH_G$ holds for regular cardinals.

In this section we will prove the existence of Easton’s models by showing that for each $G$ satisfying 1 and 2 there is a Boolean algebra $B$ such that $V^{(B)}$ is a $B$-valued model of $ZF + AC$ and in $V^{(B)}$

$$\llbracket (\forall \alpha)[\alpha \in \text{Reg} \rightarrow \overline{2^{\aleph_\alpha}} = \aleph_{G(\alpha)}] \rrbracket = 1$$

Throughout this section we assume that $V$ satisfies the GCH and the Strong Axiom

(ii) $q = \bigcup_{\alpha \in On} q^\alpha$

(iii) $\alpha \in \text{Reg} \rightarrow \bigcup_{\beta \leq \alpha} q^\beta < \aleph_\alpha$

(iv) $(\forall \gamma)(\forall \alpha)(\forall \eta) \neg [\langle 0, \gamma, \alpha, \eta \rangle \in q \land \langle 1, \gamma, \alpha, \eta \rangle \in q]$

2. $p \leq q \iff q \subseteq p$ for $p, q \in P$

3. $\mathbf{P} \triangleq \langle P, \leq \rangle$

Remark. Intuitively the conditions defining $P$ may be understood as follows. If $\langle \mathbf{M}, \mathbf{P}^\mathbf{M} \rangle$ is an elementary subsystem of $\langle V, \mathbf{P} \rangle$, then for each $\alpha \in \text{Reg}^\mathbf{M}$, $\mathbf{P}^\mathbf{M}$ adds $\aleph_G(\alpha)$-many subsets of $\aleph_\alpha$ to $\mathbf{M}$ (cf. the $\mathbf{P}$ used in the proof of Theorem 11.10). The additional requirements, in particular 1.iii, are necessary to assure that sets added at the $\alpha$th level do not affect the cardinalities at higher levels. Obviously, $\mathbf{P}$ is a proper class, and no $\mathbf{P}$ which is a set will suffice for our problem. Consequently the success of our efforts depends upon results of the preceding section and certain theorems that we must now prove.

From Definition 24.1 it is clear that each $q \in P$ uniquely determines its decomposition sequence $\langle q^\alpha | \alpha \in On \rangle$. So for each $q \in P$ we will use $q^\alpha$ to denote the $\alpha$th element of this decomposition sequence.

Our first result is simply a list of elementary properties of two families of subclasses of $P$:

$$\Gamma_\alpha \triangleq \{q \in
