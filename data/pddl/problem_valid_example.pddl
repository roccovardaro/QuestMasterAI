(define (problem retrieve-royal-sword)
    (:domain eldoria-quest)
    (:objects
        protagonist1 - protagonist
        king1 - king
        royal-sword - sword
        log1 - log
        oak-tree - tree
        village - location
        forest - location
        castle - location
    )

    (:init
        ;; Initial state as per quest description: "Il protagonista si trova nel villaggio e riceve la missione dal re."
        (at protagonist1 village)
        (at king1 village)
        (mission-active protagonist1) ; Assume mission is already received at the start for planning to focus on obstacles.

        ;; Obstacles setup:
        ;; 1. "Il sentiero per il bosco e' bloccato da un tronco caduto."
        (path-blocked village forest log1)

        ;; 2. "Un corvo ha preso la spada e l'ha portata in cima a un albero."
        (sword-on-tree royal-sword oak-tree)
        (at oak-tree forest) ; The tree is located within the forest area.

        ;; 3. "Il tempo peggiora e inizia a piovere, rendendo il terreno scivoloso."
        ;; This state affects movement, particularly when departing from or to the forest.
        (ground-slippery forest)

        ;; Other initial path conditions:
        ;; Path from forest to castle is physically clear of logs, but might be slippery.
        (path-cleared forest castle)
        ;; Path from village to village (self-loop) is clear.
        (path-cleared village village)
        ;; Path from forest to forest (self-loop) is clear.
        (path-cleared forest forest)
        ;; Path from castle to castle (self-loop) is clear.
        (path-cleared castle castle)
    )

    ;; Goal consistent with the quest: "Recuperare la spada nel bosco e riportarla al castello."
    (:goal (and
        (king-has-sword king1 royal-sword)
    ))
)