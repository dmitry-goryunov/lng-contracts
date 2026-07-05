# cheniere sabine pass spa standalone economic terms(2)

Source file: `cheniere_sabine_pass_spa_standalone_economic_terms(2).pptx`

Converted from PowerPoint to Markdown. Slide order, visible text and tables have been preserved as a readable text version.

---

## Slide 1: Cheniere Sabine Pass LNG SPAs

Cheniere Sabine Pass LNG SPAs

Standalone economic-term comparison and valuation fields

Contracts reviewed: BG, Gas Natural Fenosa, GAIL, Total

Main focus: HH-linked pricing plus fixed liquefaction/capacity economics

Output: standalone fields, RAG logic and modelling implications

05 July 2026

---

## Slide 2: Executive read

Executive read

Cheniere contracts require dedicated fields because fixed liquefaction economics are recovered in different ways.

All four contracts are FOB LNG SPAs with Henry Hub-linked commodity pricing.

BG and Gas Natural use a separate Unit Fixed Charge and Monthly Sales Charge, i.e. explicit capacity-charge mechanics.

GAIL and Total embed the fixed/liquefaction component inside CSP using Xy, with different CPI weights.

Implication for the template

Add a dedicated section for price architecture and capacity-payment mechanics. The core valuation problem is how fixed liquefaction economics are recovered and whether charges survive cancellation, suspension, force majeure or non-lifting.

GREEN: all HH-linked base commodity index

RED: price architecture

RED: cancellation / suspension mechanics

NO RAG: ACQ size

---

## Slide 3: Contract universe

Contract universe

ACQ is shown but not RAG-scored; size is buyer-specific commercial volume, not a drafting difference.

| Contract | Seller | Buyer | Signature / effective date | Visible ACQ | RAG |
| --- | --- | --- | --- | --- | --- |
| BG | Sabine Pass Liquefaction | BG Gulf Coast LNG | 25 Oct 2011 | 182.5m MMBtu/yr | NO RAG |
| Gas Natural Fenosa | Sabine Pass Liquefaction | Gas Natural Aprovisionamientos | 21 Nov 2011 | 182.5m MMBtu/yr | NO RAG |
| GAIL | Sabine Pass Liquefaction | GAIL (India) Limited | 11 Dec 2011 | 182.5m MMBtu/yr | NO RAG |
| Total | Sabine Pass Liquefaction | Total Gas & Power North America | 14 Dec 2012 | 104.75m MMBtu/yr = 91.25m AT + 13.5m ST | NO RAG |

Observation: Total is structurally different because ACQ is the sum of an Annual Tranche and a Seasonal Tranche. The Seasonal Tranche is 13.5m MMBtu, approximately 12.9% of Total ACQ.

AT = Annual Tranche

ST = Seasonal Tranche

ACQ rows unscored

---

## Slide 4: Cheniere-specific economic fields

Cheniere-specific economic fields

These fields are required to analyse how each agreement separates or embeds liquefaction economics.

| New field | Why it is needed | RAG logic |
| --- | --- | --- |
| Price architecture | Distinguishes CSP-only from CSP + UFC + Monthly Sales Charge | RED |
| Unit Fixed Charge / UFC formula | BG and Gas Natural have a separate CPI-linked fixed component | RED |
| Monthly Sales Charge | Capacity reservation charge payable monthly, not cargo-by-cargo | RED |
| X0 / Xy fixed component | GAIL and Total embed the fixed component in CSP | RED |
| CPI escalation weight | GAIL uses 15%; Total uses 11.5%; BG/GNF use UFC formula | RED |
| Charge survives cancellation / suspension? | Core economic distinction for cancelled or suspended cargoes | RED |
| Early / bridging / seasonal volumes | BG has Early Cargoes; GAIL has Bridging Volumes; Total has seasonal tranche | RED |
| Damages reference price | BG/GNF refer to CSP minus UFC; GAIL/Total use CSP-based mechanics | RED |

