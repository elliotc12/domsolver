use super::*;

pub fn hand_playable(hand: &Vec<Card>) -> bool {
    for c in hand {
        if c.is_playable() {
            return true
        }
    }
    false
}

pub fn play_turn(state: State, deck: Vec<Card>) -> Vec<State> {
    // Check if hand_playable returns true.
    // If so, for each action, run play_card on it, get the returned state
    // Run play_turn on the returned state
    // Return all the states for each action concatenated together
    // Else iff hand_playable false, return the current state
    
    if !hand_playable(&state.hand) || state.actions == 0 {
        return vec![state.clone()];    // We're done, return the played-through state
    } else {
        let mut rec_vec = vec![];
        if state.actions > 0 {
            for c in &state.hand {   // Play each possible card
                if c.is_playable() {
                    let mut c_state: State = state.clone();
                    let mut my_deck: Vec<Card> = deck.clone();
                    let c_idx: usize = c_state.hand.iter().position(|x| *x == *c).unwrap(); // position() takes a lambda function, returns an Option
                    c_state.hand.remove(c_idx);
                    println!("Playing {:?}, hand: {:?}", c, &state.hand);
                    c_state = c_state.play_action(c, &mut my_deck);
                    let c_plays = play_turn(c_state, my_deck);
                    for p in c_plays.iter() {
                        rec_vec.push(p.clone());
                    }
                }
            }
        }
        rec_vec
    }
}
