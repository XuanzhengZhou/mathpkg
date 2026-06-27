---
role: exercise
locale: en
chapter: "8"
section: "2"
exercise_number: "8.55e"
---

The axiom system for three-valued logic consists of the following axiom schemas:

(A1) $\varphi \rightarrow (\psi \rightarrow \varphi)$

(A2) $(\varphi \rightarrow \psi) \rightarrow [(\psi \rightarrow \chi) \rightarrow (\varphi \rightarrow \chi)]$

(A3) $(\neg \varphi \rightarrow \neg \psi) \rightarrow (\psi \rightarrow \varphi)$

(A4) $((\varphi \rightarrow \neg \varphi) \rightarrow \varphi) \rightarrow \varphi$

(A5) $\{\varphi \rightarrow [\varphi \rightarrow (\psi \rightarrow \chi)]\} \rightarrow \{[\varphi \rightarrow (\varphi \rightarrow \psi)] \rightarrow [\varphi \rightarrow (\varphi \rightarrow \chi)]\}$

(A6) $[\varphi \rightarrow (\varphi \rightarrow \neg \varphi)] \rightarrow \{[\neg \psi \rightarrow (\neg \psi \rightarrow \psi)] \rightarrow (\varphi \rightarrow \psi)\}$

(A7) $\varphi \rightarrow [(\varphi \rightarrow \psi) \rightarrow \psi]$

(A8) $\{[\varphi \rightarrow (\varphi \rightarrow \neg \varphi)] \rightarrow \neg [\varphi \rightarrow (\varphi \rightarrow \neg \varphi)]\} \rightarrow \varphi$

Detachment (modus ponens) is the only rule of inference.

Define for each basic sentential symbol $s$:

$$fs = 1 \quad \text{if } \langle s \rangle \in \Delta,$$
$$fs = 0 \quad \text{if } \neg \langle s \rangle \in \Delta,$$
$$fs = 2 \quad \text{otherwise.}$$

Prove by induction on $\varphi$ that

$$f^+ \varphi = 1 \quad \text{implies } \varphi \in \Delta,$$
$$f^+ \varphi = 0 \quad \text{implies } \neg \varphi \in \Delta,$$
$$f^+ \varphi = 2 \quad \text{implies } \varphi \notin \Delta \text{ and } \neg \varphi \notin \Delta.$$

To prove the analog of 8.29 (completeness/consistency), note that if $\Gamma \vdash \varphi$ then $\Gamma \cup \{\varphi \rightarrow (\varphi \rightarrow \neg \varphi)\}$ is consistent.

(e) Define the appropriate notion of functional completeness for three-valued logic. Show that our connectives $\neg$ and $\rightarrow$ are not functionally complete.
