(define (domain elias-quest)
    (:requirements :strips :typing)
    (:types
        person ; Represents characters in the story, like Elia.
        location ; Represents different places in the world (e.g., village, forest).
        spring ; Represents a magical entity, specifically the Magic Spring.
    )

    (:predicates
        (at ?p - person ?l - location) ; Indicates that a person is at a specific location.
        (drought-active ?l - location) ; True if a location is suffering from a drought (Obstacle 1).
        (quest-initiated ?p - person) ; True if Elia has decided to begin her quest (Addresses Obstacle 2: overcoming fear/resignation).
        (in-forest ?l - location) ; Helper predicate to mark locations that are part of the forest, aiding search.
        (spring-located ?p - person ?s - spring) ; True if Elia has successfully found the Magic Spring within the forest (Addresses Obstacle 3: vastness of forest).
        (spring-dormant ?s - spring) ; True if the Magic Spring is currently inactive/lifeless (Obstacle 4).
        (has-storytelling-skill ?p - person) ; True if a person (Elia) possesses her unique ability.
        (story-told-at-spring ?p - person ?s - spring) ; True if Elia has performed her storytelling to the spring.
        (spring-awakened ?s - spring) ; True if the Magic Spring has been successfully revived.
        (village-saved ?l - location) ; True if the village has been saved from the drought (Final goal predicate).
    )

    ;; Action: Elia decides to embark on her quest, overcoming the village's despair and her own initial hesitation.
    (:action initiate-quest
        :parameters (?p - person ?village - location)
        :precondition (and
            (at ?p ?village)
            (drought-active ?village) ; The quest starts because of the drought.
        )
        :effect (and
            (quest-initiated ?p) ; Elia is now on her quest.
        )
    )

    ;; Action: Elia moves from one location to another.
    (:action traverse-path
        :parameters (?p - person ?from ?to - location)
        :precondition (and
            (at ?p ?from)
            (quest-initiated ?p) ; Elia must be on her quest to move towards the goal.
        )
        :effect (and
            (not (at ?p ?from)) ; Elia leaves the 'from' location.
            (at ?p ?to) ; Elia arrives at the 'to' location.
        )
    )

    ;; Action: Elia actively searches for the Magic Spring within the vast and silent forest.
    ;; This addresses the "silence and vastness of the forest" making the spring hard to find (Obstacle 3).
    (:action search-for-spring
        :parameters (?p - person ?forest_loc - location ?magic_spring - spring)
        :precondition (and
            (at ?p ?forest_loc) ; Elia must be in the forest.
            (in-forest ?forest_loc) ; The location must be identified as part of the forest.
            (not (spring-located ?p ?magic_spring)) ; The spring must not have been found yet by Elia.
            (quest-initiated ?p) ; Elia must be on her quest.
        )
        :effect (and
            (spring-located ?p ?magic_spring) ; Elia successfully locates the spring.
        )
    )

    ;; Action: Elia uses her unique storytelling skill to awaken the dormant Magic Spring.
    ;; This demonstrates the "power of stories" and directly addresses the "inert spring" obstacle (Obstacle 4).
    (:action tell-story-to-spring
        :parameters (?p - person ?magic_spring - spring ?forest_loc - location)
        :precondition (and
            (at ?p ?forest_loc) ; Elia must be in the forest where the spring is.
            (spring-located ?p ?magic_spring) ; Elia must have found the spring.
            (spring-dormant ?magic_spring) ; The spring must still be dormant.
            (has-storytelling-skill ?p) ; Elia must possess her special skill.
        )
        :effect (and
            (story-told-at-spring ?p ?magic_spring) ; Records that a story was told.
            (not (spring-dormant ?magic_spring)) ; The spring is no longer dormant.
            (spring-awakened ?magic_spring) ; The spring is now awakened.
        )
    )

    ;; Action: Elia returns to the village after awakening the spring, signifying the end of the drought and salvation of the village.
    ;; This action connects the awakened spring to the final goal of saving the village.
    (:action return-to-village-with-rain
        :parameters (?p - person ?forest_loc ?village_loc - location ?magic_spring - spring)
        :precondition (and
            (at ?p ?forest_loc) ; Elia is in the forest (where the spring is).
            (spring-awakened ?magic_spring) ; The spring must have been awakened.
            (quest-initiated ?p) ; Elia is still on her quest to bring back rain.
        )
        :effect (and
            (not (at ?p ?forest_loc)) ; Elia leaves the forest.
            (at ?p ?village_loc) ; Elia arrives back at the village.
            (not (drought-active ?village_loc)) ; The drought at the village ends.
            (village-saved ?village_loc) ; The village is now saved.
        )
    )
)