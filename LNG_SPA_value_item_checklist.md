# LNG SPA / GSA value-item checklist project

Purpose: a repeatable process that takes one LNG sale and purchase agreement (SPA) and decomposes it into discrete, checkable value items covering price, start, end, yearly flexibilities and optionalities, plus the supporting terms (damages, credit, logistics) that change the value of those five groups.

Terminology note: the source documents are LNG SPAs. "GSA" usually denotes a pipeline gas sales agreement; the checklist works for both, but for DES/CIF or pipeline deals adjust category I (delivery, shipping, title) accordingly.

Sources for the pre-filled entries: the two decks in this folder (`cheniere_sabine_pass_spa_standalone_economic_terms.pptx`; `driftwood_lng_spa_economic_terms_comparison_formula_signature_updated.pptx`). "Not reviewed in deck" means the decks did not cover the item; it does not mean the contract lacks it.

## Workflow

1. Intake. One row of identity data per contract (category A). Store the contract PDF and note whether figures are redacted in the public filing.
2. Extraction. Work through the checklist top to bottom, one copy of the Template sheet per contract. Record values verbatim (especially price formulas), with a clause reference for every entry, and set Status on each row.
3. Status discipline. Use exactly one of: Extracted (value recorded from the text); Redacted (clause found, number hidden); Not found (searched, absent); Not reviewed (not yet checked); N/A (structurally inapplicable).
4. Epistemic rules. Never guess a redacted number; model redacted constants as scenario inputs. Distinguish fact (visible text), inference (drafting implies) and unknown. "Absent from a summary" is not "absent from the contract".
5. Comparison. Once two or more contracts are extracted, populate the matrix (items as rows, contracts as columns) and RAG-score: RED = visible economic difference; AMBER = similar framework, unresolved caveats; GREEN = no material difference detected. ACQ is a scale input, not a RAG-scored difference.
6. Valuation mapping. Feed extracted items into a five-part object model: variable commodity leg (index x volume); fixed capacity leg (UFC/MSC or embedded Xy, escalation); non-lifting logic (cancellation, suspension, charge survival, take-or-pay); optionality set (extensions, destination, seasonal, elections); adjustments (credit support, liability caps, FM tails). Every item carries a Term-type tag: Cash-flow rows feed the base DCF strip; Option rows require option-adjusted valuation (Monte Carlo, least-squares Monte Carlo or spread-option methods), never static DCF alone; Risk-structural rows feed credit, enforceability and governance adjustments. Hedgeability tags (Curve / Spread / Residual) build the hedge map: Curve items hedge against liquid benchmarks, Spread items as location, time or freight spreads, and Residual items go on the basis-risk register.
7. Enforceability screen. Before assigning value to any Option row (destination freedom, cargo rejection, deferral, price review), check legal and competition-law enforceability (item F13). If exercise is uncertain, haircut or exclude the option value.

## Checklist

Status codes: [E] Extracted, [R] Redacted, [NF] Not found, [NR] Not reviewed, [NA] Not applicable.

### A. Identity and status
- [ ] A1 Seller entity (legal name; SPV or sponsor)
- [ ] A2 Buyer entity (legal name; affiliate status)
- [ ] A3 Guarantor / credit support provider (who actually carries the credit)
- [ ] A4 Signature date and effective date (fixes vintage of constants and CPI base)
- [ ] A5 Conditions precedent: substance (FID, FNTP, approvals)
- [ ] A6 CP long-stop deadline and termination consequence
- [ ] A7 Project linkage (train/plant definitions, DFCD triggers)
- [ ] A8 Related agreements (twin SPAs, terminal or infrastructure exhibits)

### B. Term: start ("start from")
- [ ] B1 Start trigger definition (DFCD / first commercial delivery)
- [ ] B2 Early volumes before full start (early cargoes, bridging volumes, early windows)
- [ ] B3 Start-delay rights (termination or deferral after delay; FM long-stop caps)
- [ ] B4 Ramp / start-up quantity (level and duration, e.g. 50% ACQ pre-Second DFCD)

### C. Term: end and extensions ("ending")
- [ ] C1 Base term (length and trigger)
- [ ] C2 End-date mechanics (fixed expiry vs completion of quantities)
- [ ] C3 Extension options: number and length
- [ ] C4 Extension election party and notice deadline
- [ ] C5 Extension conditions (approvals, export authorisations, utilisation)
- [ ] C6 Extension-period price (same formula, reset, or new redacted constants)
- [ ] C7 Early termination triggers (default, prolonged FM, delay)

