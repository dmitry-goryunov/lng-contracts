"""LNG SPA value-item checklist: single source of truth.

Generated from the two comparison decks in this repo plus improvements from
'LNG Contract Valuation and Hedging.docx' (5 Jul 2026). Used by app.py and by
scripts/build_checklist_workbook.py. Pre-filled values come only from the decks;
redacted values are shown as [***] and must never be guessed.
"""

NRD = "Not reviewed in deck"

# (id, cat, item, record, clause, why, ragC, ragD, bg, gnf, gail, total, vitol, gunvor, s1, s2)
R = []
def a(*t): R.append(t)

CAT_A = "A. Identity and status"
a("A1", CAT_A, "Seller entity", "Legal name; SPV or sponsor", "Preamble", "Recourse and project risk sit with the SPV, not the sponsor",
  "GREEN", "GREEN", "Sabine Pass Liquefaction, LLC", "Sabine Pass Liquefaction, LLC", "Sabine Pass Liquefaction, LLC", "Sabine Pass Liquefaction, LLC",
  "Driftwood LNG LLC", "Driftwood LNG LLC", "Driftwood LNG LLC", "Driftwood LNG LLC")
a("A2", CAT_A, "Buyer entity", "Legal name; affiliate status", "Preamble", "Determines credit risk and guarantee need",
  "AMBER", "AMBER", "BG Gulf Coast LNG", "Gas Natural Aprovisionamientos", "GAIL (India) Limited", "Total Gas & Power North America",
  "Vitol Inc.", "Gunvor Singapore Pte Ltd", "Shell NA LNG LLC", "Shell NA LNG LLC")
a("A3", CAT_A, "Guarantor / credit support provider", "Named provider and form of support", "Credit support clause", "Actual credit exposure is to the support provider",
  "AMBER", "RED", "Buyer-specific; terms not extracted in deck", "Buyer-specific; terms not extracted in deck", "Buyer-specific; terms not extracted in deck", "Buyer-specific; terms not extracted in deck",
  "Named guarantor / TNW / LC mechanics", "Named guarantor; guaranty cap defined, amount redacted", "Generic acceptable credit support", "Generic acceptable credit support")
a("A4", CAT_A, "Signature / effective date", "Both dates if different", "Preamble / signature page", "Fixes vintage of price constants and CPI base",
  "N/A", "N/A", "25 Oct 2011", "21 Nov 2011", "11 Dec 2011", "14 Dec 2012",
  "2 Jun 2021", "27 May 2021", "29 Jul 2021", "29 Jul 2021")
a("A5", CAT_A, "Conditions precedent: substance", "FID, FNTP, approvals", "CP article", "Contract may never start; value is conditional",
  "AMBER", "AMBER", "Present; not compared in deck", "Present; not compared in deck", "Present; not compared in deck", "Present; not compared in deck",
  "FID-based CP; same concept, drafting differs", "FID-based CP; same concept, drafting differs", "FID-based CP; same concept, drafting differs", "FID-based CP; same concept, drafting differs")
a("A6", CAT_A, "CP long-stop deadline", "Date and termination consequence", "CP article", "Free option against the counterparty until the deadline",
  None, "AMBER", NRD, NRD, NRD, NRD,
  "31 Jul 2022", "31 Dec 2022 (later; effort wording also differs)", "Not stated in deck", "Not stated in deck")
a("A7", CAT_A, "Project linkage", "Train/plant definitions; DFCD triggers", "Definitions", "Start and ramp depend on project milestones, not calendar dates",
  "AMBER", "AMBER", "DFCD-based; 20y term runs from DFCD", "DFCD-based; 20y term runs from DFCD", "DFCD-based; 20y term runs from DFCD", "DFCD-based; 455-day FM deferral cap visible",
  "First/Second DFCD structure; express post-CP pipeline FNTP effort; possible Plant 2 cancellation wording", "First/Second DFCD structure", "First/Second DFCD structure", "First/Second DFCD structure")
a("A8", CAT_A, "Related agreements", "Twin SPAs; terminal / infrastructure exhibits", "Recitals / exhibits", "Cross-contract effects on capacity, liability and disputes",
  "AMBER", "RED", "Terminal/cooperation/tug/transport exhibits visible", "Not same exhibit set highlighted in deck", "Not same exhibit set highlighted in deck", "Not same exhibit set highlighted in deck",
  "None found", "None found", "Twin SPA with SPA2; coordination clause, separate caps", "Twin SPA with SPA1; coordination clause, separate caps")

CAT_B = "B. Term: start"
a("B1", CAT_B, "Start trigger definition", "DFCD / first commercial delivery definition", "Definitions / term article", "Start of obligations is event-driven; drives PV timing",
  "GREEN", "GREEN", "DFCD per definitions", "DFCD per definitions", "DFCD per definitions", "DFCD per definitions",
  "First DFCD", "First DFCD", "First DFCD", "First DFCD")
a("B2", CAT_B, "Early volumes before full start", "Early cargoes, bridging volumes, early windows", "Start-up provisions", "Pre-COD cargoes can carry different price and flex terms",
  "RED", None, "Early Cargoes; pre-commercial cargo pricing seen", "None highlighted in deck", "Bridging Volumes", "Early First Window Period",
  NRD, NRD, NRD, NRD)
