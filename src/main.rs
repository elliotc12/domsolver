extern crate domsolver;
use domsolver::*;

fn main() {
    let mut starting_hand = State { actions: 1,
                                    buys: 1,
                                    money: 0,
                                    bought:vec![],
                                    hand: vec![Card::COPPER,
                                               Card::COPPER,
                                               Card::VILLAGE,
                                               Card::VILLAGE]};

    let mut deck = vec![Card::COPPER, Card::COPPER, Card::COPPER];
    
    let plays = domsolver::play_turn::play_turn(&mut starting_hand, &mut deck);
    for s in plays.iter() {
        println!("state: {:?}", s);
    }
}