Retain standard SPA fields for CPs, term, delivery point, title/risk, ADP, quality, FM, credit and taxes. Add the fields above before comparing Cheniere agreements or other US liquefaction-style LNG SPAs.

---

## Slide 5: Visible price formulas

Visible price formulas

All four use 1.15 × HH, but the fixed/liquefaction component is recovered differently.

| Contract | Visible formula | Fixed / capacity component | RAG |
| --- | --- | --- | --- |
| BG | CSP = 1.15 × HH | UFCy = 1.9125 + (0.3375 × CPIy / CPI0); MSC = UFC × Q / 12 | RED |
| Gas Natural Fenosa | CSP = 1.15 × HH | UFCy = 2.1525 + (0.3375 × CPIy / CPI0); MSC = UFC × Q / 12 | RED |
| GAIL | CSP = (1.15 × HH) + Xy | Xy = (0.85 + 0.15 × CPI(y-1) / CPI0) × X0; X0 = US$3.00/MMBtu | RED |
| Total | CSP = (1.15 × HH) + Xy | Xy = (0.885 + 0.115 × CPI(y-1) / CPI0) × X0; X0 = US$3.00/MMBtu | RED |

RAG is RED because formula architecture differs, not because each contract has a different HH multiplier. The HH multiplier is common at 1.15.

For modelling: separate variable gas index exposure from fixed-capacity economics before calculating margin, cancellation value or DoP/cover damages.

---

## Slide 6: Liquefaction-margin recovery

Liquefaction-margin recovery

This is the main economic distinction across the Cheniere agreements.

BG / Gas Natural Fenosa

GAIL / Total

Cargo price
CSP = 1.15 × HH

Capacity charge
UFC × Q / 12

Cargo price
CSP = 1.15 × HH + Xy

Fixed component
inside CSP

Economic consequence: BG/GNF capacity payments can continue irrespective of the cargo actually taken. GAIL/Total embed the fixed element in the cargo price, so cancellation/suspension mechanics must be read differently.

Standalone section: Price architecture and capacity-payment mechanics

---

## Slide 7: Term and extension mechanics

Term and extension mechanics

Base term is broadly common; extension mechanics have drafting differences and approvals constraints.

| Item | BG | Gas Natural Fenosa | GAIL | Total | RAG |
| --- | --- | --- | --- | --- | --- |
| Base term | 20 years from DFCD | 20 years from DFCD | 20 years from DFCD | 20 years from DFCD | GREEN |
| Extension | Buyer may extend up to 10 years for any portion of ACQ | Similar maximum extension term | Buyer may extend up to 10 years | Buyer may extend up to 10 years | AMBER |
| Extension condition | Minimum facility utilisation / approvals and export authorisations | Similar | Approvals; no same export-authorisation wording visible in snippet | Approvals incl. LNG export licences | AMBER |
| Delayed DFCD termination | Buyer right after delay; seller has corresponding mechanics | Similar | Similar, but first-window timing differs | Similar; 455-day FM deferral cap visible | AMBER |

Note: extension mechanics generally use a buyer election up to 10 years, subject to utilisation and approval constraints.

---

## Slide 8: Volume, shape and maintenance: percentage view

Volume, shape and maintenance: percentage view

ACQ itself is unscored; numerical caps are compared as percentage of ACQ where possible.

| Item | BG | Gas Natural Fenosa | GAIL | Total | RAG |
| --- | --- | --- | --- | --- | --- |
| ACQ size | 182.5m MMBtu | 182.5m MMBtu | 182.5m MMBtu | 104.75m MMBtu | NO RAG |
| Delivery shape | Even / ratable | Even / ratable | Even / ratable | Annual Tranche + Seasonal Tranche | RED |
| Seasonal share | n/a | n/a | n/a | 13.5m / 104.75m = 12.9% of ACQ | RED |
| Major maintenance cap | 6% per year; 30% initial term | 6% per year; 30% initial term | 6% per year; 30% initial term | 6% per year; 30% initial term | GREEN |
| Inspection cap | 8.3% per year; 16.6% initial term | 8.3% per year; 16.6% initial term | 8.3% per year; 16.6% initial term | 8.3% of annual/seasonal base; 17% initial term | AMBER |