a("B3", CAT_B, "Start-delay rights", "Termination / deferral after delay; FM long-stop caps", "Term article", "Downside protection and walk-away optionality",
  "AMBER", "AMBER", "Buyer right after DFCD delay; seller has corresponding mechanics", "Similar", "Similar; first-window timing differs", "Similar; 455-day FM deferral cap visible",
  "Project-delay termination protection; possible Second DFCD / Plant 2 cancellation wording", "Project-delay termination protection", "Project-delay termination protection", "Project-delay termination protection")
a("B4", CAT_B, "Ramp / start-up quantity", "Level and duration", "Quantity article", "Reduced early volumes change early-year cashflows",
  None, "GREEN", NRD, NRD, NRD, NRD,
  "78.255m MMBtu/yr = 50% ACQ pre-Second DFCD (5.1.3(a))", "78.255m MMBtu/yr = 50% ACQ (5.1.3(a))", "26.085m MMBtu/yr = 50% ACQ (5.1.3(a))", "52.17m MMBtu/yr = 50% ACQ (5.1.3(a))")

CAT_C = "C. Term: end and extensions"
a("C1", CAT_C, "Base term", "Length and trigger", "Term article", "Core duration of cashflows",
  "GREEN", "GREEN", "20 years from DFCD", "20 years from DFCD", "20 years from DFCD", "20 years from DFCD",
  "10 years from First DFCD (4.1)", "10 years from First DFCD (4.1)", "10 years from First DFCD (4.1.1)", "10 years from First DFCD (4.1.1)")
a("C2", CAT_C, "End-date mechanics", "Fixed expiry vs completion of quantities", "Term article", "Tail value and last-year proration",
  None, None, NRD, NRD, NRD, NRD, NRD, NRD, NRD, NRD)
a("C3", CAT_C, "Extension options: number and length", "e.g. 2 x 5 years", "Term article", "Buyer-held term optionality",
  "AMBER", "RED", "Buyer may extend up to 10 years for any portion of ACQ", "Similar maximum extension term", "Buyer may extend up to 10 years", "Buyer may extend up to 10 years",
  "None found", "None found", "2 x 5-year buyer-elected extensions (4.1.2); up to 20y total", "2 x 5-year buyer-elected extensions (4.1.2); up to 20y total")
a("C4", CAT_C, "Extension election and notice", "Electing party; notice deadline", "Term article", "Option exercise boundary; affects option value",
  "AMBER", "AMBER", "Buyer elects; notice mechanics not extracted", "Buyer elects; notice mechanics not extracted", "Buyer elects; notice mechanics not extracted", "Buyer elects; notice mechanics not extracted",
  "n/a", "n/a", "Buyer elects; deadline not extracted", "Buyer elects; deadline not extracted")
a("C5", CAT_C, "Extension conditions", "Approvals, export authorisations, utilisation", "Term article", "Conditions can make the option unexercisable",
  "AMBER", None, "Minimum facility utilisation; approvals and export authorisations", "Similar", "Approvals; export-authorisation wording not visible", "Approvals incl. LNG export licences",
  "n/a", "n/a", "Not extracted", "Not extracted")
a("C6", CAT_C, "Extension-period price", "Same formula, reset, or new constants", "Price article", "The option is on price as well as term",
  None, "RED", "Not extracted", "Not extracted", "Not extracted", "Not extracted",
  "n/a", "n/a", "9.1.2 / 9.1.3: same visible JKM form; constants redacted; do not assume equal to base", "9.1.2 / 9.1.3: same visible TTF form; constants redacted; do not assume equal to base")
a("C7", CAT_C, "Early termination triggers", "Default, prolonged FM, delay", "Termination article", "Truncation risk on the value",
  "AMBER", "AMBER", "Delayed-DFCD termination rights", "Similar", "Similar", "Similar", "Project-delay termination; other triggers not reviewed", "Project-delay termination; other triggers not reviewed", "Project-delay termination; other triggers not reviewed", "Project-delay termination; other triggers not reviewed")

CAT_D = "D. Volume and yearly flexibility"
a("D1", CAT_D, "ACQ / AACQ", "Size, unit, adjustment mechanics", "Quantity article", "Scale input for all value calculations (not RAG-scored)",
  "N/A", "N/A", "182.5m MMBtu/yr", "182.5m MMBtu/yr", "182.5m MMBtu/yr", "104.75m MMBtu/yr = 91.25m AT + 13.5m ST",
  "156.51m MMBtu/yr, ~3 mtpa (5.1.1); AACQ framework", "156.51m MMBtu/yr (5.1.1); AACQ framework", "52.17m MMBtu/yr, ~1 mtpa (5.1.1)", "104.34m MMBtu/yr, ~2 mtpa (5.1.1)")
a("D2", CAT_D, "Tranche structure", "Annual vs seasonal tranches", "Quantity article", "Seasonal tranches carry different market value",
  "RED", "RED", "Single annual quantity", "Single annual quantity", "Single annual quantity", "Annual Tranche + Seasonal Tranche (ST = 12.9% of ACQ)",
  "None", "None", "Two-tranche winter structure (see D3)", "Two-tranche winter structure (see D3)")
