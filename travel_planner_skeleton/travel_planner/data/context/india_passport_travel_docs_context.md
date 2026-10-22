# Travel documents context: Indian passport holders

Data as of: 2026-10-07. Traveller assumed: Indian citizen, ordinary passport, tourism.
Purpose of this file: context for an LLM that suggests what a traveller must carry and that plans itineraries around entry rules.

---

## 1. Rules for the LLM (read first)

1. Confirm the traveller holds an Indian ordinary passport and travels for tourism. If business, study, work or a diplomatic/official passport, say this file does not cover it.
2. Look up the destination AND every transit or layover country. Transit rules differ from entry rules (section 7).
3. Match the country to its row. Members of a group (Schengen, Latin America, etc.) use the group row.
4. If the country is not in this file, say so. Give only the universal documents (section 3) and tell the traveller to check the official immigration site.
5. Always output, in this order: visa category, documents grouped by criticality, lead time, itinerary constraints, then the verify warning.
6. Confidence tags: `S` = from the source summary. `S?` = source conflicted or was unclear, so state the rule as uncertain. `G` = general knowledge, not from the source.
7. Never state an `S?` or `G` rule as certain. Say "check the official site".
8. Never invent fees, processing times, or portal names that are not in this file.
9. Always end with: "Rules change often. Confirm on the destination's official immigration site or the embassy before booking."
10. Safety flag rows (`SAFETY`) mean: also tell the traveller to check Indian government travel advisories and consider not going.

## 2. Criticality scale

| Level | Meaning | How the LLM should treat it |
| --- | --- | --- |
| C1 Critical | No boarding or no entry without it | List first. Schedule it before any non-refundable booking. |
| C2 High | Often checked at check-in or immigration, refusal possible | List second. Tell the traveller to carry it printed. |
| C3 Medium | Helps at immigration or in emergencies | List third. |
| C4 Low | Situational | Mention only when relevant to the trip. |

## 3. Universal documents (all countries)

| Document | Criticality | Notes |
| --- | --- | --- |
| Indian passport | C1 | Most countries want 6 months validity on arrival and 2 blank pages (G). Schengen: valid 3 months beyond departure, issued within 10 years (G). |
| Visa, e-Visa or ETA printout (where required) | C1 | Airlines check before boarding. Print even if e-Visa. |
| Return or onward ticket | C1 where stated, else C2 | Airlines can refuse boarding without it. |
| Accommodation proof | C2 | Asked at immigration and on arrival cards. |
| Digital arrival card (where required) | C1 where stated | Free on official sites only. |
| Travel insurance | C1 for Schengen, else C2 | Schengen cover at least EUR 30,000 (G). |
| Proof of funds (bank statements, cards, cash) | C2 | Some countries set a minimum. |
| Yellow fever certificate | C1 when required | Required for many African and South American countries, or when arriving from a risk country (G). Check per destination. |
| Passport photos (4 to 6) | C4 | For visa on arrival and paper forms. |
| Copies of passport, visa, bookings | C3 | Keep digital and paper copies, stored separately. |
| IDP plus Indian driving licence | C4 | Only if driving. |

## 4. Itinerary factors the LLM must apply

| Factor | Rule |
| --- | --- |
| Visa lead time | Embassy visa: 1 to 3 months. e-Visa: 1 to 4 weeks. Visa on arrival or visa-free: days. Plan trip dates after these. Warn before the traveller buys non-refundable tickets. |
| Stay limit | Trip length in a country must not exceed the allowed stay. Use the stay column. |
| Entry point restrictions | Some countries accept visas only at named airports or borders. Plan arrival and departure routes to match. |
| Arrival buffer | Visa on arrival queues and checks can take hours. Do not schedule anything on arrival day before 3 to 4 hours after landing (G). |
| Arrival cards | Submit within the window stated (Malaysia: within 3 days before arrival). Add a reminder before departure. |
| Multi-country trips | Check each leg: visa, stay limit, transit visa, and whether one visa covers several countries (Schengen does; East Africa Tourist Visa covers Rwanda, Kenya, Uganda). |
| Group or invitation rules | Where a tour operator, invitation letter or group is required, solo itineraries are not allowed. |
| Fees and cash | Visa on arrival fees may need USD or local cash. Plan a cash stop. |
| Permits inside a country | Some regions need permits on top of the visa (Tibet, Maldives non-Male islands, Galapagos, Eritrea, Sudan). Add them to the plan. |
| Safety | Rows marked SAFETY need an advisory check first. |
| Passport stamps | An Israel stamp can cause refusal in Kuwait, Lebanon, Libya and Yemen (S). Mention for multi-country Middle East trips. |
| Time sequencing | Do e-Visa first (fast), then book flights and hotels, then arrival cards, then insurance. Embassy visas first of all. |

