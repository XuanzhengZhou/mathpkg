---
role: proof
locale: en
of_concept: vaughts-theorem-on-atomic-countable-models
source_book: gtm037
source_chapter: "4"
source_section: "4.1"
---

For each $n \in \omega$ let

$$\Delta_n = \{\varphi \in \mathrm{Fmla}^n_{\mathcal{L}} : \neg \varphi \text{ is } n\text{-atomic or } n\text{-atomless over } \Gamma\}.$$

To apply the omitting types theorem (27.4), we must verify that $\Gamma$ locally omits each $\Delta_n$. Assume that $n \in \omega$, $\psi \in \mathrm{Fmla}^n_{\mathcal{L}}$, and that $\Gamma \cup \{\exists v_0 \cdots \exists v_{n-1} \psi\}$ has a model.

If $\psi$ is $n$-atomless over $\Gamma$, then $\neg \psi \in \Delta_n$ and the desired conclusion is obvious: $\Gamma \cup \{\exists v_0 \cdots \exists v_{n-1} (\psi \land \neg \psi)\}$ is inconsistent, so the condition holds vacuously after adjusting. More precisely, if $\psi$ is $n$-atomless, then $\neg \psi$ is $n$-atomic or $n$-atomless (indeed, $\neg \psi \in \Delta_n$), and we have $\Gamma \models \exists v_0 \cdots \exists v_{n-1} (\psi \land \neg \neg \psi)$, but the proper verification uses that we can take $\varphi = \neg \psi \in \Delta_n$ with $\Gamma \cup \{\exists v_0 \cdots \exists v_{n-1} (\psi \land \neg \varphi)\}$ inconsistent.

Otherwise $\psi$ is not $n$-atomless over $\Gamma$. Then there exists an $n$-atomic formula $\varphi$ over $\Gamma$ such that $\Gamma \models \varphi \rightarrow \psi$. Consequently $\Gamma \models \neg \psi \rightarrow \neg \varphi$. Since $\varphi$ is $n$-atomic, $\neg \varphi \in \Delta_n$. Moreover $\Gamma \cup \{\exists v_0 \cdots \exists v_{n-1} (\psi \land \neg \neg \varphi)\}$ has a model (any model of $\Gamma \cup \{\exists v_0 \cdots \exists v_{n-1} \varphi\}$ works, since $\Gamma \models \varphi \rightarrow \psi$). Thus in either case the hypothesis of 27.4 is satisfied.

By the omitting types theorem, $\Gamma$ has a countable model $\mathfrak{A}$ omitting each $\Delta_n$. For any $n$-tuple $a \in {}^n A$, let $\theta$ be the conjunction (or any formula in the $n$-type of $a$). If no $n$-atomic formula over $\Gamma$ is satisfied by $a$, then for every $n$-atomic $\varphi$, $\mathfrak{A} \models \neg \varphi[a]$. Thus the $n$-type of $a$ is contained in $\Delta_n$, contradicting that $\mathfrak{A}$ omits $\Delta_n$. Therefore $a$ satisfies some $n$-atomic formula over $\Gamma$. If $a$ does not satisfy any $n$-atomic formula, then all $n$-atomic formulas are negated by $a$, meaning $a$ realizes $\Delta_n$, impossible. Hence every $n$-tuple satisfies either an $n$-atomic formula over $\Gamma$ or an $n$-atomless formula over $\Gamma$.