a("D3", CAT_D, "Delivery shape", "Ratable vs seasonally weighted", "Scheduling article", "Winter weighting changes hedge and price exposure",
  "RED", "RED", "Even / ratable", "Even / ratable", "Even / ratable", "Annual + seasonal shape",
  "Even and ratable (5.3)", "Even and ratable (5.3)", "50-60% of AACQ scheduled Oct-Mar (5.3)", "50-60% of AACQ scheduled Oct-Mar (5.3)")
a("D4", CAT_D, "Scheduling process", "ADP, NDS, windows, change rights", "Scheduling article", "Operational flexibility hides here",
  None, "AMBER", "ADP process; standard", "ADP process; standard", "ADP process; standard", "ADP process; standard",
  "ADP/NDS common process", "ADP/NDS common process", "ADP/NDS; shape constraints matter", "ADP/NDS; shape constraints matter")
a("D5", CAT_D, "Cargo-lot rounding", "Round-up / round-down mechanics", "Quantity article", "Volume noise, not a swing right",
  None, "GREEN", NRD, NRD, NRD, NRD,
  "Round-up/down; not a swing right", "Round-up/down; not a swing right", "Round-up/down; not a swing right", "Round-up/down; not a swing right")
a("D6", CAT_D, "Maintenance reduction cap", "% per year; cumulative cap", "Quantity article", "Seller-held volume reduction option",
  "GREEN", "GREEN", "6%/yr; 30% initial term", "6%/yr; 30% initial term", "6%/yr; 30% initial term", "6%/yr; 30% initial term",
  "7.5%/yr; 25% over 6 years", "7.5%/yr; 25% over 6 years", "7.5%/yr; 25% over 6 years", "7.5%/yr; 25% over 6 years")
a("D7", CAT_D, "Inspection / other reduction caps", "% and the base it applies to", "Quantity article", "Further seller reductions; base definition matters",
  "AMBER", None, "8.3%/yr; 16.6% initial term", "8.3%/yr; 16.6% initial term", "8.3%/yr; 16.6% initial term", "8.3% of annual/seasonal base; 17% cumulative",
  "Not separately identified in deck", "Not separately identified in deck", "Not separately identified in deck", "Not separately identified in deck")
a("D8", CAT_D, "Buyer downward flexibility", "DQT, cancellation volumes", "Quantity article", "Buyer volume put; core yearly flexibility",
  "RED", "GREEN", "Cargo cancellation right (see F2)", "Cargo cancellation right (see F2)", "No equivalent seen in reviewed snippets", "Suspension right (see F3)",
  "No broad discretionary swing right detected", "No broad discretionary swing right detected", "No broad discretionary swing right detected", "No broad discretionary swing right detected")
a("D9", CAT_D, "Make-up / carry-forward", "Rights to recover or defer volumes", "Quantity article", "Softens take-or-pay; time value of volumes",
  None, None, "Not identified in decks; check full text", "Not identified in decks; check full text", "Not identified in decks; check full text", "Not identified in decks; check full text",
  "Not identified in decks; check full text", "Not identified in decks; check full text", "Not identified in decks; check full text", "Not identified in decks; check full text")
a("D10", CAT_D, "Upward flexibility", "UQT, excess cargoes, spot rights", "Quantity article", "Buyer call on extra volume",
  None, None, "Not identified in decks; check full text", "Not identified in decks; check full text", "Not identified in decks; check full text", "Not identified in decks; check full text",
  "Not identified in decks; check full text", "Not identified in decks; check full text", "Not identified in decks; check full text", "Not identified in decks; check full text")
a("D11", CAT_D, "Operational tolerance", "+/- per cargo; payment treatment", "Delivery / measurement", "Settlement noise; treatment of tolerance quantities",
  None, "AMBER", NRD, NRD, NRD, NRD,
  "Concept common; payment details redacted", "Concept common; payment details redacted", "Concept common; payment details redacted", "Concept common; payment details redacted")
a("D12", CAT_D, "First / final year proration", "Part-year quantity treatment", "Quantity article", "Edge-year cashflows",
  None, "GREEN", NRD, NRD, NRD, NRD,
  "Same first/final year treatment", "Same first/final year treatment", "Same first/final year treatment", "Same first/final year treatment")
a("D13", CAT_D, "Imbalance / penalty charges", "Charge basis and rates for under / over-delivery", "Quantity / payment articles", "Standard cash-flow template driver; affects invoiced quantity economics",
  None, None, "Not identified in decks; check full text", "Not identified in decks; check full text", "Not identified in decks; check full text", "Not identified in decks; check full text",
  "Not identified in decks; check full text", "Not identified in decks; check full text", "Not identified in decks; check full text", "Not identified in decks; check full text")

CAT_E = "E. Price"
a("E1", CAT_E, "Price architecture", "Single formula vs commodity + capacity; fixed separate or embedded", "Price article", "Determines which cashflows survive non-lifting",
  "RED", "RED", "CSP + separate UFC / Monthly Sales Charge", "CSP + separate UFC / Monthly Sales Charge", "Single CSP with embedded fixed Xy", "Single CSP with embedded fixed Xy",
  "Single blended formula: multiplier over sum of legs", "Single blended formula: separately weighted legs", "Single-index JKM formula", "Single-index TTF formula")