---

## 5. Country rules

Columns: Country | Stay | Documents with criticality | Lead time | Itinerary factors | Conf

### 5.1 Visa-free (no visa needed)

| Country | Stay | Documents (criticality) | Lead time | Itinerary factors | Conf |
| --- | --- | --- | --- | --- | --- |
| Nepal | Unlimited | Passport or voter ID (C1) | Days | Free movement under 1950 treaty. | S |
| Bhutan | Unlimited in border areas | Passport or voter ID (C1) | Days | Fees apply for travel beyond border area. | S |
| Maldives | 90 days | Passport (C1), return ticket (C1), hotel booking (C2) | Days | Non-resort islands outside Male may need government permission. | S |
| Mauritius | 90 days | Passport (C1), return ticket (C2) | Days | | S |
| Fiji | 4 months | Passport (C1), return ticket (C2) | Days | Lau Province needs special permission. | S |
| Barbados | 90 days | Passport (C1) | Days | | S |
| Dominica | 6 months | Passport (C1) | Days | | S |
| Grenada | 3 months | Passport (C1) | Days | | S |
| Haiti | 3 months | Passport (C1) | Days | SAFETY: check advisories. | S |
| Jamaica | Not stated | Passport (C1) | Days | Verify stay limit. | S? |
| Trinidad and Tobago | 90 days | Passport (C1) | Days | | S |
| Gambia | 90 days | Passport (C1), yellow fever certificate (C2, G) | Days | | S, G |
| Senegal | 90 days | Passport (C1), yellow fever certificate (C2, G) | Days | | S, G |
| Rwanda | 30 days | Passport (C1) | Days | East Africa Tourist Visa (USD 100) also valid for Kenya and Uganda. | S |
| Angola | 30 days | Passport (C1), return or onward ticket (C1), hotel confirmation (C1) | Days | Exemption since 29 Sept 2023. | S |
| Micronesia | 30 days | Passport (C1) | Days | | S |
| Vanuatu | 120 days | Passport (C1) | Days | | S |
| Palau | 30 days | Passport (C1) | Days | Free visa on arrival, added 2025. | S |
| Qatar | 30 days | Passport (C1), return ticket (C1), confirmed hotel via Discover Qatar (C1) | Days | Verify the current rule before booking. | S? |
| Oman | 14 days | Passport (C1) | Days | Tourism only. Short stay limits the itinerary. | S |
| Malaysia | 30 days | Passport (C1), Malaysia Digital Arrival Card MDAC (C1) | Days | MDAC within 3 days before arrival. Exemption runs until 31 Dec 2026. Travel after that date needs re-check. | S |
| Thailand | 30 days | Passport (C1), Thailand Digital Arrival Card TDAC (C1) | Days | Source says stay cut from 60 to 30 days from 15 Sept 2026 and also lists Thailand elsewhere as visa required. State as uncertain. | S? |
| Indonesia | 30 days | Passport (C1), fee IDR 500,000 (C1) | Days | Source labels it e-VOA, tourism only. Verify the exact process. | S? |
| Sri Lanka | 30 days | Free ETA or visa on arrival (C1), passport (C1) | Days | Verify whether ETA must be done online first. | S? |
| Kazakhstan | 14 days | Passport (C1) | Days | Also listed under e-Visa. State as uncertain. Short stay limits the itinerary. | S? |
| Tunisia | Conditional | Passport (C1), return ticket (C1), hotel booking (C1) | Days | Group of 5 or more through a travel agency only. Solo itineraries not allowed under this rule. | S |
| Palestine | Not stated | Passport (C1) | Days | Arrival by sea to Gaza prohibited. SAFETY. | S |
| Northern Cyprus | 3 months | Passport (C1) | Days | Unrecognised territory. Entry may complicate later travel to Cyprus (G). | S, G |

### 5.2 Visa on arrival

