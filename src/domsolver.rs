pub mod play_turn;

#[derive(Clone, Debug)]      // have the compiler impl basic traits for State
pub struct State {
    pub actions: i32,
    pub buys:    i32,
    pub money:   i32,
    pub bought:  Vec<i32>,
    pub hand:    Vec<Card>
}

#[derive(Clone, Debug, PartialEq)]
pub enum Card {
    COPPER,
    SILVER,
    GOLD,
    ESTATE,
    DUCHY,
    PROVINCE,
    VILLAGE,
    MARKET,
    SMITHY
}

impl State {
    fn draw_card(&mut self, deck: &mut Vec<Card>) {
        let draw = deck.remove(0);
        self.hand.push(draw);
    }
    
    fn play_action(mut self, c: &Card, deck: &mut Vec<Card>) -> State {
        self.actions -= 1;
        match *c {
            Card::VILLAGE =>
            {
                self.draw_card(deck);
                self.actions += 2;
            }
            
            Card::MARKET =>
            {
                self.draw_card(deck);
                self.actions += 1;
                self.buys += 1;
                self.money += 1;
            }

            Card::SMITHY =>
            {
                self.draw_card(deck);
                self.draw_card(deck);
                self.draw_card(deck);
            }
            _ => {}
        }
        self
    }
}

impl Card {
    fn _monetary_value(&self) -> i32 {
        return if *self == Card::COPPER { 1 }
        else if   *self == Card::SILVER { 2 }
        else if   *self == Card::GOLD   { 3 }
        else                            { 0 };
    }

    fn _victory_value(&self) -> i32 {
        return if *self == Card::ESTATE   { 1 }
        else if   *self == Card::DUCHY    { 3 }
        else if   *self == Card::PROVINCE { 6 }
        else                              { 0 };
    }

    fn _price(&self) -> i32 {
        return if *self == Card::COPPER    { 0 }
        else   if *self == Card::DUCHY     { 4 }
        else   if *self == Card::ESTATE    { 2 }
        else   if *self == Card::GOLD      { 6 }
        else   if *self == Card::MARKET    { 5 }
        else   if *self == Card::PROVINCE  { 8 }
        else   if *self == Card::SILVER    { 3 }
        else   if *self == Card::SMITHY    { 4 }
        else   if *self == Card::VILLAGE   { 5 }
        else { println!("Error, this is not a card"); 0 };
    }

    fn is_playable(&self) -> bool {
        return if *self == Card::COPPER    { false }
        else   if *self == Card::DUCHY     { false }
        else   if *self == Card::ESTATE    { false }
        else   if *self == Card::GOLD      { false }
        else   if *self == Card::MARKET    { true }
        else   if *self == Card::PROVINCE  { false }
        else   if *self == Card::SILVER    { false }
        else   if *self == Card::SMITHY    { true }
        else   if *self == Card::VILLAGE   { true }
        else { println!("Error, this is not a card"); false };
    }
}