a("E2", CAT_E, "Commodity index / indices", "HH, JKM, TTF, Brent, blends", "Price article", "Market exposure and hedge instruments",
  "GREEN", "RED", "Henry Hub", "Henry Hub", "Henry Hub", "Henry Hub",
  "JKM + TTF", "JKM + TTF", "JKM only", "TTF only")
a("E3", CAT_E, "Slope / multiplier / weights", "Values or redaction status", "Price article", "First-order value driver",
  "GREEN", "RED", "1.15 x HH", "1.15 x HH", "1.15 x HH", "1.15 x HH",
  "CSP = [***] x (JKM CSP + TTF CSP) (9.1.1)", "CSP = ([***]% JKM CSP) + ([***]% TTF CSP) (9.1.1)", "[***]% x JKM; slope redacted (9.1.1)", "[***]% x TTF; slope redacted (9.1.1)")
a("E4", CAT_E, "Constants: adders / discounts", "US$/MMBtu values; redaction status", "Price article", "First-order value driver",
  "N/A", "AMBER", "n/a in base CSP (fixed leg via UFC)", "n/a in base CSP (fixed leg via UFC)", "n/a in base CSP (fixed leg via Xy)", "n/a in base CSP (fixed leg via Xy)",
  "US$[***]/MMBtu deductions; redacted", "US$[***]/MMBtu deductions; redacted", "US$[***]/MMBtu deduction; redacted", "US$[***]/MMBtu deduction; redacted")
a("E5", CAT_E, "Floor / cap", "Levels; greater-of structures", "Price article", "Embedded options in the price formula",
  None, "AMBER", "None visible in deck", "None visible in deck", "None visible in deck", "None visible in deck",
  "Greater-of floors inside each leg; US$[***] floor redacted", "Greater-of floors inside each leg; US$[***] floor redacted", "Greater-of: ([***]% x JKM - US$[***]) vs US$[***] floor", "Greater-of: ([***]% x TTF - US$[***]) vs US$[***] floor")
a("E6", CAT_E, "Fixed capacity component", "UFC/MSC formula or X0/Xy", "Price / quantity articles", "Fixed leg size and invoicing route",
  "RED", "N/A", "UFCy = 1.9125 + (0.3375 x CPIy/CPI0); MSC = UFC x Q/12", "UFCy = 2.1525 + (0.3375 x CPIy/CPI0); MSC = UFC x Q/12", "Xy = (0.85 + 0.15 x CPI(y-1)/CPI0) x X0; X0 = US$3.00/MMBtu", "Xy = (0.885 + 0.115 x CPI(y-1)/CPI0) x X0; X0 = US$3.00/MMBtu",
  "No separate capacity charge visible", "No separate capacity charge visible", "No separate capacity charge visible", "No separate capacity charge visible")
a("E7", CAT_E, "Escalation", "CPI weight; CPI0 base convention", "Price article", "Inflation exposure of the fixed leg",
  "RED", "N/A", "Inside UFC (0.3375 term); CPI0 redacted", "Inside UFC (0.3375 term); CPI0 redacted", "15% CPI weight; CPI0 convention unknown", "11.5% CPI weight; CPI0 convention unknown",
  "None visible", "None visible", "None visible", "None visible")
a("E8", CAT_E, "FX conversion", "Source and fixing time", "Price definitions", "Settlement basis risk; ECB and 16:00 London fixings need not coincide",
  "N/A", "RED", "n/a (USD Henry Hub)", "n/a (USD Henry Hub)", "n/a (USD Henry Hub)", "n/a (USD Henry Hub)",
  "Bloomberg/Reuters spot 16:00 London, 4dp", "ECB reference rate; prior-day fallback", "n/a (JKM only)", "Bloomberg/Reuters spot 16:00 London, 4dp")
a("E9", CAT_E, "Pricing month / window", "Definition of M; averaging window", "Price definitions", "Hedge timing; asymmetric redactions here",
  None, "AMBER", NRD, NRD, NRD, NRD,
  "Redacted", "Month after ADP delivery-window month (stated in full)", "Redacted", "Redacted")
a("E10", CAT_E, "Index fallback", "Market disruption provisions", "Price article", "Tail risk if the index ceases",
  None, "GREEN", NRD, NRD, NRD, NRD,
  "Similar fallback architecture", "Similar fallback architecture", "Similar fallback architecture", "Similar fallback architecture")
a("E11", CAT_E, "Price review / reopener", "Trigger, frequency, scope", "Price article", "Reopener risk to long-term value",
  None, None, "Not identified in decks; check full text", "Not identified in decks; check full text", "Not identified in decks; check full text", "Not identified in decks; check full text",
  "Not identified in decks; check full text", "Not identified in decks; check full text", "Not identified in decks; check full text", "Not identified in decks; check full text")
a("E12", CAT_E, "Late-payment interest", "Basis and margin", "Payment article", "Credit cost of delay",
  None, "GREEN", NRD, NRD, NRD, NRD,
  "[***]% above SOFR, 360-day year (10.4.1)", "[***]% above SOFR, 360-day year (10.4.1)", "[***]% above SOFR, 360-day year (10.4.1)", "[***]% above SOFR, 360-day year (10.4.1)")