Method applied: ACQ is not RAG-scored; the percentage of ACQ is used for caps and other numeric fields where that creates a like-for-like economic comparison.

---

## Slide 9: Cancellation, suspension and early-volume mechanics

Cancellation, suspension and early-volume mechanics

These are economically central in Cheniere because fixed charges may survive non-lifting.

| Item | BG | Gas Natural Fenosa | GAIL | Total | RAG |
| --- | --- | --- | --- | --- | --- |
| Buyer cancellation / suspension | Cancellation right; Monthly Sales Charge continues | Cancellation right; Monthly Sales Charge continues | No equivalent seen in reviewed snippets | Suspension right with Suspension Fee | RED |
| Early / bridging volumes | Early Cargoes; pre-commercial cargo pricing seen | No equivalent highlighted | Bridging Volumes | Early First Window Period | RED |
| Capacity payment if cargo cancelled | Yes: MSC continues | Yes: MSC continues | n/a in same form | Suspension fee mechanics | RED |
| FM affecting LNG tanker / discharge terminal | Express clause | Express clause | Express clause; terminal wording narrower | Express clause | AMBER |

Do not value cancellation as simply “no cargo, no price”. In BG/GNF, capacity reservation payments are a separate cashflow stream.

For Total, suspension requires a separate Suspension Fee analysis rather than a shortfall-only treatment.

---

## Slide 10: Damages and remedy fields to add

Damages and remedy fields to add

The relevant reference price differs where fixed charges are separated from CSP.

| Economic item | BG | Gas Natural Fenosa | GAIL | Total | RAG |
| --- | --- | --- | --- | --- | --- |
| Buyer shortfall / cover damages | CSP-based; cancellation interacts with MSC | Same broad architecture | CSP-based cover damages | CSP-based plus suspension / idling-cost wording | RED |
| Seller DoP | Formula refers to CSP minus UFC for replacement comparison | Same broad concept | CSP/Cover Damages mechanics | CSP plus additional cost wording | RED |
| Monthly / capacity charge in remedies | MSC continues / is separately invoiced | MSC continues / separately invoiced | Not separate | Suspension Fee separate | RED |
| Off-spec LNG remedies | Similar SPA architecture | Similar | Similar | Similar | AMBER |

New rows to add to master comparison: damages reference price; capacity-charge survival; seller DoP adjustment for UFC; suspension-fee calculation; invoice type for capacity charges.

---

## Slide 11: Delivery and logistics

Delivery and logistics

Core FOB structure is common across the four agreements, but some infrastructure-specific schedules and exhibits differ.

| Item | BG | Gas Natural Fenosa | GAIL | Total | RAG |
| --- | --- | --- | --- | --- | --- |
| Delivery point / incoterm | FOB Sabine Pass Facility | FOB Sabine Pass Facility | FOB Sabine Pass Facility | FOB Sabine Pass Facility | GREEN |
| Buyer shipping | Buyer provides tankers | Same | Same | Same | GREEN |
| Destination flexibility | Buyer may market to any destination, subject to agreement | Same broad wording | Same broad wording | Same broad wording | GREEN |
| Alternate source delivery | Permitted with buyer consent and conditions | Similar; Gulf Coast affiliate carve-out visible | Similar | Similar | AMBER |
| Infrastructure exhibits | Terminal/cooperation/tug/transport exhibits visible | Not same set highlighted | Not same set highlighted | Not same set highlighted | AMBER |