### D. Volume and yearly flexibility ("yearly flexibilities")
- [ ] D1 ACQ / AACQ definition, size and adjustment mechanics
- [ ] D2 Tranche structure (annual vs seasonal tranches)
- [ ] D3 Delivery shape (ratable vs seasonally weighted)
- [ ] D4 Scheduling process (ADP, NDS, windows, change rights)
- [ ] D5 Cargo-lot rounding (round-up/down; not a swing right)
- [ ] D6 Maintenance reduction cap (% per year; cumulative cap)
- [ ] D7 Inspection and other reduction caps (% and the base they apply to)
- [ ] D8 Buyer downward flexibility (DQT, cancellation volumes)
- [ ] D9 Make-up / carry-forward rights
- [ ] D10 Upward flexibility (UQT, excess cargoes, spot rights)
- [ ] D11 Operational tolerance per cargo and its payment treatment
- [ ] D12 First and final year proration
- [ ] D13 Imbalance / penalty charges (basis and rates for under / over-delivery)

### E. Price
- [ ] E1 Price architecture (single formula vs commodity + capacity; fixed component separate or embedded)
- [ ] E2 Commodity index or indices (HH, JKM, TTF, Brent, blends)
- [ ] E3 Slope / multiplier / weights (values or redaction status)
- [ ] E4 Constants: adders and discounts (US$/MMBtu; redaction status)
- [ ] E5 Floor and cap (greater-of structures are embedded options)
- [ ] E6 Fixed capacity component (UFC/MSC formula, or X0/Xy embedded)
- [ ] E7 Escalation (CPI weight; CPI0 base-year convention)
- [ ] E8 FX conversion (source and fixing time; ECB vs Bloomberg/Reuters 16:00 London)
- [ ] E9 Pricing month / averaging window definition
- [ ] E10 Index fallback / market disruption
- [ ] E11 Price review / reopener (trigger, frequency, scope)
- [ ] E12 Late-payment interest basis
- [ ] E13 S-curve / slope bands (band thresholds and slopes; common in oil-linked SPAs)
- [ ] E14 Index lag convention (the L in slope x index(t-L))

### F. Optionality ("optionalities")
- [ ] F1 Term extension options (cross-reference C3-C6)
- [ ] F2 Cargo cancellation right (notice, fee, which charges survive)
- [ ] F3 Suspension right (fee mechanics, duration)
- [ ] F4 Capacity-charge survival on non-lifting (does MSC or the fixed leg continue?)
- [ ] F5 Destination flexibility / diversion rights
- [ ] F6 Alternate source delivery right and conditions
- [ ] F7 Upstream FM HH-basis election (replacement cargo mitigant)
- [ ] F8 Seasonal / tranche election rights
- [ ] F9 Multiple-SPA coordination (cross-default, consolidation, shared caps)
- [ ] F10 Cargo deferral / rescheduling right (time-spread option on delivery windows)
- [ ] F11 Reload / re-export rights
- [ ] F12 Diversion cost and profit-sharing on diverted cargoes
- [ ] F13 Enforceability of option rights (legal / competition-law constraints)

### G. Non-delivery and remedies economics
- [ ] G1 Take-or-pay / shortfall basis (% of ACQ; period basis annual / quarterly / monthly / cargo; reference price)
- [ ] G2 Cover damages formula
- [ ] G3 Seller DoP formula and caps
- [ ] G4 Damages reference price (CSP vs CSP minus UFC)
- [ ] G5 Mitigation / resale mechanics (in-tank resale)
- [ ] G6 FM effect on fixed charges

### H. Credit and structure
- [ ] H1 Buyer credit support (guaranty, LC, TNW triggers, timing)
- [ ] H2 Guaranty cap (amount or redaction)
- [ ] H3 Seller credit support
- [ ] H4 Liability caps (aggregate, per event)
- [ ] H5 Lender / direct agreement provisions
- [ ] H6 Assignment scope and consent

### I. Delivery, quality and FM
- [ ] I1 Delivery point / incoterm
- [ ] I2 Title and risk transfer
- [ ] I3 Shipping responsibility; tanker approval and change rights
- [ ] I4 Laytime / demurrage and port services
- [ ] I5 Quality spec and off-spec remedies
- [ ] I6 Measurement framework
- [ ] I7 FM architecture and shortage allocation (pro-rata)
- [ ] I8 DES-specific delivery terms (seller shipping / discharge obligations, demurrage allocation; n/a for FOB)