| Country | Stay | Documents (criticality) | Lead time | Itinerary factors | Conf |
| --- | --- | --- | --- | --- | --- |
| Cambodia | 30 days | Passport (C1), photo (C2), fee USD 36 (C1), return ticket (C2) | Days | Carry USD cash. | S |
| Laos | 30 days | Passport (C1), photo (C2), fee (C1) | Days | e-Visa also available. 18 of 33 border crossings accept only regular visa holders, so check the crossing before planning an overland route. | S |
| Myanmar | 28 to 30 days | e-Visa 28 days or visa on arrival 30 days (C1) | 1 to 4 weeks if e-Visa | e-Visa holders must enter via Yangon, Nay Pyi Taw, Mandalay or named Thai and Indian border crossings. SAFETY: check advisories. | S |
| Mongolia | 30 days | e-Visa or visa on arrival (C1) | Days to 1 week | | S |
| Jordan | 30 days | e-Visa or visa on arrival (C1) | Days | | S |
| Egypt | 30 days | Passport (C1), fee (C1) | Days | Variations for groups, transit and GCC residents. | S |
| Ethiopia | 90 days | e-Visa or visa on arrival (C1) | Days to 1 week | Addis Ababa Bole airport only. | S |
| Zimbabwe | 1 month | e-Visa or visa on arrival (C1) | Days to 1 week | | S |
| Madagascar | 90 days | Passport (C1), return ticket (C2) | Days | USD 59 for 61 to 90 day stays. | S |
| Sierra Leone | 30 days to 3 months | e-Visa or visa on arrival (C1) | Days to 1 week | | S |
| Burundi | 1 month | Passport (C1) | Days | | S |
| Comoros | 45 days | Passport (C1) | Days | | S |
| Guinea-Bissau | 90 days | Passport (C1) | Days | | S |
| Democratic Republic of Congo | 7 days | Visa volant letter from the Ministry (C1) | Arrange before travel | Only 7 days, so the itinerary must stay short. SAFETY. | S |
| Algeria | 30 days | Passport (C1) | Days | Approved tour operator required for southern regions. | S |
| Cape Verde | Not stated | Passport (C1) | Days | Rule per Order No. 244/GMAI/2026 (Jan 2026). Verify terms. | S? |
| Timor-Leste | 30 days | Passport (C1) | Days | | S |
| Marshall Islands | 90 days | Passport (C1) | Days | | S |
| Tuvalu | 1 month | Passport (C1) | Days | | S |
| Saint Lucia | 6 weeks | Passport (C1) | Days | | S |
| Antigua and Barbuda | 30 days | Passport (C1), fee USD 100 (C1), valid visa or residence of Canada, Schengen, UK or US (C1) | Days | If the traveller has none of these, this route is closed. | S |
| Afghanistan | 30 days | e-Visa, entry via Kabul airport only (C1) | 1 to 4 weeks | SAFETY: serious risk. Advise checking Indian advisories. | S |
| Bangladesh | Not for tourists | Visa from the Bangladesh mission (C1) | 1 to 4 weeks | Source lists visa on arrival for diplomatic and official passports only. Ordinary passport needs a visa. | S |

### 5.3 e-Visa or electronic travel authorisation

