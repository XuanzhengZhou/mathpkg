---
role: proof
locale: en
of_concept: composition-of-homotopic-chain-maps
source_book: gtm004
source_chapter: "IV"
source_section: "3. Homotopy"
---

# Proof of Composition of Homotopic Chain Maps

**Lemma 3.3.** Let $\varphi \simeq \psi : C \rightarrow D$ and $\varphi' \simeq \psi' : D \rightarrow E$, then

$$\varphi' \varphi \simeq \psi' \psi : C \rightarrow E.$$

*Proof.* Let $\Sigma : \varphi \simeq \psi$ and $T : \varphi' \simeq \psi'$, i.e.,

$$\psi - \varphi = \partial\Sigma + \Sigma\partial, \qquad \psi' - \varphi' = \partial T + T\partial.$$

First consider $\varphi'\psi - \varphi'\varphi$. Since $\varphi'$ is a chain map, we have $\varphi'\partial = \partial\varphi'$, and therefore

$$\varphi'\psi - \varphi'\varphi = \varphi'(\psi - \varphi) = \varphi'(\partial\Sigma + \Sigma\partial) = \varphi'\partial\Sigma + \varphi'\Sigma\partial = \partial(\varphi'\Sigma) + (\varphi'\Sigma)\partial.$$

Hence $\varphi'\Sigma : C \rightarrow E$ is a homotopy from $\varphi'\varphi$ to $\varphi'\psi$.

Next, since $\psi$ is a chain map, $\partial\psi = \psi\partial$, we obtain

$$\psi'\psi - \varphi'\psi = (\psi' - \varphi')\psi = (\partial T + T\partial)\psi = \partial T\psi + T\partial\psi = \partial(T\psi) + T\psi\partial = \partial(T\psi) + (T\psi)\partial.$$

Thus $T\psi : C \rightarrow E$ is a homotopy from $\varphi'\psi$ to $\psi'\psi$.

Adding the two differences:

$$\psi'\psi - \varphi'\varphi = (\psi'\psi - \varphi'\psi) + (\varphi'\psi - \varphi'\varphi) = \partial(T\psi) + (T\psi)\partial + \partial(\varphi'\Sigma) + (\varphi'\Sigma)\partial = \partial(T\psi + \varphi'\Sigma) + (T\psi + \varphi'\Sigma)\partial.$$

Therefore $T\psi + \varphi'\Sigma$ is a homotopy from $\varphi'\varphi$ to $\psi'\psi$, proving the lemma. $\square$
