---
role: proof
locale: en
of_concept: theorem-13-4-decidability-omega-s-0
source_book: gtm037
source_chapter: "13"
source_section: "Decidable and Undecidable Theories"
---

We work in an effectivized language with a unary operation symbol $s$ and an individual constant $\mathbf{O}$. By induction we set

$$\Delta 0 = \mathbf{O}; \quad \Delta(m + 1) = s\Delta m; \quad s^1 = s; \quad s^{m+1} = ss^m; \quad m = \Delta m.$$

The terms of this language are just of two kinds: $s^m\alpha$ for some variable $\alpha$, and $m$ for some $m \in \omega$, where $s^0\alpha$ is just $\alpha$. A formula will be called \emph{basic} if it has one of the following forms:

$$s^m v_i = \sigma, \quad \sigma \text{ a term not involving } v_i;$$
$$\mathbf{O} = \mathbf{O}.$$

Clearly there is an effective method for recognizing when a formula is basic. Let $\Gamma_1$ be the set of all sentences which hold in $(\omega, s, 0)$.

We now show that any formula is effectively equivalent under $\Gamma_1$ to a Boolean combination of basic formulas. Proceeding by induction on formulas, the only nontrivial case is the existential quantifier. Suppose $\exists \alpha \varphi$ is to be reduced, and by the induction hypothesis $\varphi$ is already a Boolean combination of basic formulas.

Since

$$\exists \alpha (\psi \vee \chi) \leftrightarrow (\exists \alpha \psi \vee \exists \alpha \chi)$$

is logically valid, we may by Theorem 13.3 assume that $\varphi$ is a conjunction of basic formulas and their negations. Now in general if $\alpha$ does not occur in $\psi$ then

$$\exists \alpha (\psi \wedge \chi) \leftrightarrow \psi \wedge \exists \alpha \chi$$

is logically valid. Hence we may assume that each conjunct of $\varphi$ actually involves $\alpha$. Thus we may assume that $\exists \alpha \varphi$ is the formula

$$\exists \alpha [s^{k_0} \alpha = \sigma_0 \wedge \dots \wedge s^{k_{m-1}} \alpha = \sigma_{m-1} \wedge \neg(s^{k_m} \alpha = \sigma_m) \wedge \dots \wedge \neg(s^{k_{n-1}} \alpha = \sigma_{n-1})]$$

where $0 \leq m \leq n > 0$, and $\sigma_0, \dots, \sigma_{n-1}$ do not involve $\alpha$. Noting that $\sigma = \tau$ is equivalent under $\Gamma_1$ to $s\sigma = s\tau$, if we let $l$ be the maximum of $k_0, \dots, k_{n-1}$ we easily see that $\exists \alpha \varphi$ is equivalent to a formula of the form

$$\exists \alpha [s^l \alpha = \tau_0 \wedge \dots \wedge s^l \alpha = \tau_{m-1} \wedge \neg(s^l \alpha = \tau_m) \wedge \dots \wedge \neg(s^l \alpha = \tau_{n-1})]$$

where $\tau_0, \dots, \tau_{n-1}$ do not involve $\alpha$. In turn, this formula is obviously equivalent to

$$\exists \alpha [\neg(\alpha = 0) \wedge \dots \wedge \neg(\alpha = \Delta(l - 1)) \wedge \alpha = \tau_0 \wedge \dots \wedge \alpha = \tau_{m-1} \wedge \neg(\alpha = \tau_m) \wedge \dots \wedge \neg(\alpha = \tau_{n-1})].$$

If $m > 0$, this is equivalent to

$$\tau_0 = \tau_1 \wedge \dots \wedge \tau_0 = \tau_{m-1} \wedge \neg(\tau_0 = 0) \wedge \dots \wedge \neg(\tau_0 = \Delta(l - 1)) \wedge \neg(\tau_0 = \tau_m) \wedge \dots \wedge \neg(\tau_0 = \tau_{n-1}),$$

which is a quantifier-free combination of basic formulas. If $m = 0$, it is equivalent to the negation of a finite disjunction of basic formulas.

Thus every formula is effectively equivalent to a quantifier-free combination of basic formulas. Since it is clearly decidable whether a quantifier-free combination of basic formulas holds in $(\omega, s, 0)$, the theory $\Gamma_1$ is decidable.

It is clearly possible to choose our original language $\mathcal{L}_1$ to be elementarily effective (see p. 190). By examining the above proofs it is clear that in Theorems 13.5 and 13.6 the decision method then is elementary, i.e., the set $g^{+*} \Gamma$ is elementary for the $\Gamma$'s of 13.5 and 13.6. Similar remarks apply to our other two decidability results of this chapter.