### J. Governance and other
- [ ] J1 Invoicing and payment terms
- [ ] J2 Taxes
- [ ] J3 Disputes (forum; consolidation across twin SPAs)
- [ ] J4 Sanctions / trade law
- [ ] J5 ESG / emissions / HSEC obligations
- [ ] J6 Confidentiality

## Holder / valuation inputs (companion sheet, not contract terms)

These complete the valuation identity V = sum of D(0,t) x E[(P_use - P_contract) x Q_lift - costs] but come from the holder and the market, not from the SPA. They live on the Holder_Inputs sheet and must be kept separate from extracted contract facts: freight / charter rate (Baltic, Spark, freight futures); fuel and boil-off; canal and port costs; regas capacity and variable fees (terminal tariff publications); terminal access, slots and storage; downstream use value (P_use); benchmark forward curves (Brent/JCC, HH, TTF, JKM); FX and unit conversions (EUR/USD; MWh to MMBtu); discounting convention (hurdle rate vs collateralised SOFR/OIS); tax treatment; credit / CVA inputs (IFRS 13 non-performance risk); volatility, correlation and seasonality calibration.

## Improvements over the initial deck lists

The decks already carried a good inventory (price architecture, UFC/MSC vs embedded Xy, charge survival, extension options, seasonal shape, credit support, damages reference price, RAG and fact/inference/unknown discipline). This checklist adds or makes explicit:

1. Make-up / carry-forward and upward flexibility (UQT, excess cargoes): absent from both decks, yet core "yearly flexibility" items.
2. Take-or-pay percentage and shortfall reference price as a quantified row, not only an architecture note.
3. Price review / reopener clause: not covered in either deck; material for long-term value.
4. Floors and caps as a dedicated row (the Driftwood greater-of floors are embedded options).
5. Extension price separated from the extension option itself (option on term and on price are different things).
6. FX fixing time and source as a standing row (the ECB vs 16:00 London difference generalises).
7. Pricing month / averaging window as a standing row, with the asymmetric-redaction warning.
8. Index fallback / market disruption.
9. FM effect on fixed charges (Cheniere-style capacity legs during FM; 455-day style deferral caps).
10. First/final year proration and per-cargo operational tolerance as explicit rows.
11. Guarantor identity captured at intake (A3), since credit exposure sits with the support provider.
12. A uniform five-value Status code per row, so "not found", "not reviewed" and "redacted" are never conflated.
13. One taxonomy covering both templates: HH-plus-capacity (Cheniere) and index-blend with floors (Driftwood), so the next contract slots in regardless of style.

## Second-pass improvements (from LNG Contract Valuation and Hedging.docx, 5 Jul 2026)

14. New term rows: imbalance / penalty charges (D13); S-curve / slope bands (E13); index lag convention (E14); cargo deferral / rescheduling (F10); reload / re-export rights (F11); diversion cost and profit-sharing (F12); enforceability of option rights (F13); DES-specific delivery terms (I8). G1 enriched with the take-or-pay period basis (annual / quarterly / monthly / cargo).
15. Term-type tags on every item (Cash-flow / Option / Risk-structural / Context), implementing the doc's central dichotomy: cash-flow terms feed static DCF; option terms force option-adjusted valuation.
16. Hedgeability tags (Curve / Spread / Residual / n/a) so the checklist doubles as a hedge map and basis-risk register.
17. Enforceability rule as workflow step 7: no full option value for rights that are not clearly enforceable (JFTC / European Commission context on destination clauses).
18. Holder_Inputs companion sheet separating holder-side valuation inputs from contract terms, per the doc's three-box discipline (market inputs / contractual rules / model choices).

## Files

- `LNG_SPA_value_item_checklist.xlsx`: ReadMe, blank Template sheet (85 items, one copy per new contract; Term-type and Hedgeability columns), Matrix sheet pre-filled for the eight contracts (BG, Gas Natural Fenosa, GAIL, Total, Vitol, Gunvor, Shell SPA1, Shell SPA2) using only deck-sourced facts, and Holder_Inputs (valuation inputs that are not contract terms).
- This file: methodology and the checklist in portable form.
- `checklist_data.py`: machine-readable single source of truth (85 rows, tags, matrix pre-fill, holder inputs). Imported by `app.py` and by `scripts/build_checklist_workbook.py`, which rebuilds the xlsx from it.
- `app.py`, page "Value-item checklist": interactive version; work a contract with status tracking and CSV export/resume, filter the eight-contract matrix, and consult holder inputs. Run with `streamlit run app.py`.
