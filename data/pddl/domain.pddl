(define (domain whimsical-forest-chase)
    (:requirements :strips :typing)
    (:types
        character ; Generic type for intelligent animals in the forest.
        wolf lamb - character ; Specific character types: Ulfric (wolf) and Lillo (lamb).
        location ; Areas within the whimsical forest (e.g., clearing, thicket).
        hazard ; Environmental impediments that hinder Ulfric (e.g., mud puddles, tangled vines).
        critique-type ; Categories of Lillo's unsolicited advice (e.g., culinary, fitness).
    )

    (:predicates
        ;; Core Chase Dynamics
        (at ?c - character ?l - location) ; A character is at a specific location.
        (is-aware ?c - character) ; Indicates if a character is aware of the ongoing chase.
        (is-chasing ?w - wolf ?l - lamb) ; Ulfric is actively pursuing Lillo.
        (is-evading ?l - lamb) ; Lillo is actively avoiding capture.
        (is-caught ?l - lamb) ; Lillo has been successfully captured.

        ;; Ulfric's State (reflecting his incompetence and obstacles)
        (is-distracted ?w - wolf) ; Ulfric is distracted, typically by Lillo's critiques.
        (is-clumsy ?w - wolf) ; Ulfric is currently experiencing a bout of clumsiness.
        (is-immobilized ?w - wolf) ; Ulfric is stuck, tripped, or otherwise temporarily incapacitated.
        (is-focused ?w - wolf) ; Ulfric is clear-minded and ready to act (not distracted, clumsy, or immobilized).

        ;; Lillo's Critique and Agility
        (has-critiqued ?l - lamb ?type - critique-type) ; Lillo has delivered a specific type of critique.

        ;; Environmental Factors
        (location-has-hazard ?l - location ?h - hazard) ; A specific location contains an environmental hazard.
        (hazard-present ?h - hazard) ; Indicates that a specific hazard exists in the world.

        ;; Goal Predicate
        (is-satisfied ?w - wolf) ; Ulfric has achieved his primary goal (captured and presumably consumed Lillo).
    )

    ;; Action: Ulfric initiates the chase.
    ;; This marks the beginning of the active pursuit, and Lillo becomes aware and starts evading.
    (:action initiate-chase
        :parameters (?w - wolf ?l - lamb ?loc - location)
        :precondition (and
            (at ?w ?loc)
            (at ?l ?loc)
            (not (is-aware ?l)) ; Lillo is initially unaware of Ulfric's presence/intent.
            (not (is-chasing ?w ?l))
        )
        :effect (and
            (is-chasing ?w ?l)
            (is-aware ?l)
            (is-evading ?l)
            (is-focused ?w) ; Ulfric starts the chase focused.
        )
    )

    ;; Action: Ulfric attempts to catch Lillo and SUCCEEDS.
    ;; This action represents Ulfric overcoming all obstacles and achieving his goal.
    (:action ulfric-attempts-catch-successful
        :parameters (?w - wolf ?l - lamb ?loc - location)
        :precondition (and
            (is-chasing ?w ?l)
            (at ?w ?loc)
            (at ?l ?loc)
            (is-evading ?l)
            (is-focused ?w) ; Ulfric must be focused to succeed.
            (not (exists (?h - hazard) (location-has-hazard ?loc ?h))) ; No immediate environmental hazard at the location.
        )
        :effect (and
            (not (is-chasing ?w ?l))
            (not (is-evading ?l))
            (is-caught ?l)
            (is-satisfied ?w)
            (not (is-focused ?w)) ; Chase is over, Ulfric no longer needs to be focused on it.
        )
    )

    ;; Action: Ulfric attempts to catch, but Lillo expertly evades and critiques.
    ;; This models Lillo's unparalleled agility and his ability to distract Ulfric with commentary.
    (:action ulfric-attempts-catch-lillo-evades-and-critiques
        :parameters (?w - wolf ?l - lamb ?from ?to - location ?crit - critique-type)
        :precondition (and
            (is-chasing ?w ?l)
            (at ?w ?from)
            (at ?l ?from)
            (is-evading ?l)
            (is-focused ?w) ; Ulfric starts focused, but becomes distracted.
        )
        :effect (and
            (not (at ?l ?from))
            (at ?l ?to) ; Lillo moves to a new, safer location.
            (is-distracted ?w) ; Ulfric becomes distracted by Lillo's verbal assault.
            (has-critiqued ?l ?crit)
            (not (is-focused ?w)) ; Ulfric loses focus due to distraction.
        )
    )

    ;; Action: Ulfric attempts to catch, but his profound clumsiness causes him to trip.
    ;; This directly models Ulfric's intrinsic clumsiness leading to slapstick failure.
    (:action ulfric-attempts-catch-ulfric-trips-self
        :parameters (?w - wolf ?l - lamb ?loc - location)
        :precondition (and
            (is-chasing ?w ?l)
            (at ?w ?loc)
            (at ?l ?loc)
            (is-focused ?w) ; Ulfric starts focused, but falls due to his own clumsiness.
        )
        :effect (and
            (is-clumsy ?w)
            (is-immobilized ?w) ; Ulfric is momentarily incapacitated by his fall.
            (not (is-chasing ?w ?l)) ; The chase is interrupted.
            (not (is-focused ?w)) ; Ulfric is no longer focused while clumsy and immobilized.
        )
    )

    ;; Action: Ulfric attempts to catch, but the natural environment hinders him.
    ;; This models obstacles like mud puddles, thorny bushes, or tangled vines.
    (:action ulfric-attempts-catch-environment-hinders
        :parameters (?w - wolf ?l - lamb ?loc - location ?h - hazard)
        :precondition (and
            (is-chasing ?w ?l)
            (at ?w ?loc)
            (at ?l ?loc)
            (is-focused ?w) ; Ulfric starts focused, but gets hindered by the environment.
            (location-has-hazard ?loc ?h)
            (hazard-present ?h)
        )
        :effect (and
            (is-immobilized ?w) ; Ulfric gets stuck or tangled by the hazard.
            (not (is-chasing ?w ?l)) ; The chase is interrupted.
            (not (is-focused ?w)) ; Ulfric is no longer focused while immobilized.
            ; The hazard itself is not removed, as it's a permanent part of the environment.
        )
    )

    ;; Action: Ulfric recovers from a state of distraction, clumsiness, or immobilization.
    ;; This allows Ulfric to regain his composure and resume the chase.
    (:action ulfric-recovers
        :parameters (?w - wolf)
        :precondition (or
            (is-distracted ?w)
            (is-clumsy ?w)
            (is-immobilized ?w)
        )
        :effect (and
            (not (is-distracted ?w))
            (not (is-clumsy ?w))
            (not (is-immobilized ?w))
            (is-focused ?w) ; Ulfric becomes focused again after recovery.
        )
    )

    ;; Action: Ulfric moves from one location to another.
    ;; Ulfric can only move when he is focused and not incapacitated.
    (:action ulfric-moves
        :parameters (?w - wolf ?from ?to - location)
        :precondition (and
            (at ?w ?from)
            (is-focused ?w) ; Ulfric must be focused to execute movement.
        )
        :effect (and
            (not (at ?w ?from))
            (at ?w ?to)
        )
    )

    ;; Action: Lillo moves from one location to another while evading.
    ;; This allows Lillo to create distance or lead Ulfric into new areas.
    (:action lillo-moves-evading
        :parameters (?l - lamb ?from ?to - location)
        :precondition (and
            (at ?l ?from)
            (is-evading ?l) ; Lillo can only make active evasion moves while evading.
        )
        :effect (and
            (not (at ?l ?from))
            (at ?l ?to)
        )
    )
)