---
role: proof
locale: en
of_concept: inconsistency-of-gamma-union-delta
source_book: gtm037
source_chapter: "10"
source_section: "Elements of Logic"
---

**(i) $\Rightarrow$ (ii).** By 10.88 we obtain $m \in \omega$ and $\varphi \in {}^m\Delta$ such that
$$\Gamma \vdash \varphi_0 \land \dots \land \varphi_{m-1} \rightarrow \neg\forall v_0(v_0 = v_0).$$
We may assume $m \neq 0$. Since $\Gamma \vdash \forall v_0(v_0 = v_0)$, we easily obtain using a suitable tautology
$$\Gamma \vdash \neg\varphi_0 \lor \dots \lor \neg\varphi_{m-1}.$$

**(ii) $\Rightarrow$ (i).** Since $\Gamma \vdash \neg(\varphi_0 \land \dots \land \varphi_{m-1})$ and
$\Gamma \cup \Delta \vdash \varphi_0 \land \dots \land \varphi_{m-1}$, the set $\Gamma \cup \Delta$ is inconsistent.