Keep standard logistics rows, and add a Cheniere-specific field for linked infrastructure exhibits where they affect rights, costs or facility access.

---

## Slide 12: Credit, financing and bankability fields

Credit, financing and bankability fields

These need full clause-by-clause checks before they are treated as equivalent.

| Item | BG | Gas Natural Fenosa | GAIL | Total | RAG |
| --- | --- | --- | --- | --- | --- |
| Buyer credit support | Credit support clause present | Present | Present | Present | AMBER |
| Parent / guaranty mechanics | Buyer-specific | Buyer-specific | Buyer-specific | Buyer-specific | AMBER |
| Lender / direct agreement mechanics | Project-finance style provisions | Similar | Similar | Similar | AMBER |
| Limitations on liability | Caps/limits present | Similar | Similar | Similar | AMBER |
| Representations / business practices | Present | Present | Present | Present | AMBER |

Action: do not assume credit-support equivalence from the template. Buyer-specific parent support, LC triggers and credit ratings should be extracted separately.

---

## Slide 13: First-pass RAG summary

First-pass RAG summary

High-confidence economic differences are concentrated in pricing, capacity charges, volume shape and non-lifting rights.

| Economic item | BG | Gas Natural Fenosa | GAIL | Total | RAG |
| --- | --- | --- | --- | --- | --- |
| Signature / effective date | 25 Oct 2011 | 21 Nov 2011 | 11 Dec 2011 | 14 Dec 2012 | NO RAG |
| Base commodity index | HH | HH | HH | HH | GREEN |
| Price architecture | HH + UFC/MSC | HH + UFC/MSC | HH + Xy | HH + Xy | RED |
| CPI escalation weight | UFC formula | UFC formula | 15% of X0 | 11.5% of X0 | RED |
| Delivery shape | Ratable | Ratable | Ratable | Annual + seasonal | RED |
| Buyer non-lifting right | Cancellation | Cancellation | Not same | Suspension | RED |
| Maintenance percentages | 6%/30%; 8.3%/16.6% | Same | Same | Inspection base differs; 17% cumulative | AMBER |
| DoP / damages basis | CSP-UFC interaction | CSP-UFC interaction | CSP | CSP + suspension/idling elements | RED |

---

## Slide 14: Recommended valuation object model

Recommended valuation object model

Separate cargo economics from capacity economics before computing value, hedge and risk.

1. Variable commodity leg
HH exposure: 1.15 × HH × loaded MMBtu

2. Fixed liquefaction leg
UFC/MSC or Xy component, CPI escalated

3. Non-lifting logic
Cancellation, suspension, MSC survival, suspension fee

Inputs to store per contract:

ACQ and tranche split; DFCD and term; extension volume; HH multiplier; UFC/X0/Xy formula; CPI base; monthly charge formula; cancellation/suspension right; damage reference price; FM/capacity-charge reduction; credit support; delivery profile.

Output metrics:

Gross margin by leg; fixed-capacity recovery; hedge exposure to HH and CPI; optionality/cancellation exposure; DoP/cover damages under stress cases; credit-adjusted PV.

---

## Slide 15: Caveats and next steps

Caveats and next steps

This is an economic comparison; it is not a legal blackline.

| Priority | Follow-up check | Reason |
| --- | --- | --- |
|  | Extract buyer credit-support thresholds and LC mechanics | Buyer-specific credit economics may be material. |
|  | Blackline BG vs Gas Natural for UFC and MSC survival provisions | The UFC base differs visibly; remedy/cancellation interaction matters. |
|  | Read GAIL Bridging Volumes and Total suspension fee in full | Potentially material transition-period economics. |
|  | Extract full DoP / cover damages formulas | Reference price differs where UFC is separate. |
|  | Add Cheniere-specific fields to the LNG SPA comparison template | Without them, the table understates capacity-payment economics. |

Main structural addition: add “Price architecture and capacity-payment mechanics” before the pricing RAG table.
