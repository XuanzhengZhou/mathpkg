---
role: exercise
locale: en
chapter: "2"
section: "2.6"
exercise_number: 51
---

(COMPLEX EXPLICIT DEFINITION). For each elementary function $f$ introduce a symbol $F_f$, and for each elementary relation $R$ a symbol $\mathcal{R}_R$. Also let $N_0, N_1, \ldots$ be some more symbols, and $v_0, v_1, \ldots$ variables. For logical symbols we take $\exists, \forall, \mu, \neg, \lor, \land, \rightarrow, \leftrightarrow, =$. Special symbols: $(,), <$. We define terms and formulas simultaneously and recursively:

(1) $v_i$ is a term;
(2) if $f$ is an $m$-ary elementary function and $\sigma_0, \ldots, \sigma_{m-1}$ are terms, then $F_f(\sigma_0, \ldots, \sigma_{m-1})$ is a term;
(3) $N_i$ is a term;
(4) if $R$ is an $m$-ary elementary relation and $\sigma_0, \ldots, \sigma_{m-1}$ are terms, then $\mathcal{R}_R(\sigma_0, \ldots, \sigma_{m-1})$ is a formula;
(5) if $\sigma, \tau$ are terms, then $\sigma = \tau$ and $\sigma < \tau$ are formulas;
(6) if $\varphi, \psi$ are formulas, then $\neg \varphi$, $(\varphi \lor \psi)$, $(\varphi \land \psi)$, $(\varphi \rightarrow \psi)$, $(\varphi \leftrightarrow \psi)$ are formulas;
(7) if $\varphi$ is a formula and $v_i$ is a variable, then $\exists v_i \varphi$, $\forall v_i \varphi$, and $\mu v_i \varphi$ are formulas.

Show that the set of all functions and relations definable by such formulas (with the natural interpretation) coincides with the class of elementary functions and relations.