a("E13", CAT_E, "S-curve / slope bands", "Band thresholds and slopes either side; any caps built into the formula", "Price article", "Kinked slopes change payoff convexity and hedge ratios (common in oil-linked SPAs)",
  None, None, "None visible; linear 1.15 x HH", "None visible; linear 1.15 x HH", "None visible; linear 1.15 x HH", "None visible; linear 1.15 x HH",
  "None visible; greater-of floor structure instead (E5)", "None visible; greater-of floor structure instead (E5)", "None visible; greater-of floor structure instead (E5)", "None visible; greater-of floor structure instead (E5)")
a("E14", CAT_E, "Index lag convention", "Lag L in index observation, e.g. slope x index(t-L)", "Price definitions", "Hedge timing and cash-flow mapping depend on the lag",
  None, None, NRD, NRD, NRD, NRD,
  "Tied to Pricing Month definition (see E9)", "Tied to Pricing Month definition (see E9)", "Tied to Pricing Month definition (see E9)", "Tied to Pricing Month definition (see E9)")

CAT_F = "F. Optionality"
a("F1", CAT_F, "Term extension options", "Cross-reference C3-C6", "Term article", "Headline optionality",
  "AMBER", "RED", "Up to 10y buyer extension", "Similar", "Up to 10y buyer extension", "Up to 10y buyer extension",
  "None found", "None found", "2 x 5y buyer options", "2 x 5y buyer options")
a("F2", CAT_F, "Cargo cancellation right", "Notice, fee, which charges survive", "Quantity / price articles", "Buyer put; value depends on what survives",
  "RED", None, "Cancellation right; Monthly Sales Charge continues", "Cancellation right; Monthly Sales Charge continues", "No equivalent seen in reviewed snippets", "n/a; suspension mechanism instead",
  "Not identified in deck", "Not identified in deck", "Not identified in deck", "Not identified in deck")
a("F3", CAT_F, "Suspension right", "Fee mechanics; duration", "Quantity article", "Buyer pause option with a fee",
  "RED", None, "None identified", "None identified", "None identified", "Suspension right with Suspension Fee",
  "Not identified in deck", "Not identified in deck", "Not identified in deck", "Not identified in deck")
a("F4", CAT_F, "Capacity-charge survival on non-lifting", "Does the fixed leg continue?", "Price article", "Core Cheniere-style distinction: cancelled cargo is not 'no cargo, no price'",
  "RED", "N/A", "Yes: MSC continues", "Yes: MSC continues", "No separate charge exists (embedded Xy)", "Suspension Fee mechanics instead",
  "No separate capacity charge", "No separate capacity charge", "No separate capacity charge", "No separate capacity charge")
a("F5", CAT_F, "Destination flexibility", "Restrictions; diversion consent", "Delivery article", "Geographic arbitrage value",
  "GREEN", "GREEN", "Any destination, subject to agreement", "Same broad wording", "Same broad wording", "Same broad wording",
  "Broad, subject to export / trade law", "Broad, subject to export / trade law", "Broad, subject to export / trade law", "Broad, subject to export / trade law")
a("F6", CAT_F, "Alternate source delivery", "Seller substitution right; conditions", "Delivery article", "Supply security and quality variation",
  "AMBER", "AMBER", "Permitted with buyer consent and conditions", "Similar; Gulf Coast affiliate carve-out visible", "Similar", "Similar",
  "Same concept; different conditions", "Same concept; different conditions", "Same concept; different conditions", "Same concept; different conditions")
a("F7", CAT_F, "Upstream FM HH-basis election", "Buyer election of HH-priced replacement cargoes", "FM article", "Replacement-price mitigant in shortage",
  None, "GREEN", NRD, NRD, NRD, NRD,
  "Buyer HH-basis election; cure limits (14.3.7) present", "Buyer HH-basis election; cure limits (14.3.7) present", "Buyer HH-basis election; cure limits (14.3.7) present; carve-out interaction to blackline", "Buyer HH-basis election; cure limits (14.3.7) present; carve-out interaction to blackline")
a("F8", CAT_F, "Seasonal / tranche elections", "Rights to move volume between periods", "Quantity article", "Calendar-spread optionality",
  "RED", "RED", "None identified", "None identified", "None identified", "Seasonal Tranche structure",
  "None", "None", "Winter-weighted tranche rights", "Winter-weighted tranche rights")
a("F9", CAT_F, "Multiple-SPA coordination", "Cross-default, consolidation, shared caps", "Miscellaneous", "Portfolio effects across twin contracts",
  "N/A", "RED", "n/a", "n/a", "n/a", "n/a",
  "n/a", "n/a", "Coordination clause: separate caps, no cross-default, consolidated arbitration option", "Coordination clause: separate caps, no cross-default, consolidated arbitration option")
a("F10", CAT_F, "Cargo deferral / rescheduling right", "Notice, limits, price treatment of moved cargoes", "Scheduling article", "Time-spread option on delivery windows",
  None, None, "Not identified in decks; check full text", "Not identified in decks; check full text", "Not identified in decks; check full text", "Not identified in decks; check full text",
  "Not identified in decks; check full text", "Not identified in decks; check full text", "Not identified in decks; check full text", "Not identified in decks; check full text")
a("F11", CAT_F, "Reload / re-export rights", "Any right to reload or re-export delivered cargoes", "Delivery article", "Adds spread optionality; standalone value in tight prompt markets",
  None, None, "Not identified in decks; check full text", "Not identified in decks; check full text", "Not identified in decks; check full text", "Not identified in decks; check full text",
  "Not identified in decks; check full text", "Not identified in decks; check full text", "Not identified in decks; check full text", "Not identified in decks; check full text")