| Country | Stay | Documents (criticality) | Lead time | Itinerary factors | Conf |
| --- | --- | --- | --- | --- | --- |
| Kenya | 90 days | Electronic Travel Authorisation (C1), hotel proof (C1), yellow fever certificate if applicable (C1) | Apply 3 to 90 days before travel | Fee USD 32.50. East Africa Tourist Visa also covers Rwanda and Uganda. | S |
| South Africa | 90 days | Electronic Travel Authorisation (C1) | 1 to 4 weeks | Entry via OR Tambo, Cape Town or Lanseria airports only. | S |
| Tanzania | 90 days | e-Visa or visa on arrival (C1) | Days to 1 week | | S |
| Uganda | 3 months | e-Visa before arrival (C1) | 1 to 2 weeks | East Africa Tourist Visa (USD 100) also valid for Rwanda and Kenya. | S |
| Zambia | 90 days | e-Visa (C1) | 1 to 2 weeks | | S |
| Botswana | 3 months | e-Visa (C1) | 1 to 2 weeks | | S |
| Namibia | 3 months | e-Visa (C1) | 1 to 2 weeks | | S |
| Malawi | 30 days | e-Visa (C1) | 1 to 2 weeks | | S |
| Mozambique | 30 days | e-Visa, printed SENAMI approval (C1) | 1 to 2 weeks | Visa on arrival works only with printed approval. | S |
| Morocco | 30 days | e-Visa (C1) | 1 to 2 weeks | | S |
| Nigeria | 30 days | e-Visa (C1) | 1 to 2 weeks | SAFETY: check advisories. | S |
| Benin | 30 to 90 days | e-Visa (C1) | 1 to 2 weeks | 30-day single EUR 50, 30-day multiple EUR 75, 90-day multiple EUR 100. | S |
| Gabon | 90 days | e-Visa (C1) | 1 to 2 weeks | Arrive via Libreville airport only. | S |
| Cote d'Ivoire | 3 months | e-Visa (C1) | 1 to 2 weeks | Arrive via Port Bouet airport, Abidjan. | S |
| Djibouti | 90 days | e-Visa (C1) | 1 to 2 weeks | | S |
| Togo | 15 days | e-Visa (C1) | 1 to 2 weeks | Short stay. | S |
| Liberia | 3 months | e-VOA (C1) | 1 to 2 weeks | | S |
| Guinea | 90 days | e-Visa (C1) | 1 to 2 weeks | | S |
| South Sudan | 30 to 180 days | e-Visa, printed authorisation (C1) | 1 to 4 weeks | 30-day single USD 100, 90-day multiple USD 200, 180-day multiple USD 350. SAFETY. | S |
| Lesotho, Burkina Faso, Chad, Equatorial Guinea | Not stated | e-Visa (C1) | 1 to 4 weeks | Verify terms. SAFETY for Burkina Faso and Chad. | S? |
| Libya | Not stated | e-Visa (C1) | 1 to 4 weeks | SAFETY: high risk. | S? |
| Vietnam | 90 days | Multiple-entry e-Visa (C1) | 1 to 2 weeks | Phu Quoc island is visa-free for 30 days (S). | S |
| Russia | 30 days | e-Visa (C1) | Apply 40 to 4 days before entry | Covers St Petersburg and Far East. SAFETY. | S |
| Japan | Varies | Tourist visa via the visa centre (VFS) in India (C1) | 1 to 4 weeks | Single-entry e-Visa exists for some third-country residents. | S |
| Israel | 90 days | Digital e-visa for Indian residents (C1) | 1 to 2 weeks | In place since 1 Jan 2025. SAFETY. | S |
| Iraq | 30 days | e-Visa (C1) | 1 to 4 weeks | SAFETY. | S |
| Bahrain | 14 days to 1 year | e-Visa (C1) | Days to 1 week | Single and multiple-entry options. | S |
| Azerbaijan | 30 days | e-Visa (C1) | Days to 1 week | Land borders need a prior e-Visa. About USD 30 at airport kiosks. An Armenian stamp can bring extra screening. | S |
| Georgia | 30 days | e-Visa (C1) | Days to 1 week | Reinstated May 2023. Exempt with certain US, UK, Japan, Canada, Australia, NZ, Israel, South Korea, Ireland, Schengen or GCC visa or residence (90 days in 180). | S |
| Uzbekistan | 30 days | e-Visa (C1) | Days to 1 week | 5-day visa-free transit at airports with a confirmed onward ticket. Source also mentions a 30-day visa-free introduction. State as uncertain. | S? |
| Tajikistan | 60 days | e-Visa, colour passport scan (C1) | 1 to 2 weeks | Invitation letter discretionary. | S |
| Kyrgyzstan | 60 days | e-Visa (C1), tour company invitation letter USD 50 or more (C1) | 1 to 2 weeks | Specific entry points only. Source also notes 7-day visa-free with USD 500+ voucher and return ticket. | S |
| Belarus | 30 days | e-Visa (C1) | 1 to 2 weeks | Waived with an EU or Schengen visa. SAFETY. | S |
| Serbia | 90 days in 180 | e-Visa (C1), invitation letter or accommodation proof (C1) | 1 to 2 weeks | Exempt with EU, Schengen, UK or US residence permit. | S |
| Albania | 90 days | e-Visa (C1) | 1 to 2 weeks | Exempt with Schengen, US, UK residence or 10-year UAE permit. | S |
| Ukraine | 30 days | e-Visa (C1) | 1 to 2 weeks | Reintroduced 17 Feb 2025. SAFETY. | S |
| Syria | Not stated | e-Visa (C1) | 1 to 4 weeks | SAFETY: high risk. | S? |
| Venezuela | Not stated | e-Visa (C1) | 1 to 4 weeks | SAFETY. Verify embassy status. | S? |
| Papua New Guinea | 30 days | e-Visa (C1) | 1 to 2 weeks | | S |
| Suriname | 90 days | e-Visa (C1) | 1 to 2 weeks | | S |
| Cuba | 90 days | e-Visa (C1) | 1 to 2 weeks | | S |
| Bahamas | 3 months | e-Visa (C1) | 1 to 2 weeks | Visa on arrival with valid Schengen, UK, US or Canadian visa. | S |

