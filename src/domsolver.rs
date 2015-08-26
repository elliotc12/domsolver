pub mod play_turn;

pub struct State {
    pub actions: i32,
    pub buys:    i32,
    pub gold:    i32,
    pub bought:  Vec<i32>,
}

pub enum Card {
    COPPER,
    SILVER,
    GOLD,
    ESTATE,
    DUCHY,
    PROVINCE,
    VILLAGE,
    MARKET,
    WOODCUTTER,
    SMITHY,
    THRONE_ROOM
}
