use super::*;

fn play_card(card: Card, state: State) -> State {
    state
}

fn hand_playable(hand: Vec<Card>) -> bool {
    true
}

fn do_action(state: State) -> Vec<State> {
    // Check if hand_playable returns true.
    // If so, run play_action on every action in the hand
    // Retrieve new state fro play_action
    // Run do_action on the new state, retrieve its states and return them
    if !hand_playable(state.hand) {
        return vec![state.clone()];
    }

    println!("Hello!");
    vec![state.clone()]
}

pub fn play_turn() {
    let mut mystate = State { actions: 0, gold: 0, buys: 0, bought: vec![], hand: vec![] };
    //do_action(mystate);
}
