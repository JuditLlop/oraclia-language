# Oraclia · Nucli del sistema

Oraclia és un prototip de llenguatge simbòlic i sistema de lectura relacional en desenvolupament.

Aquest document estableix el seu nucli conceptual: els principis que orienten el llenguatge, la seva estructura i el seu ús. No descriu tota l’arquitectura interna ni constitueix una gramàtica tancada.

## 1. Nucli conceptual

Oraclia treballa amb un alfabet estable de 21 símbols, cadascun amb un nucli de moviment propi.

Els símbols actuen com a operadors que permeten descriure i explorar relacions, estats, transicions i transformacions dins d’un procés.

Aquests nuclis orienten la lectura, però no constitueixen un diccionari de significats fixos. Un símbol no determina, per si sol, una interpretació.

El significat emergeix de les relacions entre símbols, de la forma que adopten, del context i de la trajectòria que construeixen al llarg del temps.

Un símbol pot modificar què es torna visible, quina diferència apareix, quines relacions entren en joc o com es transforma una configuració.

**Cada símbol conserva un nucli propi. El significat de la lectura emergeix de les relacions i del context.**

## 2. Alfabet simbòlic i camps de referència

Oraclia utilitza 21 unitats simbòliques representades amb Unicode:

| Símbol | Camp | Codi Unicode |
|---|---|---|
| ∞ | Camp obert, potencial | U+221E |
| † | Punt de referència / orientació | U+2020 |
| ◉ | Focus | U+25C9 |
| ⇡ | Ascens / progrés | U+21E1 |
| ▭ | Límit | U+25AD |
| ○ | Pausa | U+25CB |
| → | Direcció | U+2192 |
| 〰 | Cicle | U+3030 |
| ✧ | Activació | U+2727 |
| ? | Indeterminació | U+003F |
| ⊘ | Interrupció | U+2298 |
| ☲ | Contrast | U+2632 |
| ∆ | Canvi | U+2206 |
| ÷ | Tancament | U+00F7 |
| ≈ | Ajust | U+2248 |
| ✛ | Material / concret | U+271B |
| ⇤ | Retirada | U+21E4 |
| ≋ | Retorn | U+224B |
| () | Dada literal | U+0028 + U+0029 |
| Y | Bifurcació | U+0059 |
| ≡ | Síntesi | U+2261 |

La unitat `()` està formada per dos caràcters Unicode, però constitueix una sola unitat simbòlica d’Oraclia.

Aquests camps orienten la lectura de cada símbol; el significat concret emergeix de les seves relacions i del context.

L’alfabet és estable, però el comportament dels símbols és relacional i contextual.

Un mateix símbol pot participar en configuracions diferents segons:

- Els altres símbols actius.
- Les relacions entre ells.
- L’ordre i la disposició.
- La forma que produeixen.
- La trajectòria.
- El context concret de lectura.

El context no converteix els símbols en elements arbitraris: la lectura ha de mantenir una relació recognoscible amb els seus nuclis de moviment.

## 3. Relació, forma i transformació

La unitat principal de lectura és la configuració de símbols i les relacions que s’hi produeixen.

Oraclia observa:

- Quins camps simbòlics estan actius.
- Com es relacionen.
- Quina forma produeixen.
- Què es manté.
- Què apareix.
- Què desapareix.
- Què es transforma al llarg del temps.

Una configuració no s’ha de reduir necessàriament a un únic símbol. Una mateixa constel·lació pot produir formes diferents segons les relacions i la disposició.

Un patró no és simplement una repetició d’elements: és una forma de transformació que reapareix.

Aquestes relacions es poden desplegar en formes d’expressió diferents: una explicació, una pregunta, una escena, un diàleg o una imatge. Cada forma pot fer visibles aspectes diferents del moviment explorat.

## 4. Indeterminació

Oraclia no ha de forçar una lectura quan no hi ha prou estructura per sostenir-la.

Si una configuració només es pot justificar afegint supòsits sense suport en el context, el sistema pot mantenir-la com a no resolta.

Aquesta indeterminació no significa que no hi hagi pes, relació, moviment o significació. Significa que encara no hi ha prou diferenciació per construir una lectura fonamentada.

**Millor no saber que deformar.**

## 5. Relació amb la persona

La lectura que Oraclia proposa és situada, provisional i revisable.

Els símbols no representen identitats, diagnòstics ni estats psicològics fixos.

Oraclia no defineix la persona, no substitueix la seva decisió ni converteix una lectura provisional en una identitat permanent.

La persona sempre pot corregir o desmentir la lectura. Quan això passa, Oraclia revisa la seva proposta.

Una trajectòria recurrent no equival a afirmar «aquesta persona és així».

**La persona conserva el criteri.**

## 6. Àmbit d’ús

Oraclia es pot utilitzar per explorar i representar:

- Fases i transicions d’un procés.
- Relacions i canvis de configuració.
- Trajectòries i recurrències.
- Moviments dins d’una conversa o situació.
- Estructures personals, organitzatives o computacionals.
- Relacions que es volen comunicar entre persones i sistemes d’IA.

No s’utilitza per:

- Fer diagnòstics.
- Predir el futur.
- Atribuir essències personals.
- Substituir decisions humanes.
- Presentar interpretacions psicològiques, espirituals o esotèriques com si fossin veritats.

## 7. Estat del prototip

Oraclia està en desenvolupament.

El sistema explora una gramàtica relacional basada en un alfabet estable, nuclis de moviment, formes, dinàmiques i transformacions.

Aquest document proposa una formulació conjunta dels nuclis català i castellà. No constitueix una teoria definitiva ni una gramàtica tancada.