### 5.4 Embassy visa required

| Country or group | Stay | Documents (criticality) | Lead time | Itinerary factors | Conf |
| --- | --- | --- | --- | --- | --- |
| Schengen group: Austria, Belgium, Bulgaria, Croatia, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Iceland, Italy, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Netherlands, Norway, Poland, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden, Switzerland | 90 days in 180 | Schengen visa (C1), insurance EUR 30,000 (C1), hotel and ticket bookings (C1), bank statements (C2), employment or study proof (C2) | 1 to 3 months (G) | One visa covers all. Apply at the embassy of the country where you stay longest. Spain, France and Germany removed airside transit visas in 2026 (S). Airside transit via Finland, Iceland, Italy, Norway, Poland, Portugal, Switzerland needs no Schengen A visa (S). | S, G |
| United Kingdom | Varies | UK visa (C1), documents as for embassy visas (C2) | 1 to 3 months | Transit visa required except for certain Canada, NZ, Australia, EU or US visa or residence holders. | S |
| Ireland | 90 days | Irish visa (C1) | 1 to 3 months | UK C visa holders may be exempt if they enter via the UK first. | S |
| United States | Varies | US visa (C1) | Several weeks to months (G) | Transit visa required. | S |
| Canada | Varies | Canadian visa (C1) | 1 to 3 months | Transit visa required. | S |
| Australia | Varies | Online e600 visitor visa (C1) | 1 to 2 months | Transit visa required. | S |
| New Zealand | Varies | Visa plus NZeTA (C1) | 1 to 2 months | | S, G |
| China | Transit 24 hours | Visa (C1) | 1 to 4 weeks | Transit visa-free at international airports. Stapled visas for Arunachal, J&K and Ladakh residents are not recognised by India. Tibet needs a Tibet Travel Permit (about USD 10). Hainan: visa at Haikou Meilan and Sanya airports (S). | S |
| South Korea | 30 days | Tourist or transit visa (C1) | 1 to 4 weeks | Exemptions for some permanent residents and US, Australia, Canada, NZ, Schengen visa holders. Jeju is visa-free for 30 days (direct arrival). | S |
| Taiwan | 14 days | Visa or online travel authority (C1) | 1 to 4 weeks | Authority online if holding a valid or recent visa or residence from Australia, Canada, Japan, NZ, Schengen, UK or US. | S |
| Singapore | Varies | Online e-service via authorised agent or local sponsor (C1) | 1 to 2 weeks | 96-hour visa-free transit with certain Australian, Canadian, German, Japanese, NZ, UK, US or Swiss visas. | S |
| Brunei | Varies | Visa (C1) | 1 to 4 weeks | | S |
| Turkey | 30 days | Visa (C1) | 1 to 4 weeks | Conditional single-entry e-Visa if holding a Schengen, US, UK or Irish visa or residence. | S |
| Saudi Arabia | Varies | Visa (C1) | 1 to 2 weeks | Visa on arrival for Schengen, UK, US visa holders flying a Saudi carrier. 96-hour free transit visa with Saudia or flynas. Package visa via visitsaudi.com, minimum SAR 4,000 plus SAR 1,000 per extra day (S). | S |
| United Arab Emirates | 14, 60 or 90 days | Visa (C1) | 1 to 2 weeks | Visa on arrival for holders of US, UK or EU visit or residence visas with 6 months validity. Residents of Singapore, Japan, South Korea, Australia, NZ, Canada are eligible. Apply online via airlines such as Emirates, Etihad, flydubai, IndiGo (S). | S |
| Kuwait | Varies | Visa (C1) | 1 to 4 weeks | e-Visa for those with UK, US or Schengen visas or residence. | S |
| Lebanon | Varies | Visa (C1), General Security approval (C1) | 1 to 4 weeks | SAFETY. | S |
| Iran | 30 days | e-Visa (C1) | 1 to 4 weeks | Visa-free entry suspended on 22 Nov 2025. Kish Island visa-free for 14 days. SAFETY. | S |
| Pakistan | Restricted | Visa (C1) | Unclear | Admission heavily restricted after the 2025 Pahalgam attack. Kartarpur Corridor visa-free for Sikh pilgrims with a USD 20 permit. SAFETY. | S |
| North Korea | Varies | Special permit (C1) | Months | Government guides compulsory. SAFETY. | S |
| Turkmenistan | Varies | Invitation letter (C1) | 1 to 4 weeks | 10-day visa on arrival with invitation letter, or 5-day transit visa (USD 20). | S |
| Brazil | Varies | Visa (C1) | 1 to 4 weeks | | S |
| Argentina | Varies | Visa (C1) | 1 to 4 weeks | Visa-free for holders of US B1/B2/J/O/P/E/H-1B visa or Green Card from April 2026. | S |
| Chile | Varies | Visa (C1) | 1 to 4 weeks | US visa holders (not C or transit) with 6 months validity exempt. | S |
| Peru | 180 days | Visa (C1) | 1 to 4 weeks | Exempt for holders of Australia, Canada, UK, US, Schengen visa or residence with 6 months validity (180 days in 365). | S |
| Colombia | Varies | Online visa (C1) | 1 to 4 weeks | Schengen C or D, or US visa with 180+ days remaining substitutes. | S |
| Bolivia | 90 days | Online application, embassy visit (C1) | 1 to 4 weeks | Free visa at embassy. | S |
| Ecuador | Varies | Online visa (C1) | 1 to 4 weeks | Restrictions imposed Aug 2019 for misuse. Galapagos: 60 days, USD 20 Transit Control Card pre-registration. | S |
| Paraguay | Varies | Valid passport (C1) | Verify | Source says only a valid passport required. Uncertain. | S? |
| Uruguay | Varies | Prior authorisation (C1) | 1 to 4 weeks | Free visa issuance. | S |
| Guyana | Varies | Invitation letter from sponsor or host (C1) | 1 to 4 weeks | Visa on arrival with such a letter. | S |
| Mexico | Varies | Visa (C1) | 1 to 4 weeks | US, Canada, Japan, UK or Schengen visa substitutes. Transit visa required. | S |
| Costa Rica, Guatemala, Honduras, Dominican Republic | Varies | Visa (C1) | 1 to 4 weeks | US, Canada or Schengen (and for Costa Rica and Dominican Republic EU or Canada) visa substitutes. | S |
| Panama | 180 days | Visa (C1) | 1 to 4 weeks | Exempt for holders of US (1+ entry, 1+ year validity), UK, Canada, Australia, Japan, South Korea, Singapore or EU visas. | S |
| Belize | 90 days | Visa (C1) | 1 to 4 weeks | Visa on arrival for US or Canadian multiple-entry visa holders. Schengen visa exempts for 90 days. | S |
| Nicaragua | Varies | e-Visa in advance (C1) | 1 to 2 weeks | Visa on arrival removed. | S |
| El Salvador | Varies | Visa (C1) | 1 to 4 weeks | Transit visa fee reported at USD 1,000 for Indians since Oct 2023. Verify. | S? |
| Moldova | 90 days in 270 | Visa (C1) | 1 to 2 weeks | Schengen or UK C or D visa, EU or Canadian residence permit substitutes. Online visa without invitation available. | S |
| Montenegro | 30 days | Visa (C1) | 1 to 2 weeks | Schengen, UK, Ireland, US, Japan, Canada, NZ, Australia visas or residence substitute. | S |
| North Macedonia | 15 days | Visa (C1), proof of onward travel (C1) | 1 to 2 weeks | Schengen double or multiple-entry C, British, Canadian or US visa substitutes (15 days). | S |
| Bosnia and Herzegovina | 6 months | Visa (C1) | 1 to 4 weeks | National visa substitutable with EU or Schengen multiple-entry or US visa. | S |
| Cyprus | Varies | Visa (C1) | 1 to 4 weeks | Schengen double or multiple-entry C visa substitutes. | S |
| Kosovo | 15 days | Visa (C1) | 1 to 4 weeks | Schengen, US, Canada, Australia, Japan documents exempt. Kosovo stamp alone is not accepted by Serbia. | S |
| Andorra, Monaco | Varies | Schengen visa (C1) | 1 to 3 months | Andorra reached only via France or Spain. | S |
| Eritrea | Varies | Visa (C1), Travel Permit outside Asmara (C1) | 1 to 4 weeks | Permit costs 20 Eritrean nakfa. SAFETY. | S |
| Sudan | Varies | Visa (C1), travel permit outside Khartoum (C1) | 1 to 4 weeks | Darfur needs a separate permit. SAFETY. | S |
| Mali, Niger, Central African Republic | Varies | Visa (C1) | 1 to 4 weeks | SAFETY. | S |
| Ghana, Eswatini | Varies | Visa (C1) | 1 to 4 weeks | | S |
| Nauru, Solomon Islands | Varies | Visa (C1) | 1 to 4 weeks | | S |

