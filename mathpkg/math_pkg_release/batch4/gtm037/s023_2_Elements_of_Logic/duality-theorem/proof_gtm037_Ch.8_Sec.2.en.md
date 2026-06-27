---
role: proof
locale: en
of_concept: duality-theorem
source_book: gtm037
source_chapter: "Chapter 8: Sentential Logic"
source_section: "2. Elements of Logic"
---
In the case of (i) and (ii) it is just necessary to apply the definition of the duality operator (Definition 8.32) to the sentences $(\varphi \wedge \psi)^{d}$ and $(\varphi \vee \psi)^{d}$ in order to see what combination of $\varphi^{d}$ and $\psi^{d}$ they are and then check that (i) and (ii) are tautologies. For example,

$$(\varphi \wedge \psi)^{d} = (\neg (\varphi \rightarrow \neg \psi))^{d} = \neg (\varphi \rightarrow \neg \psi)^{d}$$
$$= \neg (\neg \varphi^{d} \wedge (\neg \psi)^{d}) = \neg (\neg \varphi^{d} \wedge \neg \psi^{d})$$

and $\neg (\neg \varphi^{d} \wedge \neg \psi^{d})$ is tautologically equivalent to $\varphi^{d} \vee \psi^{d}$, which yields (i). The case for (ii) is similar.

(iii) follows by straightforward induction on the structure of $\varphi$.

For (iv): The proof proceeds by induction on the structure of $\varphi$. The base cases (atomic sentences $\langle s \rangle$, $\bot$, etc.) are verified directly from the definitions. For the inductive step, suppose (iv) holds for $\varphi$ and $\psi$ and consider $\varphi \rightarrow \psi$. Then by the definition of the duality operator and the induction hypothesis, one shows $f^{+}(\varphi \to \psi) = g^{+}(\neg(\varphi \to \psi)^{d})$. Hence the conclusion of (iv) holds for $\varphi \rightarrow \psi$ if it holds for $\varphi$ and for $\psi$. Thus (iv) holds.

We can derive (v) from (iv) using the completeness theorem. First assume $\Gamma \vdash \varphi$. Thus by the completeness theorem $\Gamma \models \varphi$. We shall now establish that $\{\neg \psi^d : \psi \in \Gamma\} \models \neg \varphi^d$. To this end, let $g$ be any model such that $g^{+} \neg \psi^d = 1$ for all $\psi \in \Gamma$. Define $fs = g^{+} \neg \langle s \rangle$ for all $s \in P$. By (iv), $f^{+} \psi = g^{+} \neg \psi^d$ for every sentence $\psi$. Hence $f$ is a model of $\Gamma$, and so $f^{+} \varphi = 1$. Therefore $g^{+} \neg \varphi^d = 1$. Since $g$ is arbitrary, $\{\neg \psi^d : \psi \in \Gamma\} \models \neg \varphi^d$. By the completeness theorem, $\{\neg \psi^d : \psi \in \Gamma\} \vdash \neg \varphi^d$. The converse is proved in exactly the same way; (v) follows.

The condition (vi) is a special case of (v). Concerning (vii), recall that $(\varphi \rightarrow \psi)^d = \neg \varphi^d \wedge \psi^d$. Hence $\vdash \neg (\varphi \rightarrow \psi)^d \leftrightarrow (\psi^d \rightarrow \varphi^d)$, so (vii) follows from (vi). Finally, (viii) follows from (vii) since $\vdash \chi \leftrightarrow \theta$ is equivalent to the conjunction of $\vdash \chi \rightarrow \theta$ and $\vdash \theta \rightarrow \chi$, for any sentences $\chi$ and $\theta$.
