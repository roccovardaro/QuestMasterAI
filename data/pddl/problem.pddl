(define (problem rescue-the-princess)
    (:domain knight-quest)
    (:objects
        knight1 - knight
        princess1 - princess
        dragon1 - dragon
        sorcerer1 - sorcerer
        sword1 - sword
        relic1 - ancient_relic
        kingdom_loc - kingdom
        forest_path_loc - forest_path
        castle_gate_loc - castle_gate
        castle_interior_loc - castle_interior
        ancient_ruins_loc - ancient_ruins
    )

    (:init
        ;; Initial state as per quest description: "Il cavaliere è pronto per la sua missione, probabilmente nel suo regno o in viaggio."
        (at knight1 kingdom_loc) ; The knight begins his journey in his kingdom.
        (at sword1 kingdom_loc) ; A mighty sword is available in the kingdom.
        (at relic1 ancient_ruins_loc) ; An ancient relic is hidden in distant ruins.

        ;; The princess is in peril, held captive in the deepest part of the castle.
        (princess-imprisoned castle_interior_loc)

        ;; Obstacles to overcome:
        ;; 1. "Il sentiero per il castello è irto di pericoli e creature oscure."
        (path-blocked kingdom_loc forest_path_loc) ; The path leading from the kingdom to the forest is blocked by dangers.

        ;; 2. "Un drago malvagio custodisce il castello dove è tenuta prigioniera la principessa."
        (enemy-present dragon1 castle_gate_loc) ; A fearsome dragon guards the castle gate.

        ;; 3. "Il cavaliere deve affrontare un'antica magia o un potente stregone."
        (enemy-present sorcerer1 castle_interior_loc) ; A powerful sorcerer is inside the castle, protecting the princess.
        (magic-barrier-active castle_interior_loc) ; An ancient magic barrier protects the princess's chamber.

        ;; Define clear paths (those not explicitly blocked) to allow movement once obstacles are cleared.
        (not (path-blocked forest_path_loc castle_gate_loc))
        (not (path-blocked castle_gate_loc castle_interior_loc))
        (not (path-blocked kingdom_loc ancient_ruins_loc))
        (not (path-blocked ancient_ruins_loc kingdom_loc))

        ;; Initial status of enemies and magic barriers - they are not yet defeated or dispelled.
        (not (is-defeated dragon1))
        (not (is-defeated sorcerer1))
        (not (magic-barrier-dispelled castle_interior_loc))

        ;; The quest is not yet active; the knight must consciously begin it.
        (not (quest-active knight1))
    )

    ;; Goal consistent with the quest: "Salvare la principessa."
    (:goal (princess-rescued princess1))
)