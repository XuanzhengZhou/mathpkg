---
role: proof
locale: en
of_concept: theorem-172-lob-theorem
source_book: gtm037
source_chapter: "Part 3"
source_section: "Decidable and Undecidable Theories"
---

There clearly is an elementary function $f$ such that for any formula $\psi$ and any $m \in \omega$, $f(g^+ \psi, m) = g^+ \psi(\mathbf{m})$. Let $\mathbf{O}$ be a binary operation symbol of $\mathcal{L}$ which represents $f$, in the sense of Definition 17.1. Let $a = g^+ (\Pr\mathbf{O}(v_0, v_0) \rightarrow \varphi)$, and let $\psi$ be the sentence $\Pr\mathbf{O}(a, a) \rightarrow \varphi$. Thus if $\chi$ is the formula $\Pr\mathbf{O}(v_0, v_0) \rightarrow \varphi$, then $f(g^+ \chi, g^+ \chi) = g^+ \psi$. Hence

(1) $\Gamma \models \mathbf{O}(a, a) = \Delta g^+ \psi$;

(2) $\Gamma \models \psi \rightarrow (\Pr\Delta g^+ \psi \rightarrow \varphi)$ by (1), definition of $\psi$;

(3) $\Gamma \models \Pr\Delta g^+ (\psi \rightarrow (\Pr\Delta g^+ \psi \rightarrow \varphi))$ by (2), condition (i);

(4) $\Gamma \models \Pr\Delta g^+ \psi \rightarrow \Pr\Delta g^+ (\Pr\Delta g^+ \psi \rightarrow \varphi)$ by (3), condition (iii);

(5) $\Gamma \models \Pr\Delta g^+ (\Pr\Delta g^+ \psi \rightarrow \varphi) \rightarrow (\Pr\Delta g^+ \Pr\Delta g^+ \psi \rightarrow \Pr\Delta g^+ \varphi)$ by condition (iii);

(6) $\Gamma \models \Pr\Delta g^+ \psi \rightarrow \Pr\Delta g^+ \Pr\Delta g^+ \psi$ by condition (ii);

(7) $\Gamma \models \psi \rightarrow \Pr\Delta g^+ \varphi$ by (1)-(6);

(8) $\Gamma \models \Pr\Delta g^+ (\psi \rightarrow \Pr\Delta g^+ \varphi)$ by (7), condition (i);

(9) $\Gamma \models \Pr\Delta g^+ \psi \rightarrow \Pr\Delta g^+ \Pr\Delta g^+ \varphi$ by (8), condition (iii);

(10) $\Gamma \models \psi \rightarrow \Pr\Delta g^+ \Pr\Delta g^+ \varphi$ by (1), (9);

(11) $\Gamma \models \Pr\Delta g^+ \varphi \rightarrow \varphi$ by hypothesis;

(12) $\Gamma \models \Pr\Delta g^+ (\Pr\Delta g^+ \varphi \rightarrow \varphi)$ by (11), condition (i);

(13) $\Gamma \models \Pr\Delta g^+ \Pr\Delta g^+ \varphi \rightarrow \Pr\Delta g^+ \varphi$ by (12), condition (iii);

(14) $\Gamma \models \psi \rightarrow \Pr\Delta g^+ \varphi$ by (10), (13);

(15) $\Gamma \models \psi \rightarrow \varphi$ by (14), (11);

(16) $\Gamma \models \psi$ by (15), definition of $\psi$ (since $\psi \leftrightarrow (\Pr\mathbf{O}(a,a) \rightarrow \varphi) \leftrightarrow (\Pr\Delta g^+ \psi \rightarrow \varphi)$);

(17) $\Gamma \models \Pr\Delta g^+ \psi$ by (16), condition (i);

(18) $\Gamma \models \varphi$ by (16), (17), modus ponens.
