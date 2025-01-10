from owlready2 import *

onto = get_ontology("http://www.example.org/monster_ontology.owl")
# onto.load()

with onto:
    # --- Concepts (Classes) ---
    class Monster(Thing):
        """Main monster class"""
        pass

    # Subconcepts of Monster (monster types)
    class Vampires(Monster): pass
    class Relicts(Monster): pass
    class Specters(Monster): pass
    class Necrophages(Monster): pass
    class Beasts(Monster): pass
    class CursedOnes(Monster): pass
    class Hybrids(Monster): pass
    class Insectoids(Monster): pass
    class Elementa(Monster): pass
    class Draconids(Monster): pass
    class Ogroids(Monster): pass

    # Habitat concepts
    class Habitat(Thing): pass
    class Cave(Habitat): pass
    class Forest(Habitat): pass
    class Ruins(Habitat): pass

    # Loot (Monster reamins) concepts
    class Loot(Thing): pass
    class RelicItem(Loot): pass
    class MasterItem(Loot): pass
    class MagicItem(Loot): pass
    class CommonItem(Loot): pass

    # Witcher means of combat : weapons, oils, bombs, swords, signs
    class WitcherArsenal(Thing): pass

    class Oil(WitcherArsenal): pass

    class Bomb(WitcherArsenal): pass

    class Sign(WitcherArsenal): pass

    class Sword(WitcherArsenal): pass 
    class Material(Thing): pass
    silver = Material()
    steel = Material()
    
    Material.is_a.append(OneOf([silver, steel]))

    class HasMaterial(Thing >> Material): pass

    class silverSword (WitcherArsenal): 
        equivalent_to = [
            Sword &
            HasMaterial.value(silver) 
        ]

    class steelSword (WitcherArsenal): 
        equivalent_to = [
            Sword &
            HasMaterial.value(steel) 
        ]


    # Weakness concepts
    class Weakness(Thing): pass
    class MaterialWeakness(Weakness): 
        equivalent_to=[
            HasMaterial.value(OneOf([silver,steel]))
        ]

    class SilverWeakness(Weakness):
        equivalent_to = [
            MaterialWeakness &
            HasMaterial.value(silver)
        ] 

    class SteelWeakness(Weakness):
        equivalent_to = [
            MaterialWeakness &
            HasMaterial.value(steel)
        ] 

    silverWeakness = SilverWeakness()
    steelWeakness = SteelWeakness()

    # Monster properties
    class HasHabitat(Monster >> Habitat, FunctionalProperty): pass
    class HasWeakness(Monster >> Weakness): pass
    class DropsLoot(Monster >> Loot): pass

    class HasPrice(Loot >> float, FunctionalProperty): pass

    class HighValueLoot(Thing):
        equivalent_to =[
            Loot &
            HasPrice.min(300)
        ]

    class LowValueLoot(Thing):
        equivalent_to =[
            Loot &
            HasPrice.max(30)
        ]

    class HighValueLootMonster(Thing):
        equivalent_to =[
            Monster &
            DropsLoot.min(1, HighValueLoot)
        ]

    class LowValueLootMonster(Thing):
        equivalent_to=[
            Monster&
            DropsLoot.min(1, LowValueLoot)
        ]

    class CommonLootMonster(Thing):
        equivalent_to=[
            Monster &
            DropsLoot.min(1, CommonItem)
        ]

    class MagicLootMonster(Thing):
        equivalent_to=[
            Monster &
            DropsLoot.min(1, MagicItem)
        ]

    class MasterLootMonster(Thing):
        equivalent_to =[
            Monster &
            DropsLoot.min(1, MasterItem)
        ]

    # --- Loot items ---
    alghoulBoneMarrow = MasterItem("Alghoul Bone Marrow", HasPrice=30)
    alghoulClaw = MagicItem("Alghoul Claw", HasPrice=60)
    arachasEyes = MagicItem("Arachas Eyes", HasPrice=45)
    arachasVenom = MasterItem("Arachas Venom", HasPrice=30)
    basiliskHide = MagicItem("Basilisk Hide", HasPrice=544)
    basiliskVenom = MasterItem("Basilisk Venom", HasPrice=45)
    berserkerHide = MagicItem("Berserker Hide", HasPrice=309)    
    caveTrollLiver = MasterItem("Cave Troll Liver", HasPrice=30)

    chortHide = MagicItem("Chort Hide", HasPrice=324)
    cockatriceEgg = MagicItem("Cockatrice Egg", HasPrice=55)
    cockatriceStomach = MasterItem("Cockatrice Stomach", HasPrice=45)
    crystalizedEssence = MagicItem("Crystalized Essence", HasPrice=75)
    cyclopsEye = MasterItem("Cyclops’ Eye", HasPrice=30)
    darkEssence = MagicItem("Dark Essence", HasPrice=45)
    devourersBlood = MasterItem("Devourer’s Blood", HasPrice=30)
    drownerBrain = MasterItem("Drowner Brain", HasPrice=30)    
    drownerTongue = MasterItem("Drowner Tongue", HasPrice=30)
    ekimmaraHide = MagicItem("Ekimmara Hide", HasPrice=294)
    elementalEssence = MagicItem("Elemental Essence", HasPrice=75)    
    endregaEmbryo = MagicItem("Endrega Embryo", HasPrice=45)
    endregaHeart = MasterItem("Endrega Heart", HasPrice=30)
    eryniaEye = MagicItem("Erynia Eye", HasPrice=45)
    essenceOfWraith = MagicItem("Essence of Wraith", HasPrice=45)
    fiendsEye = MasterItem("Fiend’s Eye", HasPrice=30)
    fogletTeeth = MagicItem("Foglet Teeth", HasPrice=45)
    forktailHide = MasterItem("Forktail Hide", HasPrice=30)
    gargoyleDust = MagicItem("Gargoyle Dust", HasPrice=45)
    gargoyleHeart = MagicItem("Gargoyle Heart", HasPrice=45)
    ghoulsBlood = MasterItem("Ghoul’s Blood", HasPrice=30)
    golemsHeart = MagicItem("Golem’s Heart", HasPrice=30)
    graveHagsEar = MasterItem("Grave Hag’s Ear", HasPrice=30)
    griffinFeathers = MagicItem("Griffin Feathers", HasPrice=60)
    griffinsEgg = MagicItem("Griffin’s Egg", HasPrice=60)    
    hagTooth = MagicItem("Hag Tooth", HasPrice=60)
    harpyEggs = MasterItem("Harpy Eggs", HasPrice=30)
    harpyFeathers = MasterItem("Harpy Feathers", HasPrice=30)
    harpyTalons = MagicItem("Harpy Talons", HasPrice=45)    
    leshenResin = MagicItem("Leshen Resin", HasPrice=51)
    lightEssence = MasterItem("Light Essence", HasPrice=30)    
    lockOfLamiaHair = MagicItem("Lock of Lamia Hair", HasPrice=60)
    monsterBlood = RelicItem("Monster Blood", HasPrice=10)
    monsterBone = RelicItem("Monster Bone", HasPrice=10)
    monsterBrain = RelicItem("Monster Brain", HasPrice=10)
    monsterClaw = RelicItem("Monster Claw", HasPrice=10)
    monsterEar = RelicItem("Monster Ear", HasPrice=10)
    monsterEgg = RelicItem("Monster Egg", HasPrice=10)
    monsterEssence = RelicItem("Monster Essence", HasPrice=10)
    monsterEye = RelicItem("Monster Eye", HasPrice=10)
    monsterFeather = RelicItem("Monster Feather", HasPrice=10)
    monsterHair = RelicItem("Monster Hair", HasPrice=10)
    monsterHeart = RelicItem("Monster Heart", HasPrice=10)
    monsterHide = RelicItem("Monster Hide", HasPrice=106)
    monsterLiver = RelicItem("Monster Liver", HasPrice=10)
    monsterSaliva = RelicItem("Monster Saliva", HasPrice=10)
    monsterTongue = RelicItem("Monster Tongue", HasPrice=10)
    monsterTooth = RelicItem("Monster Tooth", HasPrice=10)    
    necrophageHide = MagicItem("Necrophage Hide", HasPrice=162)
    nekkerBlood = MasterItem("Nekker Blood", HasPrice=30)
    nekkerClaw = MasterItem("Nekker Claw", HasPrice=30)
    nekkerEye = MasterItem("Nekker Eye", HasPrice=30)
    nekkerHeart = MasterItem("Nekker Heart", HasPrice=30)
    nekkerWarriorsLiver = MasterItem("Nekker Warrior’s Liver", HasPrice=30)    
    nightwraithHair = MagicItem("Nightwraith Hair", HasPrice=45)
    powderedMonsterTissue = RelicItem("Powdered Monster Tissue", HasPrice=10)    
    rotfiendBlood = MagicItem("Rotfiend Blood", HasPrice=45)
    specterDust = MasterItem("Specter Dust", HasPrice=30)
    shaelmaarDust = MagicItem("Shaelmaar Dust", HasPrice=45)
    shaelmaarHair = MagicItem("Shaelmaar Hair", HasPrice=45)
    sirenVocalCords = RelicItem("Siren Vocal Cords", HasPrice=21)
    slyzardScalePlate = MagicItem("Slyzard Scale Plate", HasPrice=480)
    stammelfordsDust = CommonItem("Stammelford's Dust", HasPrice=14)
    trollHide = MagicItem("Troll Hide", HasPrice=177)    
    vampireFang = MagicItem("Vampire Fang", HasPrice=105)
    vampireBlood = MagicItem("Vampire Blood", HasPrice=45)
    vampireSaliva = MasterItem("Vampire Saliva", HasPrice=30)    
    waterEssence = MagicItem("Water Essence", HasPrice=60)
    waterHagTooth = MagicItem("Water Hag Tooth", HasPrice=75)    
    werewolfHide = MagicItem("Werewolf Hide", HasPrice=192)
    werewolfSaliva = MagicItem("Werewolf Saliva", HasPrice=60)
    wraithEssence = MagicItem("Wraith Essence", HasPrice=45)
    wightEar = MagicItem("Wight Ear", HasPrice=30)
    wightHair = MagicItem("Wight Hair", HasPrice=60)
    wightStomach = MagicItem("Wight Stomach", HasPrice=45)    
    wolfsLiver = CommonItem("Wolf's Liver", HasPrice=10)
    wyvernEgg = MagicItem("Wyvern Egg", HasPrice=70)
    wyvernHide = MagicItem("Wyvern Hide", HasPrice=604)

    # --- Monster individuals ---
    ekimmara = Vampires("Ekimmara")
    ekimmara.HasWeakness.append(silverWeakness)
    ekimmara.HasHabitat = Cave()
    ekimmara.DropsLoot.append(vampireFang)
    ekimmara.DropsLoot.append(ekimmaraHide)

    leshen = Relicts("Leshen")
    leshen.HasWeakness.append(silverWeakness)
    leshen.HasHabitat = Forest()
    leshen.DropsLoot.append(leshenResin)

    noonwraith = Specters("Noonwraith")
    noonwraith.HasWeakness.append(silverWeakness)
    noonwraith.HasHabitat = Ruins()
    noonwraith.DropsLoot.append(specterDust)

    griffin = Hybrids("Griffin")    
    griffin.HasWeakness.append(silverWeakness)
    griffin.HasHabitat = Ruins()
    griffin.DropsLoot.append(griffinFeathers)
    griffin.DropsLoot.append(griffinsEgg)

    # TODO: Ако играч иска някакъв предмет -> трябва да отиде на еди коя си локация (Cave)

    # --- Reasoning  ----

    # --- SUBSUMPTION ----
    for subclass in Loot.descendants():
        print(subclass.name)
   
    sync_reasoner()

    for subclass in Loot.descendants():
        print(subclass.name)

    def compare_loot(monster1, monster2):
        loot1 = list(monster1.DropsLoot)
        loot2 = list(monster2.DropsLoot)

        def get_loot_value(loot):
            return sum(item.HasPrice for item in loot if hasattr(item, 'HasPrice'))

        value1 = get_loot_value(loot1)
        value2 = get_loot_value(loot2)

        if value1 > value2:
            return f"{monster1.name} drops more expensive loot than {monster2.name}"
        elif value1 < value2:
            return f"{monster2.name} drops more expensive loot than {monster1.name}"
        else:
            return "Those two monsters drop equally expensive loot"

    result = compare_loot(noonwraith, leshen)
    print(result)

    for monster in Monster.instances():
        print(f"{monster.name} can be found in: {monster.HasHabitat.name if monster.HasHabitat else 'unknown habitat'}")
    

# save ontology in .owl file
onto.save(file="monster_ontology.owl", format="rdfxml")
