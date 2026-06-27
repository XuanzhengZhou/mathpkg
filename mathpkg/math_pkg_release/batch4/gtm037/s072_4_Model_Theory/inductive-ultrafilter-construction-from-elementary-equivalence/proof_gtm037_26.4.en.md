---
role: proof
locale: en
of_concept: inductive-ultrafilter-construction-from-elementary-equivalence
source_book: gtm037
source_chapter: "26"
source_section: "4"
---

**Proof.** The construction proceeds by transfinite induction on $\gamma \leq 2^{|n|}$, maintaining seven inductive conditions. The proof continues from the three-case analysis established in the preceding sections.

**Case 2 (Limit ordinal).** For $\gamma$ a limit ordinal, the relations $F_\gamma$ and filters $D_\gamma$ are defined as the unions of the previous stages. By Lemma 26.36, $(F_\gamma, 0, D_\gamma)$ is $(n + |\gamma|)$-consistent over $n$. Moreover,
$$|F_0 \smallsetminus F_\gamma| = \left| \bigcup_{\xi < \gamma} (F_0 \smallsetminus F_\xi) \right| \leq \sum_{\xi < \gamma} |F_0 \smallsetminus F_\xi| \leq \sum_{\xi < \gamma} (n + |\xi|) \leq (n + |\gamma|) \cdot |\gamma| = n + |\gamma|.$$
Thus condition (1) holds for $\gamma$. Condition (2) holds trivially. For conditions (3) and (4), one may assume that the ranges of the involved sequences are finite, and then the conditions follow from the inductive hypothesis. Conditions (5)--(7) are not relevant to the limit case.

**Case 3 (Successor ordinal).** Let $\gamma = \beta + 1$ with $R_\beta = (0, a_\alpha)$. The construction proceeds in two sub-steps: first to ensure condition (4), then condition (3).

*Step 1 (Condition (4)).* For every formula $\varphi$ and every $c \in {}^\omega (\operatorname{Dmn} H_\beta \cup \{a_\alpha\})$ for which there exists $d \in \operatorname{Dmn} H_\beta \cup \{a_\alpha\}$ with $c_i = d$ for all but finitely many $i < \omega$, define
$$\Gamma_{\varphi c} = \{\delta < n : \mathfrak{A} \models \varphi [\langle c_i(\delta) : i < \omega \rangle]\}.$$
The number of such sets is bounded by
$$|\operatorname{Fmla}_{\mathfrak{L}}| \cdot \left( \sum_{m \in \omega} |\gamma|^m \right) \cdot |\gamma| = |\operatorname{Fmla}_{\mathfrak{L}}| \cdot |\gamma| \cdot \aleph_0 \leq n + |\gamma|,$$
using condition (2) for $\beta$.

*Step 2 (Condition (3)).* Assume $H_\beta \neq 0$. Let $\Theta$ consist of all pairs $(\varphi, c)$ such that $\varphi$ is a formula, $c \in {}^\omega \operatorname{Dmn} H_\beta$, and for some $d \in \operatorname{Dmn} H_\beta$ we have $|\{i : c_i \neq d\}| < \aleph_0$, and moreover
$$\{\delta < n : \mathfrak{A} \models \varphi[\langle c_i(\delta) : i < \omega \rangle_{a_\alpha(\delta)}^0]\} \in D'.$$
Then $0 \neq |\Theta| \leq n + |\beta|$. Enumerate $\Theta = \{(\varphi_\nu, c_\nu) : \nu < n + |\beta|\}$.

For any $\nu < n + |\beta|$, since
$$\{\delta < n : \mathfrak{A} \models \exists v_0 \varphi_\nu[\langle c_{\nu i}(\delta) : i < \omega \rangle]\} \in D' \supseteq D_\beta,$$
condition (4) for $\beta$ implies this set belongs to $D_\beta$. For each $x \in \operatorname{Dmn} H_\beta$, choose $d_x$ with $x H_\beta d_x$. By condition (3) for $\beta$,
$$\{\delta < n : \mathfrak{B} \models \exists v_0 \varphi_\nu[\langle d_{c_{\nu i}}(\delta) : i < \omega \rangle]\} \in D_\beta.$$

