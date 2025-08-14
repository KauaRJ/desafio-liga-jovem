# Hi there! This is the Ren'Py tutorial game. It's actually a fairly bad
# example of Ren'Py programming style - the examples we present in the game
# itself are good, but to make them easy to present we wind up doing
# some non-standard high-level things.
#
# So feel free to poke around, but if you're really looking for an example
# of good Ren'Py programming style, consider checking out The Question
# instead.

# Declare the characters.
define console = Character(_('Console'), color="#c8ffc8")

init python:
    # Classe do Jogador
    class Jogador:
        def __init__(self, nome):
            self.nome = nome
            self.vida = 100
            self.vida_maxima = 100
            self.inteligencia = 10
            self.pontuacao_pratica = 0  # Variável para a pontuação acumulada
            self.habilidades = ["Condicional", "Laço", "Vetor"]

    # Classe do Inimigo (ou Desafio)
    class Desafio:
        def __init__(self, nome, vida, dificuldade, pontos):
            self.nome = nome
            self.vida = vida
            self.dificuldade = dificuldade
            self.pontos = pontos
            self.ataque_base = 15

    # Cria uma instância do jogador
    store.Jogador = Jogador("Heroi")

default hero_hp = 180
default hero_max_hp = 180
default hero_mana = 50
default hero_max_mana = 50

default enemy_hp = 200
default enemy_max_hp = 200
default enemy_mana = 100
default enemy_max_mana = 100

default attacks = {
    "basic_attack": {"damage": 20, "mana_cost": 0},
    "if_attack": {"damage": 35, "mana_cost": 10},
    "loop_attack": {"damage": 45, "mana_cost": 15},
    "vetor_attack": {"damage": 60, "mana_cost": 20}
}

default inventory = {
    "Poção de Vida": {"quantity": 3, "type": "heal", "value": 30},
    "Poção de Mana": {"quantity": 2, "type": "mana", "value": 20},
    "Antídoto": {"quantity": 1, "type": "status", "value": "veneno"},
    "Bomba": {"quantity": 2, "type": "damage", "value": 40},
    "Elixir Raro": {"quantity": 1, "type": "both", "value": 50},
    "Pergaminho": {"quantity": 1, "type": "special", "value": 0}
}

label start_combat:
    if hero_hp <= 0:
        "Você foi derrotado!"
        return
    if enemy_hp <= 0:
        "Você venceu!"
        return

    call screen combat_screen
    $ result = _return
    
    if result == "attack":
        call screen attack_screen
        $ attack_choice = _return

        if attack_choice == "back":
            call start_combat
        else:
            # Executa o ataque do jogador
            $ attack_info = attacks[attack_choice]
            $ mana_cost = attack_info["mana_cost"]
            $ damage = attack_info["damage"]
            
            if hero_mana >= mana_cost:
                $ hero_mana -= mana_cost
                $ damage_dealt = renpy.random.randint(int(damage*0.8), int(damage*1.2))
                $ enemy_hp = max(0, enemy_hp - damage_dealt)
                "Você usou [attack_choice] e causou [damage_dealt] de dano!"
                
                # Verifica se o inimigo morreu
                if enemy_hp <= 0:
                    "Inimigo derrotado!"
                    return
                    
                # Inimigo ataca
                $ enemy_damage = renpy.random.randint(15, 30)
                $ hero_hp = max(0, hero_hp - enemy_damage)
                "O inimigo contra-ataca e causa [enemy_damage] de dano!"
                
                # Verifica se o herói morreu
                if hero_hp <= 0:
                    "Você foi derrotado!"
                    return
            else:
                "Mana insuficiente para este ataque!"
            
            call start_combat
        
    elif result == "inventory":
        call screen inventory_screen
        $ item_choice = _return

        if item_choice == "back":
            call start_combat
        else:
            $ item = inventory[item_choice]
            
            if item["quantity"] > 0:
                $ item["quantity"] -= 1
                
                # Aplica efeito do item
                if item["type"] == "heal":
                    $ heal_amount = min(item["value"], hero_max_hp - hero_hp)
                    $ hero_hp += heal_amount
                    "Você usou [item_choice] e recuperou [heal_amount] de HP!"
                
                elif item["type"] == "mana":
                    $ mana_amount = min(item["value"], hero_max_mana - hero_mana)
                    $ hero_mana += mana_amount
                    "Você usou [item_choice] e recuperou [mana_amount] de Mana!"
                
                elif item["type"] == "damage":
                    $ damage_amount = item["value"]
                    $ enemy_hp = max(0, enemy_hp - damage_amount)
                    "Você usou [item_choice] e causou [damage_amount] de dano ao inimigo!"
                    
                    if enemy_hp <= 0:
                        "Inimigo derrotado!"
                        return
                
                elif item["type"] == "both":
                    $ heal_amount = min(item["value"], hero_max_hp - hero_hp)
                    $ mana_amount = min(item["value"], hero_max_mana - hero_mana)
                    $ hero_hp += heal_amount
                    $ hero_mana += mana_amount
                    "Você usou [item_choice] e recuperou [heal_amount] HP e [mana_amount] Mana!"
                
                elif item["type"] == "status":
                    "Você usou [item_choice] e curou o status [item['value']]!"
                    # Lógica de status seria implementada aqui
                
                elif item["type"] == "special":
                    "Você usou [item_choice]! Um efeito misterioso acontece..."
                    # Efeito especial seria implementado aqui
                
                # Inimigo ataca após o uso do item
                $ enemy_damage = renpy.random.randint(15, 30)
                $ hero_hp = max(0, hero_hp - enemy_damage)
                "O inimigo aproveita a abertura e causa [enemy_damage] de dano!"
                
                if hero_hp <= 0:
                    "Você foi derrotado!"
                    return
            else:
                "Você não tem mais [item_choice] no inventário!"
            
            call start_combat


    elif result == "defend":
        # Lógica de defesa (reduz dano pela metade)
        $ damage_reduction = 0.5
        $ enemy_damage = renpy.random.randint(15, 30)
        $ actual_damage = int(enemy_damage * damage_reduction)
        $ hero_hp = max(0, hero_hp - actual_damage)
        "Você se defendeu! Dano reduzido para [actual_damage]!"
        call start_combat

    elif result == "run":
        # Tentativa de fuga
        $ flee_chance = 0.7
        if renpy.random.random() < flee_chance:
            "Você fugiu com sucesso!"
            return
        else:
            "Fuga falhou! O inimigo ataca!"
            $ enemy_damage = renpy.random.randint(15, 30)
            $ hero_hp = max(0, hero_hp - enemy_damage)
            "O inimigo causa [enemy_damage] de dano!"
            call start_combat
    return

# The game starts here.
#begin start
label start:
    scene black with fade
    call start_combat
    return
#end start

label modo_DungeonCrawler:
    "Bem-vindo ao Modo Prática! Aqui você pode treinar conceitos específicos."

    # Adicione a lógica para os desafios de prática aqui.
    # Por exemplo, um menu que permite escolher qual tópico praticar.
    
    menu:
        "Praticar If/Else":
            jump desafio_if_else_pratica
        "Praticar Loops":
            jump desafio_loops_pratica
        "Voltar ao Menu Principal":
            return