---

## 6. Territories and special regions

| Place | Rule | Itinerary factors |
| --- | --- | --- |
| Hong Kong | Electronic travel authorisation, 14 days | Apply online before travel. |
| Macau | Visa not required, 30 days | |
| Cook Islands | Visa not required, 31 days | |
| Niue | Visa not required, 30 days | |
| British Virgin Islands | Visa not required, 30 days | |
| Turks and Caicos | Visa not required, 90 days | |
| Montserrat | Visa not required, 6 months | |
| Pitcairn Islands | Visa not required, 14 days | USD 35 landing fee. |
| Svalbard (Norway) | Visa not required, unlimited | Schengen visa needed to reach it from mainland Norway. |
| French overseas territories, Greenland, Faroe Islands | Visa required | |
| Puerto Rico, Guam, US Virgin Islands | Visa required | A US multiple-entry visa exempts you. |
| Bermuda, Cayman Islands, Falkland Islands | Visa required | Exceptions for certain US, Canadian or UK visa holders. |
| Tibet (China) | Tibet Travel Permit, about USD 10 | On top of the Chinese visa. |
| Maldives islands outside Male | Government permission | |
| Galapagos (Ecuador) | 60 days, USD 20 Transit Control Card | Pre-registration. |
| Kish Island (Iran), Phu Quoc (Vietnam), Jeju (South Korea) | Visa-free, limited stays | 14, 30 and 30 days. |
| Crimea | Russian-issued visa | SAFETY. |
| Transnistria | Visa not required | Register within 24 hours of arrival. |
| Abkhazia, South Ossetia, Somaliland | Visa required | SAFETY. |

