extern crate domsolver;
use domsolver::*;

fn main() {
    let starting_hand = State { actions: 1,
                                    buys: 1,
                                    money: 0,
                                    bought:vec![],
                                    hand: vec![Card::COPPER,
                                               Card::COPPER,
                                               Card::SMITHY,
                                               Card::VILLAGE]};

    let deck = vec![Card::MARKET, Card::COPPER, Card::COPPER, Card::COPPER];
    
    let plays = domsolver::play_turn::play_turn(starting_hand, deck);
    for s in plays.iter() {
        println!("state: {:?}", s);
    }
}
