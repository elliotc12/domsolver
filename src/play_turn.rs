use super::*;
use std::bool;

fn play_card(card: Card, hand: Vec<Card>, state: State) {
}

fn hand_playable(hand: Vec<Card>) -> bool {
}

fn do_action(hand: Vec<Card>, state: State) {
}

pub fn play_turn() {
    let mut mystate = State { actions: 0, gold: 0, buys: 0, bought: vec![] };
    println!("playing turn, my state is: {}", mystate.actions);
}