## 7. Transit rules

| Place | Rule |
| --- | --- |
| Spain, France, Germany | Airside transit visa removed in 2026 (Spain 4 Mar, France 10 Apr, Germany 3 Jun) for staying airside. |
| Finland, Iceland, Italy, Norway, Poland, Portugal, Switzerland | Airport transit (Schengen A) visa not required for airside transit. |
| United States, Canada, Australia, UK, Czech Republic, Mexico | Transit visa generally required. UK exceptions apply. |
| China | 24-hour transit visa-free at international airports. |
| Uzbekistan | 5-day visa-free transit at airports with onward ticket. |
| Saudi Arabia | 96-hour free transit visa with Saudia or flynas. |
| Singapore | 96-hour visa-free transit with certain visas. |

## 8. Watchlist: rules that change fast

Thailand stay limit, Malaysia exemption end (31 Dec 2026), Iran, Pakistan, Nicaragua, El Salvador, Uzbekistan, Qatar, Indonesia, and the 2026 airside transit changes.

## 9. Source and limits

Country rows come from one machine summary of Wikipedia's "Visa requirements for Indian citizens" (https://en.wikipedia.org/wiki/Visa_requirements_for_Indian_citizens), read 2026-10-07. The page cites 27 visa-free, 47 visa on arrival and 66 e-Visa countries. The summary listed 27, 23 and about 45, so sections 5.2 and 5.3 are probably incomplete. Lead times, criticality levels and tags marked G are general knowledge. Not covered: business, student, work, diplomatic or official passport travel.
