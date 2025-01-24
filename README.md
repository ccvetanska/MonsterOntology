<h2>Monster Ontology</h2>

<h3>Summary</h3>
The Monster Ontology represents the various concepts and objects in the Witcher 3 game domain. It is centered around the monsters the player fights against, their weaknesses, and the reward (Loot) they drop after being killed.
The ontology could serve new players for better orientation in the game or when developing another game with a similar theme.

<h3>Technologies</h3>
The Monster Ontology is made using Owready2 + Python.

<h3>Elements of the Ontology</h3>
The various elements of the ontology are described below in the DL language

<h4>1. Concepts (Classes)</h4>
<code>WitcherThing ⊑ Thing
Monster ⊑ WitcherThing
Beasts ⊑ [AND Monster [FILLS :HasWeakness beastOil] 
    [FILLS :HasWeakness steelWeakness]]
Vampires ⊑ [AND Monster [FILLS :HasWeakness vampireOil] 
    [FILLS :HasWeakness silverWeakness] [FILLS :HasWeakness fire]]
Relicts ⊑ [AND Monster [FILLS :HasWeakness relictOil silverWeakness]]
Specters ⊑ [AND Monster [FILLS :HasWeakness specterOil silverWeakness]]
Necrophages ⊑ [AND Monster [FILLS :HasWeakness necrofageOil silverWeakness]]
CursedOnes ⊑ [AND Monster [FILLS :HasWeakness cursedOil silverWeakness]]
Hybrids ⊑ [AND Monster [FILLS :HasWeakness hybridOil silverWeakness]]
Insectoids ⊑ [AND Monster [FILLS :HasWeakness insectoidOil silverWeakness]]
Elementa ⊑ [AND Monster [FILLS :HasWeakness elementaOil silverWeakness]]
Draconids ⊑ [AND Monster [FILLS :HasWeakness draconidOil silverWeakness]]
Ogroids ⊑ [AND Monster [FILLS :HasWeakness ogroidOil silverWeakness]]
Habitat ⊑ WitcherThing
Cave ⊑ Habitat
Forest ⊑ Habitat
Ruins ⊑ Habitat
Loot ⊑ WitcherThing
RelicItem ⊑ Loot
MasterItem ⊑ Loot
MagicItem ⊑ Loot
CommonItem ⊑ Loot
WitcherArsenal ⊑ WitcherThing
Oil ⊑ WitcherArsenal
Bomb ⊑ WitcherArsenal
Sign ⊑ WitcherArsenal
Sword ⊑ WitcherArsenal
Material ≐ [AND WitcherThing [ONE-OF silver steel]]
Element ≐ [AND WitcherThing [ONE-OF fire water]]
SilverSword ≐ [AND Sword [FILLS :HasMaterial silver]]
SteelSword ≐ [AND Sword [FILLS :HasMaterial steel]]
Weakness ⊑ WitcherThing
MaterialWeakness ≐ [AND Weakness [FILLS :HasMaterial 
    [ONE-OF silver steel]]
SilverWeakness ≐ [AND Weakness [ALL :HasMaterial silver]]
SteelWeakness ≐ [AND Weakness [ALL :HasMaterial steel]]
DancingStar ≐ [AND Bomb [FILLS :HasElement fire]]
Igni ≐ [AND Sign [FILLS :HasElement fire]]
HighValueLoot ≐ [AND Loot [ALL :HasPrice >= 100]]
LowValueLoot ≐ [AND Loot [ALL :HasPrice <= 99]]
HighValueLootMonster ≐ [AND Monster [EXISTS 1 :DropsLoot HighValueLoot]]
LowValueLootMonster ≐ [AND Monster [EXISTS 1 :DropsLoot LowValueLoot]]
CommonLootMonster ≐ [AND Monster [EXISTS 1 :DropsLoot CommonItem]]
MagicLootMonster ≐ [AND Monster [EXISTS 1 :DropsLoot MagicItem]]
KilledByFire ≐ [FILLS :hasWeakness fire]
Ekimmara ≐ [AND Vampires [FILLS :HasWeakness silverWeakness] 
        [FILLS :HasHabitat cave] 
        [FILLS :DropsLoot vampireFang ekimmaraHide]]
Leshen ≐ [AND Relicts [FILLS :HasWeakness silverWeakness] 
        [FILLS :HasHabitat forest] [FILLS :DropsLoot leshenResin]]
Noonwraith ≐ [AND Specters [FILLS :HasWeakness silverWeakness] 
        [FILLS :HasHabitat ruins] [FILLS :DropsLoot specterDust]]
Griffin ≐ [AND Hybrids [FILLS :HasWeakness silverWeakness]
        [FILLS :HasHabitat ruins] [FILLS :DropsLoot griffinFeathers griffinsEgg]]
Wolf ≐ [AND Beasts [FILLS :HasWeakness steelWeakness] 
        [FILLS :HasHabitat forest] [FILLS :DropsLoot wolfsLiver]]
</code>

<h4>2. Properties (Relations)</h4>
<img src="https://github.com/user-attachments/assets/2869d2d9-d4bb-4552-9991-60e718300525">

<h4>3. Individuals </h4>
<code>relictOil → Oil
specterOil → Oil

beastOil → Oil
cursedOil → Oil
hybridOil → Oil
vampireOil → Oil
giantWolf → Wolf
jennyOfTheWoods → Nightwraith
silver → Material
steel → Material
fire → Element
water → Element
silverWeakness → SilverWeakness
steelWeakness → SteelWeakness
dancingStar → [AND Bomb [FILLS :HasElement fire]]
alghoulBoneMarrow → [AND MasterItem [FILLS :HasPrice 30]]
basiliskHide → [AND MagicItem [FILLS :HasPrice 544]]
basiliskVenom → [AND MasterItem [FILLS :HasPrice 45]]
vampireFang → [AND MagicItem [FILLS :HasPrice 105]]
leshenResin → [AND MagicItem [FILLS :HasPrice 51]]
vampireBlood → [AND MagicItem [FILLS :HasPrice 45]]
vampireSaliva → [AND MasterItem [FILLS :HasPrice 31]]
ekimmaraHide → [AND MasterItem [FILLS :HasPrice 294]]
specterDust → [AND MasterItem [FILLS :HasPrice 35]]
wolfsLiver → [AND CommonItem [FILLS :HasPrice 10]]
griffinFeathers → [AND MagicItem [FILLS :HasPrice 60]]
griffinsEgg → [AND MasterItem [FILLS :HasPrice 65]]
wyvernEgg → [AND MagicItem [FILLS :HasPrice 604]]</code>

<h3>Example of logical reasoning</h3>
<h4>1. KB |= (giantWolf → CommonLootMonster) </h4>
<code>giantWolf <i>Type</i> Wolf 
               Wolf <i>SubClassOf</i> Monster
Wolf <i>dropsLoot</i> wolfsLiver 
                wolfsLiver <i>SubClassOf</i> CommonItem
Monster and (<i>dropsLoot</i> value CommonItem) <i>SubClassOf</i> CommonLootMonster</code>

<h3>Visualisation</h3>

<img src="https://github.com/user-attachments/assets/db273f6f-1b2f-48a2-862f-1ee3721507a1"/>
<i>Simplified graph of The Monster Ontology with degree of collapsing = 3, made with WEBVOWL 1.1.7</i>
<br/>
<h3>More</h3>
<i>For more information, see <b>MonsterOntology_documentation.pdf</b></i>
   