a("F12", CAT_F, "Diversion cost and profit-sharing", "Diversion fee (US$/MMBtu) and any profit-share on diverted cargoes", "Delivery / destination clauses", "Profit-share claws back part of the destination spread option (JFTC-flagged term)",
  None, None, "Destination 'subject to agreement'; no profit-share identified in deck", "Destination 'subject to agreement'; no profit-share identified in deck", "Destination 'subject to agreement'; no profit-share identified in deck", "Destination 'subject to agreement'; no profit-share identified in deck",
  "Broad destination flexibility; no diversion fee or profit-share identified in deck", "Broad destination flexibility; no diversion fee or profit-share identified in deck", "Broad destination flexibility; no diversion fee or profit-share identified in deck", "Broad destination flexibility; no diversion fee or profit-share identified in deck")
a("F13", CAT_F, "Enforceability of option rights", "Legal / competition-law constraints on destination, rejection, deferral and review rights", "Whole contract plus regulatory context", "Do not assign full option value to rights that are not clearly enforceable",
  None, None, "To assess against competition-law context; not a deck item", "To assess against competition-law context; not a deck item", "To assess against competition-law context; not a deck item", "To assess against competition-law context; not a deck item",
  "To assess against competition-law context; not a deck item", "To assess against competition-law context; not a deck item", "To assess against competition-law context; not a deck item", "To assess against competition-law context; not a deck item")

CAT_G = "G. Non-delivery and remedies"
a("G1", CAT_G, "Take-or-pay / shortfall basis", "% of ACQ; period basis (annual / quarterly / monthly / cargo); reference price", "Quantity / remedies", "Floor on seller revenue; buyer's minimum bill; period basis changes option value",
  "AMBER", "AMBER", "CSP-based shortfall architecture; % not extracted", "Same broad architecture", "Same broad architecture", "Same broad architecture",
  "Common framework; result scales with CSP and scheduled ACQ", "Common framework", "Common framework", "Common framework")
a("G2", CAT_G, "Cover damages", "Formula and reference price", "Remedies article", "Buyer failure-to-take economics",
  "RED", "AMBER", "CSP-based; cancellation interacts with MSC", "Same broad architecture", "CSP-based cover damages", "CSP-based plus suspension / idling-cost wording",
  "Same framework; values partly redacted", "Same framework; values partly redacted", "Same framework; values partly redacted", "Same framework; values partly redacted")
a("G3", CAT_G, "Seller DoP", "Formula and caps", "Remedies article", "Seller failure-to-deliver economics",
  "RED", "AMBER", "Refers to CSP minus UFC for replacement comparison", "Same broad concept", "CSP / cover-damages mechanics", "CSP plus additional cost wording",
  "Same architecture; caps and some values redacted", "Same architecture; caps and some values redacted", "Same architecture; caps and some values redacted", "Same architecture; caps and some values redacted")
a("G4", CAT_G, "Damages reference price", "CSP vs CSP minus UFC", "Remedies article", "Separated fixed charges change damage quantum",
  "RED", "AMBER", "CSP minus UFC", "CSP minus UFC", "CSP", "CSP + suspension / idling elements",
  "CSP-based; not further split", "CSP-based; not further split", "CSP-based; not further split", "CSP-based; not further split")
a("G5", CAT_G, "Mitigation / resale", "In-tank resale; mitigation duties", "Remedies article", "Reduces gross exposure",
  None, "AMBER", NRD, NRD, NRD, NRD,
  "To blackline", "To blackline", "In-tank DoP resale wording; to blackline", "In-tank DoP resale wording; to blackline")
a("G6", CAT_G, "FM effect on fixed charges", "Are capacity charges reduced during FM?", "FM / price articles", "FM tail risk on the fixed leg",
  "AMBER", None, "FM / capacity-charge reduction flagged as model input; extract clause", "Same", "n/a in same form (embedded)", "455-day FM deferral cap visible",
  NRD, NRD, NRD, NRD)

CAT_H = "H. Credit and structure"
a("H1", CAT_H, "Buyer credit support", "Guaranty, LC, TNW triggers, timing", "Credit article", "CVA input",
  "AMBER", "RED", "Clause present; thresholds / LC mechanics not extracted", "Present", "Present", "Present",
  "Named support / TNW / LC mechanics", "Named support / TNW / LC; timing differs", "Generic acceptable support", "Generic acceptable support")
a("H2", CAT_H, "Guaranty cap", "Amount or redaction", "Credit article", "Limits recoverable exposure",
  None, "AMBER", NRD, NRD, NRD, NRD,
  "No same capped defined term identified", "Capped defined guaranty term; amount redacted", "n/a in same form", "n/a in same form")
a("H3", CAT_H, "Seller credit support", "Any seller-side support", "Credit article", "Pre-COD seller performance risk",
  None, None, NRD, NRD, NRD, NRD, NRD, NRD, NRD, NRD)
a("H4", CAT_H, "Liability caps", "Aggregate and per-event caps", "Liability article", "Bounds on damage claims",
  "AMBER", "AMBER", "Caps / limits present; amounts not extracted", "Similar", "Similar", "Similar",
  "Present; amounts redacted", "Present; amounts redacted", "Present; amounts redacted; separate caps per SPA", "Present; amounts redacted; separate caps per SPA")
