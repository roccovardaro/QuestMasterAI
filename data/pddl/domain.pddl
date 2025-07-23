(define (domain knight-quest)
    (:requirements :strips :typing)
    (:types
        character ; Generic type for any character in the story
            knight princess enemy - character ; Specific types of characters
            dragon sorcerer - enemy ; Specific types of enemies
        location ; Places in the world
            kingdom forest_path castle_gate castle_interior ancient_ruins - location ; Specific locations
        item ; Any item that can be picked up or used
            sword ancient_relic - item ; Specific types of items
    )

    (:predicates
        (at ?o - object ?l - location) ; An object (character or item) is at a specific location.
        (quest-active ?k - knight) ; Indicates the knight is currently undertaking the quest.
        (has ?k - knight ?i - item) ; The knight possesses a specific item.
        (path-blocked ?from ?to - location) ; Indicates that a path between two locations is impassable due to obstacles or dangers.
        (enemy-present ?e - enemy ?l - location) ; An enemy (e.g., dragon, sorcerer) is currently at a particular location.
        (magic-barrier-active ?l - location) ; A magical barrier is active at a location, blocking further progress.
        (princess-imprisoned ?l - location) ; The princess is held captive at a specified location.
        (is-defeated ?e - enemy) ; An enemy has been vanquished.
        (magic-barrier-dispelled ?l - location) ; The magical barrier at a location has been removed or neutralized.
        (princess-rescued ?p - princess) ; The ultimate goal: the princess has been successfully rescued.
    )

    ;; Action: The knight officially starts the quest.
    ;; This action signifies the beginning of the adventure and activates the quest state for the knight.
    (:action start-quest
        :parameters (?k - knight ?start_loc - location)
        :precondition (at ?k ?start_loc)
        :effect (quest-active ?k)
    )

    ;; Action: The knight acquires a sword.
    ;; The sword is an essential item for fighting enemies and clearing dangerous paths.
    (:action get-sword
        :parameters (?k - knight ?s - sword ?l - location)
        :precondition (and
            (at ?k ?l)
            (at ?s ?l)
            (quest-active ?k)
        )
        :effect (and
            (has ?k ?s)
            (not (at ?s ?l)) ; The sword is no longer at the location, it's now with the knight.
        )
    )

    ;; Action: The knight finds and acquires an ancient relic.
    ;; This relic can be used as an alternative to defeating a sorcerer to dispel magic.
    (:action get-ancient-relic
        :parameters (?k - knight ?r - ancient_relic ?l - location)
        :precondition (and
            (at ?k ?l)
            (at ?r ?l)
            (quest-active ?k)
        )
        :effect (and
            (has ?k ?r)
            (not (at ?r ?l)) ; The relic is no longer at the location, it's now with the knight.
        )
    )

    ;; Action: The knight moves from one location to another.
    ;; Movement is only possible if the path between the two locations is not blocked by obstacles or dangers.
    (:action go
        :parameters (?k - knight ?from ?to - location)
        :precondition (and
            (at ?k ?from)
            (not (path-blocked ?from ?to))
            (quest-active ?k)
        )
        :effect (and
            (not (at ?k ?from))
            (at ?k ?to)
        )
    )

    ;; Action: The knight overcomes dangers on a blocked path.
    ;; This represents dealing with "creature oscure" or other perils making a path impassable.
    ;; Requires a sword to clear the path, showing the knight's combat prowess.
    (:action overcome-path-dangers
        :parameters (?k - knight ?l1 ?l2 - location ?s - sword)
        :precondition (and
            (at ?k ?l1)
            (path-blocked ?l1 ?l2)
            (has ?k ?s)
            (quest-active ?k)
        )
        :effect (not (path-blocked ?l1 ?l2))
    )

    ;; Action: The knight defeats the fearsome dragon.
    ;; The dragon guards the castle entrance and must be vanquished to proceed further into the castle.
    ;; Requires a sword for the battle.
    (:action defeat-dragon
        :parameters (?k - knight ?d - dragon ?l - location ?s - sword)
        :precondition (and
            (at ?k ?l)
            (enemy-present ?d ?l)
            (has ?k ?s)
            (quest-active ?k)
        )
        :effect (and
            (not (enemy-present ?d ?l))
            (is-defeated ?d)
        )
    )

    ;; Action: The knight confronts and defeats the powerful sorcerer.
    ;; This action not only defeats the sorcerer but also dispels any magic barrier they control, assuming they are linked.
    ;; Requires a sword for combat.
    (:action defeat-sorcerer
        :parameters (?k - knight ?s - sorcerer ?l - location ?w - sword)
        :precondition (and
            (at ?k ?l)
            (enemy-present ?s ?l)
            (has ?k ?w)
            (quest-active ?k)
        )
        :effect (and
            (not (enemy-present ?s ?l))
            (is-defeated ?s)
            (magic-barrier-dispelled ?l) ; Assuming sorcerer controls the magic barrier at that location.
        )
    )

    ;; Action: The knight uses an ancient relic to dispel a magic barrier.
    ;; This provides an alternative way to overcome magical obstacles without direct combat with a sorcerer,
    ;; offering a strategic choice for the knight.
    (:action dispel-magic-with-relic
        :parameters (?k - knight ?l - location ?r - ancient_relic)
        :precondition (and
            (at ?k ?l)
            (magic-barrier-active ?l)
            (has ?k ?r)
            (quest-active ?k)
        )
        :effect (magic-barrier-dispelled ?l)
    )

    ;; Action: The knight rescues the princess.
    ;; This is the final action, achievable only after all major threats (the dragon and the magic/sorcerer) are neutralized.
    (:action rescue-princess
        :parameters (?k - knight ?p - princess ?l - location ?d - dragon ?s - sorcerer)
        :precondition (and
            (at ?k ?l)
            (princess-imprisoned ?l)
            (is-defeated ?d) ; The dragon must be defeated to reach her.
            (magic-barrier-dispelled ?l) ; The magic barrier (or the sorcerer controlling it) must be dealt with.
            (quest-active ?k)
        )
        :effect (and
            (princess-rescued ?p)
            (not (princess-imprisoned ?l)) ; The princess is no longer imprisoned.
        )
    )
)