One then checks the hypotheses of Theorem 26.41 with the parameters $(n, m, F, D, \mathfrak{A}, \mu, a, \varphi)$ replaced by $(n, n + |\beta|, F', D', \mathfrak{B}, n + |\beta|, \langle d_{c_{\nu i}}(\delta) : \nu < n + |\beta|, i < \omega \rangle, \text{---})$.

**Verification of condition (3) for $\gamma$.** Suppose $x_i H_\gamma y_i$ for all $i < \omega$, let $\theta$ be any formula, and suppose
$$\{\delta < n : \mathfrak{A} \models \theta [\langle x_i(\delta) : i < \omega \rangle]\} \in D_\gamma.$$
Assuming $a_\alpha \notin \operatorname{Dmn} H_\beta$, we have $y_i = b$ whenever $x_i = a_\alpha$. To reformulate so that only $v_0$ receives the new value $a_\alpha(\delta)$, let $\theta'$ be obtained from $\theta$ by replacing each free occurrence of $v_0$ with a new variable $v_s$ and changing bound occurrences of $v_0$ to a still newer variable. Set $x' = x_{x_0}^s$ and $y' = y_{y_0}^s$, so that $x_i' H_\gamma y_i'$ and
$$\{\delta < n : \mathfrak{A} \models \theta' [\langle x_i'(\delta) : i < \omega \rangle]\} \in D_\gamma.$$

Let $X = \{i : x_i' = a_\alpha,\ v_i \text{ occurs in } \theta'\}$, and let $\psi$ be obtained from $\theta'$ by replacing $v_i$ with $v_0$ for each $i \in X$. Choose $w$ with $a_0 H_\beta w$, and define for each $i \in \omega$:
$$z_i = \begin{cases} x_i' & \text{if } x_i' \neq a_\alpha \text{ and } v_i \text{ occurs in } \theta', \\ a_0 & \text{otherwise,} \end{cases}$$
$$u_i = \begin{cases} y_i' & \text{if } x_i' \neq a_\alpha \text{ and } v_i \text{ occurs in } \theta', \\ w & \text{otherwise.} \end{cases}$$

By condition (4) for $\beta$,
$$\{\delta < n : \mathfrak{A} \models \varphi [\langle c_i(\delta) : i < \omega \rangle]\} \in D_\beta.$$
By condition (3) for $\beta$,
$$\{\delta < n : \mathfrak{B} \models \varphi [\langle d_i(\delta) : i < \omega \rangle]\} \in D_\beta \subseteq D_\gamma,$$
as required.

**Completion of the induction.** This completes the inductive definition. Set $\mathfrak{p} = 2^{|n|}$ and $E = D_\mathfrak{p}$. By conditions (1) and (7), $E$ is an ultrafilter over $n$. Define
$$K = \{([a]_E, [b]_E) : a H_\mathfrak{p} b\}.$$
By conditions (5) and (6), $K$ has domain $^n A / E$ and range $^n B / E$.

**Well-definedness of $K$.** Suppose $a H_\mathfrak{p} b$ and $a' H_\mathfrak{p} b'$. Then $a H_\gamma b$ and $a' H_\gamma b'$ for some $\gamma < \mathfrak{p}$. Hence:
\begin{align*}
[a]_E = [a']_E &\iff \{\delta < n : a_\delta = a'_\delta\} \in E \\
&\iff \{\delta < n : \mathfrak{A} \models (v_0 = v_1)[a_\delta, a'_\delta]\} \in E \\
&\iff \{\delta < n : \mathfrak{A} \models (v_0 = v_1)[a_\delta, a'_\delta]\} \in D_\gamma \quad \text{(by condition (4))} \\
&\iff \{\delta < n : \mathfrak{B} \models (v_0 = v_1)[b_\delta, b'_\delta]\} \in D_\gamma \quad \text{(by condition (3))} \\
&\iff [b]_E = [b']_E.
\end{align*}
This establishes that $K$ is well-defined and equality-preserving. $\square$