a("H5", CAT_H, "Lender / direct agreement", "Project finance provisions", "Financing article", "Step-in and enforceability",
  "AMBER", "GREEN", "Project-finance style provisions", "Similar", "Similar", "Similar",
  "Direct agreement present", "Direct agreement present", "Direct agreement present", "Direct agreement present")
a("H6", CAT_H, "Assignment", "Scope and consent", "Assignment article", "Transferability of contract value",
  None, "AMBER", NRD, NRD, NRD, NRD,
  "To blackline", "Broader wording around contractual entitlement to LNG", "To blackline", "To blackline")

CAT_I = "I. Delivery, quality and FM"
a("I1", CAT_I, "Delivery point / incoterm", "FOB / DES / CIF; location", "Delivery article", "Who carries shipping value and cost",
  "GREEN", "GREEN", "FOB Sabine Pass Facility", "FOB Sabine Pass Facility", "FOB Sabine Pass Facility", "FOB Sabine Pass Facility",
  "FOB Driftwood LNG Terminal, flange-to-flange (6.1)", "FOB Driftwood LNG Terminal (6.1)", "FOB Driftwood LNG Terminal (6.1)", "FOB Driftwood LNG Terminal (6.1)")
a("I2", CAT_I, "Title and risk", "Transfer point", "Delivery article", "Loss allocation",
  "GREEN", "GREEN", "At delivery point", "At delivery point", "At delivery point", "At delivery point",
  "At delivery point", "At delivery point", "At delivery point", "At delivery point")
a("I3", CAT_I, "Shipping and tankers", "Provider; approval and change rights", "Shipping article", "Fleet flexibility",
  "GREEN", "GREEN", "Buyer provides tankers", "Buyer provides tankers", "Buyer provides tankers", "Buyer provides tankers",
  "Buyer provides tankers; change rights operationally equivalent", "Same", "Same", "Same")
a("I4", CAT_I, "Laytime / demurrage / port services", "Rates and allocation", "Shipping article", "Operational cost class",
  None, "AMBER", NRD, NRD, NRD, NRD,
  "Common cost class; detailed wording differs", "Same", "Same", "Same")
a("I5", CAT_I, "Quality and off-spec", "Spec; off-spec remedies", "Quality article", "Off-spec discount or rejection economics",
  "AMBER", "AMBER", "Similar SPA architecture; remedies to check", "Similar", "Similar", "Similar",
  "No first-order spec difference; remedy calculations to check", "Same", "Same", "Same")
a("I6", CAT_I, "Measurement", "Units and testing", "Measurement article", "Settlement basis",
  None, "GREEN", NRD, NRD, NRD, NRD,
  "Common MMBtu measurement / test framework", "Same", "Same", "Same")
a("I7", CAT_I, "FM architecture and allocation", "Scope, notice, pro-rata allocation", "FM article", "Excuse scope and shortage allocation",
  "AMBER", "AMBER", "Express tanker / discharge-terminal FM clause", "Express clause", "Express clause; terminal wording narrower", "Express clause",
  "Broadly similar FM; foundation-customer pro-rata allocation equivalent", "Same", "Same; HH carve-out interaction to blackline", "Same; HH carve-out interaction to blackline")
a("I8", CAT_I, "DES-specific delivery terms", "Seller shipping / discharge obligations, demurrage allocation, destination port mechanics", "Delivery / shipping articles", "DES reverses freight cost and risk allocation relative to FOB",
  None, None, "n/a (FOB contract)", "n/a (FOB contract)", "n/a (FOB contract)", "n/a (FOB contract)",
  "n/a (FOB contract)", "n/a (FOB contract)", "n/a (FOB contract)", "n/a (FOB contract)")

CAT_J = "J. Governance and other"
a("J1", CAT_J, "Invoicing and payment", "Cycle, currency, dates", "Payment article", "Working capital",
  "AMBER", "GREEN", "Cargo invoicing standard; MSC invoiced monthly", "Same; MSC invoiced monthly", "Cargo invoicing standard", "Cargo invoicing standard",
  "Cargo invoice = CSP x loaded MMBtu; common framework", "Same", "Same", "Same")
a("J2", CAT_J, "Taxes", "Allocation", "Tax article", "Net price impact",
  None, "GREEN", "Standard field; not compared in deck", "Same", "Same", "Same",
  "No material divergence surfaced", "Same", "Same", "Same")
a("J3", CAT_J, "Disputes", "Forum; consolidation across twin SPAs", "Disputes article", "Enforcement; twin-SPA procedural effects",
  None, "AMBER", NRD, NRD, NRD, NRD,
  "Same broad class", "Same broad class", "Twin-SPA consolidation option", "Twin-SPA consolidation option")
a("J4", CAT_J, "Sanctions / trade law", "Restrictions", "Compliance article", "Destination and counterparty limits",
  None, "AMBER", NRD, NRD, NRD, NRD,
  "Same risk class; wording to blackline", "Same", "Same", "Same")
a("J5", CAT_J, "ESG / emissions / HSEC", "Data, cost, incentives", "ESG articles", "Emerging cost and reporting class",
  None, "AMBER", NRD, NRD, NRD, NRD,
  "Buyer-cost / incentive emissions language", "Extra HSEC / human-rights layer", "Stronger emissions data-access wording", "Stronger emissions data-access wording")
a("J6", CAT_J, "Confidentiality", "Scope", "Confidentiality article", "Limits information use",
  None, "AMBER", NRD, NRD, NRD, NRD,
  "Mental-impressions wording identified", "To blackline", "To blackline", "To blackline")

# Term type: Cash-flow (base DCF strip) / Option (option-adjusted treatment) / Risk-structural / Context
TT = {}
for k in ["A1","A2","A3","A4","A5","A7","A8","B1","C2","I2","I6","J6"]: TT[k] = "Context"
for k in ["A6","D4","E1","E10","F4","F9","F13","G2","G3","G4","G5","G6","H1","H2","H3","H4","H5","H6","I5","I7","J3","J4","J5"]: TT[k] = "Risk-structural"
for k in ["B3","C3","C4","C5","C6","C7","D6","D7","D8","D9","D10","E5","E11","E13","F1","F2","F3","F5","F6","F7","F8","F10","F11","F12","G1"]: TT[k] = "Option"
for k in ["B2","B4","C1","D1","D2","D3","D5","D11","D12","D13","E2","E3","E4","E6","E7","E8","E9","E12","E14","I1","I3","I4","I8","J1","J2"]: TT[k] = "Cash-flow"
# Hedgeability: Curve / Spread / Residual / n/a (indicative defaults; review per contract)
HG = {}
for k in ["E2","E3","E4","E5","E8","E12","E13"]: HG[k] = "Curve"
for k in ["D2","D3","F5","F7","F8","F10","F11","F12","I1","I3","I8"]: HG[k] = "Spread"
for k in ["C3","C4","C5","C6","C7","D4","D6","D7","D8","D9","D10","D11","D13","E6","E7","E9","E10","E11","E14","F1","F2","F3","F4","F6","G1","G2","G3","G4","G5","G6","H1","H2","H3","H4","H5","H6","I4","I5","I7","J2","J4","J5"]: HG[k] = "Residual"
def tt(i): return TT.get(i, "Context")
def hg(i): return HG.get(i, "n/a")

# Holder-side valuation inputs (not contract terms)
HOLDER = [
    ("Freight / charter rate", "Route rate, vessel spec, charter duration", "Baltic Exchange / Spark assessments; ICE / EEX LNG freight futures", "FOB-to-DES netback driver; partially hedgeable with freight futures"),
    ("Fuel and boil-off", "% of cargo or US$/MMBtu per voyage", "Internal operations / charter terms", "Delivered cost component"),
    ("Canal and port costs", "Per-transit and per-call fees", "Canal authority and port tariff schedules", "Route economics; Panama vs Suez vs direct"),
    ("Regas capacity fee", "Fixed berth / throughput charge", "Terminal tariff publications (Gate, Elengy, Fluxys, Snam, GAZ-SYSTEM)", "Delivered cost; terminal capacity has standalone value"),
    ("Regas variable fee", "Per-MWh or per-MMBtu variable rate", "Terminal tariff publications", "Netback calculation"),
    ("Terminal access / slots / storage", "Held capacity, reload rights, storage position", "Terminal agreements", "Physical optionality not visible in the SPA; convenience-yield type value"),
    ("Downstream use value (P_use)", "Resale value, avoided procurement cost or downstream margin", "Internal / market benchmarks", "The other half of the valuation identity; buyer value is P_use minus P_contract"),
    ("Benchmark forward curves", "Brent / JCC, HH, TTF, JKM strips", "ICE, CME, Platts, EIA, ACER", "Base cash-flow strip; hedge construction"),
    ("FX and unit conversion", "EUR/USD; MWh-MMBtu; tonne-MMBtu factors", "ECB / Bloomberg fixings; contract definitions", "TTF quotes EUR/MWh while contracts settle USD/MMBtu"),
    ("Discounting convention", "Internal hurdle rate vs collateralised OIS / SOFR", "NY Fed SOFR; internal policy", "Economic value and accounting fair value can differ materially"),
    ("Tax treatment", "Pre / post-tax basis; jurisdiction", "Internal tax", "Net value to the holder"),
    ("Credit / CVA inputs", "Counterparty spreads, collateral and guarantee terms", "Market CDS / internal credit", "IFRS 13 requires non-performance risk in fair value"),
    ("Volatility, correlation, seasonality", "HH-TTF-JKM-Brent-freight vols and correlations; de-seasonalised mean reversion", "Exchange settlement histories", "Calibration for option-adjusted valuation; price the forward curve correctly first"),
]

ROWS = R
FIELDS = ["id", "category", "item", "record", "clause", "why", "rag_cheniere", "rag_driftwood",
          "bg", "gnf", "gail", "total", "vitol", "gunvor", "shell_spa1", "shell_spa2"]
CONTRACTS = ["BG (SPL)", "Gas Natural Fenosa (SPL)", "GAIL (SPL)", "Total (SPL)",
             "Vitol (DWL)", "Gunvor (DWL)", "Shell SPA1 JKM (DWL)", "Shell SPA2 TTF (DWL)"]
CATEGORIES = list(dict.fromkeys(t[1] for t in ROWS